.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/message/fusion/mptctl.c

.. _`mptctl_syscall_down`:

mptctl_syscall_down
===================

.. c:function:: int mptctl_syscall_down(MPT_ADAPTER *ioc, int nonblock)

    Down the MPT adapter syscall semaphore.

    :param ioc:
        Pointer to MPT adapter
    :type ioc: MPT_ADAPTER \*

    :param nonblock:
        boolean, non-zero if O_NONBLOCK is set
    :type nonblock: int

.. _`mptctl_syscall_down.description`:

Description
-----------

All of the ioctl commands can potentially sleep, which is illegal
with a spinlock held, thus we perform mutual exclusion here.

Returns negative errno on error, or zero for success.

.. This file was automatic generated / don't edit.

