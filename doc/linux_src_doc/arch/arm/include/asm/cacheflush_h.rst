.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/cacheflush.h

.. _`secure_flush_area`:

secure_flush_area
=================

.. c:function:: void secure_flush_area(const void *addr, size_t size)

    ensure coherency across the secure boundary

    :param const void \*addr:
        virtual address

    :param size_t size:
        size of region

.. _`secure_flush_area.description`:

Description
-----------

Ensure that the specified area of memory is coherent across the secure
boundary from the non-secure side.  This is used when calling secure
firmware where the secure firmware does not ensure coherency.

.. This file was automatic generated / don't edit.

