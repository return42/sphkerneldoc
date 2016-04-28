.. -*- coding: utf-8; mode: rst -*-

.. _API-mptctl-syscall-down:

===================
mptctl_syscall_down
===================

*man mptctl_syscall_down(9)*

*4.6.0-rc5*

Down the MPT adapter syscall semaphore.


Synopsis
========

.. c:function:: int mptctl_syscall_down( MPT_ADAPTER * ioc, int nonblock )

Arguments
=========

``ioc``
    Pointer to MPT adapter

``nonblock``
    boolean, non-zero if O_NONBLOCK is set


Description
===========

All of the ioctl commands can potentially sleep, which is illegal with a
spinlock held, thus we perform mutual exclusion here.

Returns negative errno on error, or zero for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
