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
| cron_jobs | [] | This variable can be used for example to define cron jobs directly from playbook. You can use it alone or in conjuction with any of the variabes below. |
| cron_common_jobs | [] | This variable can be used to define cron jobs to be configured commonly. Tipically you would dfine this variable in the `all` metagroup. |
| cron_group_jobs | [] | This variable can be used to define cron jobs to be configured in a specific inventory group like, for example, `webservers` or `databases`.The group names obviously depend on your inventory. |
| cron_host_jobs | [] | This variable is used to define cron jobs to be configured in a specific host. |

> The values of the variables in `cron_common_jobs`, `cron_group_jobs`, `cron_host_jobs` will be merged if the variables are accessible 
for the host you are targeting. See `Example playbook` below.

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

The values defined in `cron_vars` will be added to both.

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
