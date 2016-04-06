
.. _API-sys-rt-sigsuspend:

=================
sys_rt_sigsuspend
=================

*man sys_rt_sigsuspend(9)*

*4.6.0-rc1*

replace the signal mask for a value with the ``unewset`` value until a signal is received


Synopsis
========

.. c:function:: long sys_rt_sigsuspend( sigset_t __user * unewset, size_t sigsetsize )

Arguments
=========

``unewset``
    new signal mask value

``sigsetsize``
    size of sigset_t type
