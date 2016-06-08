.. -*- coding: utf-8; mode: rst -*-

.. _mm:

*****************
Memory Management
*****************


.. _sh4:

SH-4
====


.. _sq:

Store Queue API
---------------


.. kernel-doc:: arch/sh/kernel/cpu/sh4/sq.c
    :export:

.. _sh5:

SH-5
====


.. _tlb:

TLB Interfaces
--------------


.. kernel-doc:: arch/sh/mm/tlb-sh5.c
    :internal:

.. kernel-doc:: arch/sh/include/asm/tlb_64.h
    :internal:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
