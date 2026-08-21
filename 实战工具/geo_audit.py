#!/usr/bin/env python3
"""
GEO 准备度审计工具 v1.0
检查一个网站的 GEO 准备度,输出 0-100 评分

用法:python geo_audit.py https://example.com
"""
import sys
import requests
import re
from urllib.parse import urlparse

# 12 个主流 AI 爬虫
AI_BOTS = [
    ('GPTBot', 'OpenAI 训练'),
    ('ChatGPT-User', 'OpenAI 用户'),
    ('OAI-SearchBot', 'OpenAI 搜索'),
    ('ClaudeBot', 'Anthropic 训练'),
    ('Claude-Web', 'Anthropic 用户'),
    ('PerplexityBot', 'Perplexity'),
    ('Perplexity-User', 'Perplexity 用户'),
    ('Google-Extended', 'Gemini 训练'),
    ('Applebot-Extended', 'Apple 训练'),
    ('Bytespider', '豆包(字节)'),
    ('CCBot', 'Common Crawl'),
    ('cohere-ai', 'Cohere 训练'),
]


def fetch(url, timeout=10):
    try:
        r = requests.get(url, timeout=timeout,
                         headers={'User-Agent': 'GEO-Audit-Tool/1.0'})
        return r
    except Exception as e:
        print(f"  ✗ 无法访问 {url}: {e}")
        return None


def check_robots(domain):
    """检查 robots.txt,统计允许的 AI 爬虫"""
    r = fetch(f"{domain}/robots.txt")
    if not r or r.status_code != 200:
        return None, 0
    text = r.text
    allowed = []
    blocked = []
    for bot, desc in AI_BOTS:
        # 检查这个 bot 的规则
        # 简单匹配:有 "User-agent: X" + "Disallow: /" 算阻止
        pattern = rf"User-agent:\s*{bot}[\s\S]*?(?=User-agent:|$)"
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            block = "Disallow: /" in m.group(0) and "Allow: /" not in m.group(0)
            (blocked if block else allowed).append(bot)
    return text, len(allowed)


def check_llms(domain):
    """检查 llms.txt"""
    r = fetch(f"{domain}/llms.txt")
    if r and r.status_code == 200:
        return True
    return False


def check_sitemap(domain):
    """检查 sitemap.xml"""
    r = fetch(f"{domain}/sitemap.xml")
    if r and r.status_code == 200:
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        return len(urls)
    return 0


def check_homepage(domain):
    """检查首页 SEO 基础"""
    r = fetch(domain)
    if not r:
        return None
    text = r.text
    checks = {}
    # 标题
    title_m = re.search(r'<title>(.*?)</title>', text, re.DOTALL)
    checks['title'] = title_m.group(1).strip()[:60] if title_m else None
    # 描述
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', text)
    checks['description'] = desc_m.group(1) if desc_m else None
    # H1
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
    checks['h1'] = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip() if h1_m else None
    # Schema.org
    checks['schema'] = bool(re.search(r'application/ld\+json', text))
    # OG Tags
    checks['og'] = bool(re.search(r'property=["\']og:title["\']', text))
    return checks


def score_audit(domain):
    """综合评分"""
    print(f"\n{'='*50}")
    print(f"  GEO 准备度审计")
    print(f"  目标: {domain}")
    print(f"{'='*50}\n")

    score = 0
    details = []

    # 1. robots.txt (20分)
    robots, allowed = check_robots(domain)
    if robots is None:
        details.append(('robots.txt', '不存在', 0, 20))
    else:
        pct = int(allowed / len(AI_BOTS) * 100)
        points = int(pct / 5)  # 20分封顶
        details.append(('robots.txt', f'{allowed}/{len(AI_BOTS)} 个 AI 爬虫被允许 ({pct}%)', points, 20))
        score += points

    # 2. llms.txt (15分)
    has_llms = check_llms(domain)
    if has_llms:
        details.append(('llms.txt', '存在', 15, 15))
        score += 15
    else:
        details.append(('llms.txt', '不存在', 0, 15))

    # 3. sitemap.xml (10分)
    sitemap_count = check_sitemap(domain)
    if sitemap_count > 0:
        points = min(10, sitemap_count)
        details.append(('sitemap.xml', f'存在({sitemap_count} 个 URL)', points, 10))
        score += points
    else:
        details.append(('sitemap.xml', '不存在', 0, 10))

    # 4. 首页 SEO (40分)
    checks = check_homepage(domain)
    if checks:
        if checks.get('title'):
            tlen = len(checks['title'])
            points = min(10, tlen // 6)
            details.append(('标题', f'{tlen} 字符: "{checks["title"][:30]}..."', points, 10))
            score += points
        else:
            details.append(('标题', '缺失', 0, 10))

        if checks.get('description'):
            dlen = len(checks['description'])
            points = min(10, dlen // 16)
            details.append(('描述', f'{dlen} 字符', points, 10))
            score += points
        else:
            details.append(('描述', '缺失', 0, 10))

        if checks.get('h1'):
            details.append(('H1', f'1 个: "{checks["h1"][:30]}"', 10, 10))
            score += 10
        else:
            details.append(('H1', '缺失', 0, 10))

        if checks.get('schema'):
            details.append(('Schema', '检测到 JSON-LD', 5, 5))
            score += 5
        else:
            details.append(('Schema', '未检测到', 0, 5))

        if checks.get('og'):
            details.append(('OG 标签', '已配置', 5, 5))
            score += 5
        else:
            details.append(('OG 标签', '未配置', 0, 5))
    else:
        details.append(('首页访问', '失败', 0, 40))

    # 5. AI 爬虫详情(打印)
    if robots:
        print(f"  AI 爬虫详情(robots.txt):")
        for bot, desc in AI_BOTS:
            pattern = rf"User-agent:\s*{bot}[\s\S]*?(?=User-agent:|$)"
            m = re.search(pattern, robots, re.IGNORECASE)
            if m:
                block = "Disallow: /" in m.group(0) and "Allow: /" not in m.group(0)
                mark = '✗ 阻止' if block else '✓ 允许'
                print(f"    {mark:8s} {bot:20s} ({desc})")
            else:
                print(f"    ? 未配置 {bot:18s} ({desc})")
        print()

    # 打印结果
    print(f"  检查项详情:")
    for name, status, points, max_points in details:
        pct = int(points / max_points * 100) if max_points else 0
        print(f"    {name:18s} {status:50s} {points:>3}/{max_points:>3} ({pct:>3}%)")

    # 等级评定
    if score >= 90: grade = 'A+'
    elif score >= 80: grade = 'A'
    elif score >= 70: grade = 'B+'
    elif score >= 60: grade = 'B'
    elif score >= 50: grade = 'C+'
    elif score >= 40: grade = 'C'
    elif score >= 30: grade = 'D'
    else: grade = 'F'

    print(f"\n{'='*50}")
    print(f"  总分: {score}/100 ({grade})")
    print(f"{'='*50}\n")

    # 改进建议
    print("  改进建议:")
    if not has_llms:
        print("    - 立即创建 llms.txt(用 llms_txt_generator.py)")
    if score < 50:
        print("    - 完整做一次 GEO 基础配置(参考白帽指南 30 天计划)")
    if score < 70:
        print("    - 重点优化内容(FAQ 块 + 对比表 + 数据引用)")
    if score < 90:
        print("    - 持续监测 AI 引擎引用情况,每月迭代")

    return score, grade


def main():
    if len(sys.argv) < 2:
        print("用法:python geo_audit.py https://example.com")
        print("示例:python geo_audit.py https://www.zhibushi.com")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith('http'):
        url = 'https://' + url

    parsed = urlparse(url)
    domain = f"{parsed.scheme}://{parsed.netloc}"

    score, grade = score_audit(domain)

    print(f"  详细分数:{score}分 ({grade}级)")
    print()
    return score


if __name__ == "__main__":
    main()
