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
    assert host.file('/etc/nginx/conf.d/frontend_default.conf').exists
    assert host.file('/etc/nginx/conf.d/backend_default.conf').exists


def test_default_server(host):
    f = host.file('/etc/nginx/conf.d/default.conf')
    c = nginx.loads(f.content_string)
    lf = c.server.filter('Location', '/')
    assert len(lf) == 1
    lb = c.server.filter('Location', '/backend')
    assert len(lb) == 1


def test_client_max_body_size(host):
    f = host.file('/etc/nginx/conf.d/default.conf')
    c = nginx.loads(f.content_string)
    vs = c.server.filter('Key', 'client_max_body_size')
    assert len(vs) == 1
    assert vs[0].value == '512k'
    lc = c.server.filter('Location', '/')
    vl = lc[0].filter('Key', 'client_max_body_size')
    assert len(vl) == 1
    assert vl[0].value == '5m'
