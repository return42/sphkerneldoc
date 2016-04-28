.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-clnt-iterate-for-each-xprt:

==============================
rpc_clnt_iterate_for_each_xprt
==============================

*man rpc_clnt_iterate_for_each_xprt(9)*

*4.6.0-rc5*

Apply a function to all transports


Synopsis
========

.. c:function:: int rpc_clnt_iterate_for_each_xprt( struct rpc_clnt * clnt, int (*fn) struct rpc_clnt *, struct rpc_xprt *, void *, void * data )

Arguments
=========

``clnt``
    pointer to client

``fn``
    function to apply

``data``
    void pointer to function data


Description
===========

Iterates through the list of RPC transports currently attached to the
client and applies the function fn(clnt, xprt, data).

On error, the iteration stops, and the function returns the error value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
