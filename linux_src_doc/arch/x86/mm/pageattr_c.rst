.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/pageattr.c

.. _`clflush_cache_range`:

clflush_cache_range
===================

.. c:function:: void clflush_cache_range(void *vaddr, unsigned int size)

    flush a cache range with clflush

    :param vaddr:
        virtual start address
    :type vaddr: void \*

    :param size:
        number of bytes to flush
    :type size: unsigned int

.. _`clflush_cache_range.description`:

Description
-----------

clflushopt is an unordered instruction which needs fencing with mfence or
sfence to avoid ordering issues.

.. This file was automatic generated / don't edit.

