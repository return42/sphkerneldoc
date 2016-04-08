
.. _API-rpc-net-ns:

==========
rpc_net_ns
==========

*man rpc_net_ns(9)*

*4.6.0-rc1*

Get the network namespace for this RPC client


Synopsis
========

.. c:function:: struct net ⋆ rpc_net_ns( struct rpc_clnt * clnt )

Arguments
=========

``clnt``
    RPC client to query
