
.. _API-usb-buffer-unmap:

================
usb_buffer_unmap
================

*man usb_buffer_unmap(9)*

*4.6.0-rc1*

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
