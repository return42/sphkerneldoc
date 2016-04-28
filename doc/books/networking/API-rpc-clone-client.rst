.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-clone-client:

================
rpc_clone_client
================

*man rpc_clone_client(9)*

*4.6.0-rc5*

Clone an RPC client structure


Synopsis
========

.. c:function:: struct rpc_clnt * rpc_clone_client( struct rpc_clnt * clnt )

Arguments
=========

``clnt``
    RPC client whose parameters are copied


Description
===========

Returns a fresh RPC client or an ERR_PTR.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
