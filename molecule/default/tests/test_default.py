import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_cron_service(host):
    os = host.system_info.distribution
    if os in ("ubuntu", "debian"):
        service_name = 'cron'
    else:
        service_name = 'crond'

    s = host.service(service_name)

    assert s.is_running
    assert s.is_enabled
