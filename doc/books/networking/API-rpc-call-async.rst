.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-call-async:

==============
rpc_call_async
==============

*man rpc_call_async(9)*

*4.6.0-rc5*

Perform an asynchronous RPC call


Synopsis
========

.. c:function:: int rpc_call_async( struct rpc_clnt * clnt, const struct rpc_message * msg, int flags, const struct rpc_call_ops * tk_ops, void * data )

Arguments
=========

``clnt``
    pointer to RPC client

``msg``
    RPC call parameters

``flags``
    RPC call flags

``tk_ops``
    RPC call ops

``data``
    user call data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
