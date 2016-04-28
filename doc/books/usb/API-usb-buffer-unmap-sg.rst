.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-buffer-unmap-sg:

===================
usb_buffer_unmap_sg
===================

*man usb_buffer_unmap_sg(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
