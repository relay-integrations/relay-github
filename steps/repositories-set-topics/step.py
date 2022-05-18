#!/usr/bin/env python
from github import Github, UnknownObjectException, GithubException
from relay_sdk import Interface, Dynamic as D

relay = Interface()

try:
  token = relay.get(D.connection.accessToken)
  repos = relay.get(D.repos)
  topics = relay.get(D.topics)
except:
  raise ValueError("Connection, repos, and topics are all required.")

try:
  mode = relay.get(D.mode)
except:
  mode = 'replace'

gh = Github(token)

for name in repos:
  try:
    print(f'Setting topics {topics} on {name}... ', end='')
    repo = gh.get_repo(name)

    if mode == 'add':
      topics = topics + repo.get_topics()

    repo.replace_topics(topics)

    print(f'success.')

  except (UnknownObjectException, GithubException) as err:
    print(f'unknown repository or insufficient permissions; skipping.')
