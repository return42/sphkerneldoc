.. -*- coding: utf-8; mode: rst -*-

.. _API---platform-register-drivers:

===========================
__platform_register_drivers
===========================

*man __platform_register_drivers(9)*

*4.6.0-rc5*

register an array of platform drivers


Synopsis
========

.. c:function:: int __platform_register_drivers( struct platform_driver *const * drivers, unsigned int count, struct module * owner )

Arguments
=========

``drivers``
    an array of drivers to register

``count``
    the number of drivers to register

``owner``
    module owning the drivers


Description
===========

Registers platform drivers specified by an array. On failure to register
a driver, all previously registered drivers will be unregistered.
Callers of this API should use ``platform_unregister_drivers`` to
unregister drivers in the reverse order.


Returns
=======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
