
.. _API-get-device:

==========
get_device
==========

*man get_device(9)*

*4.6.0-rc1*

increment reference count for device.


Synopsis
========

.. c:function:: struct device ⋆ get_device( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

This simply forwards the call to ``kobject_get``, though we do take care to provide for the case that we get a NULL pointer passed in.
