
.. _API-root-device-unregister:

======================
root_device_unregister
======================

*man root_device_unregister(9)*

*4.6.0-rc1*

unregister and free a root device


Synopsis
========

.. c:function:: void root_device_unregister( struct device * dev )

Arguments
=========

``dev``
    device going away


Description
===========

This function unregisters and cleans up a device that was created by ``root_device_register``.
