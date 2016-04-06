
.. _API-usb-match-id:

============
usb_match_id
============

*man usb_match_id(9)*

*4.6.0-rc1*

find first usb_device_id matching device or interface


Synopsis
========

.. c:function:: const struct usb_device_id ⋆ usb_match_id( struct usb_interface * interface, const struct usb_device_id * id )

Arguments
=========

``interface``
    the interface of interest

``id``
    array of usb_device_id structures, terminated by zero entry


Description
===========

usb_match_id searches an array of usb_device_id's and returns the first one matching the device or interface, or null. This is used when binding (or rebinding) a driver to an
interface. Most USB device drivers will use this indirectly, through the usb core, but some layered driver frameworks use it directly. These device tables are exported with
MODULE_DEVICE_TABLE, through modutils, to support the driver loading functionality of USB hotplugging.


Return
======

The first matching usb_device_id, or ``NULL``.


What Matches
============

The “match_flags” element in a usb_device_id controls which members are used. If the corresponding bit is set, the value in the device_id must match its corresponding member in
the device or interface descriptor, or else the device_id does not match.

“driver_info” is normally used only by device drivers, but you can create a wildcard “matches anything” usb_device_id as a driver's “modules.usbmap” entry if you provide an id
with only a nonzero “driver_info” field. If you do this, the USB device driver's ``probe`` routine should use additional intelligence to decide whether to bind to the specified
interface.


What Makes Good usb_device_id Tables
====================================

The match algorithm is very simple, so that intelligence in driver selection must come from smart driver id records. Unless you have good reasons to use another selection policy,
provide match elements only in related groups, and order match specifiers from specific to general. Use the macros provided for that purpose if you can.

The most specific match specifiers use device descriptor data. These are commonly used with product-specific matches; the USB_DEVICE macro lets you provide vendor and product IDs,
and you can also match against ranges of product revisions. These are widely used for devices with application or vendor specific bDeviceClass values.

Matches based on device class/subclass/protocol specifications are slightly more general; use the USB_DEVICE_INFO macro, or its siblings. These are used with single-function
devices where bDeviceClass doesn't specify that each interface has its own class.

Matches based on interface class/subclass/protocol are the most general; they let drivers bind to any interface on a multiple-function device. Use the USB_INTERFACE_INFO macro,
or its siblings, to match class-per-interface style devices (as recorded in bInterfaceClass).

Note that an entry created by USB_INTERFACE_INFO won't match any interface if the device class is set to Vendor-Specific. This is deliberate; according to the USB spec the
meanings of the interface class/subclass/protocol for these devices are also vendor-specific, and hence matching against a standard product class wouldn't work anyway. If you
really want to use an interface-based match for such a device, create a match record that also specifies the vendor ID. (Unforunately there isn't a standard macro for creating
records like this.)

Within those groups, remember that not all combinations are meaningful. For example, don't give a product version range without vendor and product IDs; or specify a protocol
without its associated class and subclass.
