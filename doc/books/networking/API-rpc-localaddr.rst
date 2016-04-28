.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-localaddr:

=============
rpc_localaddr
=============

*man rpc_localaddr(9)*

*4.6.0-rc5*

discover local endpoint address for an RPC client


Synopsis
========

.. c:function:: int rpc_localaddr( struct rpc_clnt * clnt, struct sockaddr * buf, size_t buflen )

Arguments
=========

``clnt``
    RPC client structure

``buf``
    target buffer

``buflen``
    size of target buffer, in bytes


Description
===========

Returns zero and fills in “buf” and “buflen” if successful; otherwise, a
negative errno is returned.

This works even if the underlying transport is not currently connected,
or if the upper layer never previously provided a source address.


The result of this function call is transient
=============================================

multiple calls in succession may give different results, depending on
how local networking configuration changes over time.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
