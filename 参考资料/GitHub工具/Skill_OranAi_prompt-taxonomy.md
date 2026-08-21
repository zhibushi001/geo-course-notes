# Prompt Taxonomy

Use a 15-prompt set by default. It mirrors OranGEO's practical split: category discovery, brand evaluation, and competitor comparison.

## Default Mix

| Class | Count | Purpose |
| --- | ---: | --- |
| Category discovery | 7 | Test whether AI recommends the brand when buyers ask generic category questions. |
| Brand evaluation | 5 | Test what AI says when buyers already know the brand. |
| Competitor comparison | 3 | Test alternatives, comparisons, and competitive displacement risk. |

## Category Discovery Prompts

Adapt these to the user's category, buyer, region, and use case:

1. Best `{category}` for `{market}` buyers in 2026
2. Top `{category}` tools for growing teams
3. Which `{category}` products are easiest to implement?
4. Compare leading `{category}` platforms
5. What `{category}` vendors do customers recommend?
6. Most trusted `{category}` for `{use_case}`
7. Affordable `{category}` alternatives

## Brand Evaluation Prompts

1. Is `{brand}` a good choice for `{category}`?
2. `{brand}` reviews, pros, and cons
3. `{brand}` pricing and plans
4. `{brand}` customer complaints and limitations
5. `{brand}` case studies and proof

## Competitor Prompts

1. `{brand}` vs `{competitor_1}`
2. Best alternatives to `{brand}`
3. `{brand}` compared with `{competitor_1}`, `{competitor_2}`, and `{competitor_3}`

## Quality Bar

- Use buyer language, not SEO keyword stuffing.
- Include one comparison prompt even when competitors are vague.
- Use a market modifier when the category is regional.
- Keep brand-direct prompts out of category leaderboard scores.
- Keep prompt sets stable across refreshes so movement can be measured.
