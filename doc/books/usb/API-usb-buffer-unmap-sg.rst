
.. _API-usb-buffer-unmap-sg:

===================
usb_buffer_unmap_sg
===================

*man usb_buffer_unmap_sg(9)*

*4.6.0-rc1*

free DMA mapping(s) for a scatterlist


Synopsis
========

.. c:function:: void usb_buffer_unmap_sg( const struct usb_device * dev, int is_in, struct scatterlist * sg, int n_hw_ents )

Arguments
=========

``dev``
    device to which the scatterlist will be mapped

``is_in``
    mapping transfer direction

``sg``
    the scatterlist to unmap

``n_hw_ents``
    the positive return value from usb_buffer_map_sg


Description
===========

Reverses the effect of ``usb_buffer_map_sg``.
