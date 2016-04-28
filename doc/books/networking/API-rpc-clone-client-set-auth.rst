.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-clone-client-set-auth:

=========================
rpc_clone_client_set_auth
=========================

*man rpc_clone_client_set_auth(9)*

*4.6.0-rc5*

Clone an RPC client structure and set its auth


Synopsis
========

.. c:function:: struct rpc_clnt * rpc_clone_client_set_auth( struct rpc_clnt * clnt, rpc_authflavor_t flavor )

Arguments
=========

``clnt``
    RPC client whose parameters are copied

``flavor``
    security flavor for new client


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
