# se-research-skills

A collection of Agent skills for software engineering research and development workflows.

## Skills

### Research

| Skill | Description |
|-------|-------------|
| [ese-review](ese-review/) | Review a paper against ACM/SIGSOFT Empirical Standards |
| [mh-writing](mh-writing/) | Write and improve SE research papers paragraph by paragraph (Mark Harman's guidelines) |
| [excalidraw-diagram](excalidraw-diagram/) | Generate flowcharts and architecture diagrams as .excalidraw + PNG, with SVG icon support |
| [rp-generate](rp-generate/) | Develop research ideas through adversarial dialogue, output structured proposals |

### Development Workflow

| Skill | Description |
|-------|-------------|
| [project-draft](project-draft/) | Brainstorm and design projects/features before implementation |
| [plan](plan/) | Write and execute implementation plans with subagent support |
| [tdd](tdd/) | Test-driven development with verification discipline |
| [systematic-debugging](systematic-debugging/) | Root-cause debugging methodology (four phases) |
| [code-review](code-review/) | Request and receive code reviews with technical rigor |

### Git Workflow

| Skill | Description |
|-------|-------------|
| [gh-pr](gh-pr/) | Create branch, commit, push, and open a GitHub PR |
| [git-clean](git-clean/) | Clean up feature branch after PR merge |
| [git-push](git-push/) | Push current branch to remote |

### Meta

| Skill | Description |
|-------|-------------|
| [skill-creator](skill-creator/) | Create and improve skills with TDD-based validation |

### Reporting

| Skill | Description |
|-------|-------------|
| [weekly-report](weekly-report/) | Generate Quarto slide deck for supervisor meetings |

## References

- [obra/superpowers](https://github.com/obra/superpowers) — The original skill collection that several skills in this repo were adapted from.
- [Draft Guidelines for My Students on Writing Software Engineering Research Papers](https://cragkhit.github.io/files/harman-writing-advice.pdf) — Mark Harman's writing guidelines, used as the basis for the [mh-writing](mh-writing/) skill.

## Setup

```bash
uv sync  # install Python dependencies (used by rp-generate Zotero integration)
```
