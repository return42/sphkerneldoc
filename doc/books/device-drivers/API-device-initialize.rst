
.. _API-device-initialize:

=================
device_initialize
=================

*man device_initialize(9)*

*4.6.0-rc1*

init device structure.


Synopsis
========

.. c:function:: void device_initialize( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

This prepares the device for use by other layers by initializing its fields. It is the first half of ``device_register``, if called by that function, though it can also be called
separately, so one may use ``dev``'s fields. In particular, ``get_device``/``put_device`` may be used for reference counting of ``dev`` after calling this function.

All fields in ``dev`` must be initialized by the caller to 0, except for those explicitly set to some other value. The simplest approach is to use ``kzalloc`` to allocate the
structure containing ``dev``.


NOTE
====

Use ``put_device`` to give up your reference instead of freeing ``dev`` directly once you have called this function.
