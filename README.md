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
| cron_packages | [] | Defines the list of packages to be installed in order to install Cron. Note **that this role handles the packages to install already** ([RedHat](vars/RedHat.yml), [Debian](vars/Debian.yml)) however, this variable exists for allowing you to declare your own list of packages if required. |
| cron_enable_repo | ""  | Defines the repo to be enabled when installing the packages defined in `cron_packages` variable. Note that this option only works in RedHat family distributions. |
| cron_service_enabled | true | Defines wheter or not cron service is enabled when applying this role. |
| cron_service_state | started | Defines the state of the cron service. |
| cron_crontab_backup | false | Controls if the role takes a backup of the crontab before applying any changes. Note that this variable is used to set this behaviour globally however, you can specify this behaviour individually on a specific cron var/job by setting the parameter `backup` true or false on the definition. See `Example Playbook` below. |
| cron_vars | [] | Defines the environment variables to be added to the crontab. The parameters for each *var* definition can be found on [cronvar module documentation](https://docs.ansible.com/ansible/latest/modules/cronvar_module.html). |
| cron_jobs | [] | Defines the cron jobs to be configured on the system. The parameters for each *job* definition can be found on [cron module documentation](https://docs.ansible.com/ansible/latest/modules/cron_module.html). |

### Notes:
- Crontab backups are stored on `/tmp/`.

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
        backup: true
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
