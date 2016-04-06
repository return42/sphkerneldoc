
.. _API-platform-device-del:

===================
platform_device_del
===================

*man platform_device_del(9)*

*4.6.0-rc1*

remove a platform-level device


Synopsis
========

.. c:function:: void platform_device_del( struct platform_device * pdev )

Arguments
=========

``pdev``
    platform device we're removing


Description
===========

Note that this function will also release all memory- and port-based resources owned by the device (``dev``->resource). This function must _only_ be externally called in error
cases. All other usage is a bug.
