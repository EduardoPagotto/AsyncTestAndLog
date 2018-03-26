# Test of Async whit thread and config log whit YAML
Just a Sample how to deal async and log setup with a YAML file in python

 - create a log directory

For rsyslog setup files:
- Setting in /etc/rsyslog.conf
    ...
    # provides UDP syslog reception
    module(load="imudp")
    input(type="imudp" port="514")
    ...

- Setting in /etc/rsyslog.d/40-local.conf
    ...
    local5.* /var/log/local5.log
    ...
