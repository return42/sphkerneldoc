.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-wake-up:

===========
rpc_wake_up
===========

*man rpc_wake_up(9)*

*4.6.0-rc5*

wake up all rpc_tasks


Synopsis
========

.. c:function:: void rpc_wake_up( struct rpc_wait_queue * queue )

Arguments
=========

``queue``
    rpc_wait_queue on which the tasks are sleeping


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
