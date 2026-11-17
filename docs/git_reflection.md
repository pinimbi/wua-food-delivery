# Git Reflection

**Use this as a draft for the individual presentation. Replace it with your team's actual experience before submitting.**

Our main Git challenge was coordinating changes that touched shared project files while keeping feature work isolated. A branch-per-feature workflow helped make each change easier to review. Small commits with clear messages also made it easier to see what had changed and why.

When a merge conflict occurred, we compared both versions, discussed the intended behavior with the teammate responsible for the feature, edited the file to keep the correct combined behavior, and ran the tests before completing the merge. We would avoid resolving conflicts by blindly accepting one side because that can silently remove another person's work.

Working with Git taught us that teamwork depends on communication as much as commands. Agreeing on branch names, reviewing pull requests, and updating the shared development branch regularly makes integration more predictable. In future projects, we will create issues for stories, keep pull requests focused, request review early, protect the main branch, and use CI as a shared quality check.

Before submission, add a truthful example of a conflict your team encountered and how it was resolved. The local demonstration repository does not prove that a real team conflict or GitHub review happened.