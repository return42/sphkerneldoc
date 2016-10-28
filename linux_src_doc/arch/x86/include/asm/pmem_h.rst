.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/pmem.h

.. _`arch_memcpy_to_pmem`:

arch_memcpy_to_pmem
===================

.. c:function:: void arch_memcpy_to_pmem(void __pmem *dst, const void *src, size_t n)

    copy data to persistent memory

    :param void __pmem \*dst:
        destination buffer for the copy

    :param const void \*src:
        source buffer for the copy

    :param size_t n:
        length of the copy in bytes

.. _`arch_memcpy_to_pmem.description`:

Description
-----------

Copy data to persistent memory media via non-temporal stores so that
a subsequent \ :c:func:`arch_wmb_pmem`\  can flush cpu and memory controller
write buffers to guarantee durability.

.. _`arch_wmb_pmem`:

arch_wmb_pmem
=============

.. c:function:: void arch_wmb_pmem( void)

    synchronize writes to persistent memory

    :param  void:
        no arguments

.. _`arch_wmb_pmem.description`:

Description
-----------

After a series of \ :c:func:`arch_memcpy_to_pmem`\  operations this drains data
from cpu write buffers and any platform (memory controller) buffers
to ensure that written data is durable on persistent memory media.

.. _`arch_wb_cache_pmem`:

arch_wb_cache_pmem
==================

.. c:function:: void arch_wb_cache_pmem(void __pmem *addr, size_t size)

    write back a cache range with CLWB

    :param void __pmem \*addr:
        *undescribed*

    :param size_t size:
        number of bytes to write back

.. _`arch_wb_cache_pmem.description`:

Description
-----------

Write back a cache range using the CLWB (cache line write back)
instruction.  This function requires explicit ordering with an
\ :c:func:`arch_wmb_pmem`\  call.

.. _`arch_copy_from_iter_pmem`:

arch_copy_from_iter_pmem
========================

.. c:function:: size_t arch_copy_from_iter_pmem(void __pmem *addr, size_t bytes, struct iov_iter *i)

    copy data from an iterator to PMEM

    :param void __pmem \*addr:
        PMEM destination address

    :param size_t bytes:
        number of bytes to copy

    :param struct iov_iter \*i:
        iterator with source data

.. _`arch_copy_from_iter_pmem.description`:

Description
-----------

Copy data from the iterator 'i' to the PMEM buffer starting at 'addr'.
This function requires explicit ordering with an \ :c:func:`arch_wmb_pmem`\  call.

.. _`arch_clear_pmem`:

arch_clear_pmem
===============

.. c:function:: void arch_clear_pmem(void __pmem *addr, size_t size)

    zero a PMEM memory range

    :param void __pmem \*addr:
        virtual start address

    :param size_t size:
        number of bytes to zero

.. _`arch_clear_pmem.description`:

Description
-----------

Write zeros into the memory range starting at 'addr' for 'size' bytes.
This function requires explicit ordering with an \ :c:func:`arch_wmb_pmem`\  call.

.. This file was automatic generated / don't edit.

