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
  name = relay.get(D.name)
except:
  name = None

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

try:
  fields = relay.get(D.fields)
except:
  fields = []

gh = Github(token)

try:
  if name:
    repo = gh.get_organization(org).get_repo(name)
    relay.outputs.set("repository", repo.raw_data)
  else:
    repos = gh.get_organization(org).get_repos(type=scope, sort=sort, direction=direction)
    repos = list(map(lambda x: x.raw_data, repos))

    # ensure that the full_name is part of the fields; doesn't matter if it's there twice
    fields.insert(0, 'full_name')

    # now filter to have only the fields requested so that we don't exceed payload size when saving output.
    repos = list(map(lambda repo: { key: repo[key] for key in fields }, repos))

    relay.outputs.set("repositories", repos)
except UnknownObjectException as err:
  print(f'Unknown organization or repository.')
  raise
