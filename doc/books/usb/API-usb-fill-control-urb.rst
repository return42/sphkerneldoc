
.. _API-usb-fill-control-urb:

====================
usb_fill_control_urb
====================

*man usb_fill_control_urb(9)*

*4.6.0-rc1*

initializes a control urb


Synopsis
========

.. c:function:: void usb_fill_control_urb( struct urb * urb, struct usb_device * dev, unsigned int pipe, unsigned char * setup_packet, void * transfer_buffer, int buffer_length, usb_complete_t complete_fn, void * context )

Arguments
=========

``urb``
    pointer to the urb to initialize.

``dev``
    pointer to the struct usb_device for this urb.

``pipe``
    the endpoint pipe

``setup_packet``
    pointer to the setup_packet buffer

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

Initializes a control urb with the proper information needed to submit it to a device.
