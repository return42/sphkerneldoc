.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-max-payload:

===============
rpc_max_payload
===============

*man rpc_max_payload(9)*

*4.6.0-rc5*

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

For stream transports, this is one RPC record fragment (see RFC 1831),
as we don't support multi-record requests yet. For datagram transports,
this is the size of an IP packet minus the IP, UDP, and RPC header
sizes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
