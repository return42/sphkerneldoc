.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-rt-sigprocmask:

==================
sys_rt_sigprocmask
==================

*man sys_rt_sigprocmask(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
