# Project Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Menu or prices are outdated | Medium | High | Assign a cafeteria owner to verify and publish menu changes; show last-updated time in production. |
| Personal data or passwords are exposed | Medium | High | Keep demo data fictional; require TLS, authorization, secure storage, privacy review, and security testing before real use. |
| Payment handling creates financial or compliance risk | Medium | High | Do not collect payment credentials in this prototype; integrate a vetted provider with hosted/tokenized checkout only after approval. |
| Git branches diverge and conflicts block integration | Medium | Medium | Pull develop before branching, keep changes small, review PRs, merge frequently, and record decisions. |
| Team member availability delays work | Medium | Medium | Split features into small tasks, agree weekly check-ins, document handover, and keep a visible sprint board. |
| In-memory data disappears on restart | High | Medium | State the limitation for the demo; use a database with backups and migrations for a real pilot. |