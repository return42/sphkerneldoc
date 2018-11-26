.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_mm.c

.. _`remap_io_mapping`:

remap_io_mapping
================

.. c:function:: int remap_io_mapping(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn, unsigned long size, struct io_mapping *iomap)

    remap an IO mapping to userspace

    :param vma:
        user vma to map to
    :type vma: struct vm_area_struct \*

    :param addr:
        target user address to start at
    :type addr: unsigned long

    :param pfn:
        physical address of kernel memory
    :type pfn: unsigned long

    :param size:
        size of map area
    :type size: unsigned long

    :param iomap:
        the source io_mapping
    :type iomap: struct io_mapping \*

.. _`remap_io_mapping.note`:

Note
----

this is only safe if the mm semaphore is held when called.

.. This file was automatic generated / don't edit.

