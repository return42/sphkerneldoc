
.. _API-rpc-wake-up:

===========
rpc_wake_up
===========

*man rpc_wake_up(9)*

*4.6.0-rc1*

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
