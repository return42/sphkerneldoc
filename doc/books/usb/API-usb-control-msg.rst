
.. _API-usb-control-msg:

===============
usb_control_msg
===============

*man usb_control_msg(9)*

*4.6.0-rc1*

Builds a control urb, sends it off and waits for completion


Synopsis
========

.. c:function:: int usb_control_msg( struct usb_device * dev, unsigned int pipe, __u8 request, __u8 requesttype, __u16 value, __u16 index, void * data, __u16 size, int timeout )

Arguments
=========

``dev``
    pointer to the usb device to send the message to

``pipe``
    endpoint “pipe” to send the message to

``request``
    USB message request value

``requesttype``
    USB message request type value

``value``
    USB message value

``index``
    USB message index value

``data``
    pointer to the data to send

``size``
    length in bytes of the data to send

``timeout``
    time in msecs to wait for the message to complete before timing out (if 0 the wait is forever)


Context
=======

!in_interrupt ()


Description
===========

This function sends a simple control message to a specified endpoint and waits for the message to complete, or timeout.

Don't use this function from within an interrupt context, like a bottom half handler. If you need an asynchronous message, or need to send a message from within interrupt context,
use ``usb_submit_urb``. If a thread in your driver uses this call, make sure your ``disconnect`` method can wait for it to complete. Since you don't have a handle on the URB used,
you can't cancel the request.


Return
======

If successful, the number of bytes transferred. Otherwise, a negative error number.
