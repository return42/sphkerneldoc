.. -*- coding: utf-8; mode: rst -*-

.. _API-remap-pfn-range:

===============
remap_pfn_range
===============

*man remap_pfn_range(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
