.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/cma.c

.. _`cma_init_reserved_mem`:

cma_init_reserved_mem
=====================

.. c:function:: int cma_init_reserved_mem(phys_addr_t base, phys_addr_t size, unsigned int order_per_bit, const char *name, struct cma **res_cma)

    create custom contiguous area from reserved memory

    :param phys_addr_t base:
        Base address of the reserved area

    :param phys_addr_t size:
        Size of the reserved area (in bytes),

    :param unsigned int order_per_bit:
        Order of pages represented by one bit on bitmap.

    :param const char \*name:
        The name of the area. If this parameter is NULL, the name of
        the area will be set to "cmaN", where N is a running counter of
        used areas.

    :param struct cma \*\*res_cma:
        Pointer to store the created cma region.

.. _`cma_init_reserved_mem.description`:

Description
-----------

This function creates custom contiguous area from already reserved memory.

.. _`cma_declare_contiguous`:

cma_declare_contiguous
======================

.. c:function:: int cma_declare_contiguous(phys_addr_t base, phys_addr_t size, phys_addr_t limit, phys_addr_t alignment, unsigned int order_per_bit, bool fixed, const char *name, struct cma **res_cma)

    reserve custom contiguous area

    :param phys_addr_t base:
        Base address of the reserved area optional, use 0 for any

    :param phys_addr_t size:
        Size of the reserved area (in bytes),

    :param phys_addr_t limit:
        End address of the reserved memory (optional, 0 for any).

    :param phys_addr_t alignment:
        Alignment for the CMA area, should be power of 2 or zero

    :param unsigned int order_per_bit:
        Order of pages represented by one bit on bitmap.

    :param bool fixed:
        hint about where to place the reserved area

    :param const char \*name:
        The name of the area. See function \ :c:func:`cma_init_reserved_mem`\ 

    :param struct cma \*\*res_cma:
        Pointer to store the created cma region.

.. _`cma_declare_contiguous.description`:

Description
-----------

This function reserves memory from early allocator. It should be
called by arch specific code once the early allocator (memblock or bootmem)
has been activated and all other subsystems have already allocated/reserved
memory. This function allows to create custom reserved areas.

If \ ``fixed``\  is true, reserve contiguous area at exactly \ ``base``\ .  If false,
reserve in range from \ ``base``\  to \ ``limit``\ .

.. _`cma_alloc`:

cma_alloc
=========

.. c:function:: struct page *cma_alloc(struct cma *cma, size_t count, unsigned int align, gfp_t gfp_mask)

    allocate pages from contiguous area

    :param struct cma \*cma:
        Contiguous memory region for which the allocation is performed.

    :param size_t count:
        Requested number of pages.

    :param unsigned int align:
        Requested alignment of pages (in PAGE_SIZE order).

    :param gfp_t gfp_mask:
        GFP mask to use during compaction

.. _`cma_alloc.description`:

Description
-----------

This function allocates part of contiguous memory on specific
contiguous memory area.

.. _`cma_release`:

cma_release
===========

.. c:function:: bool cma_release(struct cma *cma, const struct page *pages, unsigned int count)

    release allocated pages

    :param struct cma \*cma:
        Contiguous memory region for which the allocation is performed.

    :param const struct page \*pages:
        Allocated pages.

    :param unsigned int count:
        Number of allocated pages.

.. _`cma_release.description`:

Description
-----------

This function releases memory allocated by \ :c:func:`alloc_cma`\ .
It returns false when provided pages do not belong to contiguous area and
true otherwise.

.. This file was automatic generated / don't edit.

