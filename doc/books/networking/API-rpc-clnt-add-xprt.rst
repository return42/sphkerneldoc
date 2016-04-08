
.. _API-rpc-clnt-add-xprt:

=================
rpc_clnt_add_xprt
=================

*man rpc_clnt_add_xprt(9)*

*4.6.0-rc1*

Add a new transport to a rpc_clnt


Synopsis
========

.. c:function:: int rpc_clnt_add_xprt( struct rpc_clnt * clnt, struct xprt_create * xprtargs, int (*setup) struct rpc_clnt *, struct rpc_xprt_switch *, struct rpc_xprt *, void *, void * data )

Arguments
=========

``clnt``
    pointer to struct rpc_clnt

``xprtargs``
    pointer to struct xprt_create

``setup``
    callback to test and/or set up the connection

``data``
    pointer to setup function data


Description
===========

Creates a new transport using the parameters set in args and adds it to clnt. If ping is set, then test that connectivity succeeds before adding the new transport.
