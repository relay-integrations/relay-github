#!/usr/bin/env python
from github import Github, UnknownObjectException
from relay_sdk import Interface, Dynamic as D

relay = Interface()

try:
  token = relay.get(D.connection.accessToken)
  reponame = relay.get(D.repo)
  path = relay.get(D.path)
  contents = relay.get(D.contents)
except:
  raise ValueError("Token, repo, path, and contents are required parameters")

try:
  branch = relay.get(D.branch)
except:
  branch = 'main'

try:
  message = relay.get(D.message)
except:
  message = None

gh = Github(token)

try:
  repo = gh.get_repo(reponame)
except UnknownObjectException as err:
  raise ValueError(f'Unknown repo {repo}.')

try:
  current = repo.get_contents(path, ref=branch)
  repo.update_file(current.path, (message or f'Updating {path}'), contents, current.sha, branch=branch)

except UnknownObjectException:
  repo.create_file(path, (message or f'Creating {path}'), contents, branch=branch)
