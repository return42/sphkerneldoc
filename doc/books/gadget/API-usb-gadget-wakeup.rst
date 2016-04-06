
.. _API-usb-gadget-wakeup:

=================
usb_gadget_wakeup
=================

*man usb_gadget_wakeup(9)*

*4.6.0-rc1*

tries to wake up the host connected to this gadget


Synopsis
========

.. c:function:: int usb_gadget_wakeup( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    controller used to wake up the host


Description
===========

Returns zero on success, else negative error code if the hardware doesn't support such attempts, or its support has not been enabled by the usb host. Drivers must return device
descriptors that report their ability to support this, or hosts won't enable it.

This may also try to use SRP to wake the host and start enumeration, even if OTG isn't otherwise in use. OTG devices may also start remote wakeup even when hosts don't explicitly
enable it.
