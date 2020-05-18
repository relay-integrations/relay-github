from flask import Flask, request, jsonify, make_response
import requests

import os
import json
from urllib.parse import urljoin

port = os.getenv('PORT', '8080')
metadata_api = os.getenv('METADATA_API_URL')
metadata_api_events = urljoin(metadata_api, 'events')
debug = os.getenv('DEBUG', False)
app = Flask(__name__)


@app.route('/', methods=['POST'])
def handler():
    github_event = request.headers.get('X-Github-Event')

    if github_event is None:
        return make_response(jsonify(message='not a valid github event'), 400)
    if github_event == 'ping':
        return make_response(jsonify(message='success'), 200)
    if github_event != 'pull_request':
        return make_response(jsonify(message='only pull_request event are supported'), 400)

    event_payload = request.get_json()

    if event_payload is None:
        return make_response(jsonify(message='not a valid github event'), 400)

    pr = event_payload['pull_request']

    if event_payload['action'] == 'closed' and pr['merged'] is True:
        relay_event = {'data': {
                'repository': event_payload['repository']['full_name'],
                'branch': pr['base']['ref']}}

        request_payload = json.dumps(relay_event)

        # TODO we need to figure out how to behave when we can't successfully submit
        # an event to the metadata api. for now, we will just ignore the response.
        headers = {'Content-type': 'application/json'}
        requests.post(metadata_api_events, headers=headers, json=request_payload)

    return make_response(jsonify(message='success'), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=debug)
