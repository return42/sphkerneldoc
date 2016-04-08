
.. _API-rpc-wake-up-status:

==================
rpc_wake_up_status
==================

*man rpc_wake_up_status(9)*

*4.6.0-rc1*

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
