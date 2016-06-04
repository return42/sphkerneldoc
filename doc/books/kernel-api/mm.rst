.. -*- coding: utf-8; mode: rst -*-

.. _mm:

==========================
Memory Management in Linux
==========================


The Slab Cache
==============


.. kernel-doc:: include/linux/slab.h
    :internal:

.. kernel-doc:: mm/slab.c
    :export:

.. kernel-doc:: mm/util.c
    :export:

User Space Memory Access
========================


.. kernel-doc:: arch/x86/include/asm/uaccess_32.h
    :internal:

.. kernel-doc:: arch/x86/lib/usercopy_32.c
    :export:

More Memory Management Functions
================================


.. kernel-doc:: mm/readahead.c
    :export:

.. kernel-doc:: mm/filemap.c
    :export:

.. kernel-doc:: mm/memory.c
    :export:

.. kernel-doc:: mm/vmalloc.c
    :export:

.. kernel-doc:: mm/page_alloc.c
    :internal:

.. kernel-doc:: mm/mempool.c
    :export:

.. kernel-doc:: mm/dmapool.c
    :export:

.. kernel-doc:: mm/page-writeback.c
    :export:

.. kernel-doc:: mm/truncate.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
