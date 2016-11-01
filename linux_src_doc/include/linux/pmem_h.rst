.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pmem.h

.. _`memcpy_to_pmem`:

memcpy_to_pmem
==============

.. c:function:: void memcpy_to_pmem(void *dst, const void *src, size_t n)

    copy data to persistent memory

    :param void \*dst:
        destination buffer for the copy

    :param const void \*src:
        source buffer for the copy

    :param size_t n:
        length of the copy in bytes

.. _`memcpy_to_pmem.description`:

Description
-----------

Perform a memory copy that results in the destination of the copy
being effectively evicted from, or never written to, the processor
cache hierarchy after the copy completes.  After \ :c:func:`memcpy_to_pmem`\ 
data may still reside in cpu or platform buffers, so this operation
must be followed by a \ :c:func:`blkdev_issue_flush`\  on the pmem block device.

.. _`copy_from_iter_pmem`:

copy_from_iter_pmem
===================

.. c:function:: size_t copy_from_iter_pmem(void *addr, size_t bytes, struct iov_iter *i)

    copy data from an iterator to PMEM

    :param void \*addr:
        PMEM destination address

    :param size_t bytes:
        number of bytes to copy

    :param struct iov_iter \*i:
        iterator with source data

.. _`copy_from_iter_pmem.description`:

Description
-----------

Copy data from the iterator 'i' to the PMEM buffer starting at 'addr'.
See \ :c:func:`blkdev_issue_flush`\  note for \ :c:func:`memcpy_to_pmem`\ .

.. _`clear_pmem`:

clear_pmem
==========

.. c:function:: void clear_pmem(void *addr, size_t size)

    zero a PMEM memory range

    :param void \*addr:
        virtual start address

    :param size_t size:
        number of bytes to zero

.. _`clear_pmem.description`:

Description
-----------

Write zeros into the memory range starting at 'addr' for 'size' bytes.
See \ :c:func:`blkdev_issue_flush`\  note for \ :c:func:`memcpy_to_pmem`\ .

.. _`invalidate_pmem`:

invalidate_pmem
===============

.. c:function:: void invalidate_pmem(void *addr, size_t size)

    flush a pmem range from the cache hierarchy

    :param void \*addr:
        virtual start address

    :param size_t size:
        bytes to invalidate (internally aligned to cache line size)

.. _`invalidate_pmem.description`:

Description
-----------

For platforms that support clearing poison this flushes any poisoned
ranges out of the cache

.. _`wb_cache_pmem`:

wb_cache_pmem
=============

.. c:function:: void wb_cache_pmem(void *addr, size_t size)

    write back processor cache for PMEM memory range

    :param void \*addr:
        virtual start address

    :param size_t size:
        number of bytes to write back

.. _`wb_cache_pmem.description`:

Description
-----------

Write back the processor cache range starting at 'addr' for 'size' bytes.
See \ :c:func:`blkdev_issue_flush`\  note for \ :c:func:`memcpy_to_pmem`\ .

.. This file was automatic generated / don't edit.

