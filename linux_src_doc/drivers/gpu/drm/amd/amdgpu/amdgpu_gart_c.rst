.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_gart.c

.. _`amdgpu_gart_dummy_page_init`:

amdgpu_gart_dummy_page_init
===========================

.. c:function:: int amdgpu_gart_dummy_page_init(struct amdgpu_device *adev)

    init dummy page used by the driver

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_dummy_page_init.description`:

Description
-----------

Allocate the dummy page used by the driver (all asics).
This dummy page is used by the driver as a filler for gart entries
when pages are taken out of the GART
Returns 0 on sucess, -ENOMEM on failure.

.. _`amdgpu_gart_dummy_page_fini`:

amdgpu_gart_dummy_page_fini
===========================

.. c:function:: void amdgpu_gart_dummy_page_fini(struct amdgpu_device *adev)

    free dummy page used by the driver

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_dummy_page_fini.description`:

Description
-----------

Frees the dummy page used by the driver (all asics).

.. _`amdgpu_gart_table_vram_alloc`:

amdgpu_gart_table_vram_alloc
============================

.. c:function:: int amdgpu_gart_table_vram_alloc(struct amdgpu_device *adev)

    allocate vram for gart page table

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_table_vram_alloc.description`:

Description
-----------

Allocate video memory for GART page table
(pcie r4xx, r5xx+).  These asics require the
gart table to be in video memory.
Returns 0 for success, error for failure.

.. _`amdgpu_gart_table_vram_pin`:

amdgpu_gart_table_vram_pin
==========================

.. c:function:: int amdgpu_gart_table_vram_pin(struct amdgpu_device *adev)

    pin gart page table in vram

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_table_vram_pin.description`:

Description
-----------

Pin the GART page table in vram so it will not be moved
by the memory manager (pcie r4xx, r5xx+).  These asics require the
gart table to be in video memory.
Returns 0 for success, error for failure.

.. _`amdgpu_gart_table_vram_unpin`:

amdgpu_gart_table_vram_unpin
============================

.. c:function:: void amdgpu_gart_table_vram_unpin(struct amdgpu_device *adev)

    unpin gart page table in vram

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_table_vram_unpin.description`:

Description
-----------

Unpin the GART page table in vram (pcie r4xx, r5xx+).
These asics require the gart table to be in video memory.

.. _`amdgpu_gart_table_vram_free`:

amdgpu_gart_table_vram_free
===========================

.. c:function:: void amdgpu_gart_table_vram_free(struct amdgpu_device *adev)

    free gart page table vram

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_table_vram_free.description`:

Description
-----------

Free the video memory used for the GART page table
(pcie r4xx, r5xx+).  These asics require the gart table to
be in video memory.

.. _`amdgpu_gart_unbind`:

amdgpu_gart_unbind
==================

.. c:function:: int amdgpu_gart_unbind(struct amdgpu_device *adev, uint64_t offset, int pages)

    unbind pages from the gart page table

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param offset:
        offset into the GPU's gart aperture
    :type offset: uint64_t

    :param pages:
        number of pages to unbind
    :type pages: int

.. _`amdgpu_gart_unbind.description`:

Description
-----------

Unbinds the requested pages from the gart page table and
replaces them with the dummy page (all asics).
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_gart_map`:

amdgpu_gart_map
===============

.. c:function:: int amdgpu_gart_map(struct amdgpu_device *adev, uint64_t offset, int pages, dma_addr_t *dma_addr, uint64_t flags, void *dst)

    map dma_addresses into GART entries

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param offset:
        offset into the GPU's gart aperture
    :type offset: uint64_t

    :param pages:
        number of pages to bind
    :type pages: int

    :param dma_addr:
        DMA addresses of pages
    :type dma_addr: dma_addr_t \*

    :param flags:
        *undescribed*
    :type flags: uint64_t

    :param dst:
        *undescribed*
    :type dst: void \*

.. _`amdgpu_gart_map.description`:

Description
-----------

Map the dma_addresses into GART entries (all asics).
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_gart_bind`:

amdgpu_gart_bind
================

.. c:function:: int amdgpu_gart_bind(struct amdgpu_device *adev, uint64_t offset, int pages, struct page **pagelist, dma_addr_t *dma_addr, uint64_t flags)

    bind pages into the gart page table

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param offset:
        offset into the GPU's gart aperture
    :type offset: uint64_t

    :param pages:
        number of pages to bind
    :type pages: int

    :param pagelist:
        pages to bind
    :type pagelist: struct page \*\*

    :param dma_addr:
        DMA addresses of pages
    :type dma_addr: dma_addr_t \*

    :param flags:
        *undescribed*
    :type flags: uint64_t

.. _`amdgpu_gart_bind.description`:

Description
-----------

Binds the requested pages to the gart page table
(all asics).
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_gart_init`:

amdgpu_gart_init
================

.. c:function:: int amdgpu_gart_init(struct amdgpu_device *adev)

    init the driver info for managing the gart

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_init.description`:

Description
-----------

Allocate the dummy page and init the gart driver info (all asics).
Returns 0 for success, error for failure.

.. _`amdgpu_gart_fini`:

amdgpu_gart_fini
================

.. c:function:: void amdgpu_gart_fini(struct amdgpu_device *adev)

    tear down the driver info for managing the gart

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_gart_fini.description`:

Description
-----------

Tear down the gart driver info and free the dummy page (all asics).

.. This file was automatic generated / don't edit.

