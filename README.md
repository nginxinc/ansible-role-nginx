Ansible NGINX Role
==================

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Build Status](https://travis-ci.org/nginxinc/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/nginxinc/ansible-role-nginx)

This role installs NGINX Open Source, NGINX Plus, or NGINX Unit on your target host.

**Note:** This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

Requirements
------------

This role was developed using Ansible 2.4.0.0. Backwards compatibility is not guaranteed.

Use `ansible-galaxy install nginxinc.nginx` to install the role on your system.

It supports all platforms supported by [NGINX Open Source](https://nginx.org/en/linux_packages.html#mainline) and [NGINX Plus](https://www.nginx.com/products/technical-specs/):

**NGINX Open Source:**

```yaml
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
    - artful
    - bionic
SUSE/SLES:
  versions:
    - 12
FreeBSD:
  versions:
    - 10
    - 11
```

**NGINX Plus:**

```yaml
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
    - artful
    - bionic
Oracle Linux:
  versions:
    - 6.5
    - 7
Amazon Linux:
  versions:
    - 2018.03
SUSE/SLES:
  versions:
    - 12
FreeBSD:
  versions:
    - 10
    - 11
```

**NGINX Unit:**

```yaml
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
    - xenial
    - artful
    - bionic
Amazon Linux:
  versions:
    - 2018.03
    - 2
FreeBSD:
  versions:
    - 10
    - 11
```

Role Variables
--------------

This role has multiple variables. The defaults for all these variables are the following:

```yaml
---
# Install NGINX.
# Default is true.
nginx_enable: true

# Specify which version of NGINX you want to install.
# Options are 'opensource' or 'plus'.
# Default is 'opensource'.
type: opensource

# Specify repository origin for NGINX Open Source.
# Options are 'nginx_repository' or 'os_repository'.
# Only works if 'type' is set to 'opensource'.
# Default is nginx_repository.
install_from: nginx_repository

# Specify source repository for NGINX Open Source.
# Only works if 'install_from' is set to 'nginx_repository'.
# Defaults are the official NGINX repositories.
nginx_repository:
  debian:
    - deb https://nginx.org/packages/{{ (branch == 'mainline') | ternary('mainline/', '') }}{{ ansible_distribution|lower }}/ {{ ansible_distribution_release }} nginx
    - deb-src https://nginx.org/packages/{{ (branch == 'mainline') | ternary('mainline/', '') }}{{ ansible_distribution|lower }}/ {{ ansible_distribution_release }} nginx
  redhat:
    - https://nginx.org/packages/{{ (branch == 'mainline') | ternary('mainline/', '') }}{{ (ansible_distribution == "RedHat") | ternary('rhel/', 'centos/') }}{{ ansible_distribution_major_version|int }}/$basearch/
  suse:
    - https://nginx.org/packages/{{ (branch == 'mainline') | ternary('mainline/', '') }}sles/12

# Specify which branch of NGINX Open Source you want to install.
# Options are 'mainline' or 'stable'.
# Only works if 'install_from' is set to 'nginx_repository'.
# Default is mainline.
branch: mainline

# Install NGINX JavaScript, Perl, ModSecurity WAF (NGINX Plus only), GeoIP, Image-Filter, RTMP Media Streaming, and/or XSLT modules.
# Default is false.
modules:
  njs: false
  perl: false
  waf: false
  geoip: false
  image_filter: false
  rtmp: false
  xslt: false

# Install NGINX Amplify.
# Use your NGINX Amplify API key.
# Default is null.
amplify_enable: false
amplify_key: null

# Enable NGINX status data.
# Will enable 'stub_status' in NGINX Open Source and 'status' in NGINX Plus.
# Default is false.
status_enable: false

# Enable NGINX Plus REST API, write access to the REST API, and NGINX Plus dashboard.
# Default is false.
rest_api_enable: false
rest_api_write: false
rest_api_dashboard: false

# Location of your NGINX Plus license in your local machine.
# Default is the files folder within the NGINX Ansible role.
license:
  certificate: license/nginx-repo.crt
  key: license/nginx-repo.key

# Delete NGINX Plus license after installation for security purposes.
# Default is true.
delete_license: true

# Enable uploading NGINX configuration files to your system.
# Default for uploading files is false.
# Default location of files is the files folder within the NGINX Ansible role.
main_push_enable: false
main_push_location: conf/nginx.conf
http_push_enable: false
http_push_location: conf/http/*.conf
stream_push_enable: false
stream_push_location: conf/stream/*.conf

# Configuration variables to create a templated NGINX configuration.
# Defaults are the values found in a fresh NGINX installation.
main_template_enable: false
main_template_user: nginx
main_template_worker_processes: auto
main_template_error_level: warn
main_template_worker_connections: 1024
http_template_enable: false
http_template_keepalive_timeout: 65
http_template_listen: 80
http_template_server_name: localhost
stream_template_enable: false
stream_template_listen: 12345

# Install NGINX Unit and NGINX Unit modules.
# Use a list of supported NGINX Unit modules.
# Default is false.
unit_enable: false
unit_modules: null
```

Dependencies
------------

None

Example Playbook
----------------

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing the open source version of NGINX.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - role: nginxinc.nginx
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing NGINX Plus.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - role: nginxinc.nginx
  vars:
    type: plus
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role to a dynamic inventory containing the `nginx` tag.

```yml
---
- hosts: tag_nginx
  remote_user: root
  roles:
    - role: nginxinc.nginx
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost to install NGINX Unit and the PHP/Perl NGINX Unit language modules.

```yml
---
- hosts: localhost
  become: true
  roles:
    - role: nginxinc.nginx
  vars:
    nginx_enable: false
    unit_enable: true
    unit_modules:
      - unit-php
      - unit-perl
```

To run any of the above sample playbooks create a `setup-nginx.yml` file and paste the contents. Executing the Ansible Playbook is then as simple as executing `ansible-playbook setup-nginx.yml`.

Alternatively, you can also clone this repository instead of installing it from Ansible Galaxy. If you decide to do so, replace the role variable in the previous sample playbooks from `nginxinc.nginx` to `ansible-role-nginx`.

License
-------

[Apache License, Version 2.0](https://github.com/nginxinc/ansible-role-nginx/blob/master/LICENSE)

Author Information
------------------

Alessandro Fael Garcia

[NGINX Inc](https://www.nginx.com/)
