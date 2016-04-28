.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-frame-number:

=======================
usb_gadget_frame_number
=======================

*man usb_gadget_frame_number(9)*

*4.6.0-rc5*

returns the current frame number


Synopsis
========

.. c:function:: int usb_gadget_frame_number( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    controller that reports the frame number


Description
===========

Returns the usb frame number, normally eleven bits from a SOF packet, or
negative errno if this device doesn't support this capability.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
