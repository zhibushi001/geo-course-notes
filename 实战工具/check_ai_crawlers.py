#!/usr/bin/env python3
"""
AI 爬虫 robots.txt 检查工具 v1.0
检查你的 robots.txt 是否允许 12 个主流 AI 爬虫

用法:python check_ai_crawlers.py https://example.com
"""
import sys
import requests
import re
from urllib.parse import urlparse

# 12 个主流 AI 爬虫(完整列表)
AI_BOTS = [
    # OpenAI
    ('GPTBot', 'OpenAI 训练(ChatGPT 知识库)', True),
    ('ChatGPT-User', 'OpenAI 用户触发', True),
    ('OAI-SearchBot', 'OpenAI 搜索(ChatGPT search)', True),
    # Anthropic
    ('ClaudeBot', 'Anthropic 训练(Claude 知识)', True),
    ('Claude-Web', 'Anthropic 用户触发', True),
    # Perplexity
    ('PerplexityBot', 'Perplexity AI', True),
    ('Perplexity-User', 'Perplexity 用户', True),
    # Google
    ('Google-Extended', 'Gemini 训练', True),
    ('Googlebot', 'Google 搜索(传统)', False),  # 传统爬虫
    # Apple
    ('Applebot-Extended', 'Apple Intelligence 训练', True),
    # 字节
    ('Bytespider', '豆包训练(字节系)', True),
    # 阿里
    ('Bytespider', '豆包(字节系)', True),
    # Common Crawl
    ('CCBot', 'Common Crawl(开源数据集)', True),
    # Cohere
    ('cohere-ai', 'Cohere 训练', True),
    # Amazon
    ('Amazonbot', 'Amazon 训练(可能)', True),
    # Meta
    ('meta-externalagent', 'Meta AI', True),
    # 百度
    ('Baiduspider', '百度搜索', False),  # 传统
]


def fetch(url, timeout=10):
    try:
        r = requests.get(url, timeout=timeout,
                         headers={'User-Agent': 'AI-Crawler-Check/1.0'})
        return r
    except Exception as e:
        print(f"  ✗ 无法访问 {url}: {e}")
        return None


def parse_robots(text):
    """解析 robots.txt,返回每个 bot 的状态"""
    if not text:
        return {}

    # 分割 robots.txt 为每个 User-agent 块
    blocks = re.split(r'(?=^User-agent:)', text, flags=re.MULTILINE)
    bot_status = {}

    for block in blocks:
        if not block.strip():
            continue
        # 提取这个块的所有 User-agent
        agents = re.findall(r'^User-agent:\s*(.+?)$', block, re.MULTILINE)
        # 提取 Allow/Disallow
        allows = re.findall(r'^Allow:\s*(.+?)$', block, re.MULTILINE)
        disallows = re.findall(r'^Disallow:\s*(.+?)$', block, re.MULTILINE)

        # 简化逻辑:
        # 有 Disallow: / 且无 Allow: /  → 阻止
        # 有 Allow: / 或无 Disallow   → 允许
        for agent in agents:
            agent = agent.strip()
            if agent == '*':
                continue  # 跳过通配符

            # 检查这个 agent 的状态
            has_disallow_all = any(d.strip() == '/' for d in disallows)
            has_allow_root = any(a.strip() == '/' for a in allows)
            if has_disallow_all and not has_allow_root:
                bot_status[agent] = 'blocked'
            else:
                bot_status[agent] = 'allowed'

    return bot_status


def check_crawlers(domain):
    """检查 AI 爬虫状态"""
    r = fetch(f"{domain}/robots.txt")
    if not r or r.status_code != 200:
        return None

    return parse_robots(r.text)


def main():
    if len(sys.argv) < 2:
        print("用法:python check_ai_crawlers.py https://example.com")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith('http'):
        url = 'https://' + url
    parsed = urlparse(url)
    domain = f"{parsed.scheme}://{parsed.netloc}"

    print(f"\n{'='*60}")
    print(f"  🤖 AI 爬虫 robots.txt 检查")
    print(f"  目标: {domain}")
    print(f"{'='*60}\n")

    bot_status = check_crawlers(domain)
    if bot_status is None:
        print("  ✗ robots.txt 不存在或无法访问")
        print("  💡 建议:创建 robots.txt 包含 AI 爬虫规则")
        return

    print(f"  找到 {len(AI_BOTS)} 个主流 AI 爬虫,检查结果:\n")

    allowed_count = 0
    blocked_count = 0
    missing_count = 0

    # 按公司分组
    companies = {
        'OpenAI': [b for b in AI_BOTS if b[0].startswith(('GPT', 'ChatGPT', 'OAI'))],
        'Anthropic': [b for b in AI_BOTS if 'Claude' in b[0]],
        'Perplexity': [b for b in AI_BOTS if 'Perplexity' in b[0]],
        'Google': [b for b in AI_BOTS if 'Google' in b[0]],
        '字节/豆包': [b for b in AI_BOTS if 'Bytespider' in b[0]],
        '其他': [b for b in AI_BOTS if not (b[0].startswith(('GPT', 'ChatGPT', 'OAI', 'Claude', 'Perplexity', 'Google', 'Bytespider')))],
    }

    for company, bots in companies.items():
        print(f"  📦 {company}:")
        for bot, desc, is_ai in bots:
            status = bot_status.get(bot, None)
            if status == 'allowed':
                mark = '✓ 允许'
                allowed_count += 1
            elif status == 'blocked':
                mark = '✗ 阻止'
                blocked_count += 1
            else:
                mark = '? 未配置'
                missing_count += 1
            print(f"    {mark:10s} {bot:20s} ({desc})")
        print()

    print(f"  📊 统计:")
    print(f"    允许:   {allowed_count}/{len(AI_BOTS)}")
    print(f"    阻止:   {blocked_count}")
    print(f"    未配置: {missing_count}")

    # 评分
    score = int(allowed_count / len(AI_BOTS) * 100)
    print(f"\n  AI 爬虫可见度: {score}/100")

    if score < 50:
        print("  ⚠️ 警告:大部分 AI 爬虫被阻止!GEO 优化效果会大打折扣")
    elif score < 80:
        print("  ⚡ 部分 AI 爬虫可以访问,可进一步优化")
    else:
        print("  ✅ AI 爬虫可见度良好")

    # 生成补丁建议
    print(f"\n  💡 推荐的 robots.txt 补丁:")
    patch_lines = []
    for bot, desc, is_ai in AI_BOTS:
        if is_ai and bot_status.get(bot) != 'allowed':
            patch_lines.append(f"User-agent: {bot}")
            patch_lines.append("Allow: /")
            patch_lines.append("")

    if patch_lines:
        print("\n    # 复制以下到你的 robots.txt")
        print("    " + "-" * 40)
        for line in patch_lines[:10]:  # 只显示前 10 个
            print(f"    {line}")
        print(f"    ...(共 {len(patch_lines)//3} 个建议)")


if __name__ == "__main__":
    main()
