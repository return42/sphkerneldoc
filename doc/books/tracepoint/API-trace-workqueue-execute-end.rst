
.. _API-trace-workqueue-execute-end:

===========================
trace_workqueue_execute_end
===========================

*man trace_workqueue_execute_end(9)*

*4.6.0-rc1*

called immediately after the workqueue callback


Synopsis
========

.. c:function:: void trace_workqueue_execute_end( struct work_struct * work )

Arguments
=========

``work``
    pointer to struct work_struct


Description
===========

Allows to track workqueue execution.
