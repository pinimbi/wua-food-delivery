# Publish and complete the GitHub lab

GitHub account: `pinimbi`
Repository: https://github.com/pinimbi/wua-food-delivery (public)

## Verified online work

The repository has `main` and `develop`, with remote feature branches for authentication, menu browsing, order tracking, campus ordering, and quality/documentation. Four genuine pull requests are open against `develop`:

1. Authentication: https://github.com/pinimbi/wua-food-delivery/pull/1
2. Menu browsing: https://github.com/pinimbi/wua-food-delivery/pull/2
3. Order tracking: https://github.com/pinimbi/wua-food-delivery/pull/3
4. Campus ordering: https://github.com/pinimbi/wua-food-delivery/pull/4

PR #4 depends on PRs #1–#3; merge and verify those modules before merging the browser application. None of the four PRs has an actual teammate review or merge yet. The quality/documentation branch is published and will contain the fifth PR.

## Remaining work for the actual team

1. Open PR #5 from `feature/quality-documentation` after checking its final contents.
2. Invite actual teammates to review the PRs. On the authentication PR, request and address the lab's specified feedback on email validation, password hashing, and docstrings. Do not invent review comments.
3. Have a real teammate merge at least one PR, as required by the lab. Complete and merge the required PRs according to the course instructions.
4. Push the local `v1.0-submission` tag, create a GitHub Release from that tag, then add the verified release URL here.
5. Capture the actual GitHub contribution graph after real contributions appear.
6. Replace fictional names and DEMO IDs in `docs/demo_team.md` and the private report with the actual team details. Never publish actual student IDs unless the course explicitly requires it.

## Publishing from PowerShell

The local repository has `main`, `develop`, all five feature branches, and the `v1.0-submission` tag. When GitHub sign-in works on your computer, open this folder in PowerShell and run:

```powershell
git push --all origin
git push origin --tags
```

If Git asks you to authenticate, use Git Credential Manager or GitHub's supported sign-in prompt. Never paste your password or a one-time code into chat. The current local commit author uses a placeholder identity; set your own Git name and verified or GitHub no-reply email before creating further commits if you want them attributed to your account.

Do not treat local branches, local merges, or the local tag as online GitHub evidence.
