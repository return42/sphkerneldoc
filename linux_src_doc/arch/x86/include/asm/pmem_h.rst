.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/pmem.h

.. _`arch_memcpy_to_pmem`:

arch_memcpy_to_pmem
===================

.. c:function:: void arch_memcpy_to_pmem(void *dst, const void *src, size_t n)

    copy data to persistent memory

    :param void \*dst:
        destination buffer for the copy

    :param const void \*src:
        source buffer for the copy

    :param size_t n:
        length of the copy in bytes

.. _`arch_memcpy_to_pmem.description`:

Description
-----------

Copy data to persistent memory media via non-temporal stores so that
a subsequent pmem driver flush operation will drain posted write queues.

.. _`arch_wb_cache_pmem`:

arch_wb_cache_pmem
==================

.. c:function:: void arch_wb_cache_pmem(void *addr, size_t size)

    write back a cache range with CLWB

    :param void \*addr:
        *undescribed*

    :param size_t size:
        number of bytes to write back

.. _`arch_wb_cache_pmem.description`:

Description
-----------

Write back a cache range using the CLWB (cache line write back)
instruction. Note that \ ``size``\  is internally rounded up to be cache
line size aligned.

.. _`arch_copy_from_iter_pmem`:

arch_copy_from_iter_pmem
========================

.. c:function:: size_t arch_copy_from_iter_pmem(void *addr, size_t bytes, struct iov_iter *i)

    copy data from an iterator to PMEM

    :param void \*addr:
        PMEM destination address

    :param size_t bytes:
        number of bytes to copy

    :param struct iov_iter \*i:
        iterator with source data

.. _`arch_copy_from_iter_pmem.description`:

Description
-----------

Copy data from the iterator 'i' to the PMEM buffer starting at 'addr'.

.. _`arch_clear_pmem`:

arch_clear_pmem
===============

.. c:function:: void arch_clear_pmem(void *addr, size_t size)

    zero a PMEM memory range

    :param void \*addr:
        virtual start address

    :param size_t size:
        number of bytes to zero

.. _`arch_clear_pmem.description`:

Description
-----------

Write zeros into the memory range starting at 'addr' for 'size' bytes.

.. This file was automatic generated / don't edit.

