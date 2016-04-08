
.. _API-trace-workqueue-queue-work:

==========================
trace_workqueue_queue_work
==========================

*man trace_workqueue_queue_work(9)*

*4.6.0-rc1*

called when a work gets queued


Synopsis
========

.. c:function:: void trace_workqueue_queue_work( unsigned int req_cpu, struct pool_workqueue * pwq, struct work_struct * work )

Arguments
=========

``req_cpu``
    the requested cpu

``pwq``
    pointer to struct pool_workqueue

``work``
    pointer to struct work_struct


Description
===========

This event occurs when a work is queued immediately or once a delayed work is actually queued on a workqueue (ie: once the delay has been reached).
