
.. _API-rpc-switch-client-transport:

===========================
rpc_switch_client_transport
===========================

*man rpc_switch_client_transport(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: int rpc_switch_client_transport( struct rpc_clnt * clnt, struct xprt_create * args, const struct rpc_timeout * timeout )

Arguments
=========

``clnt``
    pointer to a struct rpc_clnt

``args``
    pointer to the new transport arguments

``timeout``
    pointer to the new timeout parameters


Description
===========

This function allows the caller to switch the RPC transport for the rpc_clnt structure 'clnt' to allow it to connect to a mirrored NFS server, for instance. It assumes that the
caller has ensured that there are no active RPC tasks by using some form of locking.

Returns zero if “clnt” is now using the new xprt. Otherwise a negative errno is returned, and “clnt” continues to use the old xprt.
