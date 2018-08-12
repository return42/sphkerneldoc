.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/wait_bit.c

.. _`wake_up_bit`:

wake_up_bit
===========

.. c:function:: void wake_up_bit(void *word, int bit)

    wake up a waiter on a bit

    :param void \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

.. _`wake_up_bit.description`:

Description
-----------

There is a standard hashed waitqueue table for generic use. This
is the part of the hashtable's accessor API that wakes up waiters
on a bit. For instance, if one were to have waiters on a bitflag,
one would call \ :c:func:`wake_up_bit`\  after clearing the bit.

In order for this to function properly, as it uses \ :c:func:`waitqueue_active`\ 
internally, some kind of memory barrier must be done prior to calling
this. Typically, this will be \ :c:func:`smp_mb__after_atomic`\ , but in some
cases where bitflags are manipulated non-atomically under a lock, one
may need to use a less regular barrier, such fs/inode.c's \ :c:func:`smp_mb`\ ,
because \ :c:func:`spin_unlock`\  does not guarantee a memory barrier.

.. This file was automatic generated / don't edit.

