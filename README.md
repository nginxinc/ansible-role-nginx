[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Molecule CI/CD](https://github.com/nginxinc/ansible-role-nginx/workflows/Molecule%20CI/CD/badge.svg)](https://github.com/nginxinc/ansible-role-nginx/actions)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# 👾 *Help make the NGINX Ansible role better by participating in our [survey](https://forms.office.com/Pages/ResponsePage.aspx?id=L_093Ttq0UCb4L-DJ9gcUKLQ7uTJaE1PitM_37KR881UM0NCWkY5UlE5MUYyWU1aTUcxV0NRUllJSC4u)!* 👾

# Ansible NGINX Role

This role installs NGINX Open Source, NGINX Plus, or the NGINX Amplify agent on your target host.

**Note:** This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

## Requirements

### NGINX Plus (Optional)

If you wish to install NGINX Plus using this role, you will need to obtain an NGINX Plus license beforehand. *You do not need to do anything beforehand if you want to install NGINX OSS.*

### Ansible

* This role is developed and tested with [maintained](https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html) versions of Ansible core (above `2.12`).
* When using Ansible core, you will also need to install the following collections:

    ```yaml
    ---
    collections:
      - name: ansible.posix
        version: 1.4.0
      - name: community.general
        version: 5.5.0
      - name: community.crypto # Only required if you plan to install NGINX Plus
        version: 2.5.0
      - name: community.docker # Only required if you plan to use Molecule (see below)
        version: 3.1.0
    ```

    **Note:** You can alternatively install the Ansible community distribution (what is known as the "old" Ansible) if you don't want to manage individual collections.
* You will need to run this role as a root user using Ansible's `become` parameter. Make sure you have set up the appropriate permissions on your target hosts.
* Instructions on how to install Ansible can be found in the [Ansible website](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#upgrading-ansible-from-version-2-9-and-older-to-version-2-10-or-later).

### Jinja2

* This role uses Jinja2 templates. Ansible core installs Jinja2 by default, but depending on your install and/or upgrade path, you might be running an outdated version of Jinja2. The minimum version of Jinja2 required for the role to properly function is `2.11`.
* Instructions on how to install Jinja2 can be found in the [Jinja2 website](https://jinja.palletsprojects.com/en/2.11.x/intro/#installation).

### Molecule (Optional)

* Molecule is used to test the various functionalities of the role. The recommended version of Molecule to test this role is `3.3`.
* Instructions on how to install Molecule can be found in the [Molecule website](https://molecule.readthedocs.io/en/latest/installation.html). *You will also need to install the Molecule Docker driver.*
* To run the NGINX Plus Molecule tests, you must copy your NGINX Plus license to the role's [`files/license`](https://github.com/nginxinc/ansible-role-nginx/blob/main/files/license/) folder.

You can alternatively add your NGINX Plus repository certificate and key to the local environment. Run the following commands to export these files as base64-encoded variables and execute the Molecule tests:

```bash
export NGINX_CRT=$( cat <path to your certificate file> | base64 )
export NGINX_KEY=$( cat <path to your key file> | base64 )
molecule test -s plus
```

## Installation

### Ansible Galaxy

Use `ansible-galaxy install nginxinc.nginx` to install the latest stable release of the role on your system. Alternatively, if you have already installed the role, use `ansible-galaxy install -f nginxinc.nginx` to update the role to the latest release.

### Git

Use `git clone https://github.com/nginxinc/ansible-role-nginx.git` to pull the latest edge commit of the role from GitHub.

## Platforms

The NGINX Ansible role supports all platforms supported by [NGINX Open Source](https://nginx.org/en/linux_packages.html), [NGINX Plus](https://docs.nginx.com/nginx/technical-specs/), and the [NGINX Amplify agent](https://github.com/nginxinc/nginx-amplify-doc/blob/master/amplify-faq.md#21-what-operating-systems-are-supported):

### NGINX Open Source

```yaml
Alpine:
  - 3.13
  - 3.14
  - 3.15
  - 3.16
Amazon Linux:
  - 2
CentOS:
  - 7.4+
Debian:
  - buster (10)
  - bullseye (11)
Red Hat:
  - 7.4+
  - 8
  - 9
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - bionic (18.04)
  - focal (20.04)
  - impish (21.10)
  - jammy (22.04)
```

### NGINX Plus

```yaml
Alpine:
  - 3.13
  - 3.14
  - 3.15
  - 3.16
Amazon Linux 2:
  - any
CentOS:
  - 7.4+
Debian:
  - buster (10)
  - bullseye (11)
FreeBSD:
  - 12.1+
  - 13
Oracle Linux:
  - 7.4+
Red Hat:
  - 7.4+
  - 8
  - 9
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - bionic (18.04)
  - focal (20.04)
  - jammy (22.04)
```

### NGINX Amplify Agent

```yaml
Amazon Linux 2:
  - any
Debian:
  - buster (10)
  - bullseye (11)
Red Hat:
  - 8
Ubuntu:
  - bionic
  - focal
```

**Note:** You can also use this role to compile NGINX Open Source from source, install NGINX Open Source on compatible yet unsupported platforms, or install NGINX Open Source on BSD systems at your own risk.

## Role Variables

This role has multiple variables. The descriptions and defaults for all these variables can be found in the **[`defaults/main/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/)** folder in the following files:

| Name | Description |
| ---- | ----------- |
| **[`main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/main.yml)** | NGINX installation variables |
| **[`amplify.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/amplify.yml)** | NGINX Amplify agent installation variables |
| **[`bsd.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/bsd.yml)** | BSD installation variables |
| **[`logrotate.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/logrotate.yml)** | Logrotate configuration variables |
| **[`selinux.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/selinux.yml)** | SELinux configuration variables |
| **[`systemd.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/defaults/main/systemd.yml)** | Systemd configuration variables |

Similarly, descriptions and defaults for preset variables can be found in the **[`vars/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/)** folder in the following files:

| Name | Description |
| ---- | ----------- |
| **[`main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/main.yml)** | List of supported NGINX platforms, modules, and Linux installation variables |

## Example Playbooks

Working functional playbook examples can be found in the **[`molecule/`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/)** folder in the following files:

| Name | Description |
| ---- | ----------- |
| **[`default/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/default/converge.yml)** | Install a specific version of NGINX and set up logrotate |
| **[`downgrade/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/downgrade/converge.yml)** | Downgrade to a specific version of NGINX |
| **[`downgrade_plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/downgrade_plus/converge.yml)** | Downgrade to a specific version of NGINX Plus |
| **[`module/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/module/converge.yml)** | Install various NGINX supported modules |
| **[`plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/plus/converge.yml)** | Install NGINX Plus and various NGINX Plus supported modules |
| **[`source/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/source/converge.yml)** | Install NGINX from source |
| **[`uninstall/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/uninstall/converge.yml)** | Uninstall NGINX |
| **[`uninstall_plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/uninstall_plus/converge.yml)** | Uninstall NGINX Plus |
| **[`upgrade/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/upgrade/converge.yml)** | Upgrade NGINX |
| **[`upgrade_plus/converge.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/molecule/upgrade_plus/converge.yml)** | Upgrade NGINX Plus |

Do note that if you install this repository via Ansible Galaxy, you will have to replace the role variable in the sample playbooks from `ansible-role-nginx` to `nginxinc.nginx`.

## Other NGINX Ansible Collections and Roles

You can find the Ansible NGINX Core collection of roles to install and configure NGINX Open Source, NGINX Plus, and NGINX App Protect [here](https://github.com/nginxinc/ansible-collection-nginx).

You can find the Ansible NGINX configuration role to configure NGINX [here](https://github.com/nginxinc/ansible-role-nginx-config).

You can find the Ansible NGINX App Protect role to install and configure NGINX App Protect WAF and NGINX App Protect DoS [here](https://github.com/nginxinc/ansible-role-nginx-app-protect).

You can find the Ansible NGINX Unit role to install NGINX Unit [here](https://github.com/nginxinc/ansible-role-nginx-unit).

## License

[Apache License, Version 2.0](https://github.com/nginxinc/ansible-role-nginx/blob/main/LICENSE)

## Author Information

[Alessandro Fael Garcia](https://github.com/alessfg)

[Grzegorz Dzien](https://github.com/gdzien)

[Tom Gamull](https://github.com/magicalyak)

&copy; [F5 Networks, Inc.](https://www.f5.com/) 2018 - 2022
