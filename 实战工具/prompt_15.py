#!/usr/bin/env python3
"""
15 个 GEO 提示词测试工具 v1.0
使用 7-5-3 黄金分布的提示词,在 6 大 AI 平台测试你的品牌引用情况

用法:
  python prompt_15.py "我的品牌"
  python prompt_15.py --brand "BrandX" --category "GEO 工具"
"""
import sys
import argparse
import json
from datetime import datetime


# 7-5-3 黄金分布
PROMPT_CATEGORIES = {
    '类别发现 (7个)': [
        "Best {category} for {market} buyers in 2026",
        "Top {category} tools for growing teams",
        "Which {category} products are easiest to implement?",
        "Compare leading {category} platforms",
        "What {category} vendors do customers recommend?",
        "Most trusted {category} for {use_case}",
        "Affordable {category} alternatives",
    ],
    '品牌评估 (5个)': [
        "Is {brand} a good choice for {category}?",
        "{brand} reviews, pros, and cons",
        "{brand} pricing and plans",
        "{brand} customer complaints and limitations",
        "{brand} case studies and proof",
    ],
    '竞品对比 (3个)': [
        "{brand} vs {competitor_1}",
        "Best alternatives to {brand}",
        "{brand} compared with {competitor_1}, {competitor_2}, and {competitor_3}",
    ],
}


# 6 大 AI 平台(用户可以手动复制提示词去查询)
AI_PLATFORMS = [
    ('ChatGPT', 'https://chat.openai.com'),
    ('Claude', 'https://claude.ai'),
    ('Perplexity', 'https://perplexity.ai'),
    ('Google Gemini', 'https://gemini.google.com'),
    ('豆包', 'https://www.doubao.com'),
    ('文心一言', 'https://yiyan.baidu.com'),
    ('通义千问', 'https://tongyi.aliyun.com'),
    ('Kimi', 'https://kimi.moonshot.cn'),
    ('DeepSeek', 'https://chat.deepseek.com'),
    ('腾讯元宝', 'https://yuanbao.tencent.com'),
]


def fill_prompts(brand, category='GEO tools', market='Chinese', use_case='AI visibility', competitor_1='Competitor A', competitor_2='Competitor B', competitor_3='Competitor C'):
    """填充提示词模板"""
    filled = []
    for category_name, prompts in PROMPT_CATEGORIES.items():
        filled.append((category_name, []))
        for p in prompts:
            filled_p = p.format(
                brand=brand,
                category=category,
                market=market,
                use_case=use_case,
                competitor_1=competitor_1,
                competitor_2=competitor_2,
                competitor_3=competitor_3,
            )
            filled[-1][1].append(filled_p)
    return filled


def main():
    parser = argparse.ArgumentParser(description='15 个 GEO 提示词测试')
    parser.add_argument('brand', nargs='?', help='你的品牌名')
    parser.add_argument('--brand', help='品牌名(同位置参数)')
    parser.add_argument('--category', default='GEO tools', help='产品/服务类别(英文)')
    parser.add_argument('--market', default='China', help='目标市场(英文)')
    parser.add_argument('--use-case', default='AI visibility', help='应用场景(英文)')
    parser.add_argument('--competitor-1', default='Competitor A', help='竞品 1')
    parser.add_argument('--competitor-2', default='Competitor B', help='竞品 2')
    parser.add_argument('--competitor-3', default='Competitor C', help='竞品 3')
    parser.add_argument('--output', default='prompt_15_output.md', help='输出文件')

    args = parser.parse_args()
    brand = args.brand or (sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else None)

    if not brand:
        parser.print_help()
        return

    print(f"\n{'='*60}")
    print(f"  🎯 GEO 15 提示词生成器")
    print(f"  品牌: {brand}")
    print(f"  类别: {args.category}")
    print(f"  市场: {args.market}")
    print(f"{'='*60}\n")

    # 生成填充后的提示词
    filled = fill_prompts(
        brand=brand,
        category=args.category,
        market=args.market,
        use_case=args.use_case,
        competitor_1=args.competitor_1,
        competitor_2=args.competitor_2,
        competitor_3=args.competitor_3,
    )

    # 输出
    print(f"  15 个测试提示词(7-5-3 黄金分布):\n")
    output_md = [f"# GEO 15 提示词测试 - {brand}", ""]
    output_md.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    output_md.append(f"**品牌**: {brand}")
    output_md.append(f"**类别**: {args.category}")
    output_md.append(f"**市场**: {args.market}")
    output_md.append("")
    output_md.append("---")
    output_md.append("")

    for cat, prompts in filled:
        print(f"  📋 {cat}:")
        output_md.append(f"## {cat}")
        output_md.append("")
        for i, p in enumerate(prompts, 1):
            print(f"    {i}. {p}")
            output_md.append(f"{i}. {p}")
        print()
        output_md.append("")

    # 输出测试说明
    print(f"  📊 接下来怎么用:")
    print(f"  1. 复制每个提示词")
    print(f"  2. 粘贴到 6 大 AI 平台")
    print(f"  3. 记录:是否提到 {brand}")
    print(f"  4. 计算:出现次数 / 15 = 引用率")
    print()

    output_md.append("---")
    output_md.append("")
    output_md.append("## 使用方法")
    output_md.append("")
    output_md.append("1. 复制每个提示词")
    output_md.append(f"2. 粘贴到 6 大 AI 平台")
    output_md.append(f"3. 记录:是否提到 {brand}")
    output_md.append(f"4. 计算:出现次数 / 15 = 引用率")
    output_md.append("")
    output_md.append("## 评分标准")
    output_md.append("")
    output_md.append(f"- **0-3 次**:弱(GEO 起步阶段)")
    output_md.append(f"- **4-7 次**:中(初见效果)")
    output_md.append(f"- **8-11 次**:强(内容被 AI 认可)")
    output_md.append(f"- **12-15 次**:很强(行业权威)")
    output_md.append("")
    output_md.append("## 10 个 AI 平台")
    output_md.append("")
    for name, url in AI_PLATFORMS:
        output_md.append(f"- [{name}]({url})")
    output_md.append("")

    # 保存
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_md))
    print(f"  ✅ 已保存到 {args.output}")
    print()


if __name__ == "__main__":
    main()
