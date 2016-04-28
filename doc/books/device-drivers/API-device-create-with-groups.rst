.. -*- coding: utf-8; mode: rst -*-

.. _API-device-create-with-groups:

=========================
device_create_with_groups
=========================

*man device_create_with_groups(9)*

*4.6.0-rc5*

creates a device and registers it with sysfs


Synopsis
========

.. c:function:: struct device * device_create_with_groups( struct class * class, struct device * parent, dev_t devt, void * drvdata, const struct attribute_group ** groups, const char * fmt, ... )

Arguments
=========

``class``
    pointer to the struct class that this device should be registered to

``parent``
    pointer to the parent struct device of this new device, if any

``devt``
    the dev_t for the char device to be added

``drvdata``
    the data to be added to the device for callbacks

``groups``
    NULL-terminated list of attribute groups to be created

``fmt``
    string for the device's name

``...``
    variable arguments


Description
===========

This function can be used by char device classes. A struct device will
be created in sysfs, registered to the specified class. Additional
attributes specified in the groups parameter will also be created
automatically.

A “dev” file will be created, showing the dev_t for the device, if the
dev_t is not 0,0. If a pointer to a parent struct device is passed in,
the newly created struct device will be a child of that device in sysfs.
The pointer to the struct device will be returned from the call. Any
further sysfs files that might be required can be created using this
pointer.

Returns ``struct device`` pointer on success, or ``ERR_PTR`` on error.


Note
====

the struct class passed to this function must have previously been
created with a call to ``class_create``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
