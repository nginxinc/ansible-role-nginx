Ansible NGINX Role
==================

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Build Status](https://travis-ci.org/nginxinc/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/nginxinc/ansible-role-nginx)

This role installs NGINX Open Source, NGINX Plus, the NGINX Amplify agent, the NGINX Controller agent, or NGINX Unit on your target host.

**Note:** This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

Requirements
------------

This role was developed using Ansible 2.4.0.0. Backwards compatibility is not guaranteed.

Use `ansible-galaxy install nginxinc.nginx` to install the role on your system.

It supports all platforms supported by [NGINX Open Source](https://nginx.org/en/linux_packages.html#mainline) and [NGINX Plus](https://www.nginx.com/products/technical-specs/):

**NGINX Open Source**

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

**NGINX Plus**

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

**NGINX Amplify**

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
Amazon Linux:
  versions:
    - 2017.09
```

**NGINX Controller**

```yaml
CentOS:
  versions:
    - 7
RedHat:
  versions:
    - 7
Debian:
  versions:
    - jessie
    - stretch
Ubuntu:
  versions:
    - xenial
    - artful
```

**NGINX Unit**

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

# Print NGINX configuration file to terminal after executing playbook.
nginx_debug_output: false

# Specify which version of NGINX you want to install.
# Options are 'opensource' or 'plus'.
# Default is 'opensource'.
nginx_type: opensource

# Specify repository origin for NGINX Open Source.
# Options are 'nginx_repository' or 'os_repository'.
# Only works if 'nginx_type' is set to 'opensource'.
# Default is nginx_repository.
nginx_install_from: nginx_repository

# Choose where to fetch the NGINX signing key from.
# Default is the official NGINX signing key host.
nginx_signing_key: https://nginx.org/keys/nginx_signing.key

# Specify source repository for NGINX Open Source.
# Only works if 'install_from' is set to 'nginx_repository'.
# Defaults are the official NGINX repositories.
nginx_repository:
  debian:
    - deb https://nginx.org/packages/{{ (nginx_branch == 'mainline') | ternary('mainline/', '') }}{{ ansible_distribution|lower }}/ {{ ansible_distribution_release }} nginx
    - deb-src https://nginx.org/packages/{{ (nginx_branch == 'mainline') | ternary('mainline/', '') }}{{ ansible_distribution|lower }}/ {{ ansible_distribution_release }} nginx
  redhat:
    - https://nginx.org/packages/{{ (nginx_branch == 'mainline') | ternary('mainline/', '') }}{{ (ansible_distribution == "RedHat") | ternary('rhel/', 'centos/') }}{{ ansible_distribution_major_version|int }}/$basearch/
  suse:
    - https://nginx.org/packages/{{ (nginx_branch == 'mainline') | ternary('mainline/', '') }}sles/12

# Specify which branch of NGINX Open Source you want to install.
# Options are 'mainline' or 'stable'.
# Only works if 'install_from' is set to 'nginx_repository'.
# Default is mainline.
nginx_branch: mainline

# Location of your NGINX Plus license in your local machine.
# Default is the files folder within the NGINX Ansible role.
nginx_license:
  certificate: license/nginx-repo.crt
  key: license/nginx-repo.key

# Delete NGINX Plus license after installation for security purposes.
# Default is true.
nginx_delete_license: true

# Install NGINX JavaScript, Perl, ModSecurity WAF (NGINX Plus only), GeoIP, Image-Filter, RTMP Media Streaming, and/or XSLT modules.
# Default is false.
nginx_modules:
  njs: false
  perl: false
  waf: false
  geoip: false
  image_filter: false
  rtmp: false
  xslt: false

# Install NGINX Amplify.
# Use your NGINX Amplify API key.
# Requires access to either the NGINX stub status or the NGINX Plus REST API.
# Default is null.
nginx_amplify_enable: false
nginx_amplify_api_key: null

# Install NGINX Controller.
# Use your NGINX Controller API key and NGINX Controller API endpoint.
# Requires NGINX Plus and write access to the NGINX Plus REST API.
# Default is null.
nginx_controller_enable: false
nginx_controller_api_key: null
nginx_controller_api_endpoint: null

# Install NGINX Unit and NGINX Unit modules.
# Use a list of supported NGINX Unit modules.
# Default is false.
nginx_unit_enable: false
nginx_unit_modules: null

# Enable NGINX status data.
# Will enable 'stub_status' in NGINX Open Source and 'status' in NGINX Plus.
# Default is false.
nginx_status_enable: false
nginx_status_port: 8080

# Enable NGINX Plus REST API, write access to the REST API, and NGINX Plus dashboard.
# Requires NGINX Plus.
# Default is false.
nginx_rest_api_enable: false
nginx_rest_api_location: /etc/nginx/conf.d/api.conf
nginx_rest_api_port: 8080
nginx_rest_api_write: false
nginx_rest_api_dashboard: false

# Enable uploading NGINX configuration files to your system.
# Default for uploading files is false.
# Default location of files is the files folder within the NGINX Ansible role.
# Upload the main NGINX configuration file.
nginx_main_upload_enable: false
nginx_main_upload_src: conf/nginx.conf
nginx_main_upload_dest: /etc/nginx
# Upload HTTP NGINX configuration files.
nginx_http_upload_enable: false
nginx_http_upload_src: conf/http/*.conf
nginx_http_upload_dest: /etc/nginx/conf.d
# Upload Stream NGINX configuration files.
nginx_stream_upload_enable: false
nginx_stream_upload_src: conf/stream/*.conf
nginx_stream_upload_dest: /etc/nginx/conf.d
# Upload HTML files.
nginx_html_upload_enable: false
nginx_html_upload_src: www/*
nginx_html_upload_dest: /usr/share/nginx/html
# Upload SSL certificates and keys.
nginx_ssl_upload_enable: false
nginx_ssl_crt_upload_src: ssl/*.crt
nginx_ssl_crt_upload_dest: /etc/ssl/certs/
nginx_ssl_key_upload_src: ssl/*.key
nginx_ssl_key_upload_dest: /etc/ssl/private/

# Enable creating dynamic templated NGINX HTML demo websites.
nginx_html_demo_template_enable: false
nginx_html_demo_template:
  default:
    template_file: www/index.html.j2
    html_file_name: index.html
    html_file_location: /usr/share/nginx/html
    web_server_name: Default

# Enable creating dynamic templated NGINX configuration files.
# Defaults are the values found in a fresh NGINX installation.
nginx_main_template_enable: false
nginx_main_template:
  template_file: nginx.conf.j2
  conf_file_name: nginx.conf
  conf_file_location: /etc/nginx/
  user: nginx
  worker_processes: auto
  error_level: warn
  worker_connections: 1024
  http_enable: true
  http_settings:
    keepalive_timeout: 65
    cache: false
    rate_limit: false
    keyval: false
  stream_enable: false
  http_global_autoindex: false

# Enable creating dynamic templated NGINX HTTP configuration files.
# Defaults will not produce a valid configuration. Instead they are meant to showcase
# the options available for templating. Each key represents a new configuration file.
# Comment out reverse_proxy or web_server depending on whether you wish to create a web server
# or load balancer configuration file.
nginx_http_template_enable: false
nginx_http_template:
  default:
    template_file: http/default.conf.j2
    conf_file_name: default.conf
    conf_file_location: /etc/nginx/conf.d/
    port: 8081
    server_name: localhost
    error_page: /usr/share/nginx/html
    https_redirect: false
    autoindex: false
    ssl:
      cert: ssl/default.crt
      key: ssl/default.key
    web_server:
      locations:
        default:
          location: /
          html_file_location: /usr/share/nginx/html
          html_file_name: index.html
          autoindex: false
      http_demo_conf: false
    reverse_proxy:
      locations:
        backend:
          location: /
          proxy_pass: http://backend
      health_check_plus: false
    upstreams:
      upstream1:
        name: backend
        lb_method: least_conn
        zone_name: backend
        zone_size: 64k
        sticky_cookie: false
        servers:
          server1:
            address: localhost
            port: 8081
            weight: 1
            health_check: max_fails=1 fail_timeout=10s

# Enable creating dynamic templated NGINX stream configuration files.
nginx_stream_template_enable: false
nginx_stream_template_listen: 12345
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

This is a sample playbook file for deploying the Ansible Galaxy NGINX role to a dynamic inventory containing the `nginx` tag.

```yaml
---
- hosts: tag_nginx
  remote_user: root
  roles:
    - role: nginxinc.nginx
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing the open source version of NGINX as a simple web server.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - ansible-role-nginx
  vars:
    nginx_http_template_enable: true
    nginx_http_template:
      default:
        port: 80
        server_name: localhost
        error_page: /usr/share/nginx/html
        autoindex: false
        web_server:
          locations:
            default:
              location: /
              html_file_location: /usr/share/nginx/html
              html_file_name: index.html
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing the open source version of NGINX as a reverse proxy.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - nginxinc.nginx
  vars:
    nginx_http_template_enable: true
    nginx_http_template:
      default:
        reverse_proxy:
          locations:
            frontend:
              location: /
              proxy_pass: http://frontend_servers
            backend:
              location: /backend
              proxy_pass: http://backend_servers
        upstreams:
          upstream_1:
            name: frontend_servers
            lb_method: least_conn
            zone_name: frontend
            zone_size: 64k
            sticky_cookie: false
            servers:
              frontend_server_1:
                address: localhost
                port: 80
                weight: 1
                health_check: max_fails=3 fail_timeout=5s
          upstream_2:
            name: backend_servers
            lb_method: least_conn
            zone_name: backend
            zone_size: 64k
            sticky_cookie: false
            servers:
              backend_server_1:
                address: localhost
                port: 8080
                weight: 1
                health_check: max_fails=3 fail_timeout=5s
```


This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing NGINX Plus.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - role: nginxinc.nginx
  vars:
    nginx_type: plus
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost to install NGINX Plus and the NGINX Controller agent.

```yaml
- hosts: localhost
  become: true
  roles:
    - role: nginxinc.nginx
  vars:
    nginx_type: plus
    nginx_rest_api_enable: true
    nginx_rest_api_write: true
    nginx_controller_enable: true
    nginx_controller_api_key: <API_KEY_HERE>
    nginx_controller_api_endpoint: https://<FQDN>/1.4
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost to install NGINX Unit and the PHP/Perl NGINX Unit language modules.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - role: nginxinc.nginx
  vars:
    nginx_enable: false
    nginx_unit_enable: true
    nginx_unit_modules:
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
