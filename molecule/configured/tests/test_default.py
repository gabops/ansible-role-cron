import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cron_jobs(host):
    c = host.run('crontab -l')

    assert('SHELL=/usr/bin/sh') in c.stdout
    assert '*/3 * * * * touch /tmp/a_job' in c.stdout

    c = host.run('crontab -l -u john.doe')
    assert 'SHELL=/usr/bin/zsh' in c.stdout
    assert '@monthly touch /tmp/and_another_job' in c.stdout

    c = host.run('crontab -l -u application')
    assert '#40 * * * 3 touch /tmp/another_job' in c.stdout


def test_cron_service(host):
    os = host.system_info.distribution
    if os in ("ubuntu", "debian"):
        service_name = 'cron'
    else:
        service_name = 'crond'

    s = host.service(service_name)

    assert s.is_running
    assert s.is_enabled
