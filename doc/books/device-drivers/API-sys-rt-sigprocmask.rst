
.. _API-sys-rt-sigprocmask:

==================
sys_rt_sigprocmask
==================

*man sys_rt_sigprocmask(9)*

*4.6.0-rc1*

change the list of currently blocked signals


Synopsis
========

.. c:function:: long sys_rt_sigprocmask( int how, sigset_t __user * nset, sigset_t __user * oset, size_t sigsetsize )

Arguments
=========

``how``
    whether to add, remove, or set signals

``nset``
    stores pending signals

``oset``
    previous value of signal mask if non-null

``sigsetsize``
    size of sigset_t type
