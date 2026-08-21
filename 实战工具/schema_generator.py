#!/usr/bin/env python3
"""
Schema.org JSON-LD 生成器 v1.0
生成 6 种常用 Schema,复制即用

用法:
  # 交互式
  python schema_generator.py
  # 命令行
  python schema_generator.py --type faq -o faq.json
"""
import sys
import argparse
import json
from datetime import datetime


def schema_article(title, author, description, url, image=None):
    """生成 Article Schema"""
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "author": {
            "@type": "Person",
            "name": author
        },
        "datePublished": datetime.now().strftime("%Y-%m-%d"),
        "dateModified": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "image": image or "https://example.com/og.png",
        "publisher": {
            "@type": "Organization",
            "name": "你的品牌",
            "logo": {
                "@type": "ImageObject",
                "url": "https://example.com/logo.png"
            }
        },
        "mainEntityOfPage": url
    }


def schema_faq(qa_list):
    """生成 FAQ Schema
    qa_list: [{"question": "Q", "answer": "A"}, ...]
    """
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": qa["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": qa["answer"]
                }
            } for qa in qa_list
        ]
    }


def schema_organization(name, url, logo, same_as=None, contact=None):
    """生成 Organization Schema"""
    schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": name,
        "url": url,
        "logo": logo,
    }
    if same_as:
        schema["sameAs"] = same_as if isinstance(same_as, list) else [same_as]
    if contact:
        schema["contactPoint"] = contact
    return schema


def schema_product(name, description, brand, price, currency, availability, url, image=None):
    """生成 Product Schema"""
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": name,
        "description": description,
        "brand": {
            "@type": "Brand",
            "name": brand
        },
        "offers": {
            "@type": "Offer",
            "price": price,
            "priceCurrency": currency,
            "availability": f"https://schema.org/{availability}",
            "url": url
        },
        "image": image or "https://example.com/product.png"
    }


def schema_howto(name, steps, total_time=None, tools=None):
    """生成 HowTo Schema
    steps: [{"name": "步骤名", "text": "详细说明"}, ...]
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "step": [
            {
                "@type": "HowToStep",
                "position": i + 1,
                "name": step["name"],
                "text": step["text"]
            } for i, step in enumerate(steps)
        ]
    }
    if total_time:
        schema["totalTime"] = total_time
    if tools:
        schema["tool"] = tools
    return schema


def schema_breadcrumb(items):
    """生成 BreadcrumbList Schema
    items: [{"name": "首页", "url": "https://..."}, ...]
    """
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": item["name"],
                "item": item["url"]
            } for i, item in enumerate(items)
        ]
    }


# FAQ 模板(常用)
FAQ_TEMPLATES = {
    'GEO 基础': [
        {"question": "什么是 GEO(Generative Engine Optimization)?",
         "answer": "GEO 是让内容在 AI 引擎(ChatGPT/Claude/豆包等)回答中被引用的优化方法。Princeton 大学 2024 年研究显示,GEO 可让内容引用率提升最高 40%。"},
        {"question": "GEO 和 SEO 有什么区别?",
         "answer": "SEO 优化网页在搜索结果中的排名(给人看),GEO 优化内容在 AI 引擎回答中的引用(给 AI 看)。两者目标不同,方法有重叠但不能等同。"},
        {"question": "GEO 需要多久见效?",
         "answer": "通常 3-6 个月积累。部分内容 24 小时内可被 AI 引用,长期引用可持续 6+ 个月。"},
    ],
    '工具使用': [
        {"question": "这个工具怎么用?",
         "answer": "提供 URL,工具自动审计 GEO 准备度并给出改进建议。"},
        {"question": "工具支持哪些 AI 爬虫?",
         "answer": "支持 12+ 主流 AI 爬虫,包括 GPTBot、ClaudeBot、PerplexityBot、Bytespider(豆包)、Google-Extended(Gemini) 等。"},
    ],
    '产品价格': [
        {"question": "多少钱?",
         "answer": "请查看价格页面或联系我们获取报价。"},
    ],
}


def interactive_mode():
    """交互式生成"""
    print(f"\n{'='*50}")
    print(f"  📋 Schema.org JSON-LD 生成器")
    print(f"{'='*50}\n")

    print("  选择 Schema 类型:")
    print("    1. Article(文章)")
    print("    2. FAQ(常见问题)")
    print("    3. Organization(组织)")
    print("    4. Product(产品)")
    print("    5. HowTo(操作指南)")
    print("    6. Breadcrumb(面包屑)")
    print("    7. FAQ 模板")
    print()

    choice = input("  请选择(1-7): ").strip()

    if choice == '1':
        # Article
        title = input("  文章标题: ").strip()
        author = input("  作者名: ").strip()
        description = input("  文章描述(150字内): ").strip()
        url = input("  文章URL: ").strip()
        schema = schema_article(title, author, description, url)

    elif choice == '2':
        # FAQ
        print("  输入 FAQ(输入空行结束):")
        qa_list = []
        while True:
            q = input("    Q: ").strip()
            if not q:
                break
            a = input("    A: ").strip()
            qa_list.append({"question": q, "answer": a})
        schema = schema_faq(qa_list)

    elif choice == '3':
        # Organization
        name = input("  组织名: ").strip()
        url = input("  官网 URL: ").strip()
        logo = input("  Logo URL: ").strip()
        schema = schema_organization(name, url, logo)

    elif choice == '4':
        # Product
        name = input("  产品名: ").strip()
        description = input("  产品描述: ").strip()
        brand = input("  品牌: ").strip()
        price = input("  价格(数字): ").strip()
        currency = input("  货币(CNY/USD): ").strip() or "CNY"
        url = input("  产品 URL: ").strip()
        schema = schema_product(name, description, brand, price, currency,
                              "InStock", url)

    elif choice == '5':
        # HowTo
        name = input("  操作指南名: ").strip()
        print("  输入步骤(空行结束):")
        steps = []
        i = 1
        while True:
            s = input(f"    步骤 {i} 名称(回车结束): ").strip()
            if not s:
                break
            t = input(f"    步骤 {i} 说明: ").strip()
            steps.append({"name": s, "text": t})
            i += 1
        schema = schema_howto(name, steps)

    elif choice == '6':
        # Breadcrumb
        print("  面包屑路径(从首页开始):")
        items = []
        i = 1
        while True:
            n = input(f"    第{i}级 名称(回车结束): ").strip()
            if not n:
                break
            u = input(f"    第{i}级 URL: ").strip()
            items.append({"name": n, "url": u})
            i += 1
        schema = schema_breadcrumb(items)

    elif choice == '7':
        # FAQ 模板
        print("  选择模板:")
        for i, name in enumerate(FAQ_TEMPLATES.keys(), 1):
            print(f"    {i}. {name}")
        tpl_choice = int(input("  请选择: ").strip()) - 1
        tpl_name = list(FAQ_TEMPLATES.keys())[tpl_choice]
        schema = schema_faq(FAQ_TEMPLATES[tpl_name])

    else:
        print("  无效选择")
        return

    output = json.dumps(schema, ensure_ascii=False, indent=2)

    print(f"\n  生成的 JSON-LD:\n")
    print(f"  <script type=\"application/ld+json\">")
    print(f"  {output}")
    print(f"  </script>")

    # 保存
    save = input("\n  保存到文件? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("  文件名(默认 schema.json): ").strip() or "schema.json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"  ✅ 已保存到 {filename}")


def main():
    parser = argparse.ArgumentParser(description='Schema.org JSON-LD 生成器')
    parser.add_argument('--type', choices=['article', 'faq', 'organization', 'product', 'howto', 'breadcrumb'],
                       help='Schema 类型')
    parser.add_argument('-o', '--output', default='schema.json', help='输出文件')
    parser.add_argument('--template', help='FAQ 模板(GEO基础/工具使用/产品价格)')

    args = parser.parse_args()

    if not args.type:
        interactive_mode()
        return

    # 命令行模式
    if args.type == 'faq' and args.template:
        tpl_name = args.template
        if tpl_name in FAQ_TEMPLATES:
            schema = schema_faq(FAQ_TEMPLATES[tpl_name])
        else:
            print(f"  模板 '{tpl_name}' 不存在")
            return
    elif args.type == 'article':
        title = input("  标题: ").strip()
        author = input("  作者: ").strip()
        description = input("  描述: ").strip()
        url = input("  URL: ").strip()
        schema = schema_article(title, author, description, url)
    else:
        print("  请用交互模式或提供完整参数")
        return

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 已保存到 {args.output}")


if __name__ == "__main__":
    main()
