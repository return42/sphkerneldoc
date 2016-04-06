
.. _API-usb-fill-bulk-urb:

=================
usb_fill_bulk_urb
=================

*man usb_fill_bulk_urb(9)*

*4.6.0-rc1*

macro to help initialize a bulk urb


Synopsis
========

.. c:function:: void usb_fill_bulk_urb( struct urb * urb, struct usb_device * dev, unsigned int pipe, void * transfer_buffer, int buffer_length, usb_complete_t complete_fn, void * context )

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


Description
===========

Initializes a bulk urb with the proper information needed to submit it to a device.
