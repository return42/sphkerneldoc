
.. _API-device-add:

==========
device_add
==========

*man device_add(9)*

*4.6.0-rc1*

add device to device hierarchy.


Synopsis
========

.. c:function:: int device_add( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

This is part 2 of ``device_register``, though may be called separately _iff_ ``device_initialize`` has been called separately.

This adds ``dev`` to the kobject hierarchy via ``kobject_add``, adds it to the global and sibling lists for the device, then adds it to the other relevant subsystems of the driver
model.

Do not call this routine or ``device_register`` more than once for any device structure. The driver model core is not designed to work with devices that get unregistered and then
spring back to life. (Among other things, it's very hard to guarantee that all references to the previous incarnation of ``dev`` have been dropped.) Allocate and register a fresh
new struct device instead.


NOTE
====

_Never_ directly free ``dev`` after calling this function, even if it returned an error! Always use ``put_device`` to give up your reference instead.
