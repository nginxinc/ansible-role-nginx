# Contributing Guidelines

The following is a set of guidelines for contributing to the NGINX Ansible role. We really appreciate that you are considering contributing!

#### Table Of Contents

[Getting Started](#getting-started)

[Contributing](#contributing)

[Code Guidelines](#code-guidelines)

- [Git Guidelines](#git-guidelines)
- [Ansible Guidelines](#ansible-guidelines)

[Code of Conduct](/CODE_OF_CONDUCT.md)

## Getting Started

Follow this project's [Installation Guide](/README.md#Installation) to install Ansible, Ansible Lint, and Molecule and get ready to develop and test the NGINX Ansible role.

### Project Structure

- The NGINX Ansible role is written in [`yaml`](https://yaml.org) and supports NGINX Open Source, NGINX Plus, NGINX Agent and NGINX Amplify.
- The project follows the standard [Ansible role directory structure](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html):
  - The main "codebase" is found in the [`tasks/`](/tasks/) directory.
  - Variables can be found in [`defaults/main/`](/defaults/main/). The filenames in this directory highlight which variables are contained in each file.
  - "Constant/hardcoded" variables can be found in [`vars/main.yml`](/vars/main.yml). Use this file if you want to create a variable that should not be tweaked by users except in exceptional circumstances.
  - Configuration templates for logrotate, SELinux, and systemd can be found in the [`templates/`](/templates/) directory.
  - [Molecule](https://molecule.readthedocs.io/) tests can be found in the [`molecule/`](/molecule/) directory. Tweak or add new scenarios as necessary. Read the [Molecule docs](https://molecule.readthedocs.io/) and check out the [`default`](/molecule/default/) Molecule scenario to get an idea of how Molecule works in action.
  - CI/CD is done via GitHub Actions using the workflow files found in the [`.github/workflows/`](/.github/workflows/) directory. If you create a new Molecule scenario, you will also need to update the [Molecule workflow](/.github/workflows/molecule.yml).

## Contributing

### Report a Bug

To report a bug, open an issue on GitHub with the label `bug` using the available bug report issue template. Please ensure the bug has not already been reported. **If the bug is a potential security vulnerability, please report it using our [security policy](/SECURITY.md).**

### Suggest a Feature or Enhancement

To suggest a feature or enhancement, please create an issue on GitHub with the label `enhancement` using the available [feature request template](/.github/feature_request_template.md). Please ensure the feature or enhancement has not already been suggested.

### Open a Pull Request (PR)

- Fork the repo, create a branch, implement your changes, add any relevant tests, and submit a PR when your changes are **tested** (using Molecule) and ready for review.
- Fill in the [PR template](/.github/pull_request_template.md).

> [!NOTE]
> If you'd like to implement a new feature, please consider creating a [feature request issue](/.github/feature_request_template.md) first to start a discussion about the feature.

#### F5 Contributor License Agreement (CLA)

F5 requires all external contributors to agree to the terms of the F5 CLA (available [here](https://github.com/f5/.github/blob/main/CLA/cla-markdown.md)) before any of their changes can be incorporated into an F5 Open Source repository.

If you have not yet agreed to the F5 CLA terms and submit a PR to this repository, a bot will prompt you to view and agree to the F5 CLA. You will have to agree to the F5 CLA terms through a comment in the PR before any of your changes can be merged. Your agreement signature will be safely stored by F5 and no longer be required in future PRs.

## Code Guidelines

### Ansible Guidelines

- Run `ansible lint` over your code to automatically resolve a lot of `yaml`, `jinja2`, and Ansible style issues.
- Run `molecule test` on your code before you submit a PR to catch any potential issues. If you are testing a specific Molecule scenario, run `molecule test -s <scenario>`. If you are testing any of the NGINX Plus scenarios (`...-plus`), you will need to procure an NGINX Plus license (check out the [F5 Trials](https://www.f5.com/trials) site to find out how to request one).
- Check out [Ansible's official tips and tricks](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html) site for more best practices.

### Git Guidelines

- Keep a clean, concise and meaningful git commit history on your branch (within reason), rebasing locally and squashing before submitting a PR.
- If possible and/or relevant, use the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format when writing a commit message, so that changelogs can be automatically generated.
- Follow the guidelines of writing a good commit message as described here <https://chris.beams.io/posts/git-commit/> and summarized in the next few points:
  - In the subject line, use the present tense ("Add feature" not "Added feature").
  - In the subject line, use the imperative mood ("Move cursor to..." not "Moves cursor to...").
  - Limit the subject line to 72 characters or less.
  - Reference issues and pull requests liberally after the subject line.
  - Add more detailed description in the body of the git message (`git commit -a` to give you more space and time in your text editor to write a good message instead of `git commit -am`).
