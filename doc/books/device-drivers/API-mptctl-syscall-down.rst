
.. _API-mptctl-syscall-down:

===================
mptctl_syscall_down
===================

*man mptctl_syscall_down(9)*

*4.6.0-rc1*

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

All of the ioctl commands can potentially sleep, which is illegal with a spinlock held, thus we perform mutual exclusion here.

Returns negative errno on error, or zero for success.
