
.. _API-xprt-disconnect-done:

====================
xprt_disconnect_done
====================

*man xprt_disconnect_done(9)*

*4.6.0-rc1*

mark a transport as disconnected


Synopsis
========

.. c:function:: void xprt_disconnect_done( struct rpc_xprt * xprt )

Arguments
=========

``xprt``
    transport to flag for disconnect
