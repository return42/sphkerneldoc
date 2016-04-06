
.. _API-sys-rt-sigqueueinfo:

===================
sys_rt_sigqueueinfo
===================

*man sys_rt_sigqueueinfo(9)*

*4.6.0-rc1*

send signal information to a signal


Synopsis
========

.. c:function:: long sys_rt_sigqueueinfo( pid_t pid, int sig, siginfo_t __user * uinfo )

Arguments
=========

``pid``
    the PID of the thread

``sig``
    signal to be sent

``uinfo``
    signal info to be sent
