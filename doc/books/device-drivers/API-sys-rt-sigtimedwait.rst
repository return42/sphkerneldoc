.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-rt-sigtimedwait:

===================
sys_rt_sigtimedwait
===================

*man sys_rt_sigtimedwait(9)*

*4.6.0-rc5*

synchronously wait for queued signals specified in ``uthese``


Synopsis
========

.. c:function:: long sys_rt_sigtimedwait( const sigset_t __user * uthese, siginfo_t __user * uinfo, const struct timespec __user * uts, size_t sigsetsize )

Arguments
=========

``uthese``
    queued signals to wait for

``uinfo``
    if non-null, the signal's siginfo is returned here

``uts``
    upper bound on process time suspension

``sigsetsize``
    size of sigset_t type


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
