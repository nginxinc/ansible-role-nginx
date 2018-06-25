FROM debian:jessie

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    software-properties-common \
    build-essential \
    libffi-dev \
    libssl-dev \
    python-dev \
    python-pip \
    git \
    apt-transport-https \
    curl \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools && pip install ansible

RUN mkdir -p /etc/ansible && echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

ENTRYPOINT ["/sbin/init"]
