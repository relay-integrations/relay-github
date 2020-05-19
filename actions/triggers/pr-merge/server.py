from flask import Flask, request, jsonify, make_response
from requests import PreparedRequest, Response, Session
from requests.adapters import HTTPAdapter

import os
import json
from typing import Container, Mapping, Optional, Text, Tuple, Union
from urllib.parse import urljoin, urlsplit, urlunsplit

import logging

port = os.getenv('PORT', '8080')
metadata_api = os.getenv('METADATA_API_URL')
metadata_api_events = urljoin(metadata_api, 'events')
debug = os.getenv('DEBUG', False)
app = Flask(__name__)

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
def handler():
    github_event = request.headers.get('X-GitHub-Event')

    if github_event is None:
        return make_response(jsonify(message='not a valid github event'), 400)
    if github_event == 'ping':
        return make_response(jsonify(message='success'), 200)
    if github_event != 'pull_request':
        return make_response(jsonify(message='only pull_request event are supported'), 400)

    logging.info("receiving event from github: {}".format(github_event))

    event_payload = request.get_json()

    if event_payload is None:
        return make_response(jsonify(message='not a valid github event'), 400)


    pr = event_payload['pull_request']

    if event_payload['action'] == 'closed' and pr['merged'] is True:
        relay_event = {
                'repository': event_payload['repository']['full_name'],
                'branch': pr['base']['ref']
        }


        # TODO replace this with the SDK
        client = Session()
        client.mount('http+api://', MetadataAPIAdapter())

        # TODO we need to figure out how to behave when we can't successfully submit
        # an event to the metadata api. for now, we will just ignore the response.
        response = client.post(
                'http+api://api/events',
                data=json.dumps({'data': relay_event}),
                headers={'content-type': 'application/json'},
        )

        response.raise_for_status()

        logging.info("relay event request finished: {}".format(response.text))

    return make_response(jsonify(message='success'), 200)

# TODO replace this with the SDK
class MetadataAPIAdapter(HTTPAdapter):

    def __init__(self, base_url: Optional[str] = None) -> None:
        if base_url is None:
            base_url = os.environ['METADATA_API_URL']

        self._base_url = base_url

        super(MetadataAPIAdapter, self).__init__()

    def send(self, request: PreparedRequest, stream: bool = False,
             timeout: Optional[Union[
                 float, Tuple[float, float], Tuple[float, None]]
             ] = None,
             verify: Union[bool, str] = True,
             cert: Optional[Union[
                 bytes, Text, Container[Union[bytes, Text]]]
             ] = None,
             proxies: Optional[Mapping[str, str]] = None) -> Response:
        (_, _, path, query, fragment) = urlsplit(request.url or '')
        request.prepare_url(
            urljoin(
                self._base_url,
                urlunsplit(('', '', path, query, fragment)),
            ),
            {},
        )

        return super(MetadataAPIAdapter, self).send(
            request,
            stream=stream,
            timeout=timeout,
            verify=verify,
            cert=cert,
            proxies=proxies,
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=debug)
