
.. _API-rpc-peeraddr:

============
rpc_peeraddr
============

*man rpc_peeraddr(9)*

*4.6.0-rc1*

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
