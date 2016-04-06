
.. _API-remap-pfn-range:

===============
remap_pfn_range
===============

*man remap_pfn_range(9)*

*4.6.0-rc1*

remap kernel memory to userspace


Synopsis
========

.. c:function:: int remap_pfn_range( struct vm_area_struct * vma, unsigned long addr, unsigned long pfn, unsigned long size, pgprot_t prot )

Arguments
=========

``vma``
    user vma to map to

``addr``
    target user address to start at

``pfn``
    physical address of kernel memory

``size``
    size of map area

``prot``
    page protection flags for this mapping


Note
====

this is only safe if the mm semaphore is held when called.
