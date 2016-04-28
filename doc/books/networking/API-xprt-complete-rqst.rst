.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-complete-rqst:

==================
xprt_complete_rqst
==================

*man xprt_complete_rqst(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
