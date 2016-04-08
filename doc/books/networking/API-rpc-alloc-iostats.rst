
.. _API-rpc-alloc-iostats:

=================
rpc_alloc_iostats
=================

*man rpc_alloc_iostats(9)*

*4.6.0-rc1*

allocate an rpc_iostats structure


Synopsis
========

.. c:function:: struct rpc_iostats ⋆ rpc_alloc_iostats( struct rpc_clnt * clnt )

Arguments
=========

``clnt``
    RPC program, version, and xprt
