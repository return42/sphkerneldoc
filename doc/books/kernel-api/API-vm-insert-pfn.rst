
.. _API-vm-insert-pfn:

=============
vm_insert_pfn
=============

*man vm_insert_pfn(9)*

*4.6.0-rc1*

insert single pfn into user vma


Synopsis
========

.. c:function:: int vm_insert_pfn( struct vm_area_struct * vma, unsigned long addr, unsigned long pfn )

Arguments
=========

``vma``
    user vma to map to

``addr``
    target user address of this page

``pfn``
    source kernel pfn


Description
===========

Similar to vm_insert_page, this allows drivers to insert individual pages they've allocated into a user vma. Same comments apply.

This function should only be called from a vm_ops->fault handler, and in that case the handler should return NULL.

vma cannot be a COW mapping.

As this is called only for pages that do not currently exist, we do not need to flush old virtual caches or the TLB.
