.. -*- coding: utf-8; mode: rst -*-

.. _API---media-device-register:

=======================
__media_device_register
=======================

*man __media_device_register(9)*

*4.6.0-rc5*

Registers a media device element


Synopsis
========

.. c:function:: int __media_device_register( struct media_device * mdev, struct module * owner )

Arguments
=========

``mdev``
    pointer to struct ``media_device``

``owner``
    should be filled with ``THIS_MODULE``


Description
===========

Users, should, instead, call the ``media_device_register`` macro.

The caller is responsible for initializing the media_device structure
before registration. The following fields must be set:

- dev must point to the parent device (usually a ``pci_dev``,
``usb_interface`` or ``platform_device`` instance).

- model must be filled with the device model name as a NUL-terminated
UTF-8 string. The device/model revision must not be stored in this
field.


The following fields are optional
=================================

- serial is a unique serial number stored as a NUL-terminated ASCII
string. The field is big enough to store a GUID in text form. If the
hardware doesn't provide a unique serial number this field must be left
empty.

- bus_info represents the location of the device in the system as a
NUL-terminated ASCII string. For PCI/PCIe devices bus_info must be set
to “PCI:” (or “PCIe:”) followed by the value of ``pci_name``. For USB
devices, the ``usb_make_path`` function must be used. This field is used
by applications to distinguish between otherwise identical devices that
don't provide a serial number.

- hw_revision is the hardware device revision in a driver-specific
format. When possible the revision should be formatted with the
KERNEL_VERSION macro.

- driver_version is formatted with the KERNEL_VERSION macro. The
version minor must be incremented when new features are added to the
userspace API without breaking binary compatibility. The version major
must be incremented when binary compatibility is broken.


Notes
=====

Upon successful registration a character device named media[0-9]+ is
created. The device major and minor numbers are dynamic. The model name
is exported as a sysfs attribute.

Unregistering a media device that hasn't been registered is *NOT* safe.


Return
======

returns zero on success or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
