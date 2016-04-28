.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-load-transport:

===================
xprt_load_transport
===================

*man xprt_load_transport(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
