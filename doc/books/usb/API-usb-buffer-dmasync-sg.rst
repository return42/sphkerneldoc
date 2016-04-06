
.. _API-usb-buffer-dmasync-sg:

=====================
usb_buffer_dmasync_sg
=====================

*man usb_buffer_dmasync_sg(9)*

*4.6.0-rc1*

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

Use this when you are re-using a scatterlist's data buffers for another USB request.
