gabops.cron
===========
[![Build Status](https://travis-ci.org/gabops/ansible-role-cron.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-cron)

Installs and configures Cron.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| cron_packages | "" | Defines the packages to be applied in order to install cron. By default, the role handles the packages to install [RedHat](vars/RedHat.yml) and [Debian](vars/Debian.yml) however you can overwrite the packages by using this variable. |
| cron_enable_repo | ""  | Defines the repo to be enabled when installing the packages defined in `cron_packages` variable. Note that this option only works in RedHat os family distributions. |
| cron_service_enabled | true | Defines wheter or not crond service is enabled when appliying this role. |
| cron_service_state | started | Defines the state of the cron service. |
| cron_contab_backup | false | Defines if the role takes a backup of the crontab before applying any changes. |
| cron_vars | [] | Defines the environment variables to be added to the crontab. The parameters for each *var* definition can be found on [cronvar module documentation](https://docs.ansible.com/ansible/latest/modules/cronvar_module.html). |
| cron_jobs | [] | Defines the cron jobs to be configured on the system. The parameters for each *job* definition can be found on [cron module documentation](https://docs.ansible.com/ansible/latest/modules/cron_module.html). |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    cron_vars:
      - name: PATH
        value: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        user: root

      - name: SHELL
        value: /usr/bin/sh
        user: root

      - name: SHELL
        value: /usr/bin/zsh
        user: john.doe

    cron_jobs:
      - name: a_job
        user: root
        job: touch /tmp/a_job
        minute: '*/3'
        hour: '*'
        day: '*'
        month: '*'
        weekday: '*'

      - name: another_job
        user: application
        job: touch /tmp/another_job
        disabled: true
        minute: 40
        hour: '*'
        day: '*'
        month: '*'
        weekday: 3

      - name: and_another_job
        user: john.doe
        job: touch /tmp/touch_monthly
        special_time: monthly

  roles:
      - role: gabops.cron
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
