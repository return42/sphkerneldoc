.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/verbs.c

.. _`__ib_alloc_pd`:

__ib_alloc_pd
=============

.. c:function:: struct ib_pd *__ib_alloc_pd(struct ib_device *device, unsigned int flags, const char *caller)

    Allocates an unused protection domain.

    :param struct ib_device \*device:
        The device on which to allocate the protection domain.

    :param unsigned int flags:
        *undescribed*

    :param const char \*caller:
        *undescribed*

.. _`__ib_alloc_pd.description`:

Description
-----------

A protection domain object provides an association between QPs, shared
receive queues, address handles, memory regions, and memory windows.

Every PD has a local_dma_lkey which can be used as the lkey value for local
memory operations.

.. _`ib_dealloc_pd`:

ib_dealloc_pd
=============

.. c:function:: void ib_dealloc_pd(struct ib_pd *pd)

    Deallocates a protection domain.

    :param struct ib_pd \*pd:
        The protection domain to deallocate.

.. _`ib_dealloc_pd.description`:

Description
-----------

It is an error to call this function while any resources in the pd still
exist.  The caller is responsible to synchronously destroy them and
guarantee no new allocations will happen.

.. _`ib_alloc_mr`:

ib_alloc_mr
===========

.. c:function:: struct ib_mr *ib_alloc_mr(struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

    Allocates a memory region

    :param struct ib_pd \*pd:
        protection domain associated with the region

    :param enum ib_mr_type mr_type:
        memory region type

    :param u32 max_num_sg:
        maximum sg entries available for registration.

.. _`ib_alloc_mr.notes`:

Notes
-----

Memory registeration page/sg lists must not exceed max_num_sg.
For mr_type IB_MR_TYPE_MEM_REG, the total length cannot exceed
max_num_sg \* used_page_size.

.. _`ib_create_wq`:

ib_create_wq
============

.. c:function:: struct ib_wq *ib_create_wq(struct ib_pd *pd, struct ib_wq_init_attr *wq_attr)

    Creates a WQ associated with the specified protection domain.

    :param struct ib_pd \*pd:
        The protection domain associated with the WQ.

    :param struct ib_wq_init_attr \*wq_attr:
        *undescribed*

.. _`ib_create_wq.description`:

Description
-----------

wq_init_attr->max_wr and wq_init_attr->max_sge determine
the requested size of the WQ, and set to the actual values allocated
on return.
If \ :c:func:`ib_create_wq`\  succeeds, then max_wr and max_sge will always be
at least as large as the requested values.

.. _`ib_destroy_wq`:

ib_destroy_wq
=============

.. c:function:: int ib_destroy_wq(struct ib_wq *wq)

    Destroys the specified WQ.

    :param struct ib_wq \*wq:
        The WQ to destroy.

.. _`ib_modify_wq`:

ib_modify_wq
============

.. c:function:: int ib_modify_wq(struct ib_wq *wq, struct ib_wq_attr *wq_attr, u32 wq_attr_mask)

    Modifies the specified WQ.

    :param struct ib_wq \*wq:
        The WQ to modify.

    :param struct ib_wq_attr \*wq_attr:
        On input, specifies the WQ attributes to modify.

    :param u32 wq_attr_mask:
        A bit-mask used to specify which attributes of the WQ
        are being modified.
        On output, the current values of selected WQ attributes are returned.

.. _`ib_map_mr_sg`:

ib_map_mr_sg
============

.. c:function:: int ib_map_mr_sg(struct ib_mr *mr, struct scatterlist *sg, int sg_nents, unsigned int *sg_offset, unsigned int page_size)

    Map the largest prefix of a dma mapped SG list and set it the memory region.

    :param struct ib_mr \*mr:
        memory region

    :param struct scatterlist \*sg:
        dma mapped scatterlist

    :param int sg_nents:
        number of entries in sg

    :param unsigned int \*sg_offset:
        offset in bytes into sg

    :param unsigned int page_size:
        page vector desired page size

.. _`ib_map_mr_sg.constraints`:

Constraints
-----------

- The first sg element is allowed to have an offset.
- Each sg element must either be aligned to page_size or virtually
contiguous to the previous element. In case an sg element has a
non-contiguous offset, the mapping prefix will not include it.
- The last sg element is allowed to have length less than page_size.
- If sg_nents total byte length exceeds the mr max_num_sge \* page_size
then only max_num_sg entries will be mapped.
- If the MR was allocated with type IB_MR_TYPE_SG_GAPS, none of these
constraints holds and the page_size argument is ignored.

Returns the number of sg elements that were mapped to the memory region.

After this completes successfully, the  memory region
is ready for registration.

.. _`ib_sg_to_pages`:

ib_sg_to_pages
==============

.. c:function:: int ib_sg_to_pages(struct ib_mr *mr, struct scatterlist *sgl, int sg_nents, unsigned int *sg_offset_p, int (*set_page)(struct ib_mr *, u64))

    Convert the largest prefix of a sg list to a page vector

    :param struct ib_mr \*mr:
        memory region

    :param struct scatterlist \*sgl:
        dma mapped scatterlist

    :param int sg_nents:
        number of entries in sg

    :param unsigned int \*sg_offset_p:
        IN:  start offset in bytes into sg
        OUT: offset in bytes for element n of the sg of the first
        byte that has not been processed where n is the return
        value of this function.

    :param int (\*set_page)(struct ib_mr \*, u64):
        driver page assignment function pointer

.. _`ib_sg_to_pages.description`:

Description
-----------

Core service helper for drivers to convert the largest
prefix of given sg list to a page vector. The sg list
prefix converted is the prefix that meet the requirements
of ib_map_mr_sg.

Returns the number of sg elements that were assigned to
a page vector.

.. _`ib_drain_sq`:

ib_drain_sq
===========

.. c:function:: void ib_drain_sq(struct ib_qp *qp)

    Block until all SQ CQEs have been consumed by the application.

    :param struct ib_qp \*qp:
        queue pair to drain

.. _`ib_drain_sq.description`:

Description
-----------

If the device has a provider-specific drain function, then
call that.  Otherwise call the generic drain function
\__ib_drain_sq().

.. _`ib_drain_sq.the-caller-must`:

The caller must
---------------


ensure there is room in the CQ and SQ for the drain work request and
completion.

allocate the CQ using \ :c:func:`ib_alloc_cq`\ .

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

.. _`ib_drain_rq`:

ib_drain_rq
===========

.. c:function:: void ib_drain_rq(struct ib_qp *qp)

    Block until all RQ CQEs have been consumed by the application.

    :param struct ib_qp \*qp:
        queue pair to drain

.. _`ib_drain_rq.description`:

Description
-----------

If the device has a provider-specific drain function, then
call that.  Otherwise call the generic drain function
\__ib_drain_rq().

.. _`ib_drain_rq.the-caller-must`:

The caller must
---------------


ensure there is room in the CQ and RQ for the drain work request and
completion.

allocate the CQ using \ :c:func:`ib_alloc_cq`\ .

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

.. _`ib_drain_qp`:

ib_drain_qp
===========

.. c:function:: void ib_drain_qp(struct ib_qp *qp)

    Block until all CQEs have been consumed by the application on both the RQ and SQ.

    :param struct ib_qp \*qp:
        queue pair to drain

.. _`ib_drain_qp.the-caller-must`:

The caller must
---------------


ensure there is room in the CQ(s), SQ, and RQ for drain work requests
and completions.

allocate the CQs using \ :c:func:`ib_alloc_cq`\ .

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

.. This file was automatic generated / don't edit.

