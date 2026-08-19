# Apply / Review This FDE Positioning

This branch repositions the portfolio around Forward Deployed Engineering and adds one runnable public proof specimen for the Runtime Wind Tunnel.

The intended narrative is:

```text
customer problem
  -> discovery
  -> technical scope
  -> integration
  -> production
  -> evaluation
  -> hardening
  -> measurable impact
  -> reusable platform capability
```

The deployments are the story. The repositories and public specimen are the supporting evidence.

---

## What Changed

The branch intentionally limits scope to:

- `README.md`
- `RESUME.md`
- `HOW_I_WORK.md`
- `DEPLOYMENTS/01-real-estate-lead-operations.md`
- `DEPLOYMENTS/02-governed-agent-execution.md`
- `DEPLOYMENTS/03-runtime-wind-tunnel.md`
- `PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md`
- `FIELD-NOTES/production-incidents.md`
- `APPLY.md`
- `specimens/agent-runtime-wind-tunnel/`

No existing production code, receipts, case-study source data, or supporting repositories are modified by this positioning branch. The only new executable code is the self-contained public Wind Tunnel specimen.

---

## Local Review

```bash
git clone https://github.com/gabeacosta/ai-portfolio.git
cd ai-portfolio
git fetch origin
git checkout agent/fde-positioning
```

Review the full branch diff:

```bash
git diff origin/main...HEAD
```

Review the primary positioning files:

```bash
git diff origin/main...HEAD -- README.md RESUME.md HOW_I_WORK.md
```

Review the deployment/proof surfaces:

```bash
git diff origin/main...HEAD -- DEPLOYMENTS/ PLAYBOOKS/ FIELD-NOTES/ APPLY.md specimens/
```

Check changed paths:

```bash
git diff --name-status origin/main...HEAD
```

---

## Run the Public Wind Tunnel Proof

```bash
cd specimens/agent-runtime-wind-tunnel
make test
make demo
make tamper
```

Expected high-level result:

```text
14 tests passing
6/6 expected matrix verdicts observed
Replay verification: FAILED after deliberate tamper
Side effects emitted during replay: 0
```

The specimen requires no API keys, network calls, Docker, or live model provider.

---

## Link / Markdown Smoke Check

At minimum, verify that the relative navigation paths render correctly on GitHub:

```text
README.md
  -> RESUME.md
  -> HOW_I_WORK.md
  -> DEPLOYMENTS/*
  -> PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md
  -> FIELD-NOTES/production-incidents.md
  -> specimens/agent-runtime-wind-tunnel/
  -> APPLY.md
```

The branch does not add a markdown-link checker dependency. The intended review remains dependency-light.

---

## Optional GitHub CLI Review

If `gh` is installed and authenticated:

```bash
gh repo view gabeacosta/ai-portfolio --web
```

Inspect the branch:

```bash
gh browse --branch agent/fde-positioning
```

Create a draft pull request if one does not already exist:

```bash
gh pr create \
  --repo gabeacosta/ai-portfolio \
  --base main \
  --head agent/fde-positioning \
  --draft \
  --title "Position portfolio for Forward Deployed Engineer roles" \
  --body "Reframes the portfolio around customer deployments, production hardening, and reusable platform capability, and adds a zero-key public Runtime Wind Tunnel specimen as executable proof."
```

---

## Merge

After review:

```bash
git checkout main
git pull --ff-only origin main
git merge --ff-only origin/agent/fde-positioning
git push origin main
```

If `main` has moved and the branch can no longer fast-forward cleanly, do not force the merge. Rebase or merge intentionally, rerun the public specimen tests, re-review the diff, and then land it through the pull request.

---

## Recruiter / Hiring-Manager Evaluation Path

For a fast review of the portfolio:

1. Start with [`README.md`](README.md) for the FDE thesis and deployment map.
2. Read [`DEPLOYMENTS/01-real-estate-lead-operations.md`](DEPLOYMENTS/01-real-estate-lead-operations.md) for customer workflow ownership.
3. Read [`DEPLOYMENTS/02-governed-agent-execution.md`](DEPLOYMENTS/02-governed-agent-execution.md) for incident-driven infrastructure hardening.
4. Open [`specimens/agent-runtime-wind-tunnel/`](specimens/agent-runtime-wind-tunnel/) and run `make demo` / `make tamper` for executable runtime-evaluation proof.
5. Read [`DEPLOYMENTS/03-runtime-wind-tunnel.md`](DEPLOYMENTS/03-runtime-wind-tunnel.md) for the larger evaluation/runtime architecture and scope boundaries.
6. Open the linked public repos to validate the other implementation evidence.
7. Use [`RESUME.md`](RESUME.md) for role alignment and [`HOW_I_WORK.md`](HOW_I_WORK.md) for operating style.

---

## Positioning Test

This branch succeeds if a reviewer can answer these questions within a few minutes:

- What customer or operating problems has Gabe owned?
- What did he actually integrate and ship?
- What failed in production and how did the architecture change?
- Which claims have public implementation evidence?
- Can one of the runtime claims be independently reproduced rather than merely read?
- How does field work become reusable platform capability?
- Why is Forward Deployed Engineer a better description than a generic AI/automation title?

If those answers are not obvious, the positioning still needs work.

[Back to portfolio](README.md)
