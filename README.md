[![Ansible Galaxy](https://img.shields.io/badge/galaxy-nginxinc.nginx-5bbdbf.svg)](https://galaxy.ansible.com/nginxinc/nginx)
[![Molecule CI/CD](https://github.com/nginxinc/ansible-role-nginx/workflows/Molecule%20CI/CD/badge.svg)](https://github.com/nginxinc/ansible-role-nginx/actions/workflows/molecule.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/nginxinc/ansible-role-nginx/badge)](https://securityscorecards.dev/viewer/?uri=github.com/nginxinc/ansible-role-nginx)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Community Support](https://badgen.net/badge/support/community/cyan?icon=awesome)](/SUPPORT.md)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# 👾 *Help make the NGINX Ansible role better by participating in our [survey](https://forms.office.com/Pages/ResponsePage.aspx?id=L_093Ttq0UCb4L-DJ9gcUKLQ7uTJaE1PitM_37KR881UM0NCWkY5UlE5MUYyWU1aTUcxV0NRUllJSC4u)!* 👾

# Ansible NGINX Role

This role installs NGINX (NGINX Open Source), NGINX Plus, NGINX Agent and/or the NGINX Amplify agent on your target host(s).

> [!IMPORTANT]
> This role is still in active development. There may be unidentified issues and the role variables may change as development continues.

## Role Requirements

### NGINX

Depending on your target NGINX use case, you might need to obtain a license or API key/token before being able to use the role:

| Product | Requirements |
|---------|--------------|
| NGINX | None |
| NGINX Plus | NGINX Plus license (both a license key and crt files) |
| NGINX Agent | A compatible control plane and (optionally) an NGINX One SaaS console data plane token |
| NGINX Amplify | API key found within the NGINX Amplify SaaS console |

### Ansible

If you want to use this role, you will need to use a supported version of Ansible core and Jinja2 as well as a few Ansible collections.

For ease of use, you can install and/or upgrade Ansible core, Jinja2, and the aforementioned Ansible collections by running the following four commands on your Ansible host:

```bash
pip install --upgrade -r https://raw.githubusercontent.com/nginxinc/ansible-role-nginx/main/.github/workflows/requirements/requirements_ansible.txt
curl -O https://raw.githubusercontent.com/nginxinc/ansible-role-nginx/main/.github/workflows/requirements/requirements_collections.yml
ansible-galaxy install --force -r requirements_collections.yml
rm -f requirements_collections.yml
```

This will also ensure you are deploying/running this role with a fully tested version of the aforementioned packages/collections.

#### Ansible core

- This role is developed and tested with [maintained](https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html) versions of Ansible core and Python.

  ***Note:** Ansible `2.18` does no longer support the `yum` module and as such, is not supported by this role until Amazon Linux 2 reaches EoL.*
- Instructions on how to install Ansible core can be found in the [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#upgrading-ansible-from-version-2-9-and-older-to-version-2-10-or-later) docs.
- When using Ansible core, you will also need to install the following Ansible collections:

  ```yaml
  ---
  collections:
    - name: ansible.posix
      version: 1.6.2
    - name: community.general
      version: 10.0.1
    - name: community.crypto # Only required if you plan to install NGINX Plus
      version: 2.22.3
    - name: community.docker # Only required if you plan to use Molecule (see below)
      version: 4.1.0
  ```

- Instructions on how to install Ansible collections can be found in the [Ansible collections](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html) guide.
- You will need to run this role as a root user using Ansible's `become` parameter. Make sure you have set up the appropriate permissions on your target hosts.

> [!TIP]
> You can alternatively install the [Ansible community distribution](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#selecting-an-ansible-package-and-version-to-install) (what is still known Ansible -- instead of Ansible core) if you don't want to manage individual collections.

#### Jinja2

- This role uses Jinja2 templates. Ansible core installs Jinja2 by default, but depending on your install and/or upgrade path, you might be running an outdated version of Jinja2. The minimum version of Jinja2 required for the role to properly function is `3.1`.
- Instructions on how to install Jinja2 can be found in the [Jinja2 website](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation).

### Testing suite (Optional)

If you want to contribute to this role, you will also need to install Ansible Lint and Molecule.

#### Ansible Lint (Optional)

- Ansible Lint is used to lint the role for both Ansible best practices and potential Ansible/YAML issues.
- Instructions on how to install Ansible Lint can be found in the [Ansible Lint website](https://ansible.readthedocs.io/projects/lint/installing/).
- Once installed, using Ansible Lint is as easy as running:

  ```bash
  ansible-lint
  ```

- For ease of use, you can install and/or upgrade Ansible Lint by running the following command on your Ansible host:

  ```bash
  pip install -r https://raw.githubusercontent.com/nginxinc/ansible-role-nginx/main/.github/workflows/requirements/requirements_ansible_lint.txt
  ```

#### Molecule (Optional)

- Molecule is used to test the various functionalities of the role.
- Instructions on how to install Molecule can be found in the [Molecule website](https://molecule.readthedocs.io/en/latest/installation.html). *You will also need to install the Molecule plugins package and the Docker Python SDK.*
- To run any of the NGINX Plus Molecule tests, you must first copy your NGINX Plus license to the role's [`files/license`](/files/license/) directory.

  You can alternatively add your NGINX Plus repository certificate and key to the local environment. Run the following commands to export these files as base64-encoded variables and execute the Molecule tests:

  ```bash
  export NGINX_CRT=$( cat <path to your certificate file> | base64 )
  export NGINX_KEY=$( cat <path to your key file> | base64 )
  molecule test -s plus
  ```

- For ease of use, you can install and/or upgrade Molecule, the Molecule plugins package, and the Docker Python SDK by running the following command on your Ansible host:

  ```bash
  pip install --upgrade -r https://raw.githubusercontent.com/nginxinc/ansible-role-nginx/main/.github/workflows/requirements/requirements_molecule.txt
  ```

## Role Installation

This role can be installed via either Ansible Galaxy (the Ansible community marketplace) or by cloning this repo. Once installed, you will need to include the role in your Ansible playbook using [the `roles` keyword, the `import_role` module, or the `include_role` module](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#using-roles).

### Ansible Galaxy

To install the latest stable release of the role on your system, use:

```bash
ansible-galaxy install nginxinc.nginx
```

Alternatively, if you have already installed the role, you can update the role to the latest release by using:

```bash
ansible-galaxy install -f nginxinc.nginx
```

To use the role, include the following task in your playbook:

```yaml
- name: Install NGINX
  ansible.builtin.include_role:
    name: nginxinc.nginx
```

### Git

To pull the latest edge commit of the role from GitHub, use:

```bash
git clone https://github.com/nginxinc/ansible-role-nginx.git
```

To use the role, include the following task in your playbook:

```yaml
- name: Install NGINX
  ansible.builtin.include_role:
    name: <path/to/repo> # e.g. <roles/ansible-role-nginx> if you clone the repo inside your project's roles directory
```

## Platforms

The NGINX Ansible role aims to work on all platforms supported by the latest mainline/stable release of [NGINX Open Source](https://nginx.org/en/linux_packages.html), [NGINX Plus](https://docs.nginx.com/nginx/technical-specs/), [NGINX Agent](https://docs.nginx.com/nginx-agent/technical-specifications/), and the [NGINX Amplify agent](https://github.com/nginxinc/nginx-amplify-doc/blob/master/amplify-faq.md#21-what-operating-systems-are-supported).

Older releases might work, but keep in mind that NGINX Open Source only actively develops against the [latest release of the mainline and stable branches](https://www.f5.com/company/blog/nginx/nginx-1-18-1-19-released), and NGINX Plus only [officially supports releases for two years](https://docs.nginx.com/nginx/releases/#support-for-current-and-previous-releases).

> [!NOTE]
> Due to the release pipeline of the various projects supported by this role, there is usually a short delay between new releases and support for the release in this role.

### NGINX Open Source

```yaml
AlmaLinux:
  - 8
  - 9
Alpine:
  - 3.18
  - 3.19
  - 3.20
Amazon Linux:
  - 2
  - 2023
Debian:
  - bullseye (11)
  - bookworm (12)
Oracle Linux:
  - 8
  - 9
Red Hat:
  - 8
  - 9
Rocky Linux:
  - 8
  - 9
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - focal (20.04)
  - jammy (22.04)
  - noble (24.04)
  - oracular (24.10)
```

### NGINX Plus

```yaml
AlmaLinux:
  - 8
  - 9
Alpine:
  - 3.17
  - 3.18
  - 3.19
  - 3.20
Amazon Linux:
  - 2
  - 2023
Debian:
  - bullseye (11)
  - bookworm (12)
FreeBSD:
  - 13
  - 14
Oracle Linux:
  - 8.1+
  - 9
Red Hat:
  - 8.1+
  - 9
Rocky Linux:
  - 8
  - 9
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - focal (20.04)
  - jammy (22.04)
  - noble (24.04)
```

### NGINX Agent

```yaml
AlmaLinux:
  - 8
  - 9
Alpine:
  - 3.17
  - 3.18
  - 3.19
  - 3.20
Amazon Linux:
  - 2
  - 2023
Debian:
  - bullseye (11)
  - bookwork (12)
FreeBSD:
  - 13
  - 14
Oracle Linux:
  - 8
  - 9
Red Hat:
  - 8
  - 9
Rocky Linux:
  - 8
  - 9
SUSE/SLES:
  - 12
  - 15
Ubuntu:
  - focal (20.04)
  - jammy (22.04)
  - noble (24.04)
```

### NGINX Amplify Agent

```yaml
Amazon Linux:
  - 2
Debian:
  - buster (10)
  - bullseye (11)
Red Hat:
  - 8
  - 9
Ubuntu:
  - bionic (18.04)
  - focal (20.04)
  - jammy (22.04)
```

> [!WARNING]
> At your own risk, you can also use this role to compile NGINX Open Source from source, install NGINX Open Source on "compatible" yet unsupported platforms, install NGINX from your respective distribution package manager, or install NGINX Open Source on BSD systems.

## Role Variables

This role has multiple variables. The descriptions and defaults for all these variables can be found in the **[`defaults/main/`](/defaults/main/)** directory in the following files:

| Name | Description |
| ---- | ----------- |
| **[`main.yml`](/defaults/main/main.yml)** | NGINX installation variables |
| **[`agent.yml`](/defaults/main/agent.yml)** | NGINX Agent installation variables |
| **[`amplify.yml`](/defaults/main/amplify.yml)** | NGINX Amplify agent installation variables |
| **[`bsd.yml`](/defaults/main/bsd.yml)** | BSD installation variables |
| **[`logrotate.yml`](/defaults/main/logrotate.yml)** | Logrotate configuration variables |
| **[`selinux.yml`](/defaults/main/selinux.yml)** | SELinux configuration variables |
| **[`systemd.yml`](/defaults/main/systemd.yml)** | Systemd configuration variables |

Similarly, descriptions and defaults for preset variables can be found in the **[`vars/`](/vars/)** directory in the following files:

| Name | Description |
| ---- | ----------- |
| **[`main.yml`](/vars/main.yml)** | List of supported NGINX platforms, modules, and Linux installation variables |

## Example Playbooks

Working functional playbook examples can be found in the **[`molecule/`](/molecule/)** folder in the following files:

| Name | Description |
| ---- | ----------- |
| **[`agent/converge.yml`](/molecule/agent/converge.yml)** | Install and configure NGINX Agent to connect to the NGINX One SaaS control plane on F5 Distributed Cloud |
| **[`amplify/converge.yml`](/molecule/amplify/converge.yml)** | Install and configure the NGINX Amplify agent |
| **[`default/converge.yml`](/molecule/default/converge.yml)** | Install a specific version of NGINX, install various NGINX supported modules, tweak systemd and set up logrotate |
| **[`distribution/converge.yml`](/molecule/distribution/converge.yml)** | Install NGINX from the distribution's package repository instead of NGINX's package repository |
| **[`downgrade/converge.yml`](/molecule/downgrade/converge.yml)** | Downgrade to a specific version of NGINX |
| **[`downgrade-plus/converge.yml`](/molecule/downgrade-plus/converge.yml)** | Downgrade to a specific version of NGINX Plus |
| **[`plus/converge.yml`](/molecule/plus/converge.yml)** | Install NGINX Plus and various NGINX Plus supported modules |
| **[`source/converge.yml`](/molecule/source/converge.yml)** | Install NGINX from source |
| **[`stable/converge.yml`](/molecule/stable/converge.yml)** | Install NGINX using the latest stable release |
| **[`uninstall/converge.yml`](/molecule/uninstall/converge.yml)** | Uninstall NGINX |
| **[`uninstall-plus/converge.yml`](/molecule/uninstall-plus/converge.yml)** | Uninstall NGINX Plus |
| **[`upgrade/converge.yml`](/molecule/upgrade/converge.yml)** | Upgrade NGINX |
| **[`upgrade-plus/converge.yml`](/molecule/upgrade-plus/converge.yml)** | Upgrade NGINX Plus |
| **[`version/converge.yml`](/molecule/version/converge.yml)** | Install a specific version of NGINX and various NGINX modules |

> [!NOTE]
> If you install this repository via Ansible Galaxy, you will need to replace the `include_role` variable in the example playbooks from `ansible-role-nginx` to `nginxinc.nginx`.

## Other NGINX Ansible Collections and Roles

You can find the Ansible NGINX Core collection of roles to install and configure NGINX Open Source, NGINX Plus, and NGINX App Protect [here](https://github.com/nginxinc/ansible-collection-nginx).

You can find the Ansible NGINX configuration role to configure NGINX [here](https://github.com/nginxinc/ansible-role-nginx-config).

You can find the Ansible NGINX App Protect role to install and configure NGINX App Protect WAF and NGINX App Protect DoS [here](https://github.com/nginxinc/ansible-role-nginx-app-protect).

## License

[Apache License, Version 2.0](/LICENSE)

## Author Information

[Alessandro Fael Garcia](https://github.com/alessfg)

[Grzegorz Dzien](https://github.com/gdzien)

[Tom Gamull](https://github.com/magicalyak)

&copy; [F5, Inc.](https://www.f5.com/) 2018 - 2024
