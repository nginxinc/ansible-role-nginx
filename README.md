Ansible NGINX Role
==================

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Build Status](https://travis-ci.org/nginxinc/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/nginxinc/ansible-role-nginx)

This role installs open source NGINX or NGINX Plus on your target host.

Requirements
------------

This role was developed using Ansible 2.4.0.0. Backwards compatibility is not guaranteed.

Use `ansible-galaxy install nginxinc.nginx` to install the role on your system.

It supports all platforms supported by [open source NGINX](https://nginx.org/en/linux_packages.html#mainline) and [NGINX Plus](https://www.nginx.com/products/technical-specs/):

**Open Source NGINX:**

    CentOS:
      versions:
        - 6
        - 7
    RedHat:
      versions:
        - 6
        - 7
    Debian:
      versions:
        - jessie
        - stretch
    Ubuntu:
      versions:
        - trusty
        - xenial
        - zesty
    SUSE/SLES:
      versions:
        - 12

**NGINX Plus:**

    CentOS:
      versions:
        - 6
        - 7
    RedHat:
      versions:
        - 6
        - 7
    Debian:
      versions:
        - wheezy
        - jessie
        - stretch
    Ubuntu:
      versions:
        - trusty
        - xenial
        - zesty
    SUSE/SLES:
      versions:
        - 12
    FreeBSD:
      versions:
        - 10.3
        - 11
    Oracle Linux:
      versions:
        - 6.5
        - 7
    Amazon Linux:
      versions:
        - 2016.09

Role Variables
--------------

This role has multiple variables. The defaults for all these variables are the following:

    ---
    # Specify which version of NGINX you want to install.
    # Options are 'opensource' or 'plus'.
    # Default is 'opensource'.
    type: opensource
    # Specify which branch of Open Source NGINX you want to install.
    # Options are 'mainline' or 'stable'.
    # Default is stable.
    branch: mainline
    # Install nginscript, perl and/or waf modules.
    # Default is false.
    modules:
      njs: false
      perl: false
      waf: false
    # Install NGINX Amplify.
    # Use your NGINX Amplify API key.
    # Default is null.
    amplify: null
    # Enable NGINX status data.
    # Will enable 'stub_status' in open source NGINX and 'status' in NGINX Plus.
    # Default is false.
    status: false
    # Enable NGINX Plus REST API and dashboard.
    # Default is false for all three variables.
    api:
      enable: false
      write: false
      dashboard: false
    # Location of your NGINX Plus license in your local machine.
    # Default is the files folder within the NGINX Ansible role.
    license:
      certificate: license/nginx-repo.crt
      key: license/nginx-repo.key
    # Location of the configuration files you wish to upload to NGINX.
    # Default is the files folder within the NGINX Ansible role.
    configuration_files:
      enable: false
      main: conf/nginx.conf
      http: conf/http/*.conf
    # Configuration variables to create a templated NGINX configuration.
    # Defaults are the values found in a fresh NGINX installation.
    configuration_templates:
      enable: false
      opensource:
        user: nginx
        worker_processes: 1
        error_level: warn
        worker_connections: 1024
        keepalive_timeout: 65
        listen: 80
        server_name: localhost
      plus:
        user: nginx
        worker_processes: auto
        error_level: notice
        worker_connections: 1024
        keepalive_timeout: 65
        listen: 80
        server_name: localhost


Dependencies
------------

None

Example Playbook
----------------

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing the open source version of NGINX.

    ---
    - hosts: localhost
      become: true
      roles:
        - role: nginxinc.nginx

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing NGINX Plus.

    ---
    - hosts: localhost
      become: true
      roles:
        - role: nginxinc.nginx
      vars:
        - type: plus

This is a sample playbook file for deploying the Ansible Galaxy NGINX role to a dynamic inventory containing the `nginx` tag.

    ---
    - hosts: tag_nginx
      remote_user: root
      roles:
        - role: nginxinc.nginx

To run any of the above sample playbooks create a `setup-nginx.yml` file and paste the contents. Executing the Ansible Playbook is then as simple as executing `ansible-playbook setup-nginx.yml`.

Alternatively, you can also clone this repository instead of installing it from Ansible Galaxy. If you decide to do so, replace the role variable in the previous sample playbooks from `nginxinc.nginx` to `ansible-role-nginx`.

License
-------

[Apache License, Version 2.0](https://github.com/nginxinc/ansible-role-nginx/blob/master/LICENSE)

Author Information
------------------

Alessandro Fael Garcia

[NGINX Inc](https://www.nginx.com/)
