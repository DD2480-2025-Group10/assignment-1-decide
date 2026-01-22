# Git work-flow 
When implementing a feature, bugfix, chore, etc begin by creating an issue on github describing what you´ll be implementing. When naming the issue it should be follow the convention `[<tag>]: <description>`, where the tag follows the standard of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).

An action will automatically create a branch and PR related to your issue. *Please select the PR under the development menu for the issue, this will automatically close the issue when the branch is merged*.

When you begin working on an issue start by assigning yourself to both the issue and the PR. Then on your local machine do the following: 

```bash
# Pull recent changes on main 
git checkout origin/main
git pull

# Checkout your branch 
git fetch origin <branch_name>
git checkout -b <branch_name> origin/<branch_name>

# Make sure your branch is up to date with main 
git rebase main
```

Now you can complete work on your branch until you are ready to merge the changes. When you have committed all the changes locally to your branch, do the following:
```bash
git rebase main
```
resolve any conflicts that may have happened while working on your branch. Lastly push your changes 
```bash
git push
```

Now you can mark your PR as ready for review and once all the tests pass you are ready to **Squash and merge** (refrain from using merge commits or rebase merging).

