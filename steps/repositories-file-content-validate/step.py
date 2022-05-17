#!/usr/bin/env python
import re
from github import Github, UnknownObjectException
from relay_sdk import Interface, Dynamic as D

relay = Interface()

try:
  token = relay.get(D.connection.accessToken)
  repos = relay.get(D.repos)
  content = relay.get(D.content)
except:
  raise ValueError("Token, repos, and content are all required parameters")

try:
  match = relay.get(D.match)
except:
  match = "positive"

try:
  path = relay.get(D.path)
except:
  path = None
  
try:
  path_regex = relay.get(D.path_regex)
except:
  path_regex = None

if (path and path_regex) or (path == None and path_regex == None):
  raise ValueError("Please set either path or path_regex")


gh = Github(token)

matches = []
for name in repos:
  try:
    print(f'Checking content in {name}... ', end='')
    repo = gh.get_repo(name)

    if path_regex:
      path = list(filter(lambda x: re.match(path_regex, x.path), repo.get_contents('/')))[0].path

    if path:
      blob = repo.get_contents(path).decoded_content.decode("utf-8")
      if re.match(content, blob):
        matches.append(name)
    else:
      raise UnknownObjectException("No files matched given regex")

    print(f'success.')

  except UnknownObjectException as err:
    print(f'cannot access file or repository; skipping. {err}')

if match == 'negative':
  matches = [x for x in repos if x not in matches]

relay.outputs.set("repositories", matches)