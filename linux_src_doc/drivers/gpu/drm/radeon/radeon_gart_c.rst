.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_gart.c

.. _`radeon_gart_table_ram_alloc`:

radeon_gart_table_ram_alloc
===========================

.. c:function:: int radeon_gart_table_ram_alloc(struct radeon_device *rdev)

    allocate system ram for gart page table

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_table_ram_alloc.description`:

Description
-----------

Allocate system memory for GART page table
(r1xx-r3xx, non-pcie r4xx, rs400).  These asics require the
gart table to be in system memory.
Returns 0 for success, -ENOMEM for failure.

.. _`radeon_gart_table_ram_free`:

radeon_gart_table_ram_free
==========================

.. c:function:: void radeon_gart_table_ram_free(struct radeon_device *rdev)

    free system ram for gart page table

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_table_ram_free.description`:

Description
-----------

Free system memory for GART page table
(r1xx-r3xx, non-pcie r4xx, rs400).  These asics require the
gart table to be in system memory.

.. _`radeon_gart_table_vram_alloc`:

radeon_gart_table_vram_alloc
============================

.. c:function:: int radeon_gart_table_vram_alloc(struct radeon_device *rdev)

    allocate vram for gart page table

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_table_vram_alloc.description`:

Description
-----------

Allocate video memory for GART page table
(pcie r4xx, r5xx+).  These asics require the
gart table to be in video memory.
Returns 0 for success, error for failure.

.. _`radeon_gart_table_vram_pin`:

radeon_gart_table_vram_pin
==========================

.. c:function:: int radeon_gart_table_vram_pin(struct radeon_device *rdev)

    pin gart page table in vram

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_table_vram_pin.description`:

Description
-----------

Pin the GART page table in vram so it will not be moved
by the memory manager (pcie r4xx, r5xx+).  These asics require the
gart table to be in video memory.
Returns 0 for success, error for failure.

.. _`radeon_gart_table_vram_unpin`:

radeon_gart_table_vram_unpin
============================

.. c:function:: void radeon_gart_table_vram_unpin(struct radeon_device *rdev)

    unpin gart page table in vram

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_table_vram_unpin.description`:

Description
-----------

Unpin the GART page table in vram (pcie r4xx, r5xx+).
These asics require the gart table to be in video memory.

.. _`radeon_gart_table_vram_free`:

radeon_gart_table_vram_free
===========================

.. c:function:: void radeon_gart_table_vram_free(struct radeon_device *rdev)

    free gart page table vram

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_table_vram_free.description`:

Description
-----------

Free the video memory used for the GART page table
(pcie r4xx, r5xx+).  These asics require the gart table to
be in video memory.

.. _`radeon_gart_unbind`:

radeon_gart_unbind
==================

.. c:function:: void radeon_gart_unbind(struct radeon_device *rdev, unsigned offset, int pages)

    unbind pages from the gart page table

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param offset:
        offset into the GPU's gart aperture
    :type offset: unsigned

    :param pages:
        number of pages to unbind
    :type pages: int

.. _`radeon_gart_unbind.description`:

Description
-----------

Unbinds the requested pages from the gart page table and
replaces them with the dummy page (all asics).

.. _`radeon_gart_bind`:

radeon_gart_bind
================

.. c:function:: int radeon_gart_bind(struct radeon_device *rdev, unsigned offset, int pages, struct page **pagelist, dma_addr_t *dma_addr, uint32_t flags)

    bind pages into the gart page table

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param offset:
        offset into the GPU's gart aperture
    :type offset: unsigned

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
        RADEON_GART_PAGE\_\* flags
    :type flags: uint32_t

.. _`radeon_gart_bind.description`:

Description
-----------

Binds the requested pages to the gart page table
(all asics).
Returns 0 for success, -EINVAL for failure.

.. _`radeon_gart_init`:

radeon_gart_init
================

.. c:function:: int radeon_gart_init(struct radeon_device *rdev)

    init the driver info for managing the gart

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_init.description`:

Description
-----------

Allocate the dummy page and init the gart driver info (all asics).
Returns 0 for success, error for failure.

.. _`radeon_gart_fini`:

radeon_gart_fini
================

.. c:function:: void radeon_gart_fini(struct radeon_device *rdev)

    tear down the driver info for managing the gart

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gart_fini.description`:

Description
-----------

Tear down the gart driver info and free the dummy page (all asics).

.. This file was automatic generated / don't edit.

