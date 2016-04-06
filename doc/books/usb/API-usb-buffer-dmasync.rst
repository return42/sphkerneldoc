
.. _API-usb-buffer-dmasync:

==================
usb_buffer_dmasync
==================

*man usb_buffer_dmasync(9)*

*4.6.0-rc1*

synchronize DMA and CPU view of buffer(s)


Synopsis
========

.. c:function:: void usb_buffer_dmasync( struct urb * urb )

Arguments
=========

``urb``
    urb whose transfer_buffer/setup_packet will be synchronized
