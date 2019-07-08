from python:3.7-slim-stretch

RUN set -x && \
  pip install \
    google-cloud-logging \
    google-cloud-storage \
    google-cloud-bigquery \
    google-cloud-pubsub \
    google-cloud-scheduler \
    tenacity \
    behave

WORKDIR /workspace
ENTRYPOINT ["/usr/local/bin/behave"]
  
