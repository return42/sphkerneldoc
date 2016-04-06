
.. _API-gadget-is-otg:

=============
gadget_is_otg
=============

*man gadget_is_otg(9)*

*4.6.0-rc1*

return true iff the hardware is OTG-ready


Synopsis
========

.. c:function:: int gadget_is_otg( struct usb_gadget * g )

Arguments
=========

``g``
    controller that might have a Mini-AB connector


Description
===========

This is a runtime test, since kernels with a USB-OTG stack sometimes run on boards which only have a Mini-B (or Mini-A) connector.
