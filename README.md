# GitHub integration

Integration with GitHub for Puppet Relay

## Triggers

This integration contains the following triggers:

| Name | Description |
|------|-------------|
| [github-trigger-event-sink](/triggers/github-trigger-event-sink) | Passes through webhook event payload to workflow |
| [github-trigger-pull-request-merged](/triggers/github-trigger-pull-request-merged) | Triggers when pull request is merged |

## Steps

This integration contains the following steps:

| Name | Description |
|------|-------------|
| [repositories-set-topics](/steps/repositories-set-topics) | Modify the topics of a list of repositories  |
| [repositories-describe](/steps/repositories-describe) | Describe the repositories owned by an organization |
