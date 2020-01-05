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
| cron_packages | "" | Defines the packages to be applied in order to install cron. By default, the role handles the packages to install (RedHat)[./vars/RedHat.yml] and (Debian)[./vars/Debian.yml] however you can overwrite the packages by using this variable. |
| cron_enable_repo | ""  | Defines the repo to be enabled when installing the packages defined in `cron_packages` variable. Note that this option only works in RedHat os family distributions. |
| cron_service_enabled | true | Defines wheter or not crond service is enabled when appliying this role. |
| cron_service_state | true | Defines the state of the cron service. Use `ignore` if you want the role to do nothing with cron when being applied. |
| cron_contab_backup | true | Defines if the role takes a backup of the crontab before applying any changes. |
| cron_vars | [] | Defines the environment variables to be added to the crontab. | 
| cron_jobs | [] | Defines Cron jobs to be applied. Tipically you will define this variable directly in the playbook. |
| cron_common_jobs | [] | Defines common Cron jobs to be applied. Tipically you will define this variable in the `all` metagroup. |
| cron_group_jobs | [] | Defines Cron jobs to be applied in a inventory group. Tipically you will define this variable in a group(s) vars of your inventory (e.g. group_vars/webservers/). |
| cron_host_jobs | [] | Defines Cron jobs to be applied in a specific host. Tipically you will define this in a host_vars file (e.g. host_vars/host-01/). |

Dependencies
------------

None.

Example Playbook
----------------

- group_vars/all/cron.yml:
```yaml
cron_common_jobs:
  - name: common-job
    user: root
    job: touch /tmp/common_job
    minute: '*/3'
    hour: '*'
    day: '*'
    month: '*'
    weekday: '*' 
```

- group_vars/webservers/cron.yml:
```yaml
cron_group_jobs:
  - name: group-job
    user: root
    job: touch /tmp/group_job
    minute: '*/3'
    hour: '*'
    day: '*'
    month: '*'
    weekday: '*' 
```

- host_vars/webserver-01/cron.yml:
```yaml
cron_host_jobs:
  - name: webserver-host-job
    user: root
    job: touch /tmp/host_job
    minute: '*/3'
    hour: '*'
    day: '*'
    month: '*'
    weekday: '*' 
```

- host_vars/database-01/cron.yml:
```yaml
cron_host_jobs:
  - name: database-host-job
    user: root
    job: touch /tmp/host_job
    minute: '*/3'
    hour: '*'
    day: '*'
    month: '*'
    weekday: '*' 
```

- The playbook:
```yaml
    - hosts: all
      vars:
        cron_vars:
        - name: PATH
          value: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin 
          user: root

        - name: SHELL
          value: /usr/bin/zsh 
          user: jdoe
        cron_jobs:
          - name: from-playbook-job
            user: root
            job: touch /tmp/host_job
            minute: '*/3'
            hour: '*'
            day: '*'
            month: '*'
            weekday: '*'
      roles:
         - role: gabops.cron
```

Following the previous example, the hypothetical host *webserver-01* will be configured with the cron jobs:
1. `common-job`
2. `group-job`
3. `webserver-host-job`
4. `from-playbook-job` 

However *database-01* will be configured with just with
1. `common-job`
2. `database-host-job` 
3. `from-playbook-job`

The values defined in `cron_vars` will be added on both.

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
