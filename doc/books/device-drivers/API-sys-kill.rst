
.. _API-sys-kill:

========
sys_kill
========

*man sys_kill(9)*

*4.6.0-rc1*

send a signal to a process


Synopsis
========

.. c:function:: long sys_kill( pid_t pid, int sig )

Arguments
=========

``pid``
    the PID of the process

``sig``
    signal to be sent
