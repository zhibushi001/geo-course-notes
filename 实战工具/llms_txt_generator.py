#!/usr/bin/env python3
"""
llms.txt 自动生成器 v1.0
自动爬取网站,生成标准 llms.txt

用法:
  python llms_txt_generator.py https://example.com -o llms.txt
  python llms_txt_generator.py https://example.com --brand "我的品牌" --category "GEO 工具"
"""
import sys
import requests
import re
import argparse
from urllib.parse import urljoin, urlparse
from collections import deque


def fetch(url, timeout=10):
    try:
        r = requests.get(url, timeout=timeout,
                         headers={'User-Agent': 'LLMs-Generator/1.0'})
        return r
    except:
        return None


def crawl_domain(domain, max_pages=20):
    """BFS 爬取站内页面"""
    print(f"  🔍 爬取 {domain} (最多 {max_pages} 页)...")

    visited = set()
    queue = deque([domain])
    pages = []

    while queue and len(pages) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        r = fetch(url)
        if not r or r.status_code != 200:
            continue

        # 提取 title + description
        title_m = re.search(r'<title>(.*?)</title>', r.text, re.DOTALL)
        title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else url

        desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', r.text)
        desc = desc_m.group(1) if desc_m else ""

        h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', r.text, re.DOTALL)
        h1 = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip() if h1_m else ""

        pages.append({
            'url': url,
            'title': title,
            'description': desc,
            'h1': h1,
        })

        # 找更多链接
        for href in re.findall(r'href=["\']([^"\']+)["\']', r.text):
            if href.startswith('#') or href.startswith('mailto:'):
                continue
            full_url = urljoin(url, href)
            if urlparse(full_url).netloc == urlparse(domain).netloc:
                if full_url not in visited:
                    queue.append(full_url)

    print(f"  ✓ 找到 {len(pages)} 个页面")
    return pages


def detect_category(pages):
    """简单的页面分类"""
    categories = {
        '产品': [],
        '服务': [],
        '博客': [],
        '文档': [],
        '关于': [],
        '其他': [],
    }

    for page in pages:
        url_lower = page['url'].lower()
        if any(k in url_lower for k in ['product', 'item', 'goods']):
            categories['产品'].append(page)
        elif any(k in url_lower for k in ['service', 'solution']):
            categories['服务'].append(page)
        elif any(k in url_lower for k in ['blog', 'news', 'post', 'article']):
            categories['博客'].append(page)
        elif any(k in url_lower for k in ['doc', 'wiki', 'guide', 'help', 'api']):
            categories['文档'].append(page)
        elif any(k in url_lower for k in ['about', 'contact', 'team', 'company']):
            categories['关于'].append(page)
        else:
            categories['其他'].append(page)

    return categories


def generate_llms_txt(domain, pages, categories, brand, category, key_pages=None):
    """生成 llms.txt 内容"""
    lines = []

    # H1 标题
    lines.append(f"# {brand}")
    lines.append("")

    # 简短描述
    if category:
        lines.append(f"> {category} - 详细描述见各页面")
    else:
        lines.append("> 网站主标题和介绍")
    lines.append("")

    # 主要页面
    if categories.get('产品') or categories.get('服务'):
        lines.append("## 主要产品/服务")
        for p in (categories.get('产品', []) + categories.get('服务', []))[:10]:
            title = p['title'][:50]
            desc = (p['description'] or p['h1'] or "")[:80]
            if desc:
                lines.append(f"- [{title}]({p['url']}):{desc}")
            else:
                lines.append(f"- [{title}]({p['url']})")
        lines.append("")

    # 文档
    if categories.get('文档'):
        lines.append("## 文档")
        for p in categories['文档'][:5]:
            lines.append(f"- [{p['title'][:50]}]({p['url']})")
        lines.append("")

    # 博客
    if categories.get('博客'):
        lines.append("## 博客/资讯")
        for p in categories['博客'][:5]:
            lines.append(f"- [{p['title'][:50]}]({p['url']})")
        lines.append("")

    # 关于
    if categories.get('关于'):
        lines.append("## 关于")
        for p in categories['关于'][:5]:
            lines.append(f"- [{p['title'][:50]}]({p['url']})")
        lines.append("")

    # 其他
    if categories.get('其他'):
        lines.append("## 其他页面")
        for p in categories['其他'][:5]:
            lines.append(f"- [{p['title'][:50]}]({p['url']})")
        lines.append("")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='llms.txt 自动生成器')
    parser.add_argument('url', help='网站 URL')
    parser.add_argument('-o', '--output', default='llms.txt', help='输出文件')
    parser.add_argument('--brand', default='品牌名', help='品牌名(用作 H1)')
    parser.add_argument('--category', default='', help='产品/服务类别描述')
    parser.add_argument('--max-pages', type=int, default=20, help='最多爬取页数')

    args = parser.parse_args()

    url = args.url
    if not url.startswith('http'):
        url = 'https://' + url
    parsed = urlparse(url)
    domain = f"{parsed.scheme}://{parsed.netloc}"

    print(f"\n{'='*60}")
    print(f"  📝 llms.txt 自动生成器")
    print(f"  目标: {domain}")
    print(f"{'='*60}\n")

    # 1. 爬取
    pages = crawl_domain(domain, max_pages=args.max_pages)
    if not pages:
        print("  ✗ 爬取失败")
        return

    # 2. 分类
    print(f"  📂 分类页面...")
    categories = detect_category(pages)
    for cat, ps in categories.items():
        if ps:
            print(f"    {cat}: {len(ps)} 个")

    # 3. 生成
    print(f"\n  📝 生成 llms.txt...")
    content = generate_llms_txt(domain, pages, categories, args.brand, args.category)

    # 4. 保存
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n  ✅ 已保存到: {args.output}")
    print(f"  📊 文件大小: {len(content)} 字符")
    print(f"\n  下一步:")
    print(f"    1. 检查生成的 llms.txt")
    print(f"    2. 上传到: {domain}/llms.txt")
    print(f"    3. 在 robots.txt 添加: Sitemap: {domain}/llms.txt")


if __name__ == "__main__":
    main()
