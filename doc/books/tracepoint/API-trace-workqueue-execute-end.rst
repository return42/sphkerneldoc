.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-workqueue-execute-end:

===========================
trace_workqueue_execute_end
===========================

*man trace_workqueue_execute_end(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
