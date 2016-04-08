
.. _API-rpc-clone-client:

================
rpc_clone_client
================

*man rpc_clone_client(9)*

*4.6.0-rc1*

Clone an RPC client structure


Synopsis
========

.. c:function:: struct rpc_clnt ⋆ rpc_clone_client( struct rpc_clnt * clnt )

Arguments
=========

``clnt``
    RPC client whose parameters are copied


Description
===========

Returns a fresh RPC client or an ERR_PTR.
