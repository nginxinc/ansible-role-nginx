# Contributing Guidelines

The following is a set of guidelines for contributing to the NGINX Ansible role. We really appreciate that you are considering contributing!

#### Table Of Contents

[Ask a Question](#ask-a-question)

[Getting Started](#getting-started)

[Contributing](#contributing)

[Code Guidelines](#code-guidelines)
*   [Git Guidelines](#git-guidelines)
*   [Ansible Guidelines](#ansible-guidelines)

[Code of Conduct](https://github.com/nginxinc/ansible-role-nginx/blob/main/CODE_OF_CONDUCT.md)

## Ask a Question

Don't know how something works? Curious if the role can achieve your desired functionality? Please open an Issue on GitHub with the label `question`.

## Getting Started

Follow our [Installation Guide](https://github.com/nginxinc/ansible-role-nginx/blob/main/README.md#Installation) to install Ansible and Molecule and get ready to use the NGINX Ansible role.

### Project Structure

*   The NGINX Ansible role is written in `yaml` and supports NGINX Open Source, NGINX Plus, and NGINX Amplify.
*   The project follows the standard [Ansible role directory structure](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html):
    *   The main code is found in `tasks/`.
    *   Variables can be found in `defaults/main/*.yml`.
    *   "Constant" variables can be found in `vars/main.yml`.
    *   Configuration templates for NGINX can be found in `templates/`.
    *   [Molecule](https://molecule.readthedocs.io/) tests can be found in `molecule/`.
    *   CI/CD is done via Travis using `.travis.yml` deployment `yaml` files.

## Contributing

### Report a Bug

To report a bug, open an issue on GitHub with the label `bug` using the available bug report issue template. Please ensure the issue has not already been reported.

### Suggest an Enhancement

To suggest an enhancement, please create an issue on GitHub with the label `enhancement` using the available feature issue template.

### Open a Pull Request

*   Fork the repo, create a branch, submit a PR when your changes are **tested** (ideally using Molecule) and ready for review.
*   Fill in [our pull request template](https://github.com/nginxinc/ansible-role-nginx/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

Note: if you’d like to implement a new feature, please consider creating a feature request issue first to start a discussion about the feature.

## Code Guidelines

### Ansible Guidelines

*   Run `molecule lint` over your code to automatically resolve a lot of `yaml` and Ansible style issues.
*   Run `molecule test --all` on your code before you submit a PR to catch any potential issues.
*   Follow these guides on some good practices for Ansible:
    *   <https://www.ansible.com/blog/ansible-best-practices-essentials>
    *   <https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html>

### Git Guidelines

*   Keep a clean, concise and meaningful git commit history on your branch (within reason), rebasing locally and squashing before submitting a PR.
*   Follow the guidelines of writing a good commit message as described here <https://chris.beams.io/posts/git-commit/> and summarised in the next few points:
    *   In the subject line, use the present tense ("Add feature" not "Added feature").
    *   In the subject line, use the imperative mood ("Move cursor to..." not "Moves cursor to...").
    *   Limit the subject line to 72 characters or less.
    *   Reference issues and pull requests liberally after the subject line.
    *   Add more detailed description in the body of the git message (`git commit -a` to give you more space and time in your text editor to write a good message instead of `git commit -am`).
