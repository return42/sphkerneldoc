.. -*- coding: utf-8; mode: rst -*-

.. _API-remap-vmalloc-range:

===================
remap_vmalloc_range
===================

*man remap_vmalloc_range(9)*

*4.6.0-rc5*

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

This function checks that addr is a valid vmalloc'ed area, and that it
is big enough to cover the vma. Will return failure if that criteria
isn't met.

Similar to ``remap_pfn_range`` (see mm/memory.c)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
