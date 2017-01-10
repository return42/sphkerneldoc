.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_mr.c

.. _`pvrdma_get_dma_mr`:

pvrdma_get_dma_mr
=================

.. c:function:: struct ib_mr *pvrdma_get_dma_mr(struct ib_pd *pd, int acc)

    get a DMA memory region

    :param struct ib_pd \*pd:
        protection domain

    :param int acc:
        access flags

.. _`pvrdma_reg_user_mr`:

pvrdma_reg_user_mr
==================

.. c:function:: struct ib_mr *pvrdma_reg_user_mr(struct ib_pd *pd, u64 start, u64 length, u64 virt_addr, int access_flags, struct ib_udata *udata)

    register a userspace memory region

    :param struct ib_pd \*pd:
        protection domain

    :param u64 start:
        starting address

    :param u64 length:
        length of region

    :param u64 virt_addr:
        I/O virtual address

    :param int access_flags:
        access flags for memory region

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_alloc_mr`:

pvrdma_alloc_mr
===============

.. c:function:: struct ib_mr *pvrdma_alloc_mr(struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

    allocate a memory region

    :param struct ib_pd \*pd:
        protection domain

    :param enum ib_mr_type mr_type:
        type of memory region

    :param u32 max_num_sg:
        maximum number of pages

.. _`pvrdma_dereg_mr`:

pvrdma_dereg_mr
===============

.. c:function:: int pvrdma_dereg_mr(struct ib_mr *ibmr)

    deregister a memory region

    :param struct ib_mr \*ibmr:
        memory region

.. This file was automatic generated / don't edit.

