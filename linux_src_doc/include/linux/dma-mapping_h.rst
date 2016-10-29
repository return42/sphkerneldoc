.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma-mapping.h

.. _`dma_mmap_attrs`:

dma_mmap_attrs
==============

.. c:function:: int dma_mmap_attrs(struct device *dev, struct vm_area_struct *vma, void *cpu_addr, dma_addr_t dma_addr, size_t size, struct dma_attrs *attrs)

    map a coherent DMA allocation into user space

    :param struct device \*dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices

    :param struct vm_area_struct \*vma:
        vm_area_struct describing requested user mapping

    :param void \*cpu_addr:
        kernel CPU-view address returned from dma_alloc_attrs

    :param dma_addr_t dma_addr:
        *undescribed*

    :param size_t size:
        size of memory originally requested in dma_alloc_attrs

    :param struct dma_attrs \*attrs:
        attributes of mapping properties requested in dma_alloc_attrs

.. _`dma_mmap_attrs.description`:

Description
-----------

Map a coherent DMA buffer previously allocated by dma_alloc_attrs
into user space.  The coherent DMA buffer must not be freed by the
driver until the user space mapping has been released.

.. This file was automatic generated / don't edit.
