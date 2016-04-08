
.. _API-xprt-lookup-rqst:

================
xprt_lookup_rqst
================

*man xprt_lookup_rqst(9)*

*4.6.0-rc1*

find an RPC request corresponding to an XID


Synopsis
========

.. c:function:: struct rpc_rqst ⋆ xprt_lookup_rqst( struct rpc_xprt * xprt, __be32 xid )

Arguments
=========

``xprt``
    transport on which the original request was transmitted

``xid``
    RPC XID of incoming reply
