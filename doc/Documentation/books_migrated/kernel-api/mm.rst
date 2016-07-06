.. -*- coding: utf-8; mode: rst -*-

.. _mm:

**************************
Memory Management in Linux
**************************


The Slab Cache
==============


.. kernel-doc:: include/linux/slab.h
    :man-sect: 9
    :internal:


.. kernel-doc:: mm/slab.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/util.c
    :man-sect: 9
    :export:


User Space Memory Access
========================


.. kernel-doc:: arch/x86/include/asm/uaccess_32.h
    :man-sect: 9
    :internal:


.. kernel-doc:: arch/x86/lib/usercopy_32.c
    :man-sect: 9
    :export:


More Memory Management Functions
================================


.. kernel-doc:: mm/readahead.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/filemap.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/memory.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/vmalloc.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/page_alloc.c
    :man-sect: 9
    :internal:


.. kernel-doc:: mm/mempool.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/dmapool.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/page-writeback.c
    :man-sect: 9
    :export:


.. kernel-doc:: mm/truncate.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
