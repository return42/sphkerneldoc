
.. _API-xprt-wake-pending-tasks:

=======================
xprt_wake_pending_tasks
=======================

*man xprt_wake_pending_tasks(9)*

*4.6.0-rc1*

wake all tasks on a transport's pending queue


Synopsis
========

.. c:function:: void xprt_wake_pending_tasks( struct rpc_xprt * xprt, int status )

Arguments
=========

``xprt``
    transport with waiting tasks

``status``
    result code to plant in each task before waking it
