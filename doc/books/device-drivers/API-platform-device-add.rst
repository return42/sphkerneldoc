.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-device-add:

===================
platform_device_add
===================

*man platform_device_add(9)*

*4.6.0-rc5*

add a platform device to device hierarchy


Synopsis
========

.. c:function:: int platform_device_add( struct platform_device * pdev )

Arguments
=========

``pdev``
    platform device we're adding


Description
===========

This is part 2 of ``platform_device_register``, though may be called
separately _iff_ pdev was allocated by ``platform_device_alloc``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
