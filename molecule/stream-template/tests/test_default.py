import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    ngx = host.file('/etc/hosts')
    assert ngx.exists
    assert ngx.user == 'root'
    assert ngx.group == 'root'
