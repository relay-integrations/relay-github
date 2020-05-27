# pull-request-merged

This trigger fires when a PR is merged.

## Event data

| Key              | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| url              | The pull request URL                                                  |
| branch           | The branch that the changes were pulled into (destination for the PR) |
| repository       | The name of the repository as username/repo-name                      |
| repositoryURL    | The URL to the repository on GitHub                                   |
| repositoryGitURL | The URL to the repository as a git:// scheme                          |
| repositorySSHURL | The SSH-style URL (e.g. git@github.com:username/repo-name             |
