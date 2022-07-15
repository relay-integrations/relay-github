#!/usr/bin/env python
import urllib.request, json
from github import Github, UnknownObjectException, GithubException
from relay_sdk import Interface, Dynamic as D

relay = Interface()

try:
  token = relay.get(D.connection.accessToken)
  org   = relay.get(D.org)
  repos = relay.get(D.repos)
except:
  raise ValueError("Token, org, and repos are required parameters")

gh = Github(token)

failures = []
for repo in repos:
  try:
    print(f'Checking CODEOWNERS for {repo["name"]}... ', end='')

    # Do it manually until https://github.com/PyGithub/PyGithub/pull/2275 is released
    req = urllib.request.Request(f'https://api.github.com/repos/{org}/{repo["name"]}/codeowners/errors')
    req.add_header('User-agent', 'Relay.sh')
    req.add_header('Authorization', f'token {token}')

    with urllib.request.urlopen(req) as url:
      data = json.loads(url.read().decode())
      if data['errors'] or data['message'] == 'Not Found':
        failures.append(repo['name'])

  except Exception as err:
    print(f'Problem with repo: {err}.')

relay.outputs.set("failures", failures)
