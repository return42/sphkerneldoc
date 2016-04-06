
.. _API-usb-composite-unregister:

========================
usb_composite_unregister
========================

*man usb_composite_unregister(9)*

*4.6.0-rc1*

unregister a composite driver


Synopsis
========

.. c:function:: void usb_composite_unregister( struct usb_composite_driver * driver )

Arguments
=========

``driver``
    the driver to unregister


Description
===========

This function is used to unregister drivers using the composite driver framework.
