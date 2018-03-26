# Test of Async whit thread and config log whit YAML
Just a Sample how to deal async and log setup with a YAML file in python

 - create a log directory

For rsyslog setup files:
- Setting in /etc/rsyslog.conf<p>
    ...<p>
    module(load="imudp") <p>
    input(type="imudp" port="514")<p>
    ...<p>
<p>
- Setting in /etc/rsyslog.d/40-local.conf
    ...<p>
    local5.* /var/log/local5.log<p>
    ...<p>
