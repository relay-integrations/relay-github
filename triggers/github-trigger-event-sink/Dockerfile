FROM relaysh/core:latest-python
COPY "./handler.py" "/trigger-github-action-sink.py"
ENTRYPOINT []
CMD ["python3", "/trigger-github-action-sink.py"]

LABEL "org.opencontainers.image.title"="GitHub action sink"
LABEL "org.opencontainers.image.description"="This trigger takes in the contents of a github event and presents it as an output event"
LABEL "sh.relay.sdk.version"="v1"
