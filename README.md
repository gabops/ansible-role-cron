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
| cron_packages | crond | Defines the package list to be applied in order to install cron. |
| cron_enable_repo | ""  | Defines the repo to be enabled when installing the packages defined in `cron_packages` variable. Note that this option only works in RedHat os family distributions. |
| cron_service_enabled | true | Defines wheter or not crond service is enabled when appliying this role. |
| cron_service_started | true | Defines wheter or not crond service is started when appliying this role. |
| cron_contab_backup | true | Defines if the role takes a backup of the crontab before applying any changes. |
| cron_vars | [] |   |
| cron_jobs | [] | A list of cron jobs to be added to the targeted host. | 
| cron_common_jobs | [] | A list of cron jobs to be applied commonly to all hosts. |
| cron_group_jobs | [] | A list of cron jobs to be applied to a specific group of hosts. |
| cron_host_jobs | [] | A list of cron jobs to be applied to a specific host. |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: servers
      vars:
        foo: bar
      roles:
         - role: gabops.cron
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
