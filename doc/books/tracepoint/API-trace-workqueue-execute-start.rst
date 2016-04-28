.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-workqueue-execute-start:

=============================
trace_workqueue_execute_start
=============================

*man trace_workqueue_execute_start(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
