
.. _API-remap-vmalloc-range:

===================
remap_vmalloc_range
===================

*man remap_vmalloc_range(9)*

*4.6.0-rc1*

map vmalloc pages to userspace


Synopsis
========

.. c:function:: int remap_vmalloc_range( struct vm_area_struct * vma, void * addr, unsigned long pgoff )

Arguments
=========

``vma``
    vma to cover (map full range of vma)

``addr``
    vmalloc memory

``pgoff``
    number of pages into addr before first page to map


Returns
=======

0 for success, -Exxx on failure

This function checks that addr is a valid vmalloc'ed area, and that it is big enough to cover the vma. Will return failure if that criteria isn't met.

Similar to ``remap_pfn_range`` (see mm/memory.c)
