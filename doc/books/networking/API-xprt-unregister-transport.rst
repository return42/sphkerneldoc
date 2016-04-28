.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-unregister-transport:

=========================
xprt_unregister_transport
=========================

*man xprt_unregister_transport(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
