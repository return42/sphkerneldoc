.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/sched.c

.. _`__rpc_do_wake_up_task_on_wq`:

__rpc_do_wake_up_task_on_wq
===========================

.. c:function:: void __rpc_do_wake_up_task_on_wq(struct workqueue_struct *wq, struct rpc_wait_queue *queue, struct rpc_task *task)

    wake up a single rpc_task

    :param wq:
        workqueue on which to run task
    :type wq: struct workqueue_struct \*

    :param queue:
        wait queue
    :type queue: struct rpc_wait_queue \*

    :param task:
        task to be woken up
    :type task: struct rpc_task \*

.. _`__rpc_do_wake_up_task_on_wq.description`:

Description
-----------

Caller must hold queue->lock, and have cleared the task queued flag.

.. _`rpc_wake_up_queued_task_set_status`:

rpc_wake_up_queued_task_set_status
==================================

.. c:function:: void rpc_wake_up_queued_task_set_status(struct rpc_wait_queue *queue, struct rpc_task *task, int status)

    wake up a task and set task->tk_status

    :param queue:
        pointer to rpc_wait_queue
    :type queue: struct rpc_wait_queue \*

    :param task:
        pointer to rpc_task
    :type task: struct rpc_task \*

    :param status:
        integer error value
    :type status: int

.. _`rpc_wake_up_queued_task_set_status.description`:

Description
-----------

If \ ``task``\  is queued on \ ``queue``\ , then it is woken up, and \ ``task->tk_status``\  is
set to the value of \ ``status``\ .

.. _`rpc_wake_up`:

rpc_wake_up
===========

.. c:function:: void rpc_wake_up(struct rpc_wait_queue *queue)

    wake up all rpc_tasks

    :param queue:
        rpc_wait_queue on which the tasks are sleeping
    :type queue: struct rpc_wait_queue \*

.. _`rpc_wake_up.description`:

Description
-----------

Grabs queue->lock

.. _`rpc_wake_up_status`:

rpc_wake_up_status
==================

.. c:function:: void rpc_wake_up_status(struct rpc_wait_queue *queue, int status)

    wake up all rpc_tasks and set their status value.

    :param queue:
        rpc_wait_queue on which the tasks are sleeping
    :type queue: struct rpc_wait_queue \*

    :param status:
        status value to set
    :type status: int

.. _`rpc_wake_up_status.description`:

Description
-----------

Grabs queue->lock

.. _`rpc_malloc`:

rpc_malloc
==========

.. c:function:: int rpc_malloc(struct rpc_task *task)

    allocate RPC buffer resources

    :param task:
        RPC task
    :type task: struct rpc_task \*

.. _`rpc_malloc.description`:

Description
-----------

A single memory region is allocated, which is split between the
RPC call and RPC reply that this task is being used for. When
this RPC is retired, the memory is released by calling rpc_free.

To prevent rpciod from hanging, this allocator never sleeps,
returning -ENOMEM and suppressing warning if the request cannot
be serviced immediately. The caller can arrange to sleep in a
way that is safe for rpciod.

Most requests are 'small' (under 2KiB) and can be serviced from a
mempool, ensuring that NFS reads and writes can always proceed,
and that there is good locality of reference for these buffers.

In order to avoid memory starvation triggering more writebacks of
NFS requests, we avoid using GFP_KERNEL.

.. _`rpc_free`:

rpc_free
========

.. c:function:: void rpc_free(struct rpc_task *task)

    free RPC buffer resources allocated via rpc_malloc

    :param task:
        RPC task
    :type task: struct rpc_task \*

.. This file was automatic generated / don't edit.

