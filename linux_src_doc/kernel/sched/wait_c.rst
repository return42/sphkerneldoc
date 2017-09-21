.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/wait.c

.. _`__wake_up`:

__wake_up
=========

.. c:function:: void __wake_up(struct wait_queue_head *wq_head, unsigned int mode, int nr_exclusive, void *key)

    wake up threads blocked on a waitqueue.

    :param struct wait_queue_head \*wq_head:
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

.. c:function:: void __wake_up_sync_key(struct wait_queue_head *wq_head, unsigned int mode, int nr_exclusive, void *key)

    wake up threads blocked on a waitqueue.

    :param struct wait_queue_head \*wq_head:
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

.. c:function:: void finish_wait(struct wait_queue_head *wq_head, struct wait_queue_entry *wq_entry)

    clean up after waiting in a queue

    :param struct wait_queue_head \*wq_head:
        waitqueue waited on

    :param struct wait_queue_entry \*wq_entry:
        wait descriptor

.. _`finish_wait.description`:

Description
-----------

Sets current thread back to running state and removes
the wait descriptor from the given waitqueue if still
queued.

.. This file was automatic generated / don't edit.

