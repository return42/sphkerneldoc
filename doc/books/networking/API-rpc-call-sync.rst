.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-call-sync:

=============
rpc_call_sync
=============

*man rpc_call_sync(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
