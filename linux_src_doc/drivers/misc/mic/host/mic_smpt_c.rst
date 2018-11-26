.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_smpt.c

.. _`mic_map`:

mic_map
=======

.. c:function:: dma_addr_t mic_map(struct mic_device *mdev, dma_addr_t dma_addr, size_t size)

    Maps a DMA address to a MIC physical address.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

    :param dma_addr:
        DMA address.
    :type dma_addr: dma_addr_t

    :param size:
        Size of the region to be mapped.
    :type size: size_t

.. _`mic_map.description`:

Description
-----------

This API converts the DMA address provided to a DMA address understood
by MIC. Caller should check for errors by calling mic_map_error(..).

returns DMA address as required by MIC.

.. _`mic_unmap`:

mic_unmap
=========

.. c:function:: void mic_unmap(struct mic_device *mdev, dma_addr_t mic_addr, size_t size)

    Unmaps a MIC physical address.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

    :param mic_addr:
        MIC physical address.
    :type mic_addr: dma_addr_t

    :param size:
        Size of the region to be unmapped.
    :type size: size_t

.. _`mic_unmap.description`:

Description
-----------

This API unmaps the mappings created by mic_map(..).

returns None.

.. _`mic_map_single`:

mic_map_single
==============

.. c:function:: dma_addr_t mic_map_single(struct mic_device *mdev, void *va, size_t size)

    Maps a virtual address to a MIC physical address.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

    :param va:
        Kernel direct mapped virtual address.
    :type va: void \*

    :param size:
        Size of the region to be mapped.
    :type size: size_t

.. _`mic_map_single.description`:

Description
-----------

This API calls pci_map_single(..) for the direct mapped virtual address
and then converts the DMA address provided to a DMA address understood
by MIC. Caller should check for errors by calling mic_map_error(..).

returns DMA address as required by MIC.

.. _`mic_unmap_single`:

mic_unmap_single
================

.. c:function:: void mic_unmap_single(struct mic_device *mdev, dma_addr_t mic_addr, size_t size)

    Unmaps a MIC physical address.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

    :param mic_addr:
        MIC physical address.
    :type mic_addr: dma_addr_t

    :param size:
        Size of the region to be unmapped.
    :type size: size_t

.. _`mic_unmap_single.description`:

Description
-----------

This API unmaps the mappings created by mic_map_single(..).

returns None.

.. _`mic_smpt_init`:

mic_smpt_init
=============

.. c:function:: int mic_smpt_init(struct mic_device *mdev)

    Initialize MIC System Memory Page Tables.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

.. _`mic_smpt_init.description`:

Description
-----------

returns 0 for success and -errno for error.

.. _`mic_smpt_uninit`:

mic_smpt_uninit
===============

.. c:function:: void mic_smpt_uninit(struct mic_device *mdev)

    UnInitialize MIC System Memory Page Tables.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

.. _`mic_smpt_uninit.description`:

Description
-----------

returns None.

.. _`mic_smpt_restore`:

mic_smpt_restore
================

.. c:function:: void mic_smpt_restore(struct mic_device *mdev)

    Restore MIC System Memory Page Tables.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

.. _`mic_smpt_restore.description`:

Description
-----------

Restore the SMPT registers to values previously stored in the
SW data structures. Some MIC steppings lose register state
across resets and this API should be called for performing
a restore operation if required.

returns None.

.. This file was automatic generated / don't edit.

