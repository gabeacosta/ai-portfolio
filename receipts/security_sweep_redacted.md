# Security Sweep (redacted)

Categories checked and tooling used across the stack, without infrastructure topology, private URLs, or exploitable specifics.

## Secret scanning

- `gitleaks` runs as a machine-wide git pre-commit hook (not per-repo), scanning every staged diff before it can be committed anywhere on the host.
- Verified live, not assumed: a fake-but-real-pattern secret was staged and committed as a test — confirmed via `GIT_TRACE` that git actually invokes the scanning hook (as opposed to a stale, never-firing hook sitting unused in a repo's local `.git/hooks/` — a real gap found and fixed during this audit).

## Audit trail integrity

- Tamper-evidence via hash chaining: every audit entry embeds the previous entry's hash, so altering or deleting a historical entry breaks the chain from that point forward, detectably.
- A rotation-safety gap was found and fixed: the chain used to reset to a fresh start whenever the log file was rotated, which meant roughly 60% of historical entries were disconnected from each other rather than one continuous chain. Fixed by falling back to the database's last-recorded hash instead of a fresh-start sentinel.
- A verifier script walks the entire chain, recomputing every hash and checking linkage — run on a schedule, alerting on any tamper or fork.

## Drift detection

- Config drift: scheduled checks diff live deployed configs against the version-controlled source of truth, alerting on divergence.
- Code drift: a similar check compares deployed source files (by hash) against the canonical repo, catching the case where a deployed system runs code that was never actually committed anywhere reviewable.
- Both checks were themselves found silently broken during this audit (pointing at a deleted path after a repo relocation) — fixed, and now include a self-test to catch that class of failure earlier next time.

## Access control

- Capability-based authorization: every action an agent takes is checked against an explicit role→capability grant, not an implicit "the agent can do whatever it's told."
- HMAC-signed request envelopes between internal services, with replay protection via a timestamp window.

## What's excluded

Specific tool output, vulnerability findings, infrastructure hostnames/IPs, and remediation timelines are not included — this describes methodology and categories, not a redacted pentest report.
