.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/mr.c

.. _`rvt_driver_mr_init`:

rvt_driver_mr_init
==================

.. c:function:: int rvt_driver_mr_init(struct rvt_dev_info *rdi)

    Init MR resources per driver

    :param struct rvt_dev_info \*rdi:
        rvt dev struct

.. _`rvt_driver_mr_init.description`:

Description
-----------

Do any intilization needed when a driver registers with rdmavt.

.. _`rvt_driver_mr_init.return`:

Return
------

0 on success or errno on failure

.. _`rvt_mr_exit`:

rvt_mr_exit
===========

.. c:function:: void rvt_mr_exit(struct rvt_dev_info *rdi)

    clean up MR \ ``rdi``\ : rvt dev structure

    :param struct rvt_dev_info \*rdi:
        *undescribed*

.. _`rvt_mr_exit.description`:

Description
-----------

called when drivers have unregistered or perhaps failed to register with us

.. _`rvt_alloc_lkey`:

rvt_alloc_lkey
==============

.. c:function:: int rvt_alloc_lkey(struct rvt_mregion *mr, int dma_region)

    allocate an lkey

    :param struct rvt_mregion \*mr:
        memory region that this lkey protects

    :param int dma_region:
        0->normal key, 1->restricted DMA key

.. _`rvt_alloc_lkey.description`:

Description
-----------

Returns 0 if successful, otherwise returns -errno.

Increments mr reference count as required.

Sets the lkey field mr for non-dma regions.

.. _`rvt_free_lkey`:

rvt_free_lkey
=============

.. c:function:: void rvt_free_lkey(struct rvt_mregion *mr)

    free an lkey

    :param struct rvt_mregion \*mr:
        mr to free from tables

.. _`rvt_get_dma_mr`:

rvt_get_dma_mr
==============

.. c:function:: struct ib_mr *rvt_get_dma_mr(struct ib_pd *pd, int acc)

    get a DMA memory region

    :param struct ib_pd \*pd:
        protection domain for this memory region

    :param int acc:
        access flags

.. _`rvt_get_dma_mr.return`:

Return
------

the memory region on success, otherwise returns an errno.
Note that all DMA addresses should be created via the
struct ib_dma_mapping_ops functions (see dma.c).

.. _`rvt_reg_user_mr`:

rvt_reg_user_mr
===============

.. c:function:: struct ib_mr *rvt_reg_user_mr(struct ib_pd *pd, u64 start, u64 length, u64 virt_addr, int mr_access_flags, struct ib_udata *udata)

    register a userspace memory region

    :param struct ib_pd \*pd:
        protection domain for this memory region

    :param u64 start:
        starting userspace address

    :param u64 length:
        length of region to register

    :param u64 virt_addr:
        *undescribed*

    :param int mr_access_flags:
        access flags for this memory region

    :param struct ib_udata \*udata:
        unused by the driver

.. _`rvt_reg_user_mr.return`:

Return
------

the memory region on success, otherwise returns an errno.

.. _`rvt_dereg_mr`:

rvt_dereg_mr
============

.. c:function:: int rvt_dereg_mr(struct ib_mr *ibmr)

    unregister and free a memory region

    :param struct ib_mr \*ibmr:
        the memory region to free

.. _`rvt_dereg_mr.description`:

Description
-----------


Note that this is called to free MRs created by \ :c:func:`rvt_get_dma_mr`\ 
or \ :c:func:`rvt_reg_user_mr`\ .

Returns 0 on success.

.. _`rvt_alloc_mr`:

rvt_alloc_mr
============

.. c:function:: struct ib_mr *rvt_alloc_mr(struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

    Allocate a memory region usable with the

    :param struct ib_pd \*pd:
        protection domain for this memory region

    :param enum ib_mr_type mr_type:
        mem region type

    :param u32 max_num_sg:
        Max number of segments allowed

.. _`rvt_alloc_mr.return`:

Return
------

the memory region on success, otherwise return an errno.

.. _`rvt_alloc_fmr`:

rvt_alloc_fmr
=============

.. c:function:: struct ib_fmr *rvt_alloc_fmr(struct ib_pd *pd, int mr_access_flags, struct ib_fmr_attr *fmr_attr)

    allocate a fast memory region

    :param struct ib_pd \*pd:
        the protection domain for this memory region

    :param int mr_access_flags:
        access flags for this memory region

    :param struct ib_fmr_attr \*fmr_attr:
        fast memory region attributes

.. _`rvt_alloc_fmr.return`:

Return
------

the memory region on success, otherwise returns an errno.

.. _`rvt_map_phys_fmr`:

rvt_map_phys_fmr
================

.. c:function:: int rvt_map_phys_fmr(struct ib_fmr *ibfmr, u64 *page_list, int list_len, u64 iova)

    set up a fast memory region

    :param struct ib_fmr \*ibfmr:
        *undescribed*

    :param u64 \*page_list:
        the list of pages to associate with the fast memory region

    :param int list_len:
        the number of pages to associate with the fast memory region

    :param u64 iova:
        the virtual address of the start of the fast memory region

.. _`rvt_map_phys_fmr.description`:

Description
-----------

This may be called from interrupt context.

.. _`rvt_map_phys_fmr.return`:

Return
------

0 on success

.. _`rvt_unmap_fmr`:

rvt_unmap_fmr
=============

.. c:function:: int rvt_unmap_fmr(struct list_head *fmr_list)

    unmap fast memory regions

    :param struct list_head \*fmr_list:
        the list of fast memory regions to unmap

.. _`rvt_unmap_fmr.return`:

Return
------

0 on success.

.. _`rvt_dealloc_fmr`:

rvt_dealloc_fmr
===============

.. c:function:: int rvt_dealloc_fmr(struct ib_fmr *ibfmr)

    deallocate a fast memory region

    :param struct ib_fmr \*ibfmr:
        the fast memory region to deallocate

.. _`rvt_dealloc_fmr.return`:

Return
------

0 on success.

.. _`rvt_lkey_ok`:

rvt_lkey_ok
===========

.. c:function:: int rvt_lkey_ok(struct rvt_lkey_table *rkt, struct rvt_pd *pd, struct rvt_sge *isge, struct ib_sge *sge, int acc)

    check IB SGE for validity and initialize

    :param struct rvt_lkey_table \*rkt:
        table containing lkey to check SGE against

    :param struct rvt_pd \*pd:
        protection domain

    :param struct rvt_sge \*isge:
        outgoing internal SGE

    :param struct ib_sge \*sge:
        SGE to check

    :param int acc:
        access flags

.. _`rvt_lkey_ok.description`:

Description
-----------

Check the IB SGE for validity and initialize our internal version
of it.

.. _`rvt_lkey_ok.return`:

Return
------

1 if valid and successful, otherwise returns 0.

increments the reference count upon success

.. _`rvt_rkey_ok`:

rvt_rkey_ok
===========

.. c:function:: int rvt_rkey_ok(struct rvt_qp *qp, struct rvt_sge *sge, u32 len, u64 vaddr, u32 rkey, int acc)

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

.. _`rvt_rkey_ok.return`:

Return
------

1 if successful, otherwise 0.

increments the reference count upon success

.. This file was automatic generated / don't edit.

