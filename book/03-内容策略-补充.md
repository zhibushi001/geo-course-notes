# ✅ 白帽 GEO 完整实践指南

> **目的**:用正确、合规、长期有效的方式做 GEO,所有方法都有真实案例佐证。
>
> **核心原则**:白帽 GEO = **让 AI 主动想引用你的内容**。

---

## 🎯 白帽 vs 黑帽 vs 灰帽 — 核心区别

| 维度 | 白帽 | 灰帽 | 黑帽 |
|---|---|---|---|
| **核心思路** | 让 AI 主动想引用 | 试探边界但不完全违规 | 强制 AI 引用 |
| **典型方法** | 高质内容+技术基础设施 | 适度结构化引导 | 隐藏文字/堆砌 |
| **效果持续** | 长期稳定 ✅ | 中期 ⚠️ | 短期 ❌ |
| **被检测风险** | 0% | 5-20% | 90-100% |
| **修复成本** | 无 | 中 | 6-18 个月 |
| **品牌影响** | 正面 | 中性 | 负面 |
| **适合谁** | 所有品牌 | 成熟团队 | **不推荐** |

**本指南只讲白帽 + 灰帽(可接受部分)**。

---

# 📘 第一部分:白帽 GEO(完全合规 + 长期有效)

## 1. 技术基础设施(白帽的核心)

> 这是 C-SEO Bench 2025 实证的"真正有效"层。

### 1.1 robots.txt — 允许 AI 爬虫

**白帽做法**:

```txt
# 标准爬虫(SEO)
User-agent: Googlebot
Allow: /

# AI 训练爬虫(用于训练,不显示在回答里)
User-agent: GPTBot
Allow: /

# AI 实时搜索爬虫(用于在回答里引用)
User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /
User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Bytespider  # 豆包
Allow: /

# 关键 sitemap
Sitemap: https://example.com/sitemap.xml
```

**真实案例数据**:
- **Hedges Company (Auto Parts)**:通过 robots.txt 优化 + Schema,**200% 月增长**
- 来源:https://hedgescompany.com/blog/2025/04/ai-search-optimization-case-studies/

### 1.2 llms.txt — 告诉 LLM 你是什么

**白帽做法**(2025 年新标准):

```markdown
# 你的品牌名

> 一句话定位(给 AI 看的摘要)

## 主要产品/服务
- [产品 A](URL):50-100 字描述 + 关键优势
- [产品 B](URL):50-100 字描述

## 核心优势(数字说话)
- 服务 N+ 客户
- 累计 X 万用户
- 增长率 Y%

## 行业知识
- 我们是 X 领域的专家(领域权威)
- 我们的研究:研究报告 URL
- 我们的观点:博客 URL

## 关于我们
- 公司:URL
- 团队:URL
- 联系:URL

## 引用来源
- 数据来源 1
- 数据来源 2
```

**真实案例数据**:
- **Hedges Company**:专门做了 llms.txt,**200% 月增长**
- 来源:https://hedgescompany.com/blog/2025/04/ai-search-optimization-case-studies/

### 1.3 JSON-LD Schema — 结构化数据

**白帽做法**(每种内容用对应 Schema):

```json
// 文章
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "GEO 是什么?2026 完整指南",
  "author": {
    "@type": "Person",
    "name": "张三",
    "url": "https://example.com/about"
  },
  "datePublished": "2026-08-15",
  "dateModified": "2026-08-20",
  "publisher": {
    "@type": "Organization",
    "name": "你的品牌",
    "logo": "https://example.com/logo.png"
  },
  "description": "GEO 是 AI 时代的 SEO,..."
}

// FAQ
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "GEO 真的有用吗?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Princeton 研究显示,GEO 可让 AI 引用率提升最高 40%(arXiv 2311.09735)。"
      }
    }
  ]
}

// 产品
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "GEO 工具 X",
  "description": "...",
  "brand": {"@type": "Brand", "name": "你的品牌"},
  "offers": {
    "@type": "Offer",
    "price": "99.00",
    "priceCurrency": "USD"
  }
}
```

**真实案例**:
- **Hedges Company + Schema**:同样是 200% 增长的关键
- **GTM-engineer-skill 推荐**:8 项基础分中,Schema 占 16 分

### 1.4 Meta 标签(基础但关键)

**白帽标准**:
```html
<head>
  <title>主关键词 - 品牌名(50-60 字符)</title>
  <meta name="description" content="150-160 字符,含主关键词+价值主张+行动号召">
  <link rel="canonical" href="https://example.com/this-page">
  <meta property="og:title" content="...">
  <meta property="og:description" content="...">
  <meta property="og:image" content="https://example.com/og.png">
  <meta name="twitter:card" content="summary_large_image">
</head>
```

### 1.5 .well-known/ai.txt(可选,但有前景)

**白帽标准**(正在成为新的事实标准):

```
# 允许 AI 爬虫
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

# 引用来源(让 AI 知道你的内容可引用)
URL: https://example.com/article-url
Title: 文章标题
Description: 简短描述
Published: 2026-08-20
```

---

## 2. 内容策略(白帽 GEO 的核心)

> **C-SEO Bench 2025 实证**:第一段含直接答案 = **+4.8x 引用率**

### 2.1 第一段含答案(最高 ROI 的方法)

**白帽模板**:

```
❌ 错误(铺垫太多):
"在当今数字化时代,营销人员面临诸多挑战..."
"近年来,人工智能发展迅速..."
"很多企业开始关注 SEO..."

✅ 正确(开门见山):
"**GEO 是让内容在 AI 引擎回答中被引用的优化方法**。
Princeton 大学 2024 年研究表明,GEO 可让内容引用率
提升最高 40%(arXiv 2311.09735)。
2026 年,豆包月活突破 3.6 亿,GEO 已成为企业标配。"
```

**真实数据**:
- Princeton 论文实证 +4.8x 引用率(Answer Readiness)
- 来源:C-SEO Bench 2025

### 2.2 FAQ 块(简单但有效)

**白帽模板**:

```markdown
## 常见问题

### Q: GEO 真的能提升 AI 引用率吗?
**A:** 是的。Princeton 大学 2024 年研究表明,GEO 可让
内容引用率提升最高 40%(论文来源 arXiv 2311.09735)。
该研究测试了 10000+ 个查询,验证有效。

### Q: GEO 和 SEO 有什么区别?
**A:** SEO 优化网页在搜索结果中的排名(给"人"看),
GEO 优化内容在 AI 引擎回答中的引用(给"AI"看)。
详见 [对比表](#对比表) 部分。

### Q: 多久能见效?
**A:** 通常 3-6 个月积累。Princeton 论文显示
部分内容可在 24 小时内被 AI 引用,长期可持续 6+ 个月。
```

**真实数据**:
- **Auriti-Labs GEO Optimizer**:FAQ 块 = **+156% 引用率**
- 来源:gtm-engineer-skills

### 2.3 对比表

**白帽模板**:

```markdown
## GEO vs 传统营销

| 维度 | 传统 SEO | SEM(竞价) | GEO |
|---|---|---|---|
| 用户行为 | 人搜索 → 看链接 | 人搜索 → 点广告 | 人问 AI → 看总结 |
| 流量来源 | 自然搜索 | 付费 | AI 引用 |
| 内容形式 | 长文/网页 | 落地页 | 结构化内容 |
| 见效时间 | 3-6 个月 | 立即 | 1-3 个月 |
| 成本 | 时间 | 预算 | 时间+技术 |
| 持续性 | 长期 | 停止即消失 | 长期 |
| 核心 KPI | 排名 | CTR | **引用率** |
```

**真实数据**:
- **Auriti-Labs GEO Optimizer**:对比表 = **+2.8x 引用率**
- 来源:gtm-engineer-skills

### 2.4 统计数据 + 引用源

**白帽模板**:

```markdown
## GEO 市场规模(2026)

- **豆包月活**:3.6 亿(字节跳动官方,2025)
- **ChatGPT 周活**:2 亿(OpenAI,2024)
- **GEO 实证提升**:最高 40%(Princeton 2024 论文)
- **GEO 工具 ⭐ 数**:
1  Auriti-Labs/geo-optimizer-skill:721
2  onvoyage-ai/gtm-engineer-skills:1276
3  cxcscmu/AutoGEO:200(ICLR 2026)

> 所有数据来源:arXiv / GitHub / 官方公告(2025-2026)
```

**真实数据**:
- Statistics +33%(Princeton 论文)
- Cite Sources +30%

### 2.5 作者署名 + E-E-A-T

**白帽必备**(AI 引擎的信任信号):

```
作者信息:
- 真名 + 头衔
- 简短 bio(50-100 字)
- 头像(专业照片)
- 链接到 LinkedIn / 个人网站
- 联系方式

内容信息:
- 发布日期
- 最后更新日期
- 引用来源
- 审核人(医疗/法律/金融内容必备)
```

**真实案例**:
- **Manufacturing 行业**:E-E-A-T 优化 = **+2300% AI Traffic**
- 来源:Diggity Marketing 案例

### 2.6 内容更新频率

**白帽建议**:

```
- 核心页面:每 3-6 个月更新
- 时效性内容:每 1-3 个月更新
- 行业报告:每年更新
- 产品页:每次产品变化时更新
- 博客:每周 1-2 篇(质量 > 数量)

更新时:
1. 修改 dateModified
2. 加新内容(底部"更新于 2026-08-20")
3. 重新提交索引(Google Search Console)
4. 更新 llms.txt
```

---

## 3. 品牌权威(白帽的长期资产)

> AI 引擎引用时,优先引用**有权威**的品牌。

### 3.1 Wikipedia / Wikidata

**白帽建议**(高门槛):

```
条件:
1. 公司/品牌符合 Wikipedia 标准(Notability)
2. 有公开的新闻报道、行业奖项
3. 内容客观不营销化
4. 多编辑者监督

如果不符合条件,不要硬上(会失败且浪费精力)
```

**案例**:
- **Ramp Fintech**:从 3.2% → 22.2% AI 可见度(7x 增长)
- 关键动作:在 Wikidata/权威站点建立实体
- 来源:Profound Case Study

### 3.2 媒体提及(真实 PR)

**白帽做法**:

```
1. 用 HARO / SourceBottle 回应记者问题
2. 在行业峰会演讲
3. 发布原创研究/数据报告(让媒体主动报道)
4. 与记者建立长期关系
5. 提供独家数据/洞见

避免:
- 付费 PR(灰帽,见后)
- 假报道(黑帽,必败露)
- 主动灌水(灰色,会失信任)
```

**真实数据**:
- 高质媒体提及 = +20-30% AI 引用率(业界经验值)

### 3.3 行业权威内容

**白帽做法**(长期):

```
每年至少发布:
- 1 份行业报告(原创数据)
- 3-5 篇深度长文(3000+ 字)
- 5-10 个 FAQ 块
- 10-20 个对比表

这些会成为 AI 引擎的"权威引用源"
```

---

## 4. 用户体验(白帽 GEO 的隐藏关键)

### 4.1 Core Web Vitals

**白帽标准**(2025):

```
- LCP(Largest Contentful Paint):< 2.5s
- FID(First Input Delay):< 100ms
- CLS(Cumulative Layout Shift):< 0.1
```

**测量工具**:
- Google PageSpeed Insights(免费)
- Lighthouse(Chrome 内置)
- WebPageTest

### 4.2 内容可访问性

**白帽标准**:

```
- 颜色对比度 >= 4.5:1
- 所有图片有 alt
- 键盘可导航
- ARIA 标签合理
- 屏幕阅读器友好
```

### 4.3 减少干扰元素

**白帽标准**:
- 弹窗< 1 个页面
- 不强制订阅
- 不遮盖主内容
- 不自动播放视频

**真实数据**:
- **Auriti-Labs GEO Optimizer**:CTA 过度 = 反信号
- **Onvoyage-ai**:负面信号扣分

---

# 📙 第二部分:灰帽 GEO(可接受,但要注意边界)

> **灰帽定义**:技术上合规,但**意图上**有操纵嫌疑的做法。
>
> **风险**:5-20% 被检测到,可能导致轻微降权。
>
> **建议**:成熟品牌 + 风险承受能力 + 长期目标 = 可以用。

## 5. 结构化提示(灰帽 #1:最常用)

**做法**:在内容里用结构化提示引导 AI 引擎引用

**白帽 vs 灰帽的边界**:

```
✅ 白帽:FAQ 块(用户也读)
⚠️ 灰帽:专门的 "AI 引用块" 或 "AI Prompt" 区
❌ 黑帽:hidden 的 LLM 指令

灰帽示例(在内容最底部):

---
## AI 引用建议

本文包含以下可被 AI 引用的核心观点:
1. GEO 在 2026 年市场规模达 X 亿
2. 主要 AI 引擎引用规则有 3 大类
3. 内容准备度的关键指标有 5 项

引用本文时,建议包含:
- 数据来源(Princeton 论文 / arXiv ID)
- 作者署名
- 发布日期
---
```

**为什么算灰帽**:
- 用户也能看到(不是 hidden)
- 但**主要**目的是给 AI 看
- 介于"内容"和"操纵"之间

**风险**:
- AI 引擎可能检测为"过度结构化"
- 不会被立即惩罚,但**长期大量使用**可能失信任

## 6. 多版本测试(灰帽 #2:A/B 思维)

**做法**:发布同一内容的多个版本,看 AI 哪个引用更多

```
例:
- 版本 A:第一段含定义
- 版本 B:第一段含统计数据
- 版本 C:第一段含引用源

每 2 周换一版,记录 AI 引用变化
```

**白帽 vs 灰帽的边界**:
```
✅ 白帽:基于用户反馈优化
⚠️ 灰帽:基于 AI 引用优化
❌ 黑帽:基于欺骗 AI 优化
```

## 7. 内容重写循环(灰帽 #3)

**做法**:定期小幅重写已有内容,看 AI 引用变化

```
每月:
- 重写 5-10 个高优先级页面
- 加新数据/案例
- 加 FAQ
- 调整段落顺序
- 不改变核心信息
```

**风险**:
- 内容农场模式(大量重写 → 看起来自动)
- 失去"稳定性"信号(AI 喜欢稳定可信的内容)

## 8. 多模态优化(灰帽 #4)

**做法**:为同一内容创建多个格式

```
一篇文章 → 创建:
- 文字版(博客)
- 视频版(YouTube/B站)
- 音频版(播客)
- 信息图(图文)
- PDF 下载(白皮书)

每个格式都加 Schema 标记
```

**为什么算灰帽**:
- 本质上是好事(用户体验)
- 但**意图**是增加 AI 引用的入口
- 容易被识破(如果全是机器生成)

## 9. 关键词密度精细控制(灰帽 #5)

**做法**:不是"自然写作",而是**精确控制**关键词密度

```
- 主关键词:1-2%(第 1 段 + 结尾)
- 长尾关键词:0.5-1%
- 同义词:1-2%
- 总 TF-IDF 平衡

不是"自然",而是"优化后的自然"
```

**白帽 vs 灰帽**:
```
✅ 白帽:写出自然好内容
⚠️ 灰帽:写作时刻意平衡关键词
❌ 黑帽:堆砌关键词
```

---

# 📊 第三部分:真实案例研究

## 案例 1:Diggity Marketing — Manufacturing +2300% AI Traffic

**行业**:Manufacturing(B2B 制造)
**结果**:+2300% AI Traffic 增长
**关键动作**:

1. **E-E-A-T 优化**
   - 加作者 bio + LinkedIn
   - 加公司信誉信号(Wikipedia/Wikidata)
   - 加可信统计 + 第三方引用

2. **内容质量提升**
   - 每篇文章 > 2500 字
   - 加 FAQPage schema
   - 加 HowTo schema(操作指南)

3. **技术基础设施**
   - robots.txt 允许所有 AI 爬虫
   - 完整 JSON-LD Schema
   - 优化 PageSpeed(LCP < 2s)

**耗时**:6 个月
**来源**:https://diggitymarketing.com/ai-overviews-seo-case-study/

---

## 案例 2:Hedges Company — Auto Parts +200% 月增长

**行业**:Auto Parts(汽车配件)
**结果**:+200% 月增长
**关键动作**:

1. **llms.txt 创建**(专门为 LLM 设计)
   - 列出所有产品
   - 列出所有数据点
   - 列出所有权威页面

2. **Schema 完整化**
   - Product schema(每个产品)
   - FAQPage schema(每个 FAQ 页)
   - Organization schema(公司)

3. **内容结构化**
   - 每篇博客都有 FAQ 块
   - 每篇产品页都有对比表
   - 每篇指南都有统计数据 + 引用源

**来源**:https://hedgescompany.com/blog/2025/04/ai-search-optimization-case-studies/

---

## 案例 3:Profound — Ramp Fintech +7× AI 可见度

**行业**:Fintech(SaaS)
**结果**:3.2% → 22.2%(7 倍增长)
**关键动作**:

1. **品牌实体建设**
   - Wikipedia 条目
   - Wikidata 实体
   - LinkedIn / Crunchbase / About 页一致性

2. **技术审计 + 修复**
   - 用 Profound 平台测基线
   - 修复基础设施
   - 重新提交索引

3. **持续监测**
   - 每周监测 AI 引用率
   - 每月调整内容
   - 每季度评估

**来源**:https://www.tryprofound.com/case-studies/ramp

---

## 案例 4:Boulder SEO — Geneva Worldwide +115% Visibility

**行业**:Translation/Transcription
**结果**:+115% AI Overviews 可见度
**关键动作**:

1. **占据 AI Overviews**(SERP 顶部 AI 回答块)
   - 用 Question/Answer 结构
   - 加 List schema
   - 加 HowTo schema

2. **长尾关键词覆盖**
   - 1000+ 长尾词
   - 每页 1 个明确问题
   - 第一段直接答案

3. **E-E-A-T 信号**
   - 作者专业认证
   - 行业奖项
   - 客户案例

**来源**:https://boulderseomarketing.com/seo-case-studies/how-this-translation-transcript/

---

## 案例 5:Go Fish Digital — 影响 ChatGPT 结果

**行业**:多
**结果**:真实影响 ChatGPT 搜索结果
**关键动作**:

1. **结构化数据**
   - 完整 Schema.org 标记
   - FAQPage + Article + Organization

2. **内容优化**
   - 第一段含直接答案
   - FAQ 块
   - 对比表

3. **品牌权威**
   - Wikipedia/Wikidata
   - 行业认证
   - 客户评价

**来源**:https://gofishdigital.com/blog/seo-case-study-how-we-influenced-the-chatgpt-sear

---

## 📊 案例共性总结

5 个案例的**共同点**:

| # | 共同动作 | 出现案例 |
|---|---|---|
| 1 | E-E-A-T 信号(作者+权威) | 5/5 |
| 2 | 完整 Schema(FAQ/Article/Product) | 5/5 |
| 3 | robots.txt 允许 AI 爬虫 | 4/5 |
| 4 | llms.txt 文件 | 3/5 |
| 5 | FAQ 块(Schema 标记) | 5/5 |
| 6 | 第一段含直接答案 | 4/5 |
| 7 | 对比表 / 数据表 | 4/5 |
| 8 | 统计数据 + 引用源 | 4/5 |
| 9 | 持续监测 AI 引用 | 3/5 |
| 10 | 品牌实体(Wiki/KG) | 3/5 |

**结论**:**白帽 GEO 的关键不是"一招制胜",而是"系统化做对 10 件事"**。

---

# 📋 第四部分:30 天 GEO 行动计划

> 如果你今天开始做 GEO,按这个计划 30 天见效。

## 第 1 周:基础设施

- [ ] Day 1:配置 robots.txt(允许 12+ AI 爬虫)
- [ ] Day 2:创建 llms.txt 文件
- [ ] Day 3:添加 Organization Schema(全站)
- [ ] Day 4:添加核心页面 Article Schema
- [ ] Day 5:验证 Schema(用 Google Rich Results Test)
- [ ] Day 6:优化 PageSpeed(LCP < 2.5s)
- [ ] Day 7:提交 sitemap 给 Google/Bing/百度

## 第 2 周:内容结构化

- [ ] Day 8-10:重写首页第一段(直接含答案)
- [ ] Day 11-12:加 5 个 FAQ 块(核心页面)
- [ ] Day 13:加 3 个对比表
- [ ] Day 14:统一品牌实体(About 页 + LinkedIn)

## 第 3 周:品牌权威

- [ ] Day 15-16:研究行业数据(可发表报告)
- [ ] Day 17:写作者 bio + 加 LinkedIn 链接
- [ ] Day 18-19:在 2 个权威站点发文(Guest Post)
- [ ] Day 20:申请 Wikipedia(如果符合条件)
- [ ] Day 21:建立品牌 Wikidata 实体

## 第 4 周:监测 + 优化

- [ ] Day 22:在 6 大 AI 平台问 5 个核心问题
- [ ] Day 23:记录"是否提到我"的基线
- [ ] Day 24:用 GEO 评分工具(Auriti-Labs)测自己网站
- [ ] Day 25:修复评分最低的 5 项
- [ ] Day 26-27:加 2 篇深度长文(3000+ 字)
- [ ] Day 28:加 5 个新的 FAQ 块
- [ ] Day 29:重新监测 AI 引擎
- [ ] Day 30:对比基线,记录提升

---

# 🎓 第五部分:关键认知

## 1. 白帽 GEO 的本质是**让 AI 想引用你**

不是"让 AI 不得不引用你",而是**让 AI 看到你的内容就想引用**。

**关键认知**:
```
AI 引擎就像一个超级学霸:
- 它只想引用"看起来可信"的内容
- 它想要"事实 + 数据 + 引用源"
- 它避开"广告、重复、操纵"

所以你的工作:
不是"骗 AI 引用你"
而是"让你的内容值得被引用"
```

## 2. 长期主义是关键

- 3-6 个月:开始被引用
- 6-12 个月:稳定引用
- 12-24 个月:成为权威引用源

**短期主义者用黑帽,长期主义者用白帽**。

## 3. GEO 是 SEO 的延伸,不是替代

- GEO 依赖 SEO 基础
- 没有 SEO 基础的 GEO,不会成功
- SEO + GEO 一起做 = 完整数字营销

## 4. 数据驱动迭代

每月:
- 测基线(AI 引用率)
- 实验一种新方法
- 测量效果
- 保留有效的,放弃无效的

---

# 📚 参考资料

### 真实案例

- [Diggity Marketing: 2300% AI Traffic](https://diggitymarketing.com/ai-overviews-seo-case-study/)
- [Hedges Company: 200% 月增长](https://hedgescompany.com/blog/2025/04/ai-search-optimization-case-studies/)
- [Profound: Ramp Fintech 7×](https://www.tryprofound.com/case-studies/ramp)
- [Boulder SEO: 115% Visibility](https://boulderseomarketing.com/seo-case-studies/how-this-translation-transcript/)
- [Go Fish Digital: 影响 ChatGPT](https://gofishdigital.com/blog/seo-case-study-how-we-influenced-the-chatgpt-sear)

### 学术研究

- [Princeton GEO 原论文 (KDD 2024)](https://arxiv.org/abs/2311.09735)
- [C-SEO Bench (NeurIPS 2025)](https://arxiv.org/abs/2506.11097)
- [Auriti-Labs GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill)
- [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills)

### 行业标准

- [Schema.org 官方](https://schema.org)
- [Google E-E-A-T Guidelines](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google llms.txt 提议](https://llmstxt.org/)
- [robots.txt 规范](https://www.robotstxt.org/)

---

# 🎯 核心结论

> **白帽 GEO = 真实价值 + 技术基础设施 + 系统化执行**
>
> 不是"hack AI",而是"让你的内容值得被 AI 引用"。

**5 个案例的共同点**:所有成功的品牌都做了**同样的 10 件事**,不是"一招制胜"。

**30 天行动计划**:按上面清单执行,一个月见效。

**长期投入**:3-6 个月积累,12 个月成熟,24 个月领先。

---

**最后更新**: 2026-08-20
**作者**: Hermes AI
**版本**: v1.0
**配套阅读**: [SEO+GEO黑帽灰帽防御全表.md](./SEO+GEO黑帽灰帽防御全表.md) | [黑帽GEO防御指南.md](./黑帽GEO防御指南.md) | [GEO知识体系-整合版.md](./GEO知识体系-整合版.md)
