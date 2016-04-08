
.. _API-xprt-get:

========
xprt_get
========

*man xprt_get(9)*

*4.6.0-rc1*

return a reference to an RPC transport.


Synopsis
========

.. c:function:: struct rpc_xprt ⋆ xprt_get( struct rpc_xprt * xprt )

Arguments
=========

``xprt``
    pointer to the transport
