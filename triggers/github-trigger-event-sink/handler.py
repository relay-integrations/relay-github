from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

import logging

relay = Interface()
app = Quart('pull-request-merged')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    github_event = request.headers.get('X-GitHub-Event')

    if github_event is None:
        return {'message': 'not a valid GitHub event'}, 400, {}
    if github_event == 'ping':
        return {'message': 'success'}, 200, {}

    logging.info("receiving event from GitHub: {}".format(github_event))

    event_payload = await request.get_json()
    if event_payload is None:
        return {'message': 'not a valid GitHub event'}, 400, {}

    relay.events.emit({
          'event_payload': event_payload
      })

    return {'message': 'success'}, 200, {}


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
