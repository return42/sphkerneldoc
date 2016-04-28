.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-buffer-unmap:

================
usb_buffer_unmap
================

*man usb_buffer_unmap(9)*

*4.6.0-rc5*

free DMA mapping(s) for an urb


Synopsis
========

.. c:function:: void usb_buffer_unmap( struct urb * urb )

Arguments
=========

``urb``
    urb whose transfer_buffer will be unmapped


Description
===========

Reverses the effect of ``usb_buffer_map``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
