
.. _API-rpc-clnt-test-and-add-xprt:

==========================
rpc_clnt_test_and_add_xprt
==========================

*man rpc_clnt_test_and_add_xprt(9)*

*4.6.0-rc1*

Test and add a new transport to a rpc_clnt


Synopsis
========

.. c:function:: int rpc_clnt_test_and_add_xprt( struct rpc_clnt * clnt, struct rpc_xprt_switch * xps, struct rpc_xprt * xprt, void * dummy )

Arguments
=========

``clnt``
    pointer to struct rpc_clnt

``xps``
    pointer to struct rpc_xprt_switch,

``xprt``
    pointer struct rpc_xprt

``dummy``
    unused
