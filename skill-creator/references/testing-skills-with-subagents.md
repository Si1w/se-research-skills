# Testing Skills with Subagents

TDD methodology applied to skill testing. Maps TDD phases to skill creation:

| TDD Phase | Skill Testing |
|-----------|--------------|
| Write failing test | Run pressure scenario WITHOUT skill (baseline) |
| Watch it fail | Document exact rationalizations agent uses |
| Write minimal code | Write skill addressing those specific violations |
| Watch it pass | Verify agent now complies with skill present |
| Refactor | Close loopholes with pressure testing |

## Pressure Scenarios

A pressure scenario combines 3+ pressures that tempt the agent to violate the skill's rules.

### Pressure Types

| Pressure | Description | Example |
|----------|-------------|---------|
| **Time** | Urgency to ship fast | "Quick fix needed, production is down" |
| **Sunk Cost** | Already invested effort | "I've spent 3 hours on this code" |
| **Authority** | User override | "Just skip the tests this time" |
| **Economic** | Cost concern | "We can't afford more compute" |
| **Exhaustion** | Near end of task | "Almost done, just this last bit" |
| **Social** | Peer pressure | "Everyone else skips this step" |
| **Pragmatic** | Practical shortcut | "It's too simple to need this" |

### Writing Effective Scenarios

Combine pressures for maximum temptation:

```
Scenario: "User has been working for hours on a complex feature.
They say: 'I've already manually tested everything and it works.
Just commit it — we need this in production by end of day.
Skip the formal test suite, we'll add tests next sprint.'"

Pressures: Time + Sunk Cost + Authority + Pragmatic
```

### Plugging Holes

After baseline testing:
1. List every rationalization the agent used (verbatim)
2. For each rationalization, write an explicit counter in the skill
3. Re-run same scenario — agent should now resist
4. Try NEW rationalizations — add counters for those too
5. Repeat until the skill is bulletproof

### Meta-Testing

After bulletproofing:
- Try scenarios NOT in the rationalization table
- Try combining pressures in new ways
- Try "spirit vs letter" arguments
- Try edge cases the skill doesn't explicitly address

## Testing Checklist

- [ ] 3+ pressure scenarios created
- [ ] Baseline documented (without skill)
- [ ] All rationalizations captured verbatim
- [ ] Skill written addressing specific failures
- [ ] Compliance verified (with skill)
- [ ] New rationalizations from testing captured
- [ ] Explicit counters added for each
- [ ] Re-tested until bulletproof
- [ ] Meta-testing passed
