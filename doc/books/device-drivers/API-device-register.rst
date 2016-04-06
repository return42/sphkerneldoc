
.. _API-device-register:

===============
device_register
===============

*man device_register(9)*

*4.6.0-rc1*

register a device with the system.


Synopsis
========

.. c:function:: int device_register( struct device * dev )

Arguments
=========

``dev``
    pointer to the device structure


Description
===========

This happens in two clean steps - initialize the device and add it to the system. The two steps can be called separately, but this is the easiest and most common. I.e. you should
only call the two helpers separately if have a clearly defined need to use and refcount the device before it is added to the hierarchy.

For more information, see the kerneldoc for ``device_initialize`` and ``device_add``.


NOTE
====

_Never_ directly free ``dev`` after calling this function, even if it returned an error! Always use ``put_device`` to give up the reference initialized in this function instead.
