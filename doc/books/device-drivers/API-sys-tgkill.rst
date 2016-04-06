
.. _API-sys-tgkill:

==========
sys_tgkill
==========

*man sys_tgkill(9)*

*4.6.0-rc1*

send signal to one specific thread


Synopsis
========

.. c:function:: long sys_tgkill( pid_t tgid, pid_t pid, int sig )

Arguments
=========

``tgid``
    the thread group ID of the thread

``pid``
    the PID of the thread

``sig``
    signal to be sent


Description
===========

This syscall also checks the ``tgid`` and returns -ESRCH even if the PID exists but it's not belonging to the target process anymore. This method solves the problem of threads
exiting and PIDs getting reused.
