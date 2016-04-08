
.. _API-rpc-bind-new-program:

====================
rpc_bind_new_program
====================

*man rpc_bind_new_program(9)*

*4.6.0-rc1*

bind a new RPC program to an existing client


Synopsis
========

.. c:function:: struct rpc_clnt ⋆ rpc_bind_new_program( struct rpc_clnt * old, const struct rpc_program * program, u32 vers )

Arguments
=========

``old``
    old rpc_client

``program``
    rpc program to set

``vers``
    rpc program version


Description
===========

Clones the rpc client and sets up a new RPC program. This is mainly of use for enabling different RPC programs to share the same transport. The Sun NFSv2/v3 ACL protocol can do
this.
