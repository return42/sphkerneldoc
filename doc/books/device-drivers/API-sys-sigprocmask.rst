
.. _API-sys-sigprocmask:

===============
sys_sigprocmask
===============

*man sys_sigprocmask(9)*

*4.6.0-rc1*

examine and change blocked signals


Synopsis
========

.. c:function:: long sys_sigprocmask( int how, old_sigset_t __user * nset, old_sigset_t __user * oset )

Arguments
=========

``how``
    whether to add, remove, or set signals

``nset``
    signals to add or remove (if non-null)

``oset``
    previous value of signal mask if non-null


Description
===========

Some platforms have their own version with special arguments; others support only sys_rt_sigprocmask.
