[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Build Status](https://travis-ci.org/nginxinc/ansible-role-nginx.svg?branch=main)](https://travis-ci.org/nginxinc/ansible-role-nginx)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# 👾 *Help make the NGINX Ansible role better by participating in our [survey](https://forms.office.com/Pages/ResponsePage.aspx?id=L_093Ttq0UCb4L-DJ9gcUKLQ7uTJaE1PitM_37KR881UM0NCWkY5UlE5MUYyWU1aTUcxV0NRUllJSC4u)!* 👾

# Ansible NGINX Role

This role installs NGINX Open Source, NGINX Plus, or the NGINX Amplify agent on your target host.

**Note:** This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

**Deprecation Warnings:**

With the advent of Ansible collections and the release of the [NGINX Core Ansible collection](https://github.com/nginxinc/ansible-collection-nginx), the decision has been made to split this role into three smaller roles and reduce the overhead of this role:
*   The NGINX Ansible role will keep working as is and be used to install and setup NGINX.
*   **The NGINX configuration functionalities included in this role will be removed in an upcoming release at some stage after December 1st 2020.** There now is a separate role to manage and create NGINX configurations available [here](https://github.com/nginxinc/ansible-role-nginx-config). Any new issues or PRs related to configuring NGINX should be submitted in the new NGINX Config repository. New issues or PRs related to configuring NGINX submitted in this repository will not be worked on.
*   **The NGINX Unit functionalities included in this role have been removed as of release 0.18.0.** There now is a separate role to install NGINX Unit available [here](https://github.com/nginxinc/ansible-role-nginx-unit). Any new issues or PRs related to NGINX Unit should be submitted in the new NGINX Unit repository. New issues or PRs related to NGINX Unit submitted in this repository will not be worked on. This disclaimer will be removed in a future release.

## Requirements

### Ansible

*   This role is developed and tested with [maintained](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#release-status) versions of Ansible. Backwards compatibility is not guaranteed.
*   Instructions on how to install Ansible can be found in the [Ansible website](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

### Molecule

*   Molecule `3.x` is used to test the various functionalities of the role.
*   Instructions on how to install Molecule can be found in the [Molecule website](https://molecule.readthedocs.io/en/latest/installation.html).

## Installation

### Ansible Galaxy

Use `ansible-galaxy install nginxinc.nginx` to install the latest stable release of the role on your system.

### Git

Use `git clone https://github.com/nginxinc/ansible-role-nginx.git` to pull the latest edge commit of the role from GitHub.

## Platforms

The NGINX Ansible role supports all platforms supported by [NGINX Open Source](https://nginx.org/en/linux_packages.html), [NGINX Plus](https://docs.nginx.com/nginx/technical-specs/), and the [NGINX Amplify agent](https://github.com/nginxinc/nginx-amplify-doc/blob/master/amplify-faq.md#21-what-operating-systems-are-supported):

### NGINX Open Source

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

### NGINX Plus

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

### NGINX Amplify Agent

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

**Note:** You can also use this role to compile NGINX Open Source from source, install NGINX Open Source on compatible yet unsupported platforms, or install NGINX Open Source on BSD systems at your own risk.

## Role Variables

This role has multiple variables. The descriptions and defaults for all these variables can be found in the **[`defaults/main/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/)** folder in the following files:

|Name|Description|
|----|-----------|
|**[`main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/main.yml)**|NGINX installation variables|
|**[`amplify.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/amplify.yml)**|NGINX Amplify agent installation variables|
|**[`template.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/template.yml)**|NGINX configuration templating variables|
|**[`upload.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/upload.yml)**|NGINX configuration/HTML/SSL upload variables|
|**[`linux.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/linux.yml)**|Linux installation variables|
|**[`bsd.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/bsd.yml)**|BSD installation variables|

Similarly, descriptions and defaults for preset variables can be found in the **[`vars/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/)** folder in the following files:

|Name|Description|
|----|-----------|
|**[`main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/main.yml)**|List of supported NGINX platforms and modules|

## Example Playbooks

Working functional playbook examples can be found in the **[`molecule/common/playbooks/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/)** folder in the following files:

|Name|Description|
|----|-----------|
|**[`default_converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/default_converge.yml)**|Install a specific version of NGINX and set up logrotate|
|**[`module_converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/module_converge.yml)**|Install various NGINX supported modules|
|**[`plus_converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/plus_converge.yml)**|Install NGINX Plus and various NGINX Plus supported modules|
|**[`source_converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/source_converge.yml)**|Install NGINX from source|
|**[`stable_push_converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/stable_push_converge.yml)**|Install NGINX using the stable branch and push a preexisting config from your system to your NGINX instance|
|**[`template_converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/common/playbooks/template_converge.yml)**|Use the NGINX configuration templating variables to create an NGINX configuration file|

Do note that if you install this repository via Ansible Galaxy, you will have to replace the role variable in the sample playbooks from `ansible-role-nginx` to `nginxinc.nginx`.

## Other NGINX Ansible Collections and Roles

You can find the Ansible NGINX Core collection of roles to install and configure NGINX Open Source, NGINX Plus, and NGINX App Protect [here](https://github.com/nginxinc/ansible-collection-nginx).

You can find the Ansible NGINX configuration role to configure NGINX [here](https://github.com/nginxinc/ansible-role-nginx-config).

You can find the Ansible NGINX App Protect role to install and configure NGINX App Protect [here](https://github.com/nginxinc/ansible-role-nginx-app-protect).

You can find the Ansible NGINX Controller collection of roles to install and configure NGINX Controller [here](https://github.com/nginxinc/ansible-collection-nginx_controller).

You can find the Ansible NGINX Unit role to install NGINX Unit [here](https://github.com/nginxinc/ansible-role-nginx-unit).

## License

[Apache License, Version 2.0](https://github.com/nginxinc/ansible-role-nginx/blob/main/LICENSE)

## Author Information

[Alessandro Fael Garcia](https://github.com/alessfg)

[Grzegorz Dzien](https://github.com/gdzien)

[Tom Gamull](https://github.com/magicalyak)

&copy; [F5 Networks, Inc.](https://www.f5.com/) 2018 - 2020
