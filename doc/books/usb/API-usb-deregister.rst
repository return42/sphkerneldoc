
.. _API-usb-deregister:

==============
usb_deregister
==============

*man usb_deregister(9)*

*4.6.0-rc1*

unregister a USB interface driver


Synopsis
========

.. c:function:: void usb_deregister( struct usb_driver * driver )

Arguments
=========

``driver``
    USB operations of the interface driver to unregister


Context
=======

must be able to sleep


Description
===========

Unlinks the specified driver from the internal USB driver list.


NOTE
====

If you called ``usb_register_dev``, you still need to call ``usb_deregister_dev`` to clean up your driver's allocated minor numbers, this ⋆ call will no longer do it for you.
