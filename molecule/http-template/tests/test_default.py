import nginx
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


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


# Test for https://github.com/nginxinc/ansible-role-nginx/pull/157
# def test_client_max_body_size(host):
#     f = host.file('/etc/nginx/conf.d/default.conf')
#     c = nginx.loads(f.content_string)
#     vs = c.server.filter('Key', 'client_max_body_size')
#     assert len(vs) == 1
#     assert vs[0].value == '512k'
#     l = c.server.filter('Location', '/')
#     vl = l[0].filter('Key', 'client_max_body_size')
#     assert len(vl) == 1
#     assert vl[0].value == '5m'
