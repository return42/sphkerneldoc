.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-wake-pending-tasks:

=======================
xprt_wake_pending_tasks
=======================

*man xprt_wake_pending_tasks(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
