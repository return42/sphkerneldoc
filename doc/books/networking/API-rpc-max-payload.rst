
.. _API-rpc-max-payload:

===============
rpc_max_payload
===============

*man rpc_max_payload(9)*

*4.6.0-rc1*

Get maximum payload size for a transport, in bytes


Synopsis
========

.. c:function:: size_t rpc_max_payload( struct rpc_clnt * clnt )

Arguments
=========

``clnt``
    RPC client to query


Description
===========

For stream transports, this is one RPC record fragment (see RFC 1831), as we don't support multi-record requests yet. For datagram transports, this is the size of an IP packet
minus the IP, UDP, and RPC header sizes.
