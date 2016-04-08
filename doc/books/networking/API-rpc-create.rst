
.. _API-rpc-create:

==========
rpc_create
==========

*man rpc_create(9)*

*4.6.0-rc1*

create an RPC client and transport with one call


Synopsis
========

.. c:function:: struct rpc_clnt ⋆ rpc_create( struct rpc_create_args * args )

Arguments
=========

``args``
    rpc_clnt create argument structure


Description
===========

Creates and initializes an RPC transport and an RPC client.

It can ping the server in order to determine if it is up, and to see if it supports this program and version. RPC_CLNT_CREATE_NOPING disables this behavior so asynchronous tasks
can also use rpc_create.
