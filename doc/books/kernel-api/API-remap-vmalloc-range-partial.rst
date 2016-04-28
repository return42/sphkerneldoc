.. -*- coding: utf-8; mode: rst -*-

.. _API-remap-vmalloc-range-partial:

===========================
remap_vmalloc_range_partial
===========================

*man remap_vmalloc_range_partial(9)*

*4.6.0-rc5*

map vmalloc pages to userspace


Synopsis
========

.. c:function:: int remap_vmalloc_range_partial( struct vm_area_struct * vma, unsigned long uaddr, void * kaddr, unsigned long size )

Arguments
=========

``vma``
    vma to cover

``uaddr``
    target user address to start at

``kaddr``
    virtual address of vmalloc kernel memory

``size``
    size of map area


Returns
=======

0 for success, -Exxx on failure

This function checks that ``kaddr`` is a valid vmalloc'ed area, and that
it is big enough to cover the range starting at ``uaddr`` in ``vma``.
Will return failure if that criteria isn't met.

Similar to ``remap_pfn_range`` (see mm/memory.c)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
