
.. _API-rpc-call-sync:

=============
rpc_call_sync
=============

*man rpc_call_sync(9)*

*4.6.0-rc1*

Perform a synchronous RPC call


Synopsis
========

.. c:function:: int rpc_call_sync( struct rpc_clnt * clnt, const struct rpc_message * msg, int flags )

Arguments
=========

``clnt``
    pointer to RPC client

``msg``
    RPC call parameters

``flags``
    RPC call flags
