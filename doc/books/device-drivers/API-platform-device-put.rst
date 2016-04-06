
.. _API-platform-device-put:

===================
platform_device_put
===================

*man platform_device_put(9)*

*4.6.0-rc1*

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

Free all memory associated with a platform device. This function must _only_ be externally called in error cases. All other usage is a bug.
