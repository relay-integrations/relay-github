FROM relaysh/core:latest-python
RUN apk add --no-cache build-base libffi-dev && pip --no-cache-dir install PyGithub
COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="GitHub step validate file content"
LABEL "org.opencontainers.image.description"="This step validates that a given file in a GitHub repository matches content specification"
LABEL "sh.relay.sdk.version"="v1"

