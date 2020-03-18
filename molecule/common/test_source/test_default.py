import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_running_and_enabled(host):
    ngx = host.service("nginx")
    assert ngx.is_running
    assert ngx.is_enabled


def test_hosts_file(host):
    ngx = host.file('/etc/hosts')
    assert ngx.exists
    assert ngx.user == 'root'
    assert ngx.group == 'root'


def test_endpoint(host):
    command = """curl -I http://localhost/"""
    cmd = host.run(command)
    assert '200 OK' in cmd.stdout
