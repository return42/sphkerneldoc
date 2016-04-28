.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-queue-reset-device:

======================
usb_queue_reset_device
======================

*man usb_queue_reset_device(9)*

*4.6.0-rc5*

Reset a USB device from an atomic context


Synopsis
========

.. c:function:: void usb_queue_reset_device( struct usb_interface * iface )

Arguments
=========

``iface``
    USB interface belonging to the device to reset


Description
===========

This function can be used to reset a USB device from an atomic context,
where ``usb_reset_device`` won't work (as it blocks).

Doing a reset via this method is functionally equivalent to calling
``usb_reset_device``, except for the fact that it is delayed to a
workqueue. This means that any drivers bound to other interfaces might
be unbound, as well as users from usbfs in user space.


Corner cases
============

- Scheduling two resets at the same time from two different drivers
attached to two different interfaces of the same device is possible;
depending on how the driver attached to each interface handles
->``pre_reset``, the second reset might happen or not.

- If the reset is delayed so long that the interface is unbound from its
driver, the reset will be skipped.

- This function can be called during .\ ``probe``. It can also be called
during .\ ``disconnect``, but doing so is pointless because the reset
will not occur. If you really want to reset the device during
.\ ``disconnect``, call ``usb_reset_device`` directly -- but watch out
for nested unbinding issues!


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
