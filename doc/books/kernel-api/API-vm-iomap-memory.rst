
.. _API-vm-iomap-memory:

===============
vm_iomap_memory
===============

*man vm_iomap_memory(9)*

*4.6.0-rc1*

remap memory to userspace


Synopsis
========

.. c:function:: int vm_iomap_memory( struct vm_area_struct * vma, phys_addr_t start, unsigned long len )

Arguments
=========

``vma``
    user vma to map to

``start``
    start of area

``len``
    size of area


Description
===========

This is a simplified ``io_remap_pfn_range`` for common driver use. The driver just needs to give us the physical memory range to be mapped, we'll figure out the rest from the vma
information.

NOTE! Some drivers might want to tweak vma->vm_page_prot first to get whatever write-combining details or similar.
