.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/lib/usercopy_64.c

.. _`clean_cache_range`:

clean_cache_range
=================

.. c:function:: void clean_cache_range(void *addr, size_t size)

    write back a cache range with CLWB

    :param void \*addr:
        *undescribed*

    :param size_t size:
        number of bytes to write back

.. _`clean_cache_range.description`:

Description
-----------

Write back a cache range using the CLWB (cache line write back)
instruction. Note that \ ``size``\  is internally rounded up to be cache
line size aligned.

.. This file was automatic generated / don't edit.

