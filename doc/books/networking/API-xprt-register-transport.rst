.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-register-transport:

=======================
xprt_register_transport
=======================

*man xprt_register_transport(9)*

*4.6.0-rc5*

register a transport implementation


Synopsis
========

.. c:function:: int xprt_register_transport( struct xprt_class * transport )

Arguments
=========

``transport``
    transport to register


Description
===========

If a transport implementation is loaded as a kernel module, it can call
this interface to make itself known to the RPC client.


0
=

transport successfully registered -EEXIST: transport already registered
-EINVAL: transport module being unloaded


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
