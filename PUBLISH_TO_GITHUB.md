# GitHub status and remaining course evidence

GitHub account: `pinimbi`  
Repository: https://github.com/pinimbi/wua-food-delivery (public)

## Verified online work

The repository has `main` and `develop`, with remote feature branches for authentication, menu browsing, order tracking, campus ordering, and quality/documentation. Five genuine pull requests are open against `develop`:

1. Authentication: https://github.com/pinimbi/wua-food-delivery/pull/1
2. Menu browsing: https://github.com/pinimbi/wua-food-delivery/pull/2
3. Order tracking: https://github.com/pinimbi/wua-food-delivery/pull/3
4. Campus ordering: https://github.com/pinimbi/wua-food-delivery/pull/4
5. Quality and documentation: https://github.com/pinimbi/wua-food-delivery/pull/5

PR #4 depends on PRs #1–#3. PR #5 tests and workflow also depend on those backend modules being merged to `develop`. GitHub currently reports two failing workflow checks on PR #5 for this reason. No PR has an actual teammate review or merge yet.

## Remaining work for the actual team

1. Merge prerequisite PRs #1–#3 through genuine teammate-reviewed workflow, then rerun CI and verify PRs #4 and #5.
2. Invite actual teammates to review the PRs. On the authentication PR, request and address the lab’s specified feedback on email validation, password hashing, and docstrings. Do not invent review comments.
3. Have a real teammate merge at least one PR, as required by the lab. Complete and merge the required PRs according to course instructions.
4. Push the local `v1.0-submission` tag, create a GitHub Release from that tag, then add the verified release URL here.
5. Capture the actual GitHub contribution graph after genuine team contributions appear.
6. Replace fictional names and DEMO IDs in `docs/demo_team.md` and the private report with actual team details. Never publish actual student IDs unless the course explicitly requires it.

## Publishing the local tag

The local repository has the `v1.0-submission` tag. When GitHub sign-in works on your computer, open the project folder in PowerShell and run:

```powershell
git push origin --tags
```

If Git asks you to authenticate, use Git Credential Manager or GitHub’s supported sign-in prompt. Never paste your password or a one-time code into chat. The local commit author uses a placeholder identity; set your own Git name and verified or GitHub no-reply email before creating further local commits if you want them attributed to your account.

Do not treat local branches, local merges, or the local tag as online evidence.
