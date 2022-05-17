#!/usr/bin/env python
from github import Github, UnknownObjectException
from relay_sdk import Interface, Dynamic as D

relay = Interface()

try:
  token = relay.get(D.connection.accessToken)
  org = relay.get(D.org)
except:
  raise ValueError("Token and org are required parameters")

try:
  scope = relay.get(D.scope)
except:
  scope = "all"

try:
  sort = relay.get(D.sort)
except:
  sort = "created"

try:
  direction = relay.get(D.direction)
except:
  direction = "asc"

gh = Github(token)

try:
  repos = gh.get_organization(org).get_repos(type=scope, sort=sort, direction=direction)
  repos = list(map(lambda x: x.raw_data, repos))
except UnknownObjectException as err:
  print(f'Unknown org {org}.')
  raise

relay.outputs.set("repositories", repos)
