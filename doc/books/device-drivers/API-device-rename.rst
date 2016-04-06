
.. _API-device-rename:

=============
device_rename
=============

*man device_rename(9)*

*4.6.0-rc1*

renames a device


Synopsis
========

.. c:function:: int device_rename( struct device * dev, const char * new_name )

Arguments
=========

``dev``
    the pointer to the struct device to be renamed

``new_name``
    the new name of the device


Description
===========

It is the responsibility of the caller to provide mutual exclusion between two different calls of device_rename on the same device to ensure that new_name is valid and won't
conflict with other devices.


Note
====

Don't call this function. Currently, the networking layer calls this function, but that will change. The following text from Kay Sievers offers


some insight
============

Renaming devices is racy at many levels, symlinks and other stuff are not replaced atomically, and you get a “move” uevent, but it's not easy to connect the event to the old and
new device. Device nodes are not renamed at all, there isn't even support for that in the kernel now.

In the meantime, during renaming, your target name might be taken by another driver, creating conflicts. Or the old name is taken directly after you renamed it -- then you get
events for the same DEVPATH, before you even see the “move” event. It's just a mess, and nothing new should ever rely on kernel device renaming. Besides that, it's not even
implemented now for other things than (driver-core wise very simple) network devices.

We are currently about to change network renaming in udev to completely disallow renaming of devices in the same namespace as the kernel uses, because we can't solve the problems
properly, that arise with swapping names of multiple interfaces without races. Means, renaming of eth[0-9]⋆ will only be allowed to some other name than eth[0-9]⋆, for the
aforementioned reasons.

Make up a “real” name in the driver before you register anything, or add some other attributes for userspace to find the device, or use udev to add symlinks -- but never rename
kernel devices later, it's a complete mess. We don't even want to get into that and try to implement the missing pieces in the core. We really have other pieces to fix in the
driver core mess. :)
