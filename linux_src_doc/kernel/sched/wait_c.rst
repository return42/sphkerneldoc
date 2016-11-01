.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/wait.c

.. _`__wake_up`:

__wake_up
=========

.. c:function:: void __wake_up(wait_queue_head_t *q, unsigned int mode, int nr_exclusive, void *key)

    wake up threads blocked on a waitqueue.

    :param wait_queue_head_t \*q:
        the waitqueue

    :param unsigned int mode:
        which threads

    :param int nr_exclusive:
        how many wake-one or wake-many threads to wake up

    :param void \*key:
        is directly passed to the wakeup function

.. _`__wake_up.description`:

Description
-----------

It may be assumed that this function implies a write memory barrier before
changing the task state if and only if any tasks are woken up.

.. _`__wake_up_sync_key`:

__wake_up_sync_key
==================

.. c:function:: void __wake_up_sync_key(wait_queue_head_t *q, unsigned int mode, int nr_exclusive, void *key)

    wake up threads blocked on a waitqueue.

    :param wait_queue_head_t \*q:
        the waitqueue

    :param unsigned int mode:
        which threads

    :param int nr_exclusive:
        how many wake-one or wake-many threads to wake up

    :param void \*key:
        opaque value to be passed to wakeup targets

.. _`__wake_up_sync_key.description`:

Description
-----------

The sync wakeup differs that the waker knows that it will schedule
away soon, so while the target thread will be woken up, it will not
be migrated to another CPU - ie. the two threads are 'synchronized'
with each other. This can prevent needless bouncing between CPUs.

On UP it can prevent extra preemption.

It may be assumed that this function implies a write memory barrier before
changing the task state if and only if any tasks are woken up.

.. _`finish_wait`:

finish_wait
===========

.. c:function:: void finish_wait(wait_queue_head_t *q, wait_queue_t *wait)

    clean up after waiting in a queue

    :param wait_queue_head_t \*q:
        waitqueue waited on

    :param wait_queue_t \*wait:
        wait descriptor

.. _`finish_wait.description`:

Description
-----------

Sets current thread back to running state and removes
the wait descriptor from the given waitqueue if still
queued.

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

.. _`wake_up_atomic_t`:

wake_up_atomic_t
================

.. c:function:: void wake_up_atomic_t(atomic_t *p)

    Wake up a waiter on a atomic_t

    :param atomic_t \*p:
        The atomic_t being waited on, a kernel virtual address

.. _`wake_up_atomic_t.description`:

Description
-----------

Wake up anyone waiting for the atomic_t to go to zero.

Abuse the bit-waker function and its waitqueue hash table set (the atomic_t
check is done by the waiter's wake function, not the by the waker itself).

.. This file was automatic generated / don't edit.

