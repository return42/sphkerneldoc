.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/dma/coherent.c

.. _`dma_alloc_from_dev_coherent`:

dma_alloc_from_dev_coherent
===========================

.. c:function:: int dma_alloc_from_dev_coherent(struct device *dev, ssize_t size, dma_addr_t *dma_handle, void **ret)

    allocate memory from device coherent pool

    :param dev:
        device from which we allocate memory
    :type dev: struct device \*

    :param size:
        size of requested memory area
    :type size: ssize_t

    :param dma_handle:
        This will be filled with the correct dma handle
    :type dma_handle: dma_addr_t \*

    :param ret:
        This pointer will be filled with the virtual address
        to allocated area.
    :type ret: void \*\*

.. _`dma_alloc_from_dev_coherent.description`:

Description
-----------

This function should be only called from per-arch \ :c:func:`dma_alloc_coherent`\ 
to support allocation from per-device coherent memory pools.

Returns 0 if dma_alloc_coherent should continue with allocating from
generic memory areas, or !0 if dma_alloc_coherent should return \ ``ret``\ .

.. _`dma_release_from_dev_coherent`:

dma_release_from_dev_coherent
=============================

.. c:function:: int dma_release_from_dev_coherent(struct device *dev, int order, void *vaddr)

    free memory to device coherent memory pool

    :param dev:
        device from which the memory was allocated
    :type dev: struct device \*

    :param order:
        the order of pages allocated
    :type order: int

    :param vaddr:
        virtual address of allocated pages
    :type vaddr: void \*

.. _`dma_release_from_dev_coherent.description`:

Description
-----------

This checks whether the memory was allocated from the per-device
coherent memory pool and if so, releases that memory.

Returns 1 if we correctly released the memory, or 0 if the caller should
proceed with releasing memory from generic pools.

.. _`dma_mmap_from_dev_coherent`:

dma_mmap_from_dev_coherent
==========================

.. c:function:: int dma_mmap_from_dev_coherent(struct device *dev, struct vm_area_struct *vma, void *vaddr, size_t size, int *ret)

    mmap memory from the device coherent pool

    :param dev:
        device from which the memory was allocated
    :type dev: struct device \*

    :param vma:
        vm_area for the userspace memory
    :type vma: struct vm_area_struct \*

    :param vaddr:
        cpu address returned by dma_alloc_from_dev_coherent
    :type vaddr: void \*

    :param size:
        size of the memory buffer allocated
    :type size: size_t

    :param ret:
        result from \ :c:func:`remap_pfn_range`\ 
    :type ret: int \*

.. _`dma_mmap_from_dev_coherent.description`:

Description
-----------

This checks whether the memory was allocated from the per-device
coherent memory pool and if so, maps that memory to the provided vma.

Returns 1 if \ ``vaddr``\  belongs to the device coherent pool and the caller
should return \ ``ret``\ , or 0 if they should proceed with mapping memory from
generic areas.

.. This file was automatic generated / don't edit.

