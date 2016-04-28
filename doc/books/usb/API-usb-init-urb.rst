.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-init-urb:

============
usb_init_urb
============

*man usb_init_urb(9)*

*4.6.0-rc5*

initializes a urb so that it can be used by a USB driver


Synopsis
========

.. c:function:: void usb_init_urb( struct urb * urb )

Arguments
=========

``urb``
    pointer to the urb to initialize


Description
===========

Initializes a urb so that the USB subsystem can use it properly.

If a urb is created with a call to ``usb_alloc_urb`` it is not necessary
to call this function. Only use this if you allocate the space for a
struct urb on your own. If you call this function, be careful when
freeing the memory for your urb that it is no longer in use by the USB
core.

Only use this function if you _really_ understand what you are doing.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
