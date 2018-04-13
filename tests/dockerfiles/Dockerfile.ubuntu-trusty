FROM ubuntu:trusty

RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y software-properties-common && rm -rf /var/lib/apt/lists/*

RUN apt-add-repository -y ppa:ansible/ansible && apt-get update && apt-get install -y \
    git \
    ansible \
    apt-transport-https \
    curl \
 && rm -rf /var/lib/apt/lists/*

RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

ENTRYPOINT ["/sbin/init"]
