.. -*- coding: utf-8; mode: rst -*-

==========
pageattr.c
==========


.. _`clflush_cache_range`:

clflush_cache_range
===================

.. c:function:: void clflush_cache_range (void *vaddr, unsigned int size)

    flush a cache range with clflush

    :param void \*vaddr:
        virtual start address

    :param unsigned int size:
        number of bytes to flush



.. _`clflush_cache_range.description`:

Description
-----------

clflushopt is an unordered instruction which needs fencing with mfence or
sfence to avoid ordering issues.

