FROM relaysh/core:latest-python
RUN apk add --no-cache build-base libffi-dev \
    && pip --no-cache-dir install PyGithub   \
    && apk --no-cache del build-base

COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="GitHub step describe repositories"
LABEL "org.opencontainers.image.description"="This step describes all the repositories matching given criteria within a GitHub org"
LABEL "sh.relay.sdk.version"="v1"

