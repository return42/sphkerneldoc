
.. _API-xprt-register-transport:

=======================
xprt_register_transport
=======================

*man xprt_register_transport(9)*

*4.6.0-rc1*

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

If a transport implementation is loaded as a kernel module, it can call this interface to make itself known to the RPC client.


0
=

transport successfully registered -EEXIST: transport already registered -EINVAL: transport module being unloaded
