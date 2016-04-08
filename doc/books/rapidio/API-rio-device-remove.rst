
.. _API-rio-device-remove:

=================
rio_device_remove
=================

*man rio_device_remove(9)*

*4.6.0-rc1*

Remove a RIO device from the system


Synopsis
========

.. c:function:: int rio_device_remove( struct device * dev )

Arguments
=========

``dev``
    the RIO device structure to match against


Description
===========

Remove a RIO device from the system. If it has an associated driver, then run the driver ``remove`` method. Then update the reference count.
