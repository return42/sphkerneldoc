
.. _API-xprt-reserve-xprt:

=================
xprt_reserve_xprt
=================

*man xprt_reserve_xprt(9)*

*4.6.0-rc1*

serialize write access to transports


Synopsis
========

.. c:function:: int xprt_reserve_xprt( struct rpc_xprt * xprt, struct rpc_task * task )

Arguments
=========

``xprt``
    pointer to the target transport

``task``
    task that is requesting access to the transport


Description
===========

This prevents mixing the payload of separate requests, and prevents transport connects from colliding with writes. No congestion control is provided.
