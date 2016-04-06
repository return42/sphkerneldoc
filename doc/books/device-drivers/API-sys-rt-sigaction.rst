
.. _API-sys-rt-sigaction:

================
sys_rt_sigaction
================

*man sys_rt_sigaction(9)*

*4.6.0-rc1*

alter an action taken by a process


Synopsis
========

.. c:function:: long sys_rt_sigaction( int sig, const struct sigaction __user * act, struct sigaction __user * oact, size_t sigsetsize )

Arguments
=========

``sig``
    signal to be sent

``act``
    new sigaction

``oact``
    used to save the previous sigaction

``sigsetsize``
    size of sigset_t type
