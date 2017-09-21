.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/dma-coherent.c

.. _`dma_alloc_from_dev_coherent`:

dma_alloc_from_dev_coherent
===========================

.. c:function:: int dma_alloc_from_dev_coherent(struct device *dev, ssize_t size, dma_addr_t *dma_handle, void **ret)

    allocate memory from device coherent pool

    :param struct device \*dev:
        device from which we allocate memory

    :param ssize_t size:
        size of requested memory area

    :param dma_addr_t \*dma_handle:
        This will be filled with the correct dma handle

    :param void \*\*ret:
        This pointer will be filled with the virtual address
        to allocated area.

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

    :param struct device \*dev:
        device from which the memory was allocated

    :param int order:
        the order of pages allocated

    :param void \*vaddr:
        virtual address of allocated pages

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

    :param struct device \*dev:
        device from which the memory was allocated

    :param struct vm_area_struct \*vma:
        vm_area for the userspace memory

    :param void \*vaddr:
        cpu address returned by dma_alloc_from_dev_coherent

    :param size_t size:
        size of the memory buffer allocated

    :param int \*ret:
        result from \ :c:func:`remap_pfn_range`\ 

.. _`dma_mmap_from_dev_coherent.description`:

Description
-----------

This checks whether the memory was allocated from the per-device
coherent memory pool and if so, maps that memory to the provided vma.

Returns 1 if we correctly mapped the memory, or 0 if the caller should
proceed with mapping memory from generic pools.

.. This file was automatic generated / don't edit.

