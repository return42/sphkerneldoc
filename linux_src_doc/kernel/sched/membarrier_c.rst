.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/membarrier.c

.. _`sys_membarrier`:

sys_membarrier
==============

.. c:function:: long sys_membarrier(int cmd, int flags)

    issue memory barriers on a set of threads

    :param cmd:
        Takes command values defined in enum membarrier_cmd.
    :type cmd: int

    :param flags:
        Currently needs to be 0. For future extensions.
    :type flags: int

.. _`sys_membarrier.description`:

Description
-----------

If this system call is not implemented, -ENOSYS is returned. If the
command specified does not exist, not available on the running
kernel, or if the command argument is invalid, this system call
returns -EINVAL. For a given command, with flags argument set to 0,
this system call is guaranteed to always return the same value until
reboot.

All memory accesses performed in program order from each targeted thread
is guaranteed to be ordered with respect to \ :c:func:`sys_membarrier`\ . If we use
the semantic "barrier()" to represent a compiler barrier forcing memory
accesses to be performed in program order across the barrier, and
\ :c:func:`smp_mb`\  to represent explicit memory barriers forcing full memory
ordering across the barrier, we have the following ordering table for
each pair of \ :c:func:`barrier`\ , \ :c:func:`sys_membarrier`\  and \ :c:func:`smp_mb`\ :

The pair ordering is detailed as (O: ordered, X: not ordered):

\ :c:func:`barrier`\    \ :c:func:`smp_mb`\  \ :c:func:`sys_membarrier`\ 
\ :c:func:`barrier`\           X           X            O
\ :c:func:`smp_mb`\            X           O            O
\ :c:func:`sys_membarrier`\    O           O            O

.. This file was automatic generated / don't edit.

