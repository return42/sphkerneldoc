
.. _API-xprt-load-transport:

===================
xprt_load_transport
===================

*man xprt_load_transport(9)*

*4.6.0-rc1*

load a transport implementation


Synopsis
========

.. c:function:: int xprt_load_transport( const char * transport_name )

Arguments
=========

``transport_name``
    transport to load


0
=

transport successfully loaded -ENOENT: transport module not available
