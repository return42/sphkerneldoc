.. -*- coding: utf-8; mode: rst -*-

.. _API-rpcb-getport-async:

==================
rpcb_getport_async
==================

*man rpcb_getport_async(9)*

*4.6.0-rc5*

obtain the port for a given RPC service on a given host


Synopsis
========

.. c:function:: void rpcb_getport_async( struct rpc_task * task )

Arguments
=========

``task``
    task that is waiting for portmapper request


Description
===========

This one can be called for an ongoing RPC request, and can be used in an
async (rpciod) context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
