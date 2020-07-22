# Changelog

## 0.15.0 (Unreleased)

BREAKING CHANGES:

*   The Debian and Ubuntu repositories have slightly changed. You may run into some duplication issues when running the role on a preexisting target that already has had NGINX installed using the role. To fix this, manually remove the old repository source.
*   If you use `custom_options` you will now need to manually end each directive with a semicolon.
*   The `status` directive is no longer supported in NGINX Plus, and the `stub_status` directive has been reworked into a template.
*   The listen directive structure in the `stream` template has been updated to the listen directive structure found in the `http` template. You can now specify multiple `listen` directives in the same `server` block as well as include any extra `listen` options you might need.

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

*   Add support to configure logrotate.
*   Add support for Ubuntu Focal.
*   Add support to configure SELinux.
*   Two new variables have been introduced -- `nginx_install` and `nginx_configure` -- to let you choose whether you want to install NGINX, configure NGINX, or both.

ENHANCEMENTS:

*   Molecule tests using Testinfra have been migrated to use Ansible instead.
*   The role now uses `include_tasks` instead of `import_tasks` when possible to speed up the role's execution time.
*   Improve configuration templating capabilities:
    *   Add support for unix upstreams.
    *   Add PID templating option.
    *   Add support for down parameter in upstreams.
    *   Add option for custom error pages.
    *   Add SSL support to `stream` contexts.

BUG FIXES:

*   `nginx_debug_output` would sometimes fail if NGINX had not been automatically started by the system upon installation.
*   If `http_demo_conf` was undefined the web server template interpolation would fail.

## 0.14.0 (April 22, 2020)

This is a relatively minor release, but it includes a potential breaking change (hence the version bump). The one major new feature is the ability to install/build NGINX Open Source from source.

BREAKING CHANGES:

*   The NGINX Controller agent can no longer be installed using this role. Please use the Ansible collection linked in the README.

FEATURES:

*   Install/build NGINX from source options now available.
*   Implement NGINX http sub module templating.
*   NGINX config is now correctly validated each run.
*   SSL Private Key data is hidden when running the role with the `--diff` flag.

BUG FIXES:

*   The role should no longer sporadically cause apt update to fail in amd64 systems when installing NGINX from an official repository.
*   Modules should now correctly install when using a specific NGINX Plus version.

## 0.13.0 (December 13, 2019)

BREAKING CHANGES:

*   The new listen templating options are not backwards with the previous listen templating options. Check the `README` or `molecule/template_module/playbook.yml` for examples on how to use the new listen template.
*   BSD and Linux NGINX installation tasks have undergone some major changes. As such, you may have to update your playbooks accordingly.

FEATURES:

*   Improve NGINX http templating:
    *   Multiple server support in HTTP contexts.
    *   Header support.
    *   OCSP stapling.
    *   Improved proxy settings.
    *   Logging settings.
    *   Improved SSL settings.
    *   Improved authentication settings.
    *   Max body size support.
    *   Improved listen templating.
*   Switch to Molecule for testing.
*   Add support for Debian Buster.
*   Support for specifying which version of NGINX to install.
*   Split default variables into multiple functional files.
*   Improve support for Alpine distributions.
*   Support for updating or removing NGINX from your system.
*   Implemented tags to support running specific tasks instead of the whole role.

BUG FIXES:

*   Module installation when using NGINX Plus has been fixed.
*   Websockets templating has been reenabled after being accidentally deleted.
*   When deleting your NGINX Plus license from the system, the NGINX Plus repository will also be deleted to prevent issues further down the line if you run a repository update since there will not be a license anymore to authenticate into the NGINX Plus repository.

## 0.12.0 (May 22, 2019)

FEATURES:

*   Improve NGINX http templating - following parameters are now supported:
    *   Websockets.
    *   Basic authentication.
    *   Proxy cache.
    *   Proxy redirect.
    *   Proxy timeouts.
    *   SSL.
    *   Root (in server context).
    *   Add basic NGINX stream templating.
    *   Add support for RHEL 8 and Alpine Linux.

BUG FIXES:

*   Fix module installation tasks.

## 0.11.0 (Januray 14, 2019)

FEATURES:

*   Allow setting a custom apt and rpm signing key host.
*   Add support for enabling an http to https redirects.
*   Add ansible_managed to templates.
*   Rename html_app_name to web_server_name.
*   Rename load_balancer block to reverse_proxy.
*   Allow setting the listen port when using SSL.
*   Improve SSL defaults.
*   Allow setting http or https server locations in proxy_pass.

BUG FIXES:

*   Ignore undefined values for autoindex and health check.
*   Clarify that the redirect variable refers to a http to https redirect.

## 0.10.1 (November 26, 2018)

BUG FIXES:

*   Fix HTML template to use correct variable name.

## 0.10.0 (November 26, 2018)

FEATURES:

*   Improve templating support for health checks, multiple location blocks, and auto indexing.

BUG FIXES:

*   Fetching the NGINX signing key is now more reliable.
*   Fixed HTML templating.

## 0.9.0 (October 18, 2018)

FEATURES:

*   Refactor NGINX templating and file uploading.
*   Add ability to upload and template HTML files.
*   Add ability to upload SSL keys and certificates.

## 0.8.0 (September 17, 2018)

FEATURES:

*   Add ability to install NGINX Plus Controller agent.
*   Refactor installation of NGINX Amplify agent.
*   Rename variables to be prefixed with `nginx_`.

BUG FIXES:

*   Correct spelling of name in `tasks/prerequisites/setup-debian.yml`.

## 0.7.1 (August 21, 2018)

FEATURES:

*   Add enabled parameter to NGINX and NGINX Unit handlers.

## 0.7.0 (August 4, 2018)

FEATURES:

*   Add Amazon Linux 2 support for NGINX Plus.
*   Add ability to delete NGINX Plus license after installation.

BUG FIXES:

*   GeoIP module can now be properly installed.
*   Module installation will no longer fail if only one module is specified.

## 0.6.0 (July 19, 2018)

FEATURES:

*   Improve NGINX Unit related documentation.
*   Add FreeBSD and Amazon Linux 2 support for NGINX Unit.
*   Allow users to install NGINX Unit without having to also install NGINX.

## 0.5.0 (June 28, 2018)

FEATURES:

*   Add support for NGINX Unit.

## 0.4.0 (May 25, 2018)

FEATURES:

*   Implement support for FreeBSD.
*   Allow users to select the default NGINX repository.

## 0.3.0 (April 19, 2018)

FEATURES:

*   Improve Travis CI testing strategy.

BUG FIXES:

*   Fix templating and push tasks.

## 0.2.0 (April 12, 2018)

FEATURES:

*   Add support for all first party NGINX modules.

BUG FIXES:

*   Role should now work correctly in distros with old versions of Python.
*   Rest API configuration will now only be created when rest_api_enable is set to true (an empty file would be created in previous versions if rest_api_enable was set to false).
*   Uploading/dynamically generating files should now result in the files being uploaded/created to/in the correct directory.

## 0.1.0 - Initial release (Januray 26, 2018)

Initial release of the NGINX Ansible role. Features include:

*   Install NGINX Open Source or NGINX Plus.
*   Choose between stable or mainline NGINX Open Source.
*   Install NGINX Amplify.
*   Install NGINX Javascript, Perl, and ModSecurity WAF NGINX modules.
*   Enable the NGINX Plus REST API and dashboard.
*   Upload NGINX configuration files.
*   Templated NGINX configuration system.
