# Changelog

## 0.14.0

This is a relatively minor release, but it includes a potential breaking change (hence the version bump). The one major new feature is the ability to install/build NGINX Open Source from source.

Features:

*   Install/build NGINX from source options now available
*   Implement NGINX http sub module templating
*   NGINX config is now correctly validated each run
*   SSL Private Key data is hidden when running the role with the --diff flag

Bug fixes:

*   The role should no longer sporadically cause apt update to fail in amd64 systems when installing NGINX from an official repository
*   Modules should now correctly install when using a specific NGINX Plus version

Breaking changes:

*   The NGINX Controller agent can no longer be installed using this role. Please use the Ansible collection linked in the README

## 0.13.0

Features:

*   Improve NGINX http templating:
    *   Multiple server support in HTTP contexts
    *   Header support
    *   OCSP stapling
    *   Improved proxy settings
    *   Logging settings
    *   Improved SSL settings
    *   Improved authentication settings
    *   Max body size support
    *   Improved listen templating
*   Switch to Molecule for testing
*   Add support for Debian Buster
*   Support for specifying which version of NGINX to install
*   Split default variables into multiple functional files
*   Improve support for Alpine distributions
*   Support for updating or removing NGINX from your system
*   Implemented tags to support running specific tasks instead of the whole role

Bug fixes:

*   Module installation when using NGINX Plus has been fixed
*   Websockets templating has been reenabled after being accidentally deleted
*   When deleting your NGINX Plus license from the system, the NGINX Plus repository will also be deleted to prevent issues further down the line if you run a repository update since there will not be a license anymore to authenticate into the NGINX Plus repository.

Breaking changes:

*   The new listen templating options are not backwards with the previous listen templating options. Check the `README` or `molecule/template_module/playbook.yml` for examples on how to use the new listen template.
*   BSD and Linux NGINX installation tasks have undergone some major changes. As such, you may have to update your playbooks accordingly.

## 0.12.0

Features:

*   Improve NGINX http templating - following parameters are now supported:
    *   Websockets
    *   Basic authentication
    *   Proxy cache
    *   Proxy redirect
    *   Proxy timeouts
    *   SSL
    *   Root (in server context)
    *   Add basic NGINX stream templating
    *   Add support for RHEL 8 and Alpine Linux

Bug fixes:

*   Fix module installation tasks

## 0.11.0

Features:

*   Allow setting a custom apt and rpm signing key host
*   Add support for enabling an http to https redirects
*   Add ansible_managed to templates
*   Rename html_app_name to web_server_name
*   Rename load_balancer block to reverse_proxy
*   Allow setting the listen port when using SSL
*   Improve SSL defaults
*   Allow setting http or https server locations in proxy_pass

Bug fixes:

*   Ignore undefined values for autoindex and health check
*   Clarify that the redirect variable refers to a http to https redirect

## 0.10.1

Bug fixes:

*   Fix HTML template to use correct variable name

## 0.10.0

Features:

*   Improve templating support for health checks, multiple location blocks, and auto indexing

Bug fixes:

*   Fetching the NGINX signing key is now more reliable
*   Fixed HTML templating

## 0.9.0

Features:

*   Refactor NGINX templating and file uploading
*   Add ability to upload and template HTML files
*   Add ability to upload SSL keys and certificates

## 0.8.0

Features:

*   Add ability to install NGINX Plus Controller agent
*   Refactor installation of NGINX Amplify agent
*   Rename variables to be prefixed with `nginx_`

Bug fixes:

*   Correct spelling of name in `tasks/prerequisites/setup-debian.yml`

## 0.7.1

Features:

*   Add enabled parameter to NGINX and NGINX Unit handlers

## 0.7.0

Features:

*   Add Amazon Linux 2 support for NGINX Plus
*   Add ability to delete NGINX Plus license after installation

Bug fixes:

*   GeoIP module can now be properly installed
*   Module installation will no longer fail if only one module is specified

## 0.6.0

Features:

*   Improve NGINX Unit related documentation
*   Add FreeBSD and Amazon Linux 2 support for NGINX Unit
*   Allow users to install NGINX Unit without having to also install NGINX

## 0.5.0

Features:

*   Add support for NGINX Unit

## 0.4.0

Features:

*   Implement support for FreeBSD
*   Allow users to select the default NGINX repository

## 0.3.0

New features:

*   Improve Travis CI testing strategy

Bug fixes:

*   Fix templating and push tasks

## 0.2.0

New features:

*   Add support for all first party NGINX modules

Bug fixes:

*   Role should now work correctly in distros with old versions of Python
*   Rest API configuration will now only be created when rest_api_enable is set to true (an empty file would be created in previous versions if rest_api_enable was set to false)
*   Uploading/dynamically generating files should now result in the files being uploaded/created to/in the correct directory

## 0.1.0 - Initial release

Initial release of the NGINX Ansible role. Features include:

*   Install NGINX Open Source or NGINX Plus.
*   Choose between stable or mainline NGINX Open Source.
*   Install NGINX Amplify.
*   Install NGINX Javascript, Perl, and ModSecurity WAF NGINX modules.
*   Enable the NGINX Plus REST API and dashboard.
*   Upload NGINX configuration files.
*   Templated NGINX configuration system.
