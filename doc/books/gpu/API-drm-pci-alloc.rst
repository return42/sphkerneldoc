
.. _API-drm-pci-alloc:

=============
drm_pci_alloc
=============

*man drm_pci_alloc(9)*

*4.6.0-rc1*

Allocate a PCI consistent memory block, for DMA.


Synopsis
========

.. c:function:: drm_dma_handle_t ⋆ drm_pci_alloc( struct drm_device * dev, size_t size, size_t align )

Arguments
=========

``dev``
    DRM device

``size``
    size of block to allocate

``align``
    alignment of block


Return
======

A handle to the allocated memory block on success or NULL on failure.
