.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/dma/contiguous.c

.. _`dma_contiguous_reserve`:

dma_contiguous_reserve
======================

.. c:function:: void dma_contiguous_reserve(phys_addr_t limit)

    reserve area(s) for contiguous memory handling

    :param limit:
        End address of the reserved memory (optional, 0 for any).
    :type limit: phys_addr_t

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

    :param size:
        Size of the reserved area (in bytes),
    :type size: phys_addr_t

    :param base:
        Base address of the reserved area optional, use 0 for any
    :type base: phys_addr_t

    :param limit:
        End address of the reserved memory (optional, 0 for any).
    :type limit: phys_addr_t

    :param res_cma:
        Pointer to store the created cma region.
    :type res_cma: struct cma \*\*

    :param fixed:
        hint about where to place the reserved area
    :type fixed: bool

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

.. c:function:: struct page *dma_alloc_from_contiguous(struct device *dev, size_t count, unsigned int align, bool no_warn)

    allocate pages from contiguous area

    :param dev:
        Pointer to device for which the allocation is performed.
    :type dev: struct device \*

    :param count:
        Requested number of pages.
    :type count: size_t

    :param align:
        Requested alignment of pages (in PAGE_SIZE order).
    :type align: unsigned int

    :param no_warn:
        Avoid printing message about failed allocation.
    :type no_warn: bool

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

    :param dev:
        Pointer to device for which the pages were allocated.
    :type dev: struct device \*

    :param pages:
        Allocated pages.
    :type pages: struct page \*

    :param count:
        Number of allocated pages.
    :type count: int

.. _`dma_release_from_contiguous.description`:

Description
-----------

This function releases memory allocated by \ :c:func:`dma_alloc_from_contiguous`\ .
It returns false when provided pages do not belong to contiguous area and
true otherwise.

.. This file was automatic generated / don't edit.

