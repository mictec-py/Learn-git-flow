# Learn-git-flow
learning github essentials using python simple excersices

We'll mainly make use of Github issues, branching, pull requests (PR) and reviews.

Workflow:

    Fork the given repository to your Github profile
    Each drill or checkpoint will be given out as a Github issue.

    For each issue (for example this), create a branch thus:

    <issue-number>-issue-tittle>
    e.g.
    1-hr-arraysum for the first issue on this repo.

    Your solutions should be put in a folder named issue-<number> (number padded with 0's) e.g. issue-001
    Work out your solution from the branch, then commit changes and push.
    Raise a PR against your master branch (not this project's master branch).
    Your PR will then be reviewed by your peers and merged appropriately



Quick Git walkthrough:

    Fork the repo (click on the "Fork" button at the top-right).

    Clone your forked repo, e.g.

    git clone https://github.com/yourusername/learn-git-flow.git

    Create a branch for your solution, e.g.

    git checkout -b 1-drill-0-sum-array

    After making changes, stage the changes:

    git add --all

    Commit the staged changes, e.g.

    git commit -m "solution: hackerrank sum-array"

    Push your changes, e.g.

    git push origin 1-hr-sum-array

Making A pull request:

NOTE: Make sure you choose your master branch as the base, and not the original repo's master.

Reviewing Code: Your code will be reviewed and if it looks good, your pull request will be accepted and the merge done.

