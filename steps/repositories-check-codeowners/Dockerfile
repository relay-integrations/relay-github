FROM relaysh/core:latest-python
RUN apk add --no-cache build-base libffi-dev \
    && pip --no-cache-dir install PyGithub   \
    && apk --no-cache del build-base

COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="GitHub step check repositories for valid CODEOWNER"
LABEL "org.opencontainers.image.description"="This step validates the CODEOWNERS file in all the repositories listed"
LABEL "sh.relay.sdk.version"="v1"

