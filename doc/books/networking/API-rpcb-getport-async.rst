
.. _API-rpcb-getport-async:

==================
rpcb_getport_async
==================

*man rpcb_getport_async(9)*

*4.6.0-rc1*

obtain the port for a given RPC service on a given host


Synopsis
========

.. c:function:: void rpcb_getport_async( struct rpc_task * task )

Arguments
=========

``task``
    task that is waiting for portmapper request


Description
===========

This one can be called for an ongoing RPC request, and can be used in an async (rpciod) context.
