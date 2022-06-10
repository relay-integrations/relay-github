# repositories-describe

This step will describe the repositories belonging to an organization. It requires a
token with the proper access, otherwise you'll very quickly hit GitHub API rate-limiting.

## Usage

Pass a token and the org name, and then either the name or some parameters for
filtering and ordering the list. If you pass a name, it will return a complete
object representing that repository. If you pass filter/order params, it will
return a list of all matching repos.

By default, this list is only the name of each repository. If you'd like
more fields returned, list them in the `fields` parameter.
