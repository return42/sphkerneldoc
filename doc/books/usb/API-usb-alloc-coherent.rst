
.. _API-usb-alloc-coherent:

==================
usb_alloc_coherent
==================

*man usb_alloc_coherent(9)*

*4.6.0-rc1*

allocate dma-consistent buffer for URB_NO_xxx_DMA_MAP


Synopsis
========

.. c:function:: void ⋆ usb_alloc_coherent( struct usb_device * dev, size_t size, gfp_t mem_flags, dma_addr_t * dma )

Arguments
=========

``dev``
    device the buffer will be used with

``size``
    requested buffer size

``mem_flags``
    affect whether allocation may block

``dma``
    used to return DMA address of buffer


Return
======

Either null (indicating no buffer could be allocated), or the cpu-space pointer to a buffer that may be used to perform DMA to the specified device. Such cpu-space buffers are
returned along with the DMA address (through the pointer provided).


Note
====

These buffers are used with URB_NO_xxx_DMA_MAP set in urb->transfer_flags to avoid behaviors like using “DMA bounce buffers”, or thrashing IOMMU hardware during URB
completion/resubmit. The implementation varies between platforms, depending on details of how DMA will work to this device. Using these buffers also eliminates cacheline sharing
problems on architectures where CPU caches are not DMA-coherent. On systems without bus-snooping caches, these buffers are uncached.

When the buffer is no longer used, free it with ``usb_free_coherent``.
