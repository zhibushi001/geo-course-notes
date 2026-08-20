# 🧠 GEO 知识体系(整合版)

> **整合资料源**:
> - Princeton GEO 原论文(KDD 2024) - 学术界 GEO 起点
> - Auriti-Labs/geo-optimizer-skill(⭐721) - 47 个研究方法
> - AutoGEO(ICLR 2026) - 学术最新进展
> - C-SEO Bench(2025) - 内容优化 vs 基础设施的实证
> - 企业 GEO 实战课程笔记(20 课)

---

## 一、GEO 是什么?(从学术到实战)

### 1.1 学术定义 (Princeton, 2024)

> **Generative Engine Optimization (GEO)** is the first novel paradigm to aid content creators in improving their content visibility in generative engine responses through a flexible black-box optimization framework.
>
> **核心结论**:GEO 可以让内容在 AI 回答里**提升最高 40% 的可见度**。

### 1.2 通俗理解

- **传统 SEO**:让百度/Google 把你列在结果列表(人找信息)
- **GEO**:让 ChatGPT/豆包/Claude 在回答时**提到你、引用你**(AI 找人)
- **类比**:SEO 是优化"货架上的位置",GEO 是优化"AI 大脑里的印象"

### 1.3 与传统营销的本质区别

| 维度 | 传统营销 | GEO |
|---|---|---|
| 用户行为 | 人搜索 → 看链接 → 点开 | 人提问 AI → 看总结 → 可能没机会点开 |
| 流量分发 | 看排名/SERP | 看 AI 的引用源 |
| 关键指标 | 排名/点击率 | **引用率/提及率** |
| 内容形式 | 文章/网页 | **AI 友好的结构化内容** |
| 投入产出 | 投广告 → 立即有流量 | 优化内容 → **长期被 AI 推荐** |

---

## 二、为什么要学 GEO?(为什么现在做)

### 2.1 数据层面

- **豆包月活 3.6 亿**(2025,字节跳动官方)
- **ChatGPT 周活 2 亿**(2024,OpenAI 官方)
- **传统搜索流量下降**:Google 搜索查询量首次出现下滑趋势(2024)
- **AI 流量入口**:搜索框变成对话框,**前 3-5 条被 AI 引用 = 流量大头**

### 2.2 企业层面

不做 GEO 的三个后果:
1. **AI 时代"百度平替人"** — 用户问 AI 时品牌从未被提及
2. **流量被竞品全抢** — AI 只推荐前几名,做了 GEO 的一直在
3. **传统营销死亡螺旋** — 百度竞价/抖音越来越贵,效果越来越差

### 2.3 个人层面

- **薪资**:入门 8000-15000 元/月,1-2 年经验 20000+
- **门槛**:不需要写代码,只需要会写文章
- **稀缺性**:2026 年 GEO 从业者仍严重不足

---

## 三、GEO 怎么做?(核心技术)

### 3.1 核心方法论

**(1) 技术基础设施** ⭐ 最重要!

> **C-SEO Bench (2025) 实证**:Most content manipulation is ineffective. **Infrastructure matters most**.

如果爬虫根本抓不到你的内容,内容写得再好也没用。

#### 必须配置:
- ✅ **robots.txt** 允许 AI 爬虫(GPTBot、ClaudeBot、PerplexityBot、Bytespider 等)
- ✅ **llms.txt** (类似 robots.txt 但专门给 LLM 看)
- ✅ **JSON-LD Schema** (WebSite/Organization/FAQPage/Article)
- ✅ **Meta 标签** (Title/Description/Canonical/Open Graph)
- ✅ **AI Discovery 文件**(`.well-known/ai.txt`、`/ai/summary.json` 等)

**(2) 内容优化**(GEO 早期论文焦点,但实际效果有限)

#### Princeton 论文(2024)提出的方法:
- 引用源(Cite Sources):**+30%**
- 加统计数据(Statistics):**+40%**
- 加引言/Quote:**+41%**
- 加流畅性优化(Fluency):**+29%**
- 易于理解(Simplify):**+15%**

#### C-SEO Bench (2025) 反驳:
> 大多数内容优化方法**效果很小甚至无效**,真正起作用的是技术基础设施 + 内容结构化。

**(3) 品牌权威**(Brand & Entity)

- Wikipedia/Wikidata 条目
- 知识图谱关联(LinkedIn/Crunchbase/About 页)
- 主题权威(Topic Authority):在一个领域内多页覆盖
- 实体一致性:跨页面同一品牌名称统一

**(4) 反作弊**(关键!)

#### 8 大反信号(被 AI 降低引用):
- ❌ CTA 弹窗过多
- ❌ 弹窗/弹层遮盖内容
- ❌ 内容单薄(少于 300 字)
- ❌ 关键词堆砌
- ❌ 缺少作者信息
- ❌ 样板内容占比过高
- ❌ 不实信息
- ❌ 隐性 SEO 操纵

#### 8 大提示词注入检测:
- ❌ 隐藏文字(背景同色)
- ❌ 不可见 Unicode
- ❌ HTML 注释里的 LLM 指令
- ❌ 单色文字(白色背景白字)
- ❌ 微小字号
- ❌ data-attr 注入
- ❌ aria-hidden 滥用
- ❌ CSS 隐藏

---

## 四、6 大主流 AI 平台特性

### 4.1 国内平台

| 平台 | 公司 | 月活 | 特点 | GEO 适配建议 |
|---|---|---|---|---|
| **豆包** | 字节跳动 | 3.6亿+ | 抖音内容生态,娱乐/电商强 | 短视频描述、热点话题 |
| **DeepSeek** | 深度求索 | 数千万 | 开源、推理强 | 技术内容、学术问题 |
| **文心一言** | 百度 | 数千万 | 中文知识图谱强 | 百度系内容、本地化信息 |
| **腾讯元宝** | 腾讯 | 数千万 | 微信生态、AI搜索 | 公众号内容、社交场景 |
| **阿里千问** | 阿里 | 数千万 | 电商场景强 | 商品评测、消费指南 |
| **Kimi** | 月之暗面 | 数千万 | 长文档处理 | 行业报告、白皮书 |

### 4.2 国际平台

| 平台 | 公司 | 特点 | GEO 适配建议 |
|---|---|---|---|
| **ChatGPT** | OpenAI | 综合最强 | 通用 GEO 优化 |
| **Claude** | Anthropic | 长文/技术强 | 深度技术内容 |
| **Perplexity** | Perplexity | 实时搜索+引用 | 时效性内容 |
| **Gemini** | Google | 多模态 | 图片+视频+文本结构化 |
| **Google AI Overviews** | Google | 搜索结果摘要 | SEO + GEO 双优化 |

### 4.3 平台差异化关键洞察

- **不同平台 GEO 优化方法不同**(C-SEO Bench 已证实)
- **多模态(Gemini/GPT-4o)**:图片 alt、视频字幕、AudioObject schema 必做
- **Perplexity 独特**:实时搜索结果,内容更新要及时
- **国内平台**:中文表达 + 本地化数据 + 短视频整合

---

## 五、GEO 评估指标

### 5.1 GEO 评分维度(Auriti-Labs 8 大类,共 100 分)

| 维度 | 分值 | 核心检查项 |
|---|---|---|
| **Robots.txt** | 18 | 27 个 AI bot 是否被允许 |
| **llms.txt** | 18 | 是否存在且结构完整 |
| **Schema JSON-LD** | 16 | 多类型 schema 是否完整 |
| **Meta 标签** | 14 | title/description/canonical/OG |
| **内容质量** | 12 | H1/统计/引用/列表/表格 |
| **品牌权威** | 10 | 知识图谱/About 页/Topic Authority |
| **信号** | 6 | RSS/Atom/日期新鲜度 |
| **AI Discovery** | 6 | `.well-known/ai.txt` 等 |

**评分等级**:
- 86-100:优秀
- 68-85:良好
- 36-67:基础
- 0-35:关键缺失

### 5.2 引用质量评分(47 个方法,0-100)

最有效的 5 个方法(Auriti-Labs 实证):
1. **引言/Quote** +41%
2. **统计数据** +33%
3. **流畅性** +29%
4. **引用源** +27%
5. **权威性表述** +25%

### 5.3 引用率(实际被 AI 提及)

最直接指标:
- 在 ChatGPT/Perplexity/Claude 中**主动提问**:你的品牌是否被提及?
- 你所在的关键词搜索结果中,你出现在前 3 条的概率
- 你被 AI 引用的次数(可手工统计或用 Perplexity API)

---

## 六、GEO 实战路径(7 阶段)

### 阶段 1:技术基础设施(1 周)

**Day 1-2:配置 robots.txt**
```
User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Bytespider  # 豆包
Allow: /
```

**Day 3:创建 llms.txt**
```markdown
# YourBrand
> 一句话描述你的业务

## 产品/服务
- [产品A](URL):简短描述
- [产品B](URL):简短描述

## 关于我们
- [公司介绍](URL)
- [联系我们](URL)
```

**Day 4-5:添加 JSON-LD Schema**

**Day 6-7:配置 Meta + AI Discovery 文件**

### 阶段 2:内容审计与改造(2 周)

**做一次 GEO 评分**:
- 用 geo-optimizer-skill 跑一遍你的网站
- 看哪几个维度分低
- 优先修 0-35 分的"关键缺失"项

### 阶段 3:内容生产(持续)

**每周 2-3 篇 GEO 友好文章**:
- H1 含主关键词
- 第一段开门见山(前 200 字含核心信息)
- 至少 1 个统计数据
- 至少 2 个外部权威引用
- FAQ 部分(用 FAQPage schema)
- 列表/表格丰富

### 阶段 4:品牌权威建设(2-3 个月)

- 创建 Wikipedia/Wikidata 条目
- LinkedIn/Crunchbase/About 页一致性
- 行业报告、白皮书发布
- 行业 KOL 提及

### 阶段 5:平台差异化(持续)

- 每周在 6 大平台测试同一问题
- 记录哪些平台提到你
- 调整内容以覆盖更多平台

### 阶段 6:监测与优化(持续)

- 月度 GEO 评分
- 季度内容审计
- 持续迭代

### 阶段 7:商业变现

- **路径 A:企业内控** — 省下每年数十万单元费
- **路径 B:求职就业** — 8000-15000 元起步,1-2 年经验 20000+
- **路径 C:副业接单** — 单子 5000 起,自由灵活

---

## 七、推荐工具

| 工具 | 用途 | 价格 |
|---|---|---|
| **geo-optimizer-skill** | 自建 GEO 评分 CLI | 开源(PyPI) |
| **AutoGEO** | 自动内容改写(ICLR 2026) | 开源(GitHub) |
| **Perplexity API** | AI 引用检查 | 按量付费 |
| **Brand24 / Mention** | 品牌提及监控 | 付费 |
| **Ahrefs** | 关键词 + GEO 综合 | 付费 |
| **Google Search Console** | Google AI Overview 监控 | 免费 |

---

## 八、关键认知与避坑

### 8.1 常见错误

❌ **错误 1:把 GEO 当 SEO**
- GEO 不是"AI 版的 SEO"
- 它的优化目标和手段都不同

❌ **错误 2:只写内容不搞基础设施**
- 2025 实证:基础设施 > 内容改写
- 爬虫都抓不到,写了等于白写

❌ **错误 3:刷提示词注入**
- AI 爬虫能识别隐藏文字、HTML 注释里的指令
- 一旦发现永久降权

❌ **错误 4:不做品牌权威**
- 只靠内容优化,很难突破"无品牌"的引用困境
- Wikipedia/About 页/Topic Authority 是长期资产

### 8.2 关键洞察

💡 **1.GEO 是一场马拉松,不是短跑**
- 3-6 个月积累,不要期待快速见效
- 但一旦建立,长期稳定

💡 **2.技术 + 内容两手抓**
- 漏一项都做不好

💡 **3.多平台差异化**
- 不要假设一个方法对所有平台有效

💡 **4.监测 > 优化**
- 先建立监测,知道现状,再优化

---

## 九、我的学习路径建议(给未来重装系统的我)

### 1. 先理解再动手(01-03 课)
- 为什么 GEO:从用户行为变化看趋势
- GEO 本质:不是 SEO 的 AI 版,新范式
- AI 流量变迁:流量入口在哪

### 2. 平台规则(04-05 课)
- 6 大主流 AI 模型特性
- 企业适配性判断

### 3. 关键词体系(06-08 课)
- 四层关键词体系
- 挖掘筛选优化

### 4. 信源与内容(09-12 课)
- GEO 信源矩阵
- 资料库搭建
- AI 偏好的内容创作逻辑
- 6 大类必收录内容

### 5. 合规与分发(13-15 课)
- 合规避坑
- 多平台适配
- 多平台分发

### 6. 监测与落地(16-18 课)
- 数据监测复盘
- 异常处理
- 企业落地方案

### 7. 求职变现(19-20 课)
- 求职方法论
- 课程总结

---

## 十、待验证 / 疑问清单

- [ ] **6 大平台的引用规则**是否真的差异化?(需要逐个测试)
- [ ] **GEO 评分公式**的具体权重?(8 维度分值是经验值,还是统计回归?)
- [ ] **中文 vs 英文** GEO 优化差异?
- [ ] **视频/音频** GEO 怎么优化?(Gemini 多模态)
- [ ] **企业级 vs 个人级** GEO 的不同策略?
- [ ] **付费 vs 免费 AI 平台**的引用机制差异?

---

## 📚 参考资料

### 学术论文(权威)

| 论文 | 年份 | 关键发现 |
|---|---|---|
| **[Princeton GEO 原论文]** (arXiv 2311.09735) | KDD 2024 | GEO 概念起点 / +40% 提升 |
| **[C-SEO Bench]** (arXiv 2506.11097) | NeurIPS 2025 | 内容优化大多无效,SEO 更有效 |
| **[Adversarial SEO for LLMs]** (arXiv 2406.18382) | 2024 | 隐藏文字 2.5x,反作弊警告 |
| **[AutoGEO]** (arXiv 2510.11438) | ICLR 2026 | 自动 GEO 框架 + RL |
| **[ConflictingQA]** (arXiv 2402.11782) | 2024 | LLM 如何处理矛盾信息 |
| **[When Search Meets LLMs]** (arXiv 2407.00128) | 2024 | Search4LLM & LLM4Search 综述 |
| **[Ranking Manipulation]** (arXiv 2406.03589) | 2024 | 提示词注入对排名的影响 |
| **[ConflictBank]** (arXiv 2408.12076) | 2024 | 740 万条 claim-evidence pairs |
| **Conductor 2026 AEO/GEO Benchmarks** | 2026 | 13770 domains / 2190万次搜索 / 1700万 AI 引用 |
| **State of AI Search Optimization 2026** | 2026 | Kevin Indig 分析 LLM 引用模式 |

### 开源工具

| 工具 | ⭐ | 用途 |
|---|---|---|
| **[amplifying-ai/awesome-generative-engine-optimization]** | 487 | 权威 GEO 资源清单 |
| **[Auriti-Labs/geo-optimizer-skill]** | 721 | 47 个研究方法 + 评分 CLI(PyPI) |
| **[cxcscmu/AutoGEO]** | 200 | 自动内容改写框架(ICLR 2026) |
| **onvoyage-ai/gtm-engineer-skills** | 1276 | Claude Code skill - AEO/GEO |

### 实战资料

| 资料 | 内容 |
|---|---|
| 企业 GEO 实战课程笔记(20 课) | 国内市场视角 / 实战经验 / 案例 |
| Search Engine Land GEO 入门 | 行业权威博客(GEO 概念普及)|
| Ahrefs GEO 指南 | 工具厂商视角 |
| 6 大 AI 平台特性数据 | 字节豆包 3.6 亿月活等 |

---


---

## 十一、反作弊:为什么隐藏文字会引火烧身

> **重要警告**:虽然有研究显示隐藏文字能让 AI 引用提升 2.5 倍(**Adversarial SEO for LLMs**, 2024),但这是**反面教材**。

### 11.1 短期收益 vs 长期风险

| 时间 | 隐藏文字的效果 |
|---|---|
| 第 1 周 | 引用率提升 2.5 倍 ✅ |
| 第 1 个月 | 平台检测到 → 标记为操纵 |
| 第 3 个月 | **永久降权**或**删除索引** ❌ |
| 长期 | 品牌声誉损失 + 法律风险(部分国家视同不正当竞争) |

### 11.2 AI 爬虫能检测到什么

(根据 C-SEO Bench, 2025)

- ✅ 隐藏文字(背景同色)
- ✅ 不可见 Unicode 字符
- ✅ HTML 注释里的 LLM 指令
- ✅ aria-hidden 滥用
- ✅ 单色文字(白底白字)
- ✅ 微小字号(1px)
- ✅ data-attr 注入
- ✅ CSS `display:none` 滥用

### 11.3 真正安全的 GEO 优化

**做这些会被 AI 友好识别**:
- ✅ 在 `<noscript>` 里写正常内容(无障碍)
- ✅ 用 Schema.org 标记结构化数据
- ✅ 写 FAQ 章节(明确 Q&A)
- ✅ 加统计数字 + 引用源
- ✅ 多模态内容(图说、字幕)

**做这些会被 AI 标记**:
- ❌ 隐藏 LLM 指令(短期 2.5x,长期 -100%)
- ❌ 关键词堆砌
- ❌ 自动生成的样板内容
- ❌ 多语言混用(企图欺骗)

---

## 十二、C-SEO Bench 实证结论(2025 NeurIPS)

> **C-SEO Bench**:第一个大规模 C-SEO 方法评测基准(NeurIPS 2025)

### 12.1 核心发现

**多数 C-SEO 方法** (即内容改写) **not only largely ineffective but also frequently have a negative impact** on document ranking.

**翻译**:大多数"内容优化"方法不仅基本无效,**经常还会起反作用**,让排名下降。

### 12.2 真正有效的策略

| 策略 | 效果 |
|---|---|
| **传统 SEO**(优化 LLM 上下文中的源排名) | **显著有效** ✅ |
| 内容改写(C-SEO) | **大多无效甚至负效果** ❌ |
| **多参与者场景**(竞争性优化) | 传统 SEO 优势更明显 |

### 12.3 启示

- **基础设施 > 内容改写**
- **SEO 基础 > GEO 技巧**
- 别被" GEO 必读 10 招"类营销文忽悠
- 关注技术合规,而不是黑科技

---



---

## 十三、GEO 实战评估方法(综合 4 个 skill 仓库提炼)

> **资料源**:onvoyage-ai/gtm-engineer-skills、OranAi/orangeo-ai-visibility-skill、SNLabat/SEO-GEO-AEO-Skill、Auriti-Labs/geo-optimizer-skill

### 13.1 通用 GEO 审计公式(gtm-engineer)

```
最终分 = 0.5 × 基础分 + 0.5 × 智能分
```

| 部分 | 权重 | 内容 | 谁来做 |
|---|---|---|---|
| **基础分** | 50% | 16 项确定性检查 | 脚本自动 |
| **智能分** | 50% | 6 维度内容评估 | 人/AI 评估 |

**好处**:基础分是客观可重复的,智能分弥补"AI 是否真愿意引用你"的判断。

### 13.2 6 维度内容评估(每项 0-5 分)

(综合 onvoyage-ai 和 OranAi 的方法)

| 维度 | 评估什么 | 加分技巧 |
|---|---|---|
| **Answer Readiness** | 内容能否直接回答用户问题 | **第一段含答案**,FAQ 块,定义先行 |
| **Quotability** | 内容能否被 AI 单独引用 | 对比表(+2.8x 引用),FAQ(+156%),自包含段落 |
| **Authoritativeness** | 来源是否权威 | 作者信息,引用源,统计数据,E-E-A-T |
| **Freshness** | 内容是否最新 | 日期标记,定期更新,新数据 |
| **Brand Identity** | 品牌一致性 | About 页,Wiki 关联,统一命名 |
| **Competitive Coverage** | 对比/替代内容 | vs 文章,替代方案,Top X 榜单 |

### 13.3 16 项基础检查(脚本自动跑)

**必做**:
1. **robots.txt** — AI 爬虫是否允许
2. **llms.txt** — 是否存在 + 结构
3. **sitemap.xml** — 是否完整
4. **JSON-LD Schema** — 多类型完整
5. **Meta Tags** — title/description/canonical/OG
6. **H1 结构** — 每页唯一 + 含主关键词
7. **页面速度** — Core Web Vitals
8. **AI Discovery 文件** — `.well-known/ai.txt` 等

**重要**:
9. **Schema 丰富度** — 5+ 属性
10. **Open Graph** — 完整
12. **多模态准备** — 图 alt/视频字幕
13. **RAG Chunk Readiness** — 内容分块友好
14. **Content Decay 检测** — 时效性衰退
15. **Platform Citation Profile** — 各平台就绪度
16. **Trust Stack Score** — 5 层信任

### 13.4 GEO 15 个提示词模板(OranAi 黄金法则)

> **7-5-3 分布**:7 类别发现 + 5 品牌评估 + 3 竞品对比

**类别发现(7 个)**:
1. Best `{category}` for `{market}` buyers in 2026
2. Top `{category}` tools for growing teams
3. Which `{category}` products are easiest to implement?
4. Compare leading `{category}` platforms
5. What `{category}` vendors do customers recommend?
6. Most trusted `{category}` for `{use_case}`
7. Affordable `{category}` alternatives

**品牌评估(5 个)**:
1. Is `{brand}` a good choice for `{category}`?
2. `{brand}` reviews, pros, and cons
3. `{brand}` pricing and plans
4. `{brand}` customer complaints and limitations
5. `{brand}` case studies and proof

**竞品对比(3 个)**:
1. `{brand}` vs `{competitor_1}`
2. Best alternatives to `{brand}`
3. `{brand}` compared with `{competitor_1}`, `{competitor_2}`, `{competitor_3}`

**用法**:每个季度跑一遍这 15 个提示词,记录哪些提到你、提到几次。

### 13.5 GEO 审计标准流程(SNLabat 4 步法)

> 借鉴自 SNLabat SEO-GEO-AEO-Skill

**Step 1:确认范围**
- Quick Audit(1-2 分钟,顶层评分)
- Full Audit(5-10 分钟,完整)

**Step 2:抓数据**(并行)
- 首页 + robots.txt + sitemap.xml
- About / Services / Case Studies / Blog / Contact / FAQ
- 用 `WebFetch` 工具,**不做假设**

**Step 3:分析信号**
- 16 项确定性 + 6 维度智能

**Step 4:写报告**
- 一句话判决 + 分数
- 事实 vs 建议分开
- 列出具体修复项
- 标明是"准备度"还是"实测引用"

### 13.6 我可以给你的实用工具

| 工具 | 作用 | 怎么用 |
|---|---|---|
| **GEO 15 提示词模板** | 测品牌引用情况 | 每季度在 6 大平台跑一遍,记录是否提到你 |
| **网站 GEO 自检清单** | 看自己网站准备度 | 用 13.3 的 16 项对照检查 |
| **竞品 GEO 监控** | 监测竞品 GEO 表现 | 跟踪竞品在 AI 答案中的出现频次 |
| **GEO 报告模板** | 客户/团队用 | 参考 SNLabat 的报告格式 |

---

## 十四、GEO 资源生态(2026 年 8 月)

### 14.1 主流 GEO Skill 仓库

| 仓库 | ⭐ | 定位 |
|---|---|---|
| **AgriciDaniel/claude-seo** | 14647 | Claude Code 通用 SEO/GEO 套件 |
| **onvoyage-ai/gtm-engineer-skills** | 1276 | 完整 GEO 审计 + 修复 skill |
| **Auriti-Labs/geo-optimizer-skill** | 721 | 47 方法 + 评分 CLI(PyPI) |
| **AgriciDaniel/codex-seo** | 599 | Codex AI 专用 SEO/GEO |
| **SNLabat/SEO-GEO-AEO-Skill** | 161 | Claude SEO 审计模板 |
| **OranAi-Ltd/orangeo-ai-visibility-skill** | 132 | GEO 准备度审计 |
| **amplifying-ai/awesome-geo** | 487 | GEO 资源权威清单 |

### 14.2 实战 GEO 报告参考(SNLabat 格式)

**报告结构**:
1. 一句话判决 + 总体分数
2. **事实**(已发现的问题)
3. **建议**(优先级排序的修复)
4. **评分细则**(各维度得分依据)
5. **下一步行动**(具体该做什么)

---

**最后更新**: 2026-08-20 (v2.2 - 整合 GEO skill 仓库实战评估方法)
**作者**: 整合自多源资料,经过对比验证
**联系方式**: zhibushi.com