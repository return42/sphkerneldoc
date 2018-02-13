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
Note that all DMA addresses should be created via the functions in
struct dma_virt_ops.

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

.. _`rvt_dereg_clean_qp_cb`:

rvt_dereg_clean_qp_cb
=====================

.. c:function:: void rvt_dereg_clean_qp_cb(struct rvt_qp *qp, u64 v)

    callback from iterator \ ``qp``\  - the qp \ ``v``\  - the mregion (as u64)

    :param struct rvt_qp \*qp:
        *undescribed*

    :param u64 v:
        *undescribed*

.. _`rvt_dereg_clean_qp_cb.description`:

Description
-----------

This routine fields the callback for all QPs and
for QPs in the same PD as the MR will call the
\ :c:func:`rvt_qp_mr_clean`\  to potentially cleanup references.

.. _`rvt_dereg_clean_qps`:

rvt_dereg_clean_qps
===================

.. c:function:: void rvt_dereg_clean_qps(struct rvt_mregion *mr)

    find QPs for reference cleanup \ ``mr``\  - the MR that is being deregistered

    :param struct rvt_mregion \*mr:
        *undescribed*

.. _`rvt_dereg_clean_qps.description`:

Description
-----------

This routine iterates RC QPs looking for references
to the lkey noted in mr.

.. _`rvt_check_refs`:

rvt_check_refs
==============

.. c:function:: int rvt_check_refs(struct rvt_mregion *mr, const char *t)

    check references \ ``mr``\  - the megion \ ``t``\  - the caller identification

    :param struct rvt_mregion \*mr:
        *undescribed*

    :param const char \*t:
        *undescribed*

.. _`rvt_check_refs.description`:

Description
-----------

This routine checks MRs holding a reference during
when being de-registered.

If the count is non-zero, the code calls a clean routine then
waits for the timeout for the count to zero.

.. _`rvt_mr_has_lkey`:

rvt_mr_has_lkey
===============

.. c:function:: bool rvt_mr_has_lkey(struct rvt_mregion *mr, u32 lkey)

    is MR \ ``mr``\  - the mregion \ ``lkey``\  - the lkey

    :param struct rvt_mregion \*mr:
        *undescribed*

    :param u32 lkey:
        *undescribed*

.. _`rvt_ss_has_lkey`:

rvt_ss_has_lkey
===============

.. c:function:: bool rvt_ss_has_lkey(struct rvt_sge_state *ss, u32 lkey)

    is mr in sge tests \ ``ss``\  - the sge state \ ``lkey``\ 

    :param struct rvt_sge_state \*ss:
        *undescribed*

    :param u32 lkey:
        *undescribed*

.. _`rvt_ss_has_lkey.description`:

Description
-----------

This code tests for an MR in the indicated
sge state.

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

.. _`rvt_set_page`:

rvt_set_page
============

.. c:function:: int rvt_set_page(struct ib_mr *ibmr, u64 addr)

    page assignment function called by ib_sg_to_pages

    :param struct ib_mr \*ibmr:
        memory region

    :param u64 addr:
        dma address of mapped page

.. _`rvt_set_page.return`:

Return
------

0 on success

.. _`rvt_map_mr_sg`:

rvt_map_mr_sg
=============

.. c:function:: int rvt_map_mr_sg(struct ib_mr *ibmr, struct scatterlist *sg, int sg_nents, unsigned int *sg_offset)

    map sg list and set it the memory region

    :param struct ib_mr \*ibmr:
        memory region

    :param struct scatterlist \*sg:
        dma mapped scatterlist

    :param int sg_nents:
        number of entries in sg

    :param unsigned int \*sg_offset:
        offset in bytes into sg

.. _`rvt_map_mr_sg.return`:

Return
------

number of sg elements mapped to the memory region

.. _`rvt_fast_reg_mr`:

rvt_fast_reg_mr
===============

.. c:function:: int rvt_fast_reg_mr(struct rvt_qp *qp, struct ib_mr *ibmr, u32 key, int access)

    fast register physical MR

    :param struct rvt_qp \*qp:
        the queue pair where the work request comes from

    :param struct ib_mr \*ibmr:
        the memory region to be registered

    :param u32 key:
        updated key for this memory region

    :param int access:
        access flags for this memory region

.. _`rvt_fast_reg_mr.description`:

Description
-----------

Returns 0 on success.

.. _`rvt_invalidate_rkey`:

rvt_invalidate_rkey
===================

.. c:function:: int rvt_invalidate_rkey(struct rvt_qp *qp, u32 rkey)

    invalidate an MR rkey

    :param struct rvt_qp \*qp:
        queue pair associated with the invalidate op

    :param u32 rkey:
        rkey to invalidate

.. _`rvt_invalidate_rkey.description`:

Description
-----------

Returns 0 on success.

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
        the fast memory region to set up

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

.. _`rvt_sge_adjacent`:

rvt_sge_adjacent
================

.. c:function:: bool rvt_sge_adjacent(struct rvt_sge *last_sge, struct ib_sge *sge)

    is isge compressible

    :param struct rvt_sge \*last_sge:
        last outgoing SGE written

    :param struct ib_sge \*sge:
        SGE to check

.. _`rvt_sge_adjacent.description`:

Description
-----------

If adjacent will update last_sge to add length.

.. _`rvt_sge_adjacent.return`:

Return
------

true if isge is adjacent to last sge

.. _`rvt_lkey_ok`:

rvt_lkey_ok
===========

.. c:function:: int rvt_lkey_ok(struct rvt_lkey_table *rkt, struct rvt_pd *pd, struct rvt_sge *isge, struct rvt_sge *last_sge, struct ib_sge *sge, int acc)

    check IB SGE for validity and initialize

    :param struct rvt_lkey_table \*rkt:
        table containing lkey to check SGE against

    :param struct rvt_pd \*pd:
        protection domain

    :param struct rvt_sge \*isge:
        outgoing internal SGE

    :param struct rvt_sge \*last_sge:
        last outgoing SGE written

    :param struct ib_sge \*sge:
        SGE to check

    :param int acc:
        access flags

.. _`rvt_lkey_ok.description`:

Description
-----------

Check the IB SGE for validity and initialize our internal version
of it.

Increments the reference count when a new sge is stored.

.. _`rvt_lkey_ok.return`:

Return
------

0 if compressed, 1 if added , otherwise returns -errno.

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

