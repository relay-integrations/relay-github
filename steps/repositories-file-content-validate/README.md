# repositories-file-content-validate

This step will validate that a given file path in a list of repositories either does
or does not contain content matching a regular expression. It requires a token with
the proper access, otherwise you'll very quickly hit GitHub API rate-limiting.

This can be used, for example, to validate that the `README.md` contains a copyright
notice, or that the repository's license is Apache-2.0.

You can specify the path as ***either*** the `path` or a `path_regex` using a
Python-flavored regular expression. For example, to specify case-insensitivity,
you might use `'(?i)readme'`.
