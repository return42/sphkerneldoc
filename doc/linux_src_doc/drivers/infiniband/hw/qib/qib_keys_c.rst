.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_keys.c

.. _`qib_alloc_lkey`:

qib_alloc_lkey
==============

.. c:function:: int qib_alloc_lkey(struct rvt_mregion *mr, int dma_region)

    allocate an lkey

    :param struct rvt_mregion \*mr:
        memory region that this lkey protects

    :param int dma_region:
        0->normal key, 1->restricted DMA key

.. _`qib_alloc_lkey.description`:

Description
-----------

Returns 0 if successful, otherwise returns -errno.

Increments mr reference count as required.

Sets the lkey field mr for non-dma regions.

.. _`qib_free_lkey`:

qib_free_lkey
=============

.. c:function:: void qib_free_lkey(struct rvt_mregion *mr)

    free an lkey

    :param struct rvt_mregion \*mr:
        mr to free from tables

.. _`qib_rkey_ok`:

qib_rkey_ok
===========

.. c:function:: int qib_rkey_ok(struct rvt_qp *qp, struct rvt_sge *sge, u32 len, u64 vaddr, u32 rkey, int acc)

    check the IB virtual address, length, and RKEY

    :param struct rvt_qp \*qp:
        qp for validation

    :param struct rvt_sge \*sge:
        SGE state

    :param u32 len:
        length of data

    :param u64 vaddr:
        virtual address to place data

    :param u32 rkey:
        rkey to check

    :param int acc:
        access flags

.. _`qib_rkey_ok.description`:

Description
-----------

Return 1 if successful, otherwise 0.

increments the reference count upon success

.. This file was automatic generated / don't edit.

