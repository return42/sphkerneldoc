.. -*- coding: utf-8; mode: rst -*-

.. _API-vm-insert-page:

==============
vm_insert_page
==============

*man vm_insert_page(9)*

*4.6.0-rc5*

insert single page into user vma


Synopsis
========

.. c:function:: int vm_insert_page( struct vm_area_struct * vma, unsigned long addr, struct page * page )

Arguments
=========

``vma``
    user vma to map to

``addr``
    target user address of this page

``page``
    source kernel page


Description
===========

This allows drivers to insert individual pages they've allocated into a
user vma.

The page has to be a nice clean _individual_ kernel allocation. If you
allocate a compound page, you need to have marked it as such
(__GFP_COMP), or manually just split the page up yourself (see
``split_page``).

NOTE! Traditionally this was done with “``remap_pfn_range``” which took
an arbitrary page protection parameter. This doesn't allow that. Your
vma protection will have to be set up correctly, which means that if you
want a shared writable mapping, you'd better ask for a shared writable
mapping!

The page does not need to be reserved.

Usually this function is called from f_op-> ``mmap`` handler under
mm->mmap_sem write-lock, so it can change vma->vm_flags. Caller must
set VM_MIXEDMAP on vma if it wants to call this function from other
places, for example from page-fault handler.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
