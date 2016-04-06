
.. _API-device-unregister:

=================
device_unregister
=================

*man device_unregister(9)*

*4.6.0-rc1*

unregister device from system.


Synopsis
========

.. c:function:: void device_unregister( struct device * dev )

Arguments
=========

``dev``
    device going away.


Description
===========

We do this in two parts, like we do ``device_register``. First, we remove it from all the subsystems with ``device_del``, then we decrement the reference count via ``put_device``.
If that is the final reference count, the device will be cleaned up via ``device_release`` above. Otherwise, the structure will stick around until the final reference to the device
is dropped.
