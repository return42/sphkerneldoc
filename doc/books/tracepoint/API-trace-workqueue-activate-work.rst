
.. _API-trace-workqueue-activate-work:

=============================
trace_workqueue_activate_work
=============================

*man trace_workqueue_activate_work(9)*

*4.6.0-rc1*

called when a work gets activated


Synopsis
========

.. c:function:: void trace_workqueue_activate_work( struct work_struct * work )

Arguments
=========

``work``
    pointer to struct work_struct


Description
===========

This event occurs when a queued work is put on the active queue, which happens immediately after queueing unless ``max_active`` limit is reached.
