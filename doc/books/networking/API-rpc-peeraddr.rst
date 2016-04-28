.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-peeraddr:

============
rpc_peeraddr
============

*man rpc_peeraddr(9)*

*4.6.0-rc5*

extract remote peer address from clnt's xprt


Synopsis
========

.. c:function:: size_t rpc_peeraddr( struct rpc_clnt * clnt, struct sockaddr * buf, size_t bufsize )

Arguments
=========

``clnt``
    RPC client structure

``buf``
    target buffer

``bufsize``
    length of target buffer


Description
===========

Returns the number of bytes that are actually in the stored address.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
