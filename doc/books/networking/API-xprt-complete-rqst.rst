
.. _API-xprt-complete-rqst:

==================
xprt_complete_rqst
==================

*man xprt_complete_rqst(9)*

*4.6.0-rc1*

called when reply processing is complete


Synopsis
========

.. c:function:: void xprt_complete_rqst( struct rpc_task * task, int copied )

Arguments
=========

``task``
    RPC request that recently completed

``copied``
    actual number of bytes received from the transport


Description
===========

Caller holds transport lock.
