Ansible NGINX Role
==================

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Build Status](https://travis-ci.org/nginxinc/ansible-role-nginx.svg?branch=main)](https://travis-ci.org/nginxinc/ansible-role-nginx)

This role installs NGINX Open Source, NGINX Plus, the NGINX Amplify agent, or NGINX Unit on your target host.

**Note:** This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

**Deprecation Warnings:**

With the advent of Ansible collections and to reduce the overhead of this role, the decision has been made to split this role into three smaller roles:
*   The NGINX Ansible role will keep working as is and be used to install and setup NGINX.
*   There now is a separate role to manage and create NGINX configurations available [here](https://github.com/nginxinc/ansible-role-nginx-config). Any new issues or PRs related to configuring NGINX should be submitted in the new NGINX Config repository. New issues or PRs related to configuring NGINX submitted in this repository will not be worked on. The NGINX configuration functionalities included in this role will be removed in an upcoming release.
*   NGINX Unit now has a separate role available [here](https://github.com/nginxinc/ansible-role-nginx-unit). Any new issues or PRs related to NGINX Unit should be submitted in the new NGINX Unit repository. New issues or PRs related to NGINX Unit submitted in this repository will not be worked on. The NGINX Unit functionalities included in this role will be removed in an upcoming release.

Requirements
------------

**Ansible**

This role was developed and tested with [maintained](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#release-status) versions of Ansible. Backwards compatibility is not guaranteed.

Instructions on how to install Ansible can be found in the [Ansible website](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

**Molecule**

Molecule is used to test the various functionalities of the role.

Instructions on how to install Molecule can be found in the [Molecule website](https://molecule.readthedocs.io/en/latest/installation.html).

Installation
------------

**Ansible Galaxy**

Use `ansible-galaxy install nginxinc.nginx` to install the latest stable release of the role on your system.

**Git**

Use `git clone https://github.com/nginxinc/ansible-role-nginx.git` to pull the latest edge commit of the role from GitHub.

Platforms
---------

The NGINX Ansible role supports all platforms supported by [NGINX Open Source](https://nginx.org/en/linux_packages.html), [NGINX Plus](https://docs.nginx.com/nginx/technical-specs/), the [NGINX Amplify agent](https://github.com/nginxinc/nginx-amplify-doc/blob/master/amplify-faq.md#21-what-operating-systems-are-supported), and [NGINX Unit](https://unit.nginx.org/installation/#official-packages):

**NGINX Open Source**

```yaml
Alpine:
  - 3.9
  - 3.10
  - 3.11
  - 3.12
CentOS:
  - 6
  - 7.4+
  - 8
Debian:
  - stretch
  - buster
Red Hat:
  - 6
  - 7.4+
  - 8
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - xenial
  - bionic
  - eoan
  - focal
```

**NGINX Plus**

```yaml
Alpine:
  - 3.9
  - 3.10
  - 3.11
Amazon Linux:
  - 2018.03
Amazon Linux 2:
  - any
CentOS:
  - 6.5+
  - 7.4+
  - 8
Debian:
  - stretch
  - buster
FreeBSD:
  - 11.2+
  - 12
Oracle Linux:
  - 6.5+
  - 7.4+
Red Hat:
  - 6.5+
  - 7.4+
  - 8
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - xenial
  - bionic
  - eoan
  - focal
```

**NGINX Amplify Agent**

```yaml
Amazon Linux:
  - 2017.09
CentOS:
  - 6
  - 7
Debian:
  - jessie
  - stretch
Red Hat:
  - 6
  - 7
Ubuntu:
  - xenial
  - bionic
  - focal
```

**NGINX Unit**

```yaml
Amazon Linux:
  - 2018.03
Amazon Linux 2:
  - any
CentOS:
  - 6
  - 7
  - 8
Debian:
  - stretch
  - buster
Red Hat:
  - 6
  - 7
  - 8
Ubuntu:
  - xenial
  - bionic
  - focal
```

**Note:** You can also use this role to compile NGINX Open Source from source, install NGINX Open Source on compatible yet unsupported platforms, or install NGINX Open Source on BSD systems at your own risk.

Role Variables
--------------

This role has multiple variables. The descriptions and defaults for all these variables can be found in the **`defaults/main/`** directory in the following files:

-   **[defaults/main/main.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/main.yml):** NGINX installation variables
-   **[defaults/main/amplify.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/amplify.yml):** NGINX Amplify agent installation variables
-   **[defaults/main/template.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/template.yml):** NGINX configuration templating variables
-   **[defaults/main/upload.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/upload.yml):** NGINX configuration/HTML/SSL upload variables
-   **[defaults/main/linux.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/linux.yml):** Linux installation variables
-   **[defaults/main/bsd.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/bsd.yml):** BSD installation variables
-   **[defaults/main/unit.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/unit.yml):** NGINX Unit installation variables

Similarly, descriptions and defaults for preset variables can be found in the **`vars/`** directory in the following files:

-   **[vars/main.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/main.yml):** List of supported NGINX platforms and modules

Example Playbooks
-----------------

Working functional playbook examples can be found in the **`molecule/common/`** directory in the following files:

-   **[molecule/common/playbooks/default_converge.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/default_converge.yml):** Install a specific version of NGINX and set up logrotate
-   **[molecule/common/playbooks/module_converge.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/module_converge.yml):** Install various NGINX supported modules
-   **[molecule/common/playbooks/plus_converge.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/plus_converge.yml):** Install NGINX Plus and various NGINX Plus supported modules
-   **[molecule/common/playbooks/source_converge.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/source_converge.yml):** Install NGINX from source
-   **[molecule/common/playbooks/stable_push_converge.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/stable_push_converge.yml):** Install NGINX using the stable branch and push a preexisting config from your system to your NGINX instance
-   **[molecule/common/playbooks/template_converge.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/template_converge.yml):** Use the NGINX configuration templating variables to create an NGINX configuration file
-   **[molecule/common/playbooks/unit_converge.yml](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/unit_converge.yml):** Install NGINX Unit

Do note that if you install this repository via Ansible Galaxy, you will have to replace the role variable in the sample playbooks from `ansible-role-nginx` to `nginxinc.nginx`.

Other NGINX Roles
-----------------

You can find an Ansible role to configure NGINX [here](https://github.com/nginxinc/ansible-role-nginx-config)

You can find an Ansible role to install and configure NGINX App Protect [here](https://github.com/nginxinc/ansible-role-nginx-app-protect)

You can find an Ansible collection of roles to install and configure NGINX Controller [here](https://github.com/nginxinc/ansible-collection-nginx_controller)

You can find an Ansible role to install NGINX Unit [here](https://github.com/nginxinc/ansible-role-nginx-unit)

License
-------

[Apache License, Version 2.0](https://github.com/nginxinc/ansible-role-nginx/blob/main/LICENSE)

Author Information
------------------

[Alessandro Fael Garcia](https://github.com/alessfg)

[Grzegorz Dzien](https://github.com/gdzien)

[Tom Gamull](https://github.com/magicalyak)

&copy; [F5 Networks, Inc.](https://www.f5.com/) 2018 - 2020
