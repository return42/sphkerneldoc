.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma-mapping.h

.. _`dma_attr_write_barrier`:

DMA_ATTR_WRITE_BARRIER
======================

.. c:function::  DMA_ATTR_WRITE_BARRIER()

    of each attribute should be defined in Documentation/DMA-attributes.txt.

.. _`dma_attr_write_barrier.dma_attr_write_barrier`:

DMA_ATTR_WRITE_BARRIER
----------------------

DMA to a memory region with this attribute
forces all pending DMA writes to complete.

.. _`dma_mmap_attrs`:

dma_mmap_attrs
==============

.. c:function:: int dma_mmap_attrs(struct device *dev, struct vm_area_struct *vma, void *cpu_addr, dma_addr_t dma_addr, size_t size, unsigned long attrs)

    map a coherent DMA allocation into user space

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param vma:
        vm_area_struct describing requested user mapping
    :type vma: struct vm_area_struct \*

    :param cpu_addr:
        kernel CPU-view address returned from dma_alloc_attrs
    :type cpu_addr: void \*

    :param dma_addr:
        *undescribed*
    :type dma_addr: dma_addr_t

    :param size:
        size of memory originally requested in dma_alloc_attrs
    :type size: size_t

    :param attrs:
        attributes of mapping properties requested in dma_alloc_attrs
    :type attrs: unsigned long

.. _`dma_mmap_attrs.description`:

Description
-----------

Map a coherent DMA buffer previously allocated by dma_alloc_attrs
into user space.  The coherent DMA buffer must not be freed by the
driver until the user space mapping has been released.

.. This file was automatic generated / don't edit.

