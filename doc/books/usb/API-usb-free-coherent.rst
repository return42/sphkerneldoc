
.. _API-usb-free-coherent:

=================
usb_free_coherent
=================

*man usb_free_coherent(9)*

*4.6.0-rc1*

free memory allocated with ``usb_alloc_coherent``


Synopsis
========

.. c:function:: void usb_free_coherent( struct usb_device * dev, size_t size, void * addr, dma_addr_t dma )

Arguments
=========

``dev``
    device the buffer was used with

``size``
    requested buffer size

``addr``
    CPU address of buffer

``dma``
    DMA address of buffer


Description
===========

This reclaims an I/O buffer, letting it be reused. The memory must have been allocated using ``usb_alloc_coherent``, and the parameters must match those provided in that allocation
request.
