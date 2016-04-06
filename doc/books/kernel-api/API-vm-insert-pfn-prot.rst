
.. _API-vm-insert-pfn-prot:

==================
vm_insert_pfn_prot
==================

*man vm_insert_pfn_prot(9)*

*4.6.0-rc1*

insert single pfn into user vma with specified pgprot


Synopsis
========

.. c:function:: int vm_insert_pfn_prot( struct vm_area_struct * vma, unsigned long addr, unsigned long pfn, pgprot_t pgprot )

Arguments
=========

``vma``
    user vma to map to

``addr``
    target user address of this page

``pfn``
    source kernel pfn

``pgprot``
    pgprot flags for the inserted page


Description
===========

This is exactly like vm_insert_pfn, except that it allows drivers to to override pgprot on a per-page basis.

This only makes sense for IO mappings, and it makes no sense for cow mappings. In general, using multiple vmas is preferable; vm_insert_pfn_prot should only be used if using
multiple VMAs is impractical.
