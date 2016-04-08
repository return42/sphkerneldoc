
.. _API-xprt-put:

========
xprt_put
========

*man xprt_put(9)*

*4.6.0-rc1*

release a reference to an RPC transport.


Synopsis
========

.. c:function:: void xprt_put( struct rpc_xprt * xprt )

Arguments
=========

``xprt``
    pointer to the transport
