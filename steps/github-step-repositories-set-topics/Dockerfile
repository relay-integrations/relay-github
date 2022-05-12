FROM relaysh/core:latest-python
RUN apk add --no-cache build-base libffi-dev && pip --no-cache-dir install PyGithub
COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="GitHub step set repository topics"
LABEL "org.opencontainers.image.description"="This step will add or replace topics on a GitHub repository"
LABEL "sh.relay.sdk.version"="v1"

