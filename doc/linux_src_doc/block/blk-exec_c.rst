.. -*- coding: utf-8; mode: rst -*-

==========
blk-exec.c
==========

.. _`blk_end_sync_rq`:

blk_end_sync_rq
===============

.. c:function:: void blk_end_sync_rq (struct request *rq, int error)

    executes a completion event on a request

    :param struct request \*rq:
        request to complete

    :param int error:
        end I/O status of the request


.. _`blk_execute_rq_nowait`:

blk_execute_rq_nowait
=====================

.. c:function:: void blk_execute_rq_nowait (struct request_queue *q, struct gendisk *bd_disk, struct request *rq, int at_head, rq_end_io_fn *done)

    insert a request into queue for execution

    :param struct request_queue \*q:
        queue to insert the request in

    :param struct gendisk \*bd_disk:
        matching gendisk

    :param struct request \*rq:
        request to insert

    :param int at_head:
        insert request at head or tail of queue

    :param rq_end_io_fn \*done:
        I/O completion handler


.. _`blk_execute_rq_nowait.description`:

Description
-----------

Description::

   Insert a fully prepared request at the back of the I/O scheduler queue
   for execution.  Don't wait for completion.

Note::

   This function will invoke ``done`` directly if the queue is dead.


.. _`blk_execute_rq`:

blk_execute_rq
==============

.. c:function:: int blk_execute_rq (struct request_queue *q, struct gendisk *bd_disk, struct request *rq, int at_head)

    insert a request into queue for execution

    :param struct request_queue \*q:
        queue to insert the request in

    :param struct gendisk \*bd_disk:
        matching gendisk

    :param struct request \*rq:
        request to insert

    :param int at_head:
        insert request at head or tail of queue


.. _`blk_execute_rq.description`:

Description
-----------

Description::

   Insert a fully prepared request at the back of the I/O scheduler queue
   for execution and wait for completion.

