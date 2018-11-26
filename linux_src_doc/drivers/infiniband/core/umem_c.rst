.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/umem.c

.. _`ib_umem_get`:

ib_umem_get
===========

.. c:function:: struct ib_umem *ib_umem_get(struct ib_ucontext *context, unsigned long addr, size_t size, int access, int dmasync)

    Pin and DMA map userspace memory.

    :param context:
        userspace context to pin memory for
    :type context: struct ib_ucontext \*

    :param addr:
        userspace virtual address to start at
    :type addr: unsigned long

    :param size:
        length of region to pin
    :type size: size_t

    :param access:
        IB_ACCESS_xxx flags for memory being pinned
    :type access: int

    :param dmasync:
        flush in-flight DMA when the memory region is written
    :type dmasync: int

.. _`ib_umem_get.description`:

Description
-----------

If access flags indicate ODP memory, avoid pinning. Instead, stores
the mm for future page fault handling in conjunction with MMU notifiers.

.. _`ib_umem_release`:

ib_umem_release
===============

.. c:function:: void ib_umem_release(struct ib_umem *umem)

    release memory pinned with ib_umem_get

    :param umem:
        umem struct to release
    :type umem: struct ib_umem \*

.. This file was automatic generated / don't edit.

