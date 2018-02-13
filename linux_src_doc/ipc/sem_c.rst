.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/sem.c

.. _`unmerge_queues`:

unmerge_queues
==============

.. c:function:: void unmerge_queues(struct sem_array *sma)

    unmerge queues, if possible.

    :param struct sem_array \*sma:
        semaphore array

.. _`unmerge_queues.description`:

Description
-----------

The function unmerges the wait queues if complex_count is 0.
It must be called prior to dropping the global semaphore array lock.

.. _`merge_queues`:

merge_queues
============

.. c:function:: void merge_queues(struct sem_array *sma)

    merge single semop queues into global queue

    :param struct sem_array \*sma:
        semaphore array

.. _`merge_queues.description`:

Description
-----------

This function merges all per-semaphore queues into the global queue.
It is necessary to achieve FIFO ordering for the pending single-sop
operations when a multi-semop operation must sleep.
Only the alter operations must be moved, the const operations can stay.

.. _`newary`:

newary
======

.. c:function:: int newary(struct ipc_namespace *ns, struct ipc_params *params)

    Create a new semaphore set

    :param struct ipc_namespace \*ns:
        namespace

    :param struct ipc_params \*params:
        ptr to the structure that contains key, semflg and nsems

.. _`newary.description`:

Description
-----------

Called with sem_ids.rwsem held (as a writer)

.. _`perform_atomic_semop_slow`:

perform_atomic_semop_slow
=========================

.. c:function:: int perform_atomic_semop_slow(struct sem_array *sma, struct sem_queue *q)

    Attempt to perform semaphore operations on a given array.

    :param struct sem_array \*sma:
        semaphore array

    :param struct sem_queue \*q:
        struct sem_queue that describes the operation

.. _`perform_atomic_semop_slow.description`:

Description
-----------

Caller blocking are as follows, based the value
indicated by the semaphore operation (sem_op):

(1) >0 never blocks.
(2)  0 (wait-for-zero operation): semval is non-zero.
(3) <0 attempting to decrement semval to a value smaller than zero.

Returns 0 if the operation was possible.
Returns 1 if the operation is impossible, the caller must sleep.
Returns <0 for error codes.

.. _`wake_const_ops`:

wake_const_ops
==============

.. c:function:: int wake_const_ops(struct sem_array *sma, int semnum, struct wake_q_head *wake_q)

    wake up non-alter tasks

    :param struct sem_array \*sma:
        semaphore array.

    :param int semnum:
        semaphore that was modified.

    :param struct wake_q_head \*wake_q:
        lockless wake-queue head.

.. _`wake_const_ops.description`:

Description
-----------

wake_const_ops must be called after a semaphore in a semaphore array
was set to 0. If complex const operations are pending, wake_const_ops must
be called with semnum = -1, as well as with the number of each modified
semaphore.
The tasks that must be woken up are added to \ ``wake_q``\ . The return code
is stored in q->pid.
The function returns 1 if at least one operation was completed successfully.

.. _`do_smart_wakeup_zero`:

do_smart_wakeup_zero
====================

.. c:function:: int do_smart_wakeup_zero(struct sem_array *sma, struct sembuf *sops, int nsops, struct wake_q_head *wake_q)

    wakeup all wait for zero tasks

    :param struct sem_array \*sma:
        semaphore array

    :param struct sembuf \*sops:
        operations that were performed

    :param int nsops:
        number of operations

    :param struct wake_q_head \*wake_q:
        lockless wake-queue head

.. _`do_smart_wakeup_zero.description`:

Description
-----------

Checks all required queue for wait-for-zero operations, based
on the actual changes that were performed on the semaphore array.
The function returns 1 if at least one operation was completed successfully.

.. _`update_queue`:

update_queue
============

.. c:function:: int update_queue(struct sem_array *sma, int semnum, struct wake_q_head *wake_q)

    look for tasks that can be completed.

    :param struct sem_array \*sma:
        semaphore array.

    :param int semnum:
        semaphore that was modified.

    :param struct wake_q_head \*wake_q:
        lockless wake-queue head.

.. _`update_queue.description`:

Description
-----------

update_queue must be called after a semaphore in a semaphore array
was modified. If multiple semaphores were modified, update_queue must
be called with semnum = -1, as well as with the number of each modified
semaphore.
The tasks that must be woken up are added to \ ``wake_q``\ . The return code
is stored in q->pid.
The function internally checks if const operations can now succeed.

The function return 1 if at least one semop was completed successfully.

.. _`set_semotime`:

set_semotime
============

.. c:function:: void set_semotime(struct sem_array *sma, struct sembuf *sops)

    set sem_otime

    :param struct sem_array \*sma:
        semaphore array

    :param struct sembuf \*sops:
        operations that modified the array, may be NULL

.. _`set_semotime.description`:

Description
-----------

sem_otime is replicated to avoid cache line trashing.
This function sets one instance to the current time.

.. _`do_smart_update`:

do_smart_update
===============

.. c:function:: void do_smart_update(struct sem_array *sma, struct sembuf *sops, int nsops, int otime, struct wake_q_head *wake_q)

    optimized update_queue

    :param struct sem_array \*sma:
        semaphore array

    :param struct sembuf \*sops:
        operations that were performed

    :param int nsops:
        number of operations

    :param int otime:
        force setting otime

    :param struct wake_q_head \*wake_q:
        lockless wake-queue head

.. _`do_smart_update.description`:

Description
-----------

\ :c:func:`do_smart_update`\  does the required calls to update_queue and wakeup_zero,
based on the actual changes that were performed on the semaphore array.
Note that the function does not do the actual wake-up: the caller is
responsible for calling \ :c:func:`wake_up_q`\ .
It is safe to perform this call after dropping all locks.

.. _`find_alloc_undo`:

find_alloc_undo
===============

.. c:function:: struct sem_undo *find_alloc_undo(struct ipc_namespace *ns, int semid)

    lookup (and if not present create) undo array

    :param struct ipc_namespace \*ns:
        namespace

    :param int semid:
        semaphore array id

.. _`find_alloc_undo.description`:

Description
-----------

The function looks up (and if not present creates) the undo structure.
The size of the undo structure depends on the size of the semaphore
array, thus the alloc path is not that straightforward.
Lifetime-rules: sem_undo is rcu-protected, on success, the function
performs a \ :c:func:`rcu_read_lock`\ .

.. This file was automatic generated / don't edit.

