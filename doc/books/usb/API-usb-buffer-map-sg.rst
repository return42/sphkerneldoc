.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-buffer-map-sg:

=================
usb_buffer_map_sg
=================

*man usb_buffer_map_sg(9)*

*4.6.0-rc5*

create scatterlist DMA mapping(s) for an endpoint


Synopsis
========

.. c:function:: int usb_buffer_map_sg( const struct usb_device * dev, int is_in, struct scatterlist * sg, int nents )

Arguments
=========

``dev``
    device to which the scatterlist will be mapped

``is_in``
    mapping transfer direction

``sg``
    the scatterlist to map

``nents``
    the number of entries in the scatterlist


Return
======

Either < 0 (indicating no buffers could be mapped), or the number of DMA
mapping array entries in the scatterlist.


Note
====

The caller is responsible for placing the resulting DMA addresses from
the scatterlist into URB transfer buffer pointers, and for setting the
URB_NO_TRANSFER_DMA_MAP transfer flag in each of those URBs.

Top I/O rates come from queuing URBs, instead of waiting for each one to
complete before starting the next I/O. This is particularly easy to do
with scatterlists. Just allocate and submit one URB for each DMA mapping
entry returned, stopping on the first error or when all succeed. Better
yet, use the usb_sg_*() calls, which do that (and more) for you.

This call would normally be used when translating scatterlist requests,
rather than ``usb_buffer_map``, since on some hardware (with IOMMUs) it
may be able to coalesce mappings for improved I/O efficiency.

Reverse the effect of this call with ``usb_buffer_unmap_sg``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
