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
Alpine:
  versions:
    - 3.8
    - 3.9
    - 3.10
CentOS:
  versions:
    - 6
    - 7.4+
    - 8
Debian:
  versions:
    - stretch
    - buster
FreeBSD:
  versions:
    - 11.2+
    - 12
RedHat:
  versions:
    - 6
    - 7.4+
    - 8
SUSE/SLES:
  versions:
    - 12
    - 15
Ubuntu:
  versions:
    - xenial
    - bionic
```

**NGINX Plus**

```yaml
Alpine:
  versions:
    - 3.8
    - 3.9
    - 3.10
Amazon Linux:
  versions:
    - 2018.03
Amazon Linux 2:
  versions:
    - LTS
CentOS:
  versions:
    - 6.5+
    - 7.4+
    - 8
Debian:
  versions:
    - stretch
    - buster
FreeBSD:
  versions:
    - 11.2+
    - 12
Oracle Linux:
  versions:
    - 6.5+
    - 7.4+
RedHat:
  versions:
    - 6.5+
    - 7.4+
    - 8
SUSE/SLES:
  versions:
    - 12
    - 15
Ubuntu:
  versions:
    - xenial
    - bionic
```

**NGINX Amplify Agent**

```yaml
Amazon Linux:
  versions:
    - 2017.09
CentOS:
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
    - bionic
RedHat:
  versions:
    - 6
    - 7
```

**NGINX Controller Agent**

```yaml
Amazon Linux:
  versions:
    - 2017.09
Amazon Linux 2:
  versions:
    - LTS
CentOS:
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
    - bionic
RedHat:
  versions:
    - 6
    - 7
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
    - buster
Ubuntu:
  versions:
    - xenial
    - bionic
Amazon Linux:
  versions:
    - 2018.03
Amazon Linux 2:
  versions:
    - 2
FreeBSD:
  versions:
    - 10
    - 11
```

Role Variables
--------------

This role has multiple variables. The descriptions and defaults for all these variables
are in the directory **defaults/main** in the following files:

- **[main.yml: Common variables](defaults/main/main.yml)**
- **[linux.yml: Linux common varables (nginx_linux_\*, nginx_plus_linux_\*)](defaults/main/linux.yml)**
- **[bsd.yml: BSD common variables (nginx_bsd_\*, nginx_plus_bsd_\*)](defaults/main/bsd.yml)**
- **[freebsd.yml: FreeBSD variables (nginx_freebsd_\*)](defaults/main/freebsd.yml)**


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
    - role: nginxinc.nginx
  vars:
    nginx_http_template_enable: true
    nginx_http_template:
      default:
        template_file: http/default.conf.j2
        conf_file_name: default.conf
        conf_file_location: /etc/nginx/conf.d/
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
              autoindex: false
          http_demo_conf: false
```

This is a sample playbook file for deploying the Ansible Galaxy NGINX role in a localhost and installing the open source version of NGINX as a reverse proxy.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - role: nginxinc.nginx
  vars:
    nginx_http_template_enable: true
    nginx_http_template:
      default:
        template_file: http/default.conf.j2
        conf_file_name: default.conf
        conf_file_location: /etc/nginx/conf.d/
        servers:
          server1:  
            listen:
              listen_localhost:
                #ip: 0.0.0.0
                port: 80
                opts:
                  - default_server
            server_name: localhost
            error_page: /usr/share/nginx/html
            autoindex: false
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
                address: 0.0.0.0
                port: 8081
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
                address: 0.0.0.0
                port: 8082
                weight: 1
                health_check: max_fails=3 fail_timeout=5s
      frontend:
        template_file: http/default.conf.j2
        conf_file_name: frontend_default.conf
        conf_file_location: /etc/nginx/conf.d/
        servers:
          server1:
            listen:
              listen_localhost:
                ip: 0.0.0.0
                port: 8081
                opts: []
            server_name: localhost
            error_page: /usr/share/nginx/html
            autoindex: false
            web_server:
              locations:
                frontend_site:
                  location: /
                  proxy_hide_headers:
                    - X-Powered-By
                  html_file_location: /usr/share/nginx/html
                  html_file_name: index.html
                  autoindex: false
              http_demo_conf: false
      backend:
        template_file: http/default.conf.j2
        conf_file_name: backend_default.conf
        conf_file_location: /etc/nginx/conf.d/
        servers:
          server1:
            listen:
              listen_localhost:
                ip: 0.0.0.0
                port: 8082
                opts: []
            server_name: localhost
            error_page: /usr/share/nginx/html
            autoindex: false
            web_server:
              locations:
                backend_site:
                  location: /
                  html_file_location: /usr/share/nginx/html
                  html_file_name: index.html
                  autoindex: false
              http_demo_conf: false
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
    nginx_rest_api_port: 80
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

[Alessandro Fael Garcia](https://github.com/alessfg)

[Grzegorz Dzien](https://github.com/gdzien)

&copy; [NGINX, Inc.](https://www.nginx.com/) 2018 - 2019
