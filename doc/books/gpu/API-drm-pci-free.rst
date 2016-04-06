
.. _API-drm-pci-free:

============
drm_pci_free
============

*man drm_pci_free(9)*

*4.6.0-rc1*

Free a PCI consistent memory block


Synopsis
========

.. c:function:: void drm_pci_free( struct drm_device * dev, drm_dma_handle_t * dmah )

Arguments
=========

``dev``
    DRM device

``dmah``
    handle to memory block
