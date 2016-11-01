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

.. _`perform_atomic_semop`:

perform_atomic_semop
====================

.. c:function:: int perform_atomic_semop(struct sem_array *sma, struct sem_queue *q)

    Perform (if possible) a semaphore operation

    :param struct sem_array \*sma:
        semaphore array

    :param struct sem_queue \*q:
        struct sem_queue that describes the operation

.. _`perform_atomic_semop.description`:

Description
-----------

Returns 0 if the operation was possible.
Returns 1 if the operation is impossible, the caller must sleep.
Negative values are error codes.

.. _`wake_up_sem_queue_do`:

wake_up_sem_queue_do
====================

.. c:function:: void wake_up_sem_queue_do(struct list_head *pt)

    do the actual wake-up

    :param struct list_head \*pt:
        list of tasks to be woken up

.. _`wake_up_sem_queue_do.description`:

Description
-----------

Do the actual wake-up.
The function is called without any locks held, thus the semaphore array
could be destroyed already and the tasks can disappear as soon as the
status is set to the actual return code.

.. _`wake_const_ops`:

wake_const_ops
==============

.. c:function:: int wake_const_ops(struct sem_array *sma, int semnum, struct list_head *pt)

    wake up non-alter tasks

    :param struct sem_array \*sma:
        semaphore array.

    :param int semnum:
        semaphore that was modified.

    :param struct list_head \*pt:
        list head for the tasks that must be woken up.

.. _`wake_const_ops.description`:

Description
-----------

wake_const_ops must be called after a semaphore in a semaphore array
was set to 0. If complex const operations are pending, wake_const_ops must
be called with semnum = -1, as well as with the number of each modified
semaphore.
The tasks that must be woken up are added to \ ``pt``\ . The return code
is stored in q->pid.
The function returns 1 if at least one operation was completed successfully.

.. _`do_smart_wakeup_zero`:

do_smart_wakeup_zero
====================

.. c:function:: int do_smart_wakeup_zero(struct sem_array *sma, struct sembuf *sops, int nsops, struct list_head *pt)

    wakeup all wait for zero tasks

    :param struct sem_array \*sma:
        semaphore array

    :param struct sembuf \*sops:
        operations that were performed

    :param int nsops:
        number of operations

    :param struct list_head \*pt:
        list head of the tasks that must be woken up.

.. _`do_smart_wakeup_zero.description`:

Description
-----------

Checks all required queue for wait-for-zero operations, based
on the actual changes that were performed on the semaphore array.
The function returns 1 if at least one operation was completed successfully.

.. _`update_queue`:

update_queue
============

.. c:function:: int update_queue(struct sem_array *sma, int semnum, struct list_head *pt)

    look for tasks that can be completed.

    :param struct sem_array \*sma:
        semaphore array.

    :param int semnum:
        semaphore that was modified.

    :param struct list_head \*pt:
        list head for the tasks that must be woken up.

.. _`update_queue.description`:

Description
-----------

update_queue must be called after a semaphore in a semaphore array
was modified. If multiple semaphores were modified, update_queue must
be called with semnum = -1, as well as with the number of each modified
semaphore.
The tasks that must be woken up are added to \ ``pt``\ . The return code
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

.. c:function:: void do_smart_update(struct sem_array *sma, struct sembuf *sops, int nsops, int otime, struct list_head *pt)

    optimized update_queue

    :param struct sem_array \*sma:
        semaphore array

    :param struct sembuf \*sops:
        operations that were performed

    :param int nsops:
        number of operations

    :param int otime:
        force setting otime

    :param struct list_head \*pt:
        list head of the tasks that must be woken up.

.. _`do_smart_update.description`:

Description
-----------

do_smart_update() does the required calls to update_queue and wakeup_zero,
based on the actual changes that were performed on the semaphore array.
Note that the function does not do the actual wake-up: the caller is
responsible for calling wake_up_sem_queue_do(@pt).
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

.. _`get_queue_result`:

get_queue_result
================

.. c:function:: int get_queue_result(struct sem_queue *q)

    retrieve the result code from sem_queue

    :param struct sem_queue \*q:
        Pointer to queue structure

.. _`get_queue_result.description`:

Description
-----------

Retrieve the return code from the pending queue. If IN_WAKEUP is found in
q->status, then we must loop until the value is replaced with the final

.. _`get_queue_result.value`:

value
-----

This may happen if a task is woken up by an unrelated event (e.g.
signal) and in parallel the task is woken up by another task because it got
the requested semaphores.

The function can be called with or without holding the semaphore spinlock.

.. This file was automatic generated / don't edit.

