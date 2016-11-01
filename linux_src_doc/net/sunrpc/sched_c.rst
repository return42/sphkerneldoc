.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/sched.c

.. _`__rpc_do_wake_up_task_on_wq`:

__rpc_do_wake_up_task_on_wq
===========================

.. c:function:: void __rpc_do_wake_up_task_on_wq(struct workqueue_struct *wq, struct rpc_wait_queue *queue, struct rpc_task *task)

    wake up a single rpc_task

    :param struct workqueue_struct \*wq:
        workqueue on which to run task

    :param struct rpc_wait_queue \*queue:
        wait queue

    :param struct rpc_task \*task:
        task to be woken up

.. _`__rpc_do_wake_up_task_on_wq.description`:

Description
-----------

Caller must hold queue->lock, and have cleared the task queued flag.

.. _`rpc_wake_up`:

rpc_wake_up
===========

.. c:function:: void rpc_wake_up(struct rpc_wait_queue *queue)

    wake up all rpc_tasks

    :param struct rpc_wait_queue \*queue:
        rpc_wait_queue on which the tasks are sleeping

.. _`rpc_wake_up.description`:

Description
-----------

Grabs queue->lock

.. _`rpc_wake_up_status`:

rpc_wake_up_status
==================

.. c:function:: void rpc_wake_up_status(struct rpc_wait_queue *queue, int status)

    wake up all rpc_tasks and set their status value.

    :param struct rpc_wait_queue \*queue:
        rpc_wait_queue on which the tasks are sleeping

    :param int status:
        status value to set

.. _`rpc_wake_up_status.description`:

Description
-----------

Grabs queue->lock

.. _`rpc_malloc`:

rpc_malloc
==========

.. c:function:: int rpc_malloc(struct rpc_task *task)

    allocate RPC buffer resources

    :param struct rpc_task \*task:
        RPC task

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

    :param struct rpc_task \*task:
        RPC task

.. This file was automatic generated / don't edit.

