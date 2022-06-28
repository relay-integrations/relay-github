# repositories-file-content-update

This step will create or update the contents of a file in a GitHub repository.
It will create a single commit on the branch provided rather than creating a PR,
so your branch protection rules may not allow it to commit to `main`.

It requires a token with the proper write access to the repository.
