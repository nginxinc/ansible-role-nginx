Ansible NGINX Role
==================

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Build Status](https://travis-ci.org/nginxinc/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/nginxinc/ansible-role-nginx)

This role installs NGINX Open Source, NGINX Plus, the NGINX Amplify agent, or NGINX Unit on your target host.

**Note:** This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

Requirements
------------

**Ansible**

This role was developed and tested with [maintained](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#release-status) versions of Ansible. Backwards compatibility is not guaranteed.

Instructions on how to install Ansible can be found in the [Ansible website](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

**Molecule**

Molecule is used to test the various functionailities of the role. Instructions on how to install Molecule can be found in the [Molecule website](https://molecule.readthedocs.io/en/latest/installation.html).

Installation
------------

**Ansible Galaxy**

Use `ansible-galaxy install nginxinc.nginx` to install the latest stable release of the role on your system.

**Git**

Use `git clone https://github.com/nginxinc/ansible-role-nginx.git` to pull the latest edge commit of the role from GitHub.

Platforms
---------

The NGINX Ansible role supports all platforms supported by [NGINX Open Source](https://nginx.org/en/linux_packages.html#mainline), [NGINX Plus](https://www.nginx.com/products/technical-specs/), the [NGINX Amplify agent](https://github.com/nginxinc/nginx-amplify-doc/blob/master/amplify-faq.md#21-what-operating-systems-are-supported), and [NGINX Unit](https://unit.nginx.org/installation/#official-packages):

**NGINX Open Source**

```yaml
Alpine:
  versions:
    - 3.8
    - 3.9
    - 3.10
    - 3.11
CentOS:
  versions:
    - 6
    - 7
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
    - focal
```

**NGINX Plus**

```yaml
Alpine:
  versions:
    - 3.8
    - 3.9
    - 3.10
    - 3.11
Amazon Linux:
  versions:
    - 2018.03
Amazon Linux 2:
  versions:
    - any
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
    - focal
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
    - xenial
    - bionic
RedHat:
  versions:
    - 6
    - 7
```

**NGINX Unit**

```yaml
Amazon Linux:
  versions:
    - 2018.03
Amazon Linux 2:
  versions:
    - any
CentOS:
  versions:
    - 6
    - 7
    - 8
Debian:
  versions:
    - stretch
    - buster
RedHat:
  versions:
    - 6
    - 7
    - 8
Ubuntu:
  versions:
    - xenial
    - bionic
    - focal
```

Role Variables
--------------

This role has multiple variables. The descriptions and defaults for all these variables can be found in the **`defaults/main`** directory in the following files:

-   **[defaults/main/main.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/defaults/main/main.yml):** NGINX installation variables
-   **[defaults/main/amplify.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/defaults/main/amplify.yml):** NGINX Amplify agent installation variables
-   **[defaults/main/template.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/defaults/main/template.yml):** NGINX configuration templating variables
-   **[defaults/main/upload.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/defaults/main/upload.yml):** NGINX configuration/HTML/SSL upload variables
-   **[defaults/main/linux.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/defaults/main/linux.yml):** Linux installation variables
-   **[defaults/main/bsd.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/defaults/main/bsd.yml):** BSD installation variables
-   **[defaults/main/unit.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/defaults/main/unit.yml):** NGINX Unit installation variables

Example Playbooks
-----------------

Working functional playbook examples can be found in the **`molecule/common`** directory in the following files:

-   **[molecule/common/playbook_default.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/molecule/common/playbook_default.yml):** Install a specific version of NGINX and set up logrotate
-   **[molecule/common/playbook_module.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/molecule/common/playbook_module.yml):** Install various NGINX supported modules
-   **[molecule/common/playbook_source.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/molecule/common/playbook_source.yml):** Install NGINX from source
-   **[molecule/common/playbook_stable_push.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/molecule/common/playbook_stable_push.yml):** Install NGINX using the stable branch and push a preexisting config from your system to your NGINX instance
-   **[molecule/common/playbook_template.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/molecule/common/playbook_template.yml):** Use the NGINX configuration templating variables to create an NGINX configuration file
-   **[molecule/common/playbook_unit.yml](https://github.com/nginxinc/ansible-role-nginx/blob/master/molecule/common/playbook_unit.yml):** Install NGINX Unit

Do note that if you install this repository via Ansible Galaxy, you will have to replace the role variable in the sample playbooks from `ansible-role-nginx` to `nginxinc.nginx`.

Other NGINX Roles
-----------------

You can find an Ansible collection of roles to help you install and configure NGINX Controller [here](https://github.com/nginxinc/ansible-collection-nginx_controller)

You can find an Ansible role to help you install and configure NGINX App Protect [here](https://github.com/nginxinc/ansible-role-nginx-app-protect)

License
-------

[Apache License, Version 2.0](https://github.com/nginxinc/ansible-role-nginx/blob/master/LICENSE)

Author Information
------------------

[Alessandro Fael Garcia](https://github.com/alessfg)

[Grzegorz Dzien](https://github.com/gdzien)

&copy; [NGINX, Inc.](https://www.nginx.com/) 2018 - 2020
