
.. _API-usb-bulk-msg:

============
usb_bulk_msg
============

*man usb_bulk_msg(9)*

*4.6.0-rc1*

Builds a bulk urb, sends it off and waits for completion


Synopsis
========

.. c:function:: int usb_bulk_msg( struct usb_device * usb_dev, unsigned int pipe, void * data, int len, int * actual_length, int timeout )

Arguments
=========

``usb_dev``
    pointer to the usb device to send the message to

``pipe``
    endpoint “pipe” to send the message to

``data``
    pointer to the data to send

``len``
    length in bytes of the data to send

``actual_length``
    pointer to a location to put the actual length transferred in bytes

``timeout``
    time in msecs to wait for the message to complete before timing out (if 0 the wait is forever)


Context
=======

!in_interrupt ()


Description
===========

This function sends a simple bulk message to a specified endpoint and waits for the message to complete, or timeout.

Don't use this function from within an interrupt context, like a bottom half handler. If you need an asynchronous message, or need to send a message from within interrupt context,
use ``usb_submit_urb`` If a thread in your driver uses this call, make sure your ``disconnect`` method can wait for it to complete. Since you don't have a handle on the URB used,
you can't cancel the request.

Because there is no ``usb_interrupt_msg`` and no USBDEVFS_INTERRUPT ioctl, users are forced to abuse this routine by using it to submit URBs for interrupt endpoints. We will take
the liberty of creating an interrupt URB (with the default interval) if the target is an interrupt endpoint.


Return
======

If successful, 0. Otherwise a negative error number. The number of actual bytes transferred will be stored in the ``actual_length`` parameter.
