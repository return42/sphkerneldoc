.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/hisilicon/sec/sec_drv.c

.. _`sec_queue_alloc_start_safe`:

sec_queue_alloc_start_safe
==========================

.. c:function:: struct sec_queue *sec_queue_alloc_start_safe( void)

    get a hw queue from appropriate instance

    :param void:
        no arguments
    :type void: 

.. _`sec_queue_alloc_start_safe.description`:

Description
-----------

This function does extremely simplistic load balancing. It does not take into
account NUMA locality of the accelerator, or which cpu has requested the
queue.  Future work may focus on optimizing this in order to improve full
machine throughput.

.. _`sec_queue_stop_release`:

sec_queue_stop_release
======================

.. c:function:: int sec_queue_stop_release(struct sec_queue *queue)

    free up a hw queue for reuse

    :param queue:
        The queue we are done with.
    :type queue: struct sec_queue \*

.. _`sec_queue_stop_release.description`:

Description
-----------

This will stop the current queue, terminanting any transactions
that are inflight an return it to the pool of available hw queuess

.. _`sec_queue_empty`:

sec_queue_empty
===============

.. c:function:: bool sec_queue_empty(struct sec_queue *queue)

    Is this hardware queue currently empty.

    :param queue:
        *undescribed*
    :type queue: struct sec_queue \*

.. _`sec_queue_empty.description`:

Description
-----------

We need to know if we have an empty queue for some of the chaining modes
as if it is not empty we may need to hold the message in a software queue
until the hw queue is drained.

.. _`sec_queue_send`:

sec_queue_send
==============

.. c:function:: int sec_queue_send(struct sec_queue *queue, struct sec_bd_info *msg, void *ctx)

    queue up a single operation in the hw queue

    :param queue:
        The queue in which to put the message
    :type queue: struct sec_queue \*

    :param msg:
        The message
    :type msg: struct sec_bd_info \*

    :param ctx:
        Context to be put in the shadow array and passed back to cb on result.
    :type ctx: void \*

.. _`sec_queue_send.description`:

Description
-----------

This function will return -EAGAIN if the queue is currently full.

.. This file was automatic generated / don't edit.

