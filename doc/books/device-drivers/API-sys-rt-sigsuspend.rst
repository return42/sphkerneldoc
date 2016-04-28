.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-rt-sigsuspend:

=================
sys_rt_sigsuspend
=================

*man sys_rt_sigsuspend(9)*

*4.6.0-rc5*

replace the signal mask for a value with the ``unewset`` value until a
signal is received


Synopsis
========

.. c:function:: long sys_rt_sigsuspend( sigset_t __user * unewset, size_t sigsetsize )

Arguments
=========

``unewset``
    new signal mask value

``sigsetsize``
    size of sigset_t type


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
