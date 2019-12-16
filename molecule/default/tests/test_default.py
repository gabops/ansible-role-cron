import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cron_jobs(host):
    c = host.run('crontab -l')

    assert '*/3 * * * * touch /tmp/cron_job' in c.stdout
    assert '*/3 * * * * touch /tmp/common_job' in c.stdout
    assert '*/3 * * * * touch /tmp/group_job' in c.stdout
    assert '*/3 * * * * touch /tmp/host_job' in c.stdout


def test_cron_service(host):
    os = host.system_info.distribution
    if os in ("ubuntu", "debian"):
        service_name = 'cron'
    elif os in ("amzn", "centos"):
        service_name = 'crond'

    s = host.service(service_name)

    assert s.is_running
    assert s.is_enabled
