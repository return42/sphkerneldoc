.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-buffer-dmasync-sg:

=====================
usb_buffer_dmasync_sg
=====================

*man usb_buffer_dmasync_sg(9)*

*4.6.0-rc5*

synchronize DMA and CPU view of scatterlist buffer(s)


Synopsis
========

.. c:function:: void usb_buffer_dmasync_sg( const struct usb_device * dev, int is_in, struct scatterlist * sg, int n_hw_ents )

Arguments
=========

``dev``
    device to which the scatterlist will be mapped

``is_in``
    mapping transfer direction

``sg``
    the scatterlist to synchronize

``n_hw_ents``
    the positive return value from usb_buffer_map_sg


Description
===========

Use this when you are re-using a scatterlist's data buffers for another
USB request.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
