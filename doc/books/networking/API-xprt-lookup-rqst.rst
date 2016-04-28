.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-lookup-rqst:

================
xprt_lookup_rqst
================

*man xprt_lookup_rqst(9)*

*4.6.0-rc5*

find an RPC request corresponding to an XID


Synopsis
========

.. c:function:: struct rpc_rqst * xprt_lookup_rqst( struct rpc_xprt * xprt, __be32 xid )

Arguments
=========

``xprt``
    transport on which the original request was transmitted

``xid``
    RPC XID of incoming reply


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
