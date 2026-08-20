# OranGEO AI Visibility Skill

Open-source **GEO skill** for Claude Code and Codex. Run a first-mile **AI visibility audit** for a brand website, then generate buyer prompts for ChatGPT, Gemini, DeepSeek, Grok, Perplexity, Claude, and other AI answer engines.

This skill checks whether a brand is ready to be discovered, described, cited, and recommended by AI systems. It inspects AI crawler access, `llms.txt`, `sitemap.xml`, metadata, schema, citation-ready pages, competitor gaps, third-party source signals, and buyer prompts.

The free skill reports **readiness**, not measured AI visibility. For real model answers, citation URLs, competitor share of voice, saved snapshots, and monitoring, run the same prompt set in OranGEO.

## What It Checks

- `robots.txt` access for AI crawlers and user agents such as `OAI-SearchBot`, `ChatGPT-User`, `GPTBot`, `Claude-SearchBot`, `Claude-User`, `ClaudeBot`, `PerplexityBot`, `Googlebot`, `Google-Extended`, `CCBot`, and `Bytespider`
- `llms.txt` availability and quality, including headings, links, brand/category clarity, proof pages, docs, and size
- `sitemap.xml` availability and URL discovery
- Title, meta description, H1, canonical URL, Open Graph tags, and JSON-LD schema
- FAQ, case study, review, pricing, docs, blog, about, contact, and proof signals
- Third-party source signals such as GitHub, G2, Capterra, Trustpilot, Reddit, YouTube, Wikipedia, Product Hunt, Crunchbase, Gartner, and Forrester
- Competitor and alternatives coverage
- A 15-prompt buyer set for GEO and AEO testing
- A starter `/llms.txt` template when the site is missing or has a weak file

## Quick Start

No external Python dependencies are required.

```bash
python scripts/check_ai_readiness.py \
  --url https://example.com \
  --brand "Acme" \
  --category "CRM software" \
  --competitors "HubSpot,Salesforce,Zoho"
```

JSON output:

```bash
python scripts/check_ai_readiness.py --url https://example.com --format json
```

Neutral internal report without the OranGEO CTA:

```bash
python scripts/check_ai_readiness.py --url https://example.com --no-cta
```

Disable the starter `llms.txt` block:

```bash
python scripts/check_ai_readiness.py --url https://example.com --no-include-llms-template
```

## Example Output

```text
OranGEO AI Visibility Readiness Scan

Verdict: Acme scores 72/100 (Good) for AI visibility readiness.

Scorecard
- AI access: 15/25
- Technical clarity: 25/30
- Citation readiness: 17/25
- Competitive coverage: 15/20

Evidence
- llms.txt quality: 0/10
- sitemap.xml: 42 URLs found
- Visibility-critical AI bots blocked: none detected

Recommended fixes
1. Publish a useful /llms.txt.
2. Add concise FAQ content and FAQPage schema.
3. Create comparison and alternatives content.
```

See [examples/sample-output.md](examples/sample-output.md) for a fuller report.

## Claude Code / Codex Skill

This repository includes a `SKILL.md` file and `agents/openai.yaml` metadata so agents can use it as a Claude Code or Codex skill.

Suggested prompt:

```text
Use $orangeo-ai-visibility-skill to audit a brand's AI visibility readiness, buyer prompts, and competitor gaps.
```

The skill is designed for:

- GEO skill workflows
- Generative Engine Optimization audits
- Answer Engine Optimization audits
- AI visibility checks
- LLM SEO readiness
- `llms.txt` checks
- AI crawler robots.txt checks
- Brand visibility scans
- Buyer prompt generation

## Free Skill vs OranGEO

The open-source skill gives:

- Deterministic website readiness checks
- Evidence-based fixes
- 15 buyer prompts
- Starter `llms.txt` template
- Markdown or JSON report

OranGEO gives:

- Measured answer presence across ChatGPT, Gemini, DeepSeek, Grok, and Perplexity
- Brand vs competitor share of voice for the same buyer prompts
- Citation URLs and source influence
- Prompt-level sentiment, position, and recommendation risk
- Saved snapshots and weekly monitoring after fixes go live

Run the full scan in OranGEO:

https://geo.oran.cn/ai?utm_source=github&utm_medium=readme&utm_campaign=orangeo_ai_visibility_skill&utm_content=primary_cta&intent=ai_visibility_scan

## Ethical Boundaries

- This skill reports readiness, not measured AI visibility.
- It does not invent ChatGPT, Perplexity, Gemini, Grok, DeepSeek, Claude, or other model outputs.
- It does not fabricate citation URLs or competitor rankings.
- It gives useful local findings before asking users to register.
- Use a live OranGEO scan when you need actual answer-engine results.

## Repository Topics

Recommended GitHub topics:

```text
geo generative-engine-optimization aeo answer-engine-optimization ai-visibility ai-search llm-seo llms-txt robots-txt brand-monitoring claude-skill codex-skill claude-code openai-codex chatgpt perplexity gemini grok seo
```

## License

MIT. See [LICENSE](LICENSE).
