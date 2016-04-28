.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-wake-up-status:

==================
rpc_wake_up_status
==================

*man rpc_wake_up_status(9)*

*4.6.0-rc5*

wake up all rpc_tasks and set their status value.


Synopsis
========

.. c:function:: void rpc_wake_up_status( struct rpc_wait_queue * queue, int status )

Arguments
=========

``queue``
    rpc_wait_queue on which the tasks are sleeping

``status``
    status value to set


Description
===========

Grabs queue->lock


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
