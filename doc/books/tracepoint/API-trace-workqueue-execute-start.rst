
.. _API-trace-workqueue-execute-start:

=============================
trace_workqueue_execute_start
=============================

*man trace_workqueue_execute_start(9)*

*4.6.0-rc1*

called immediately before the workqueue callback


Synopsis
========

.. c:function:: void trace_workqueue_execute_start( struct work_struct * work )

Arguments
=========

``work``
    pointer to struct work_struct


Description
===========

Allows to track workqueue execution.
