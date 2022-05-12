#!/usr/bin/env python
from github import Github, UnknownObjectException
from relay_sdk import Interface, Dynamic as D

relay = Interface()

try:
  token = relay.get(D.token)
  repos = relay.get(D.repos)
  topics = relay.get(D.topics)
except:
  raise ValueError("Token, repos, and topics are all required parameters")

mode = relay.get(D.mode)
gh = Github(token)

for name in repos:
  try:
    print(f'Setting topics {topics} on {name}... ', end='')
    repo = gh.get_repo(name)

    if mode == 'add':
      topics = topics + repo.get_topics()

    repo.replace_topics(topics)

    print(f'success.')

  except UnknownObjectException as err:
    print(f'unknown repository or insufficient permissions; skipping.')
