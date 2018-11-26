.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/mga/mga_dma.c

.. _`mga_do_agp_dma_bootstrap`:

mga_do_agp_dma_bootstrap
========================

.. c:function:: int mga_do_agp_dma_bootstrap(struct drm_device *dev, drm_mga_dma_bootstrap_t *dma_bs)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param dma_bs:
        *undescribed*
    :type dma_bs: drm_mga_dma_bootstrap_t \*

.. _`mga_do_agp_dma_bootstrap.description`:

Description
-----------

\todo
Investigate whether there is any benefit to storing the WARP microcode in
AGP memory.  If not, the microcode may as well always be put in PCI
memory.

\todo
This routine needs to set dma_bs->agp_mode to the mode actually configured
in the hardware.  Looking just at the Linux AGP driver code, I don't see
an easy way to determine this.

\sa mga_do_dma_bootstrap, mga_do_pci_dma_bootstrap

.. _`mga_do_pci_dma_bootstrap`:

mga_do_pci_dma_bootstrap
========================

.. c:function:: int mga_do_pci_dma_bootstrap(struct drm_device *dev, drm_mga_dma_bootstrap_t *dma_bs)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param dma_bs:
        *undescribed*
    :type dma_bs: drm_mga_dma_bootstrap_t \*

.. _`mga_do_pci_dma_bootstrap.description`:

Description
-----------

\todo
The algorithm for decreasing the size of the primary DMA buffer could be
better.  The size should be rounded up to the nearest page size, then
decrease the request size by a single page each pass through the loop.

\todo
Determine whether the maximum address passed to drm_pci_alloc is correct.
The same goes for drm_legacy_addbufs_pci.

\sa mga_do_dma_bootstrap, mga_do_agp_dma_bootstrap

.. _`mga_driver_unload`:

mga_driver_unload
=================

.. c:function:: void mga_driver_unload(struct drm_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. _`mga_driver_lastclose`:

mga_driver_lastclose
====================

.. c:function:: void mga_driver_lastclose(struct drm_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. This file was automatic generated / don't edit.

