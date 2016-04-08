
.. _API-xprt-unregister-transport:

=========================
xprt_unregister_transport
=========================

*man xprt_unregister_transport(9)*

*4.6.0-rc1*

unregister a transport implementation


Synopsis
========

.. c:function:: int xprt_unregister_transport( struct xprt_class * transport )

Arguments
=========

``transport``
    transport to unregister


0
=

transport successfully unregistered -ENOENT: transport never registered
