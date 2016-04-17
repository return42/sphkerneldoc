.. -*- coding: utf-8; mode: rst -*-

=======
verbs.c
=======


.. _`ib_alloc_pd`:

ib_alloc_pd
===========

.. c:function:: struct ib_pd *ib_alloc_pd (struct ib_device *device)

    Allocates an unused protection domain.

    :param struct ib_device \*device:
        The device on which to allocate the protection domain.



.. _`ib_alloc_pd.description`:

Description
-----------

A protection domain object provides an association between QPs, shared
receive queues, address handles, memory regions, and memory windows.

Every PD has a local_dma_lkey which can be used as the lkey value for local
memory operations.



.. _`ib_dealloc_pd`:

ib_dealloc_pd
=============

.. c:function:: void ib_dealloc_pd (struct ib_pd *pd)

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

.. c:function:: struct ib_mr *ib_alloc_mr (struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

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
max_num_sg * used_page_size.



.. _`ib_map_mr_sg`:

ib_map_mr_sg
============

.. c:function:: int ib_map_mr_sg (struct ib_mr *mr, struct scatterlist *sg, int sg_nents, unsigned int page_size)

    Map the largest prefix of a dma mapped SG list and set it the memory region.

    :param struct ib_mr \*mr:
        memory region

    :param struct scatterlist \*sg:
        dma mapped scatterlist

    :param int sg_nents:
        number of entries in sg

    :param unsigned int page_size:
        page vector desired page size



.. _`ib_map_mr_sg.constraints`:

Constraints
-----------

- The first sg element is allowed to have an offset.
- Each sg element must be aligned to page_size (or physically

  contiguous to the previous element). In case an sg element has a
  non contiguous offset, the mapping prefix will not include it.

- The last sg element is allowed to have length less than page_size.
- If sg_nents total byte length exceeds the mr max_num_sge * page_size

  then only max_num_sg entries will be mapped.

- If the MR was allocated with type IB_MR_TYPE_SG_GAPS_REG, non of these

  constraints holds and the page_size argument is ignored.

Returns the number of sg elements that were mapped to the memory region.

After this completes successfully, the  memory region
is ready for registration.



.. _`ib_sg_to_pages`:

ib_sg_to_pages
==============

.. c:function:: int ib_sg_to_pages (struct ib_mr *mr, struct scatterlist *sgl, int sg_nents, int (*set_page) (struct ib_mr *, u64)

    Convert the largest prefix of a sg list to a page vector

    :param struct ib_mr \*mr:
        memory region

    :param struct scatterlist \*sgl:
        dma mapped scatterlist

    :param int sg_nents:
        number of entries in sg

    :param int (\*set_page) (struct ib_mr \*, u64):
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

.. c:function:: void ib_drain_sq (struct ib_qp *qp)

    Block until all SQ CQEs have been consumed by the application.

    :param struct ib_qp \*qp:
        queue pair to drain



.. _`ib_drain_sq.description`:

Description
-----------

If the device has a provider-specific drain function, then
call that.  Otherwise call the generic drain function
:c:func:`__ib_drain_sq`.



.. _`ib_drain_sq.the-caller-must`:

The caller must
---------------


ensure there is room in the CQ and SQ for the drain work request and
completion.

allocate the CQ using :c:func:`ib_alloc_cq` and the CQ poll context cannot be
IB_POLL_DIRECT.

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.



.. _`ib_drain_rq`:

ib_drain_rq
===========

.. c:function:: void ib_drain_rq (struct ib_qp *qp)

    Block until all RQ CQEs have been consumed by the application.

    :param struct ib_qp \*qp:
        queue pair to drain



.. _`ib_drain_rq.description`:

Description
-----------

If the device has a provider-specific drain function, then
call that.  Otherwise call the generic drain function
:c:func:`__ib_drain_rq`.



.. _`ib_drain_rq.the-caller-must`:

The caller must
---------------


ensure there is room in the CQ and RQ for the drain work request and
completion.

allocate the CQ using :c:func:`ib_alloc_cq` and the CQ poll context cannot be
IB_POLL_DIRECT.

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.



.. _`ib_drain_qp`:

ib_drain_qp
===========

.. c:function:: void ib_drain_qp (struct ib_qp *qp)

    Block until all CQEs have been consumed by the application on both the RQ and SQ.

    :param struct ib_qp \*qp:
        queue pair to drain



.. _`ib_drain_qp.the-caller-must`:

The caller must
---------------


ensure there is room in the CQ(s), SQ, and RQ for drain work requests
and completions.

allocate the CQs using :c:func:`ib_alloc_cq` and the CQ poll context cannot be
IB_POLL_DIRECT.

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

