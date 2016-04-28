.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-set-device-state:

====================
usb_set_device_state
====================

*man usb_set_device_state(9)*

*4.6.0-rc5*

change a device's current state (usbcore, hcds)


Synopsis
========

.. c:function:: void usb_set_device_state( struct usb_device * udev, enum usb_device_state new_state )

Arguments
=========

``udev``
    pointer to device whose state should be changed

``new_state``
    new state value to be stored


Description
===========

udev->state is _not_ fully protected by the device lock. Although most
transitions are made only while holding the lock, the state can can
change to USB_STATE_NOTATTACHED at almost any time. This is so that
devices can be marked as disconnected as soon as possible, without
having to wait for any semaphores to be released. As a result, all
changes to any device's state must be protected by the
device_state_lock spinlock.

Once a device has been added to the device tree, all changes to its
state should be made using this routine. The state should _not_ be set
directly.

If udev->state is already USB_STATE_NOTATTACHED then no change is
made. Otherwise udev->state is set to new_state, and if new_state is
USB_STATE_NOTATTACHED then all of udev's descendants' states are also
set to USB_STATE_NOTATTACHED.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
