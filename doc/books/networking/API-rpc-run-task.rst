.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-run-task:

============
rpc_run_task
============

*man rpc_run_task(9)*

*4.6.0-rc5*

Allocate a new RPC task, then run rpc_execute against it


Synopsis
========

.. c:function:: struct rpc_task * rpc_run_task( const struct rpc_task_setup * task_setup_data )

Arguments
=========

``task_setup_data``
    pointer to task initialisation data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
