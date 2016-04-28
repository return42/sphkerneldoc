.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-get-current-frame-number:

============================
usb_get_current_frame_number
============================

*man usb_get_current_frame_number(9)*

*4.6.0-rc5*

return current bus frame number


Synopsis
========

.. c:function:: int usb_get_current_frame_number( struct usb_device * dev )

Arguments
=========

``dev``
    the device whose bus is being queried


Return
======

The current frame number for the USB host controller used with the given
USB device. This can be used when scheduling isochronous requests.


Note
====

Different kinds of host controller have different “scheduling horizons”.
While one type might support scheduling only 32 frames into the future,
others could support scheduling up to 1024 frames into the future.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
