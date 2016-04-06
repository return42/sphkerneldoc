
.. _API-usb-clear-halt:

==============
usb_clear_halt
==============

*man usb_clear_halt(9)*

*4.6.0-rc1*

tells device to clear endpoint halt/stall condition


Synopsis
========

.. c:function:: int usb_clear_halt( struct usb_device * dev, int pipe )

Arguments
=========

``dev``
    device whose endpoint is halted

``pipe``
    endpoint “pipe” being cleared


Context
=======

!in_interrupt ()


Description
===========

This is used to clear halt conditions for bulk and interrupt endpoints, as reported by URB completion status. Endpoints that are halted are sometimes referred to as being
“stalled”. Such endpoints are unable to transmit or receive data until the halt status is cleared. Any URBs queued for such an endpoint should normally be unlinked by the driver
before clearing the halt condition, as described in sections 5.7.5 and 5.8.5 of the USB 2.0 spec.

Note that control and isochronous endpoints don't halt, although control endpoints report “protocol stall” (for unsupported requests) using the same status code used to report a
true stall.

This call is synchronous, and may not be used in an interrupt context.


Return
======

Zero on success, or else the status code returned by the underlying ``usb_control_msg`` call.
