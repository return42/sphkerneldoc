
.. _API-usb-fill-int-urb:

================
usb_fill_int_urb
================

*man usb_fill_int_urb(9)*

*4.6.0-rc1*

macro to help initialize a interrupt urb


Synopsis
========

.. c:function:: void usb_fill_int_urb( struct urb * urb, struct usb_device * dev, unsigned int pipe, void * transfer_buffer, int buffer_length, usb_complete_t complete_fn, void * context, int interval )

Arguments
=========

``urb``
    pointer to the urb to initialize.

``dev``
    pointer to the struct usb_device for this urb.

``pipe``
    the endpoint pipe

``transfer_buffer``
    pointer to the transfer buffer

``buffer_length``
    length of the transfer buffer

``complete_fn``
    pointer to the usb_complete_t function

``context``
    what to set the urb context to.

``interval``
    what to set the urb interval to, encoded like the endpoint descriptor's bInterval value.


Description
===========

Initializes a interrupt urb with the proper information needed to submit it to a device.

Note that High Speed and SuperSpeed interrupt endpoints use a logarithmic encoding of the endpoint interval, and express polling intervals in microframes (eight per millisecond)
rather than in frames (one per millisecond).

Wireless USB also uses the logarithmic encoding, but specifies it in units of 128us instead of 125us. For Wireless USB devices, the interval is passed through to the host
controller, rather than being translated into microframe units.
