.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-device-put:

===================
platform_device_put
===================

*man platform_device_put(9)*

*4.6.0-rc5*

destroy a platform device


Synopsis
========

.. c:function:: void platform_device_put( struct platform_device * pdev )

Arguments
=========

``pdev``
    platform device to free


Description
===========

Free all memory associated with a platform device. This function must
_only_ be externally called in error cases. All other usage is a bug.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
