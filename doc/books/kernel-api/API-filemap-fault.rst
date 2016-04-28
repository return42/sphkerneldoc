.. -*- coding: utf-8; mode: rst -*-

.. _API-filemap-fault:

=============
filemap_fault
=============

*man filemap_fault(9)*

*4.6.0-rc5*

read in file data for page fault handling


Synopsis
========

.. c:function:: int filemap_fault( struct vm_area_struct * vma, struct vm_fault * vmf )

Arguments
=========

``vma``
    vma in which the fault was taken

``vmf``
    struct vm_fault containing details of the fault


Description
===========

``filemap_fault`` is invoked via the vma operations vector for a mapped
memory region to read in file data during a page fault.

The goto's are kind of ugly, but this streamlines the normal case of
having it in the page cache, and handles the special cases reasonably
without having a lot of duplicated code.

vma->vm_mm->mmap_sem must be held on entry.

If our return value has VM_FAULT_RETRY set, it's because
``lock_page_or_retry`` returned 0. The mmap_sem has usually been
released in this case. See ``__lock_page_or_retry`` for the exception.

If our return value does not have VM_FAULT_RETRY set, the mmap_sem
has not been released.

We never return with VM_FAULT_RETRY and a bit from VM_FAULT_ERROR
set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
