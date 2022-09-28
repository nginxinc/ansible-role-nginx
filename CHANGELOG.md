# Changelog

## 0.23.2 (September 28, 2022)

FEATURES:

* Check NGINX Plus license is valid before trying to install NGINX Plus (this means the role now requires the `community.crypto` collection).
* Add Ubuntu jammy (22.04) to the NGINX list of tested and supported platforms.
* Add RHEL 9 to the NGINX list of tested and supported platforms.
* Add Alpine Linux 3.16 to the NGINX list of tested and supported platforms (and remove Alpine Linux 3.12).
* Add CODEOWNERS file.

ENHANCEMENTS:

* Add support for PCRE 2 and OpenSSL 3.0 (built from source) when building NGINX from source.
* Tweak Release Drafter config.
* Bump the Ansible `community.general` collection to `5.5.0`, `ansible.posix` collection to `1.4.0` and `community.docker` collection to `3.1.0`.
* Re-add Alpine Linux tests to `downgrade` Molecule scenarios.

BUG FIXES:

* Ensure gpg-agent is installed on Ubuntu/Debian to avoid APT key tasks failures.
* Always refresh the `yum` cache.
* The role can now correctly upgrade NGINX to the latest release on Alpine Linux.

TESTS:

* Update GitHub actions to only skip \*plus\* scenarios when the NGINX Plus license secrets are not present (it used to only run the NGINX Plus test scenarios during internal PRs).
* Add SLES 15 to all Molecule tests.
* Create downgrade and upgrade tests for NGINX Plus.
* Remove Yamllint (Ansible Lint now incorporates Yamllint).
* Skip Ansible Lint line length and no templates in name rules. Slightly refactor code to incorporate changes added to Ansible Lint 6.7.0.

## 0.23.1 (April 6, 2022)

FEATURES:

* Add Molecule testing infrastructure for RHEL 7/8.
* Rename all modules to use the fully qualified collection name (FQCN) per Ansible guidelines.

ENHANCEMENTS:

* Bump the Ansible `community.general` collection to `4.7.0` and `community.docker` collection to `2.3.0`.
* Streamline configuring SELinux.
* Add `TimeoutStartSec` parameter to Systemd template.
* Update Dependabot to trigger updates at the same time across all NGINX core roles at the same time and to avoid triggering release drafter on GitHub actions dependency updates.

BUG FIXES:

Ansible check mode runs will no longer fail if NGINX has not yet been installed.

## 0.23.0 (February 16, 2022)

BREAKING CHANGES:

* CentOS 8 has reached EoL and has thus been removed from the list of supported platforms.
* The NGINX Plus `cookie-flag` module is no longer supported as of R26 and has been removed.
* Remove SELinux parameters deprecated since `0.17`.

FEATURES:

* Backwards support for older versions of Ansible (e.g. Ansible `<2.12`).
* Update NGINX Amplify repositories to use Python 3 when possible.
* Add Alpine Linux 3.15 to the NGINX Plus list of tested and supported platforms (and remove Alpine Linux 3.11).

ENHANCEMENTS:

* Use `pcre2` by default when possible.
* Bump the Ansible `community.general` collection to `4.4.0` and `community.docker` collection to `2.1.1`.

BUG FIXES:

* The Molecule `upgrade` scenario verification test no longer has to be updated on each new NGINX OSS release.
* Add GPG key for Ubuntu Focal during APT repository setup.

## 0.22.0 (December 9, 2021)

BREAKING CHANGES:

* The `nginx_state` variable has been replaced with `nginx_setup` and instead of using `present`, `absent`, `latest` you should now use `install`, `uninstall` and `upgrade`.
* `nginx_install` variable is no more. Use `nginx_enable` instead.
* Ansible core `2.12` is now a minimum requirement for the role.

FEATURES:

* Pin repository data when installing NGINX OSS on Alpine and Debian distributions.
* You can now downgrade versions of NGINX and switch from stable to mainline and viceversa. You will need to specify the NGINX branch and version you wish to install when tweaking versions.
* Add Alpine Linux 3.15 to the NGINX OSS list of tested and supported platforms (and remove Alpine Linux 3.11).

ENHANCEMENTS:

* Bump the Ansible `community.general` collection to `4.1.0` and `community.docker` collection to `2.0.2`.

BUG FIXES:

* When building NGINX from source, the original source FTP repository `ftp.pcre.org` is not available anymore, according to <http://pcre.org>. The FTP repository has been updated to use `ftp.exim.org` instead.
* Uninstalling NGINX should now work correctly under most scenarios.

## 0.21.3 (October 25, 2021)

ENHANCEMENTS:

* Change Dependabot frequency from daily to weekly.
* Minor touch-up of GitHub actions workflows.

## 0.21.2 (October 7, 2021)

ENHANCEMENTS:

* Remove RHEL/CentOS 6 task specific parameters given those platforms have reached EOL.
* Change Ansible Lint exceptions from using an ID identifier to a text identifier.
* Move non NGINX specific dependencies from the role into the Molecule Dockerfile.

BUG FIXES:

* Always update NGINX dependencies to the latest available version to avoid outdated dependency issues (e.g. outdated CA certificates).
* The Check NGINX handler should now be run in the correct directory in BSD systems.

## 0.21.1 (September 29, 2021)

FEATURES:

Support installing NGINX OSS in Amazon Linux.

ENHANCEMENTS:

* Update the README and Ansible metadata matrix of supported distributions for NGINX OSS and NGINX Plus.
* Update the Molecule tests to include the newly supported distributions and remove distributions that are no longer supported for NGINX OSS and NGINX Plus.
* Bump the Ansible `community.general` collection to `3.7.0`, `ansible.posix` collection to `1.3.0` and `community.docker` collection to `1.9.1`.

## 0.21.0 (August 11, 2021)

BREAKING CHANGES:

Remove the deprecation warning in the README detailing the advent of the [NGINX Core Ansible collection](https://github.com/nginxinc/ansible-collection-nginx) and the subsequent splitting from this role of the [Ansible NGINX Config role](https://github.com/nginxinc/ansible-role-nginx-config) and the [Ansible NGINX Unit role](https://github.com/nginxinc/ansible-role-nginx-unit).

FEATURES:

* Add a `nginx_manage_repo` feature flag which allows disabling NGINX repo management by this role.
* Add a `nginx_install_epel_release` feature flag which allows epel-release to not be installed by this role if so desired.

ENHANCEMENTS:

Bump the Ansible `community.general` collection to `3.5.0` and `community.docker` collection to `1.9.0`.

## 0.20.0 (June 9, 2021)

BREAKING CHANGES:

* The NGINX Plus repository has been updated. This might cause some issues when running the role on an instance that already has NGINX Plus installed. **Starting with NGINX Plus R25, you will need to install NGINX Plus using release `0.20.0`. If you are trying to install R23, please use release `0.19.2`. NGINX Plus R24 should work with both release `0.19.2` and `0.20.0`.**
* The NGINX Plus modsecurity module is no longer supported by this role. Until NGINX Plus R25 is released, you might keep using release `0.19.2` if you wish to install modsecurity.

ENHANCEMENTS:

* Replace Ansible base with Ansible core. Ansible core will be the "core" Ansible release moving forward from Ansible `2.11`.
* Update GitHub actions to add a workflow dispatch option.
* Replace "yes"/"no" boolean values with "true"/"false" to comply with YAML spec `1.2`.
* Bump the Ansible `community.general` collection to `3.2.0` and `community.docker` collection to `1.7.0`.

BUG FIXES:

Change the url used to grep the latest NGINX version when installing from source. This should avoid the source install failing whenever the `stable` release is higher than the latest `mainline`.

## 0.19.2 (April 28, 2021)

FEATURES:

* Replace Ansible community distribution with Ansible base and add the necessary extra collections as a dependency requirement. For reference, these are:

    ```yaml
    ---
    collections:
      - name: community.general
        version: 3.0.0
      - name: ansible.posix
        version: 1.2.0
      - name: community.docker  # This collection is only used as part of the Molecule testing suite
        version: 1.5.0
    ```

* Explicitly list Jinja2 `2.11.3` as a requirement, as well as detail the minimum supported version (`2.11.x`).
* Add support for Dependabot.
* Initial implementation of Release Drafter.

ENHANCEMENTS:

* Only run GitHub actions Galaxy CI/CD workflow when a new release is published.
* Add Alpine `3.13` to the list of NGINX Plus supported platforms.
* Specify GitHub actions Ubuntu release.
* Minor GitHub template tweaks, including the creation of a SECURITY doc.
* Add Molecule NGINX OSS tests for Alpine 3.13, remove Molecule tests for Debian stretch, and update list of supported platforms.
* Update Ansible base to `2.10.8`, Ansible Lint to `5.0.7`, Molecule to `3.3.0`, yamllint to `1.26.1` and Docker Python SDK to `5.0.0`.
* Consolidate Molecule testing scenarios to address changes introduced in Ansible Lint `5.*`.
* Override of systemd `Restart` value by using proper `nginx_service_restart` variable.

BUG FIXES:

* Add `state` parameter to package module in Molecule verification tests.
* Change the command directory when running the NGINX configuration check handler to prevent edge case errors when the handler is run from a directory that the NGINX process' user does not have access to.

## 0.19.1 (January 11, 2021)

ENHANCEMENTS:

* The GitHub actions Molecule CI/CD workflow should now correctly avoid running 'plus' related tests on external PRs.
* Update Ansible base to `2.10.4`, Ansible to `2.10.5`, Molecule to `3.2.2` and Docker Python SDK to `4.4.1`.
* Update copyright notice.

## 0.19.0 (December 23, 2020)

BREAKING CHANGES:

**The NGINX configuration functionalities included in this role have been removed as of release 0.19.0.** There now is a separate role to manage and create NGINX configurations available [here](https://github.com/nginxinc/ansible-role-nginx-config). Any new issues or PRs related to configuring NGINX should be submitted in the new NGINX configuration Ansible role repository. New issues or PRs related to configuring NGINX submitted in this repository will not be worked on.

ENHANCEMENTS:

The GitHub actions Molecule CI/CD workflow is no longer run on a new release (this is not necessary since it already runs on every push).

## 0.18.2 (December 22, 2020)

ENHANCEMENTS:

* Update Molecule to `3.2.1` and Docker Python SDK to `4.4.0`.
* Add Alpine `3.12` to supported platforms for NGINX Plus.
* Remove Alpine `3.9` and CentOS/RHEL `6` from supported platforms due to EOL.
* Replace TravisCI with GitHub actions.

## 0.18.1 (November 17, 2020)

ENHANCEMENTS:

Switch NGINX keysites and OSS default repository data from a dictionary to individual variables to prevent potential issues arisen from Jinja2 dictionary run-time evaluations.

BUG FIXES:

Fix issue whereas SELinux state would not be correctly set back to `enforcing` when `nginx_selinux: true`.

## 0.18.0 (November 13, 2020)

BREAKING CHANGES:

**The NGINX Unit functionalities included in this role have been removed as of release 0.18.0.** There now is a separate role to install NGINX Unit available [here](https://github.com/nginxinc/ansible-role-nginx-unit). Any new issues or PRs related to NGINX Unit should be submitted in the new NGINX Unit Ansible role repository. New issues or PRs related to NGINX Unit submitted in this repository will not be worked on.

## 0.17.4 (November 12, 2020)

ENHANCEMENTS:

Implement a new syntax to specify modules to be installed. You can now use the following format if you want further fine grained control over how you install modules:

```yaml
- name: njs  # Required
  state: present  # Optional
  version: =1.19.4+0.4.4-1~bionic  # Optional
```

The old method of specifying modules (using a list of names) still works as expected.

## 0.17.3 (November 9, 2020)

ENHANCEMENTS:

* Add survey to README.
* Improve README structure and use tables where relevant.
* Update Ansible (now Ansible base) to `2.10.3`, Ansible (now Ansible Community Distribution) to `2.10.3`, Ansible Lint to `4.3.7`, Molecule to `3.1.5`, and yamllint to `1.25.0`.
* Optimize NGINX Plus install/remove tasks.

BUG FIXES:

* Prevent TravisCI from trying to build (and failing) NGINX Plus images on external PRs.
* Fix naming for SELinux facts dictionary.
* Role now runs correctly when using Ansible's check mode.
* Removing the NGINX Plus license in RHEL based distros should no longer return a repository not found error.
* Fix issue when removing NGINX Plus license on some distributions.
* Fix Amazon Linux NGINX Plus install while at it.

## 0.17.2 (September 24, 2020)

BUG FIXES:

Fix an issue where sometimes the role handlers will fail in distros where NGINX is not started upon installation.

## 0.17.1 (September 22, 2020)

ENHANCEMENTS:

* The role will no longer fail automatically on unsupported platforms, but the error message will still be displayed.
* The `Check NGINX` handler now always outputs an `ok` state instead of `changed` since it's a read-only operation with no traceable changes.

## 0.17.0 (September 20, 2020)

BREAKING CHANGES:

* The process to install modules has changed. You will now have to use a list variable, `nginx_modules`, instead of manually setting the modules you want to install to `true` or `false`. This change will also simplify adding future supported modules to this role. You can find a list of supported modules for NGINX and NGINX Plus in [`vars/main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/main.yml).
* Modules can no longer be added to your NGINX config using this role. Please use the [`nginx_config`](https://github.com/nginxinc/ansible-role-nginx-config) role instead.
* Changed `nginx_configure` default value from `true` to `false` to further promote the adoption of the [NGINX config](https://github.com/nginxinc/ansible-role-nginx-config) role.

FEATURES:

* A new variable has been introduced:
  * `nginx_setup_license` -- Determine whether you want to use this role to upload your NGINX license to your target host.
* The role will now fail automatically if you try to deploy NGINX from an official repository in an unsupported distribution. You can find a list of supported distributions for NGINX and NGINX Plus in [`vars/main.yml`](https://github.com/nginxinc/ansible-role-nginx/blob/main/vars/main.yml)
* Three new tags have been introduced -- `nginx_setup_license`, `nginx_enable` and `nginx_check_support`.
* Add Alpine 3.12 to the list of supported platforms.
* Remove Alpine 3.8 from the list of supported platforms.
* Add NGINX Plus tests to TravisCI

ENHANCEMENTS:

* Added handlers to check for NGINX syntax validity and fail if any errors are detected.
* Switch to using `ansible_facts` wherever possible.
* Major backend refactoring to reduce the number of files and tasks.
* You can now specify an `nginx_repository` for NGINX Plus too.
* Moved "constant" variables to `vars/main.yml`.
* Included deprecation warnings in task names and files.
* Improved tasks naming conventions.
* Update Ansible to `2.9.13` and Ansible Lint to `4.3.5`.

BUG FIXES:

* NGINX Plus repository data for RHEL based distros is now appropriately set.
* Building NGINX from source should now work as expected in CentOS/RHEL 6 systems running Python `2.6` or earlier versions of `2.7`.

## 0.16.0 (August 28, 2020)

BREAKING CHANGES:

The Debian and Ubuntu repositories have slightly changed. You may run into some duplication issues when running the role on a preexisting target that already has had NGINX installed using the role. To fix this, manually remove the old repository source.

ENHANCEMENTS:

* Update Ansible to `2.9.12` and Ansible Lint to `4.3.2`.
* Explicitly define `mode` in relevant tasks.
* Explicitly define the `nginx` `apt_repository` filename in Debian based distros.

FEATURES:

TravisCI now always uses the latest version of Docker.

BUG FIXES:

Building OpenSSL from source should now work properly in CentOS 8.

## 0.15.0 (August 20, 2020)

DEPRECATION WARNING:

With the advent of Ansible collections and to reduce the overhead of this role, the decision has been made to split this role into three smaller roles:

* The NGINX Ansible role will keep working as is and be used to install and setup NGINX.
* There now is a separate role to manage and create NGINX configurations available [here](https://github.com/nginxinc/ansible-role-nginx-config). Any new issues or PRs related to configuring NGINX should be submitted in the new NGINX Config repository. New issues or PRs related to configuring NGINX submitted in this repository will not be worked on. The NGINX configuration functionalities included in this role will be removed in an upcoming release.
* NGINX Unit now has a separate role available [here](https://github.com/nginxinc/ansible-role-nginx-unit). Any new issues or PRs related to NGINX Unit should be submitted in the new NGINX Unit repository. New issues or PRs related to NGINX Unit submitted in this repository will not be worked on. The NGINX Unit functionalities included in this role will be removed in an upcoming release.

BREAKING CHANGES:

* The Debian and Ubuntu repositories have slightly changed. You may run into some duplication issues when running the role on a preexisting target that already has had NGINX installed using the role. To fix this, manually remove the old repository source.
* If you use `custom_options` you will now need to manually end each directive with a semicolon.
* The `status` directive is no longer supported in NGINX Plus, and the `stub_status` directive has been reworked into a template.
* The listen directive structure in the `stream` template has been updated to the listen directive structure found in the `http` template. You can now specify multiple `listen` directives in the same `server` block as well as include any extra `listen` options you might need.

    Old configuration example

    ```yaml
    listen_address: localhost
    listen_port: 80
    udp_enable: false
    ```

    New configuration example

    ```yaml
    listen:
      listen_localhost:
        ip: 0.0.0.0  # Wrap in square brackets for IPv6 addresses
        port: 80
        ssl: false
        opts: []  # Listen opts like udp which will be added (ssl is automatically added if you specify 'ssl:').
    ```

    The one major change is that instead of using `udp_enable: true` you will now need to use `opts: [udp]` if you wish to enable `udp`.

FEATURES:

* Add support to configure logrotate.
* Add support for Ubuntu Focal.
* Add support to configure SELinux.
* Two new variables have been introduced -- `nginx_enable` and `nginx_configure` -- to let you choose whether you want to install NGINX, configure NGINX, or both.

ENHANCEMENTS:

* Molecule tests using Testinfra have been migrated to use Ansible instead.
* The role now uses `include_tasks` instead of `import_tasks` when possible to speed up the role's execution time.
* Improve configuration cleanup capabilities. You can now remove all `*.conf` files in a given directory, or specify a list of files you wish to delete.
* Improve configuration templating capabilities:
  * Add support for unix upstreams.
  * Add PID templating option.
  * Add support for down parameter in upstreams.
  * Add option for custom error pages.
  * Add SSL support to `stream` contexts.

BUG FIXES:

* `nginx_debug_output` would sometimes fail if NGINX had not been automatically started by the system upon installation.
* If `http_demo_conf` was undefined the web server template interpolation would fail.

## 0.14.0 (April 22, 2020)

This is a relatively minor release, but it includes a potential breaking change (hence the version bump). The one major new feature is the ability to install/build NGINX Open Source from source.

BREAKING CHANGES:

The NGINX Controller agent can no longer be installed using this role. Please use the Ansible collection linked in the README.

FEATURES:

* Install/build NGINX from source options now available.
* Implement NGINX http sub module templating.
* NGINX config is now correctly validated each run.
* SSL Private Key data is hidden when running the role with the `--diff` flag.

BUG FIXES:

* The role should no longer sporadically cause apt update to fail in amd64 systems when installing NGINX from an official repository.
* Modules should now correctly install when using a specific NGINX Plus version.

## 0.13.0 (December 13, 2019)

BREAKING CHANGES:

* The new listen templating options are not backwards with the previous listen templating options. Check the `README` or `molecule/template_module/playbook.yml` for examples on how to use the new listen template.
* BSD and Linux NGINX installation tasks have undergone some major changes. As such, you may have to update your playbooks accordingly.

FEATURES:

* Improve NGINX http templating:
  * Multiple server support in HTTP contexts.
  * Header support.
  * OCSP stapling.
  * Improved proxy settings.
  * Logging settings.
  * Improved SSL settings.
  * Improved authentication settings.
  * Max body size support.
  * Improved listen templating.
* Switch to Molecule for testing.
* Add support for Debian Buster.
* Support for specifying which version of NGINX to install.
* Split default variables into multiple functional files.
* Improve support for Alpine distributions.
* Support for updating or removing NGINX from your system.
* Implemented tags to support running specific tasks instead of the whole role.

BUG FIXES:

* Module installation when using NGINX Plus has been fixed.
* Websockets templating has been reenabled after being accidentally deleted.
* When deleting your NGINX Plus license from the system, the NGINX Plus repository will also be deleted to prevent issues further down the line if you run a repository update since there will not be a license anymore to authenticate into the NGINX Plus repository.

## 0.12.0 (May 22, 2019)

FEATURES:

Improve NGINX http templating - following parameters are now supported:

* Websockets.
* Basic authentication.
* Proxy cache.
* Proxy redirect.
* Proxy timeouts.
* SSL.
* Root (in server context).
* Add basic NGINX stream templating.
* Add support for RHEL 8 and Alpine Linux.

BUG FIXES:

Fix module installation tasks.

## 0.11.0 (Januray 14, 2019)

FEATURES:

* Allow setting a custom apt and rpm signing key host.
* Add support for enabling an http to https redirects.
* Add ansible_managed to templates.
* Rename html_app_name to web_server_name.
* Rename load_balancer block to reverse_proxy.
* Allow setting the listen port when using SSL.
* Improve SSL defaults.
* Allow setting http or https server locations in proxy_pass.

BUG FIXES:

* Ignore undefined values for autoindex and health check.
* Clarify that the redirect variable refers to a http to https redirect.

## 0.10.1 (November 26, 2018)

BUG FIXES:

Fix HTML template to use correct variable name.

## 0.10.0 (November 26, 2018)

FEATURES:

Improve templating support for health checks, multiple location blocks, and auto indexing.

BUG FIXES:

* Fetching the NGINX signing key is now more reliable.
* Fixed HTML templating.

## 0.9.0 (October 18, 2018)

FEATURES:

* Refactor NGINX templating and file uploading.
* Add ability to upload and template HTML files.
* Add ability to upload SSL keys and certificates.

## 0.8.0 (September 17, 2018)

FEATURES:

* Add ability to install NGINX Plus Controller agent.
* Refactor installation of NGINX Amplify agent.
* Rename variables to be prefixed with `nginx_`.

BUG FIXES:

Correct spelling of name in `tasks/prerequisites/setup-debian.yml`.

## 0.7.1 (August 21, 2018)

FEATURES:

Add enabled parameter to NGINX and NGINX Unit handlers.

## 0.7.0 (August 4, 2018)

FEATURES:

* Add Amazon Linux 2 support for NGINX Plus.
* Add ability to delete NGINX Plus license after installation.

BUG FIXES:

* GeoIP module can now be properly installed.
* Module installation will no longer fail if only one module is specified.

## 0.6.0 (July 19, 2018)

FEATURES:

* Improve NGINX Unit related documentation.
* Add FreeBSD and Amazon Linux 2 support for NGINX Unit.
* Allow users to install NGINX Unit without having to also install NGINX.

## 0.5.0 (June 28, 2018)

FEATURES:

Add support for NGINX Unit.

## 0.4.0 (May 25, 2018)

FEATURES:

* Implement support for FreeBSD.
* Allow users to select the default NGINX repository.

## 0.3.0 (April 19, 2018)

FEATURES:

Improve Travis CI testing strategy.

BUG FIXES:

Fix templating and push tasks.

## 0.2.0 (April 12, 2018)

FEATURES:

Add support for all first party NGINX modules.

BUG FIXES:

* Role should now work correctly in distros with old versions of Python.
* Rest API configuration will now only be created when rest_api_enable is set to true (an empty file would be created in previous versions if rest_api_enable was set to false).
* Uploading/dynamically generating files should now result in the files being uploaded/created to/in the correct directory.

## 0.1.0 - Initial release (Januray 26, 2018)

Initial release of the NGINX Ansible role. Features include:

* Install NGINX Open Source or NGINX Plus.
* Choose between stable or mainline NGINX Open Source.
* Install NGINX Amplify.
* Install NGINX Javascript, Perl, and ModSecurity WAF NGINX modules.
* Enable the NGINX Plus REST API and dashboard.
* Upload NGINX configuration files.
* Templated NGINX configuration system.
