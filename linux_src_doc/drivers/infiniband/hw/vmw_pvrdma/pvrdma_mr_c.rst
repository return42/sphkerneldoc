.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_mr.c

.. _`pvrdma_get_dma_mr`:

pvrdma_get_dma_mr
=================

.. c:function:: struct ib_mr *pvrdma_get_dma_mr(struct ib_pd *pd, int acc)

    get a DMA memory region

    :param pd:
        protection domain
    :type pd: struct ib_pd \*

    :param acc:
        access flags
    :type acc: int

.. _`pvrdma_reg_user_mr`:

pvrdma_reg_user_mr
==================

.. c:function:: struct ib_mr *pvrdma_reg_user_mr(struct ib_pd *pd, u64 start, u64 length, u64 virt_addr, int access_flags, struct ib_udata *udata)

    register a userspace memory region

    :param pd:
        protection domain
    :type pd: struct ib_pd \*

    :param start:
        starting address
    :type start: u64

    :param length:
        length of region
    :type length: u64

    :param virt_addr:
        I/O virtual address
    :type virt_addr: u64

    :param access_flags:
        access flags for memory region
    :type access_flags: int

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_alloc_mr`:

pvrdma_alloc_mr
===============

.. c:function:: struct ib_mr *pvrdma_alloc_mr(struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

    allocate a memory region

    :param pd:
        protection domain
    :type pd: struct ib_pd \*

    :param mr_type:
        type of memory region
    :type mr_type: enum ib_mr_type

    :param max_num_sg:
        maximum number of pages
    :type max_num_sg: u32

.. _`pvrdma_dereg_mr`:

pvrdma_dereg_mr
===============

.. c:function:: int pvrdma_dereg_mr(struct ib_mr *ibmr)

    deregister a memory region

    :param ibmr:
        memory region
    :type ibmr: struct ib_mr \*

.. This file was automatic generated / don't edit.

