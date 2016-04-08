
.. _API-rpc-peeraddr2str:

================
rpc_peeraddr2str
================

*man rpc_peeraddr2str(9)*

*4.6.0-rc1*

return remote peer address in printable format


Synopsis
========

.. c:function:: const char ⋆ rpc_peeraddr2str( struct rpc_clnt * clnt, enum rpc_display_format_t format )

Arguments
=========

``clnt``
    RPC client structure

``format``
    address format


NB
==

the lifetime of the memory referenced by the returned pointer is the same as the rpc_xprt itself. As long as the caller uses this pointer, it must hold the RCU read lock.
