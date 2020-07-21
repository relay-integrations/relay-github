# github-trigger-event-sink

This trigger is an almost-transparent pass through for event actions from github.
Its purpose is to provide a compatibility layer for Github Actions, by enabling the
payload from the webhook to be used on the filesystem of a Relay step. 

The payload will be wrapped in an additional map called `event_payload` and
needs to be unwrapped at the step level in order to use it; see the example below.

## Event data

| Key              | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| event_payload    | The payload of the incoming webhook request

## Example Usage

```yaml
parameters:
  event_payload:
    description: "The full json payload from the incoming github event"
triggers:
  - name: github-event
    source:
      type: webhook
      image: relaysh/github-trigger-event-sink
    binding:
      parameters:
        event_payload: !Data event_payload
steps:
  - name: dump-payload
    image: relaysh/core
    spec:
      event_payload: !Parameter event_payload
    input:
      - mkdir -p /github/workflow
      - "ni get | jq .event_payload > /github/workflow/event.json"
      - cat /github/workflow/event.json
```
