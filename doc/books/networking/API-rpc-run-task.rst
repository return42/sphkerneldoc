
.. _API-rpc-run-task:

============
rpc_run_task
============

*man rpc_run_task(9)*

*4.6.0-rc1*

Allocate a new RPC task, then run rpc_execute against it


Synopsis
========

.. c:function:: struct rpc_task ⋆ rpc_run_task( const struct rpc_task_setup * task_setup_data )

Arguments
=========

``task_setup_data``
    pointer to task initialisation data
