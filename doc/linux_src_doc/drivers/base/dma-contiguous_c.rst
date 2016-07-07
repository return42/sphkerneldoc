.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/dma-contiguous.c

.. _`dma_contiguous_reserve`:

dma_contiguous_reserve
======================

.. c:function:: void dma_contiguous_reserve(phys_addr_t limit)

    reserve area(s) for contiguous memory handling

    :param phys_addr_t limit:
        End address of the reserved memory (optional, 0 for any).

.. _`dma_contiguous_reserve.description`:

Description
-----------

This function reserves memory from early allocator. It should be
called by arch specific code once the early allocator (memblock or bootmem)
has been activated and all other subsystems have already allocated/reserved
memory.

.. _`dma_contiguous_reserve_area`:

dma_contiguous_reserve_area
===========================

.. c:function:: int dma_contiguous_reserve_area(phys_addr_t size, phys_addr_t base, phys_addr_t limit, struct cma **res_cma, bool fixed)

    reserve custom contiguous area

    :param phys_addr_t size:
        Size of the reserved area (in bytes),

    :param phys_addr_t base:
        Base address of the reserved area optional, use 0 for any

    :param phys_addr_t limit:
        End address of the reserved memory (optional, 0 for any).

    :param struct cma \*\*res_cma:
        Pointer to store the created cma region.

    :param bool fixed:
        hint about where to place the reserved area

.. _`dma_contiguous_reserve_area.description`:

Description
-----------

This function reserves memory from early allocator. It should be
called by arch specific code once the early allocator (memblock or bootmem)
has been activated and all other subsystems have already allocated/reserved
memory. This function allows to create custom reserved areas for specific
devices.

If \ ``fixed``\  is true, reserve contiguous area at exactly \ ``base``\ .  If false,
reserve in range from \ ``base``\  to \ ``limit``\ .

.. _`dma_alloc_from_contiguous`:

dma_alloc_from_contiguous
=========================

.. c:function:: struct page *dma_alloc_from_contiguous(struct device *dev, size_t count, unsigned int align)

    allocate pages from contiguous area

    :param struct device \*dev:
        Pointer to device for which the allocation is performed.

    :param size_t count:
        Requested number of pages.

    :param unsigned int align:
        Requested alignment of pages (in PAGE_SIZE order).

.. _`dma_alloc_from_contiguous.description`:

Description
-----------

This function allocates memory buffer for specified device. It uses
device specific contiguous memory area if available or the default
global one. Requires architecture specific \ :c:func:`dev_get_cma_area`\  helper
function.

.. _`dma_release_from_contiguous`:

dma_release_from_contiguous
===========================

.. c:function:: bool dma_release_from_contiguous(struct device *dev, struct page *pages, int count)

    release allocated pages

    :param struct device \*dev:
        Pointer to device for which the pages were allocated.

    :param struct page \*pages:
        Allocated pages.

    :param int count:
        Number of allocated pages.

.. _`dma_release_from_contiguous.description`:

Description
-----------

This function releases memory allocated by \ :c:func:`dma_alloc_from_contiguous`\ .
It returns false when provided pages do not belong to contiguous area and
true otherwise.

.. This file was automatic generated / don't edit.

