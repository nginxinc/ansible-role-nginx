import nginx
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_is_installed(host):
    ngx = host.package("nginx")
    assert ngx.is_installed


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


def test_generated_files(host):
    assert host.file('/etc/nginx/conf.d/default.conf').exists


def test_default_server(host):
    f = host.file('/etc/nginx/conf.d/default.conf')
    c = nginx.loads(f.content_string)
    lf = c.server.filter('Location', '/')
    assert len(lf) == 1
