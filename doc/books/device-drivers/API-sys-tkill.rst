
.. _API-sys-tkill:

=========
sys_tkill
=========

*man sys_tkill(9)*

*4.6.0-rc1*

send signal to one specific task


Synopsis
========

.. c:function:: long sys_tkill( pid_t pid, int sig )

Arguments
=========

``pid``
    the PID of the task

``sig``
    signal to be sent


Description
===========

Send a signal to only one task, even if it's a CLONE_THREAD task.
