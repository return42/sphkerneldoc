
.. _API-rpc-get-timeout:

===============
rpc_get_timeout
===============

*man rpc_get_timeout(9)*

*4.6.0-rc1*

Get timeout for transport in units of HZ


Synopsis
========

.. c:function:: unsigned long rpc_get_timeout( struct rpc_clnt * clnt )

Arguments
=========

``clnt``
    RPC client to query
