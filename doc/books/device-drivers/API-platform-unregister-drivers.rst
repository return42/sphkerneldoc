.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-unregister-drivers:

===========================
platform_unregister_drivers
===========================

*man platform_unregister_drivers(9)*

*4.6.0-rc5*

unregister an array of platform drivers


Synopsis
========

.. c:function:: void platform_unregister_drivers( struct platform_driver *const * drivers, unsigned int count )

Arguments
=========

``drivers``
    an array of drivers to unregister

``count``
    the number of drivers to unregister


Description
===========

Unegisters platform drivers specified by an array. This is typically
used to complement an earlier call to ``platform_register_drivers``.
Drivers are unregistered in the reverse order in which they were
registered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
