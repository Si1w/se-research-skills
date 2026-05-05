# Persuasion Principles for Skill Design

Understanding WHY compliance techniques work helps you apply them systematically when writing discipline-enforcing skills.

Based on: Cialdini (2021) influence principles, Meincke et al. (2025) testing with N=28,000 AI conversations — compliance increased from 33% to 72%.

## The Seven Principles

### 1. Authority
Skills written as expert guidance carry more weight.
- **Apply:** Use definitive language ("The Iron Law", "MANDATORY", "NEVER")
- **Apply:** Reference real-world impact data ("95% first-time fix rate")

### 2. Commitment & Consistency
Once an agent starts following a process, it tends to continue.
- **Apply:** Start with small, easy steps that establish the pattern
- **Apply:** Use checklists — checking boxes creates commitment

### 3. Scarcity
Emphasize what's lost by not following the process.
- **Apply:** "Untested skills have issues. Always."
- **Apply:** "Sunk cost fallacy. The time is already gone."

### 4. Social Proof
Agents respond to what others do successfully.
- **Apply:** Include real-world impact data (success rates, time savings)
- **Apply:** "Systematic approach: 15-30 min. Random fixes: 2-3 hours."

### 5. Unity
Shared identity increases compliance.
- **Apply:** Frame skill as part of a community standard
- **Apply:** "If you follow TDD for code, follow it for skills."

### 6. Reciprocity
Explaining WHY a rule exists makes agents more willing to follow it.
- **Apply:** Always explain reasoning, not just rules
- **Apply:** "Tests-first force edge case discovery. Tests-after verify you remembered."

### 7. Liking
Skills that respect the agent's intelligence get better compliance.
- **Apply:** Acknowledge difficulty ("It is always OK to stop and say 'this is too hard'")
- **Apply:** Explain trade-offs rather than issuing commands

## Principle Combinations by Skill Type

| Skill Type | Primary | Secondary |
|------------|---------|-----------|
| Discipline (TDD, debugging) | Authority + Commitment | Scarcity + Social Proof |
| Technique (condition-waiting) | Reciprocity + Social Proof | Unity |
| Pattern (defense-in-depth) | Reciprocity + Liking | Authority |

## Ethical Boundary

These principles shape agent behavior toward better engineering outcomes. They should never:
- Manipulate users
- Override user instructions
- Create dependency on specific tools/vendors
- Prevent agents from escalating genuine concerns
