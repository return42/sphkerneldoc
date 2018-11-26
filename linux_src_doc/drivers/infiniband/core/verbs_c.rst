.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/verbs.c

.. _`__ib_alloc_pd`:

\__ib_alloc_pd
==============

.. c:function:: struct ib_pd *__ib_alloc_pd(struct ib_device *device, unsigned int flags, const char *caller)

    Allocates an unused protection domain.

    :param device:
        The device on which to allocate the protection domain.
    :type device: struct ib_device \*

    :param flags:
        *undescribed*
    :type flags: unsigned int

    :param caller:
        *undescribed*
    :type caller: const char \*

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

    :param pd:
        The protection domain to deallocate.
    :type pd: struct ib_pd \*

.. _`ib_dealloc_pd.description`:

Description
-----------

It is an error to call this function while any resources in the pd still
exist.  The caller is responsible to synchronously destroy them and
guarantee no new allocations will happen.

.. _`rdma_copy_ah_attr`:

rdma_copy_ah_attr
=================

.. c:function:: void rdma_copy_ah_attr(struct rdma_ah_attr *dest, const struct rdma_ah_attr *src)

    Copy rdma ah attribute from source to destination.

    :param dest:
        Pointer to destination ah_attr. Contents of the destination
        pointer is assumed to be invalid and attribute are overwritten.
    :type dest: struct rdma_ah_attr \*

    :param src:
        Pointer to source ah_attr.
    :type src: const struct rdma_ah_attr \*

.. _`rdma_replace_ah_attr`:

rdma_replace_ah_attr
====================

.. c:function:: void rdma_replace_ah_attr(struct rdma_ah_attr *old, const struct rdma_ah_attr *new)

    Replace valid ah_attr with new new one.

    :param old:
        Pointer to existing ah_attr which needs to be replaced.
        old is assumed to be valid or zero'd
    :type old: struct rdma_ah_attr \*

    :param new:
        Pointer to the new ah_attr.
    :type new: const struct rdma_ah_attr \*

.. _`rdma_replace_ah_attr.description`:

Description
-----------

\ :c:func:`rdma_replace_ah_attr`\  first releases any reference in the old ah_attr if
old the ah_attr is valid; after that it copies the new attribute and holds
the reference to the replaced ah_attr.

.. _`rdma_move_ah_attr`:

rdma_move_ah_attr
=================

.. c:function:: void rdma_move_ah_attr(struct rdma_ah_attr *dest, struct rdma_ah_attr *src)

    Move ah_attr pointed by source to destination.

    :param dest:
        Pointer to destination ah_attr to copy to.
        dest is assumed to be valid or zero'd
    :type dest: struct rdma_ah_attr \*

    :param src:
        Pointer to the new ah_attr.
    :type src: struct rdma_ah_attr \*

.. _`rdma_move_ah_attr.description`:

Description
-----------

\ :c:func:`rdma_move_ah_attr`\  first releases any reference in the destination ah_attr
if it is valid. This also transfers ownership of internal references from
src to dest, making src invalid in the process. No new reference of the src
ah_attr is taken.

.. _`rdma_create_ah`:

rdma_create_ah
==============

.. c:function:: struct ib_ah *rdma_create_ah(struct ib_pd *pd, struct rdma_ah_attr *ah_attr)

    Creates an address handle for the given address vector.

    :param pd:
        The protection domain associated with the address handle.
    :type pd: struct ib_pd \*

    :param ah_attr:
        The attributes of the address vector.
    :type ah_attr: struct rdma_ah_attr \*

.. _`rdma_create_ah.description`:

Description
-----------

It returns 0 on success and returns appropriate error code on error.
The address handle is used to reference a local or global destination
in all UD QP post sends.

.. _`rdma_create_user_ah`:

rdma_create_user_ah
===================

.. c:function:: struct ib_ah *rdma_create_user_ah(struct ib_pd *pd, struct rdma_ah_attr *ah_attr, struct ib_udata *udata)

    Creates an address handle for the given address vector. It resolves destination mac address for ah attribute of RoCE type.

    :param pd:
        The protection domain associated with the address handle.
    :type pd: struct ib_pd \*

    :param ah_attr:
        The attributes of the address vector.
    :type ah_attr: struct rdma_ah_attr \*

    :param udata:
        pointer to user's input output buffer information need by
        provider driver.
    :type udata: struct ib_udata \*

.. _`rdma_create_user_ah.description`:

Description
-----------

It returns 0 on success and returns appropriate error code on error.
The address handle is used to reference a local or global destination
in all UD QP post sends.

.. _`rdma_move_grh_sgid_attr`:

rdma_move_grh_sgid_attr
=======================

.. c:function:: void rdma_move_grh_sgid_attr(struct rdma_ah_attr *attr, union ib_gid *dgid, u32 flow_label, u8 hop_limit, u8 traffic_class, const struct ib_gid_attr *sgid_attr)

    Sets the sgid attribute of GRH, taking ownership of the reference

    :param attr:
        Pointer to AH attribute structure
    :type attr: struct rdma_ah_attr \*

    :param dgid:
        Destination GID
    :type dgid: union ib_gid \*

    :param flow_label:
        Flow label
    :type flow_label: u32

    :param hop_limit:
        Hop limit
    :type hop_limit: u8

    :param traffic_class:
        traffic class
    :type traffic_class: u8

    :param sgid_attr:
        Pointer to SGID attribute
    :type sgid_attr: const struct ib_gid_attr \*

.. _`rdma_move_grh_sgid_attr.description`:

Description
-----------

This takes ownership of the sgid_attr reference. The caller must ensure
\ :c:func:`rdma_destroy_ah_attr`\  is called before destroying the rdma_ah_attr after
calling this function.

.. _`rdma_destroy_ah_attr`:

rdma_destroy_ah_attr
====================

.. c:function:: void rdma_destroy_ah_attr(struct rdma_ah_attr *ah_attr)

    Release reference to SGID attribute of ah attribute.

    :param ah_attr:
        Pointer to ah attribute
    :type ah_attr: struct rdma_ah_attr \*

.. _`rdma_destroy_ah_attr.description`:

Description
-----------

Release reference to the SGID attribute of the ah attribute if it is
non NULL. It is safe to call this multiple times, and safe to call it on
a zero initialized ah_attr.

.. _`ib_resolve_eth_dmac`:

ib_resolve_eth_dmac
===================

.. c:function:: int ib_resolve_eth_dmac(struct ib_device *device, struct rdma_ah_attr *ah_attr)

    Resolve destination mac address

    :param device:
        Device to consider
    :type device: struct ib_device \*

    :param ah_attr:
        address handle attribute which describes the
        source and destination parameters
        \ :c:func:`ib_resolve_eth_dmac`\  resolves destination mac address and L3 hop limit It
        returns 0 on success or appropriate error code. It initializes the
        necessary ah_attr fields when call is successful.
    :type ah_attr: struct rdma_ah_attr \*

.. _`_ib_modify_qp`:

\_ib_modify_qp
==============

.. c:function:: int _ib_modify_qp(struct ib_qp *qp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    :param qp:
        *undescribed*
    :type qp: struct ib_qp \*

    :param attr:
        *undescribed*
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        *undescribed*
    :type attr_mask: int

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`ib_modify_qp_with_udata`:

ib_modify_qp_with_udata
=======================

.. c:function:: int ib_modify_qp_with_udata(struct ib_qp *ib_qp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    Modifies the attributes for the specified QP.

    :param ib_qp:
        The QP to modify.
    :type ib_qp: struct ib_qp \*

    :param attr:
        On input, specifies the QP attributes to modify.  On output,
        the current values of selected QP attributes are returned.
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        A bit-mask used to specify which attributes of the QP
        are being modified.
    :type attr_mask: int

    :param udata:
        pointer to user's input output buffer information
        are being modified.
        It returns 0 on success and returns appropriate error code on error.
    :type udata: struct ib_udata \*

.. _`ib_alloc_mr`:

ib_alloc_mr
===========

.. c:function:: struct ib_mr *ib_alloc_mr(struct ib_pd *pd, enum ib_mr_type mr_type, u32 max_num_sg)

    Allocates a memory region

    :param pd:
        protection domain associated with the region
    :type pd: struct ib_pd \*

    :param mr_type:
        memory region type
    :type mr_type: enum ib_mr_type

    :param max_num_sg:
        maximum sg entries available for registration.
    :type max_num_sg: u32

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

    :param pd:
        The protection domain associated with the WQ.
    :type pd: struct ib_pd \*

    :param wq_attr:
        A list of initial attributes required to create the
        WQ. If WQ creation succeeds, then the attributes are updated to
        the actual capabilities of the created WQ.
    :type wq_attr: struct ib_wq_init_attr \*

.. _`ib_create_wq.description`:

Description
-----------

wq_attr->max_wr and wq_attr->max_sge determine
the requested size of the WQ, and set to the actual values allocated
on return.
If \ :c:func:`ib_create_wq`\  succeeds, then max_wr and max_sge will always be
at least as large as the requested values.

.. _`ib_destroy_wq`:

ib_destroy_wq
=============

.. c:function:: int ib_destroy_wq(struct ib_wq *wq)

    Destroys the specified WQ.

    :param wq:
        The WQ to destroy.
    :type wq: struct ib_wq \*

.. _`ib_modify_wq`:

ib_modify_wq
============

.. c:function:: int ib_modify_wq(struct ib_wq *wq, struct ib_wq_attr *wq_attr, u32 wq_attr_mask)

    Modifies the specified WQ.

    :param wq:
        The WQ to modify.
    :type wq: struct ib_wq \*

    :param wq_attr:
        On input, specifies the WQ attributes to modify.
    :type wq_attr: struct ib_wq_attr \*

    :param wq_attr_mask:
        A bit-mask used to specify which attributes of the WQ
        are being modified.
        On output, the current values of selected WQ attributes are returned.
    :type wq_attr_mask: u32

.. _`ib_map_mr_sg`:

ib_map_mr_sg
============

.. c:function:: int ib_map_mr_sg(struct ib_mr *mr, struct scatterlist *sg, int sg_nents, unsigned int *sg_offset, unsigned int page_size)

    Map the largest prefix of a dma mapped SG list and set it the memory region.

    :param mr:
        memory region
    :type mr: struct ib_mr \*

    :param sg:
        dma mapped scatterlist
    :type sg: struct scatterlist \*

    :param sg_nents:
        number of entries in sg
    :type sg_nents: int

    :param sg_offset:
        offset in bytes into sg
    :type sg_offset: unsigned int \*

    :param page_size:
        page vector desired page size
    :type page_size: unsigned int

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

    :param mr:
        memory region
    :type mr: struct ib_mr \*

    :param sgl:
        dma mapped scatterlist
    :type sgl: struct scatterlist \*

    :param sg_nents:
        number of entries in sg
    :type sg_nents: int

    :param sg_offset_p:
        IN:  start offset in bytes into sg
        OUT: offset in bytes for element n of the sg of the first
        byte that has not been processed where n is the return
        value of this function.
    :type sg_offset_p: unsigned int \*

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

    :param qp:
        queue pair to drain
    :type qp: struct ib_qp \*

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

    :param qp:
        queue pair to drain
    :type qp: struct ib_qp \*

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

    :param qp:
        queue pair to drain
    :type qp: struct ib_qp \*

.. _`ib_drain_qp.the-caller-must`:

The caller must
---------------


ensure there is room in the CQ(s), SQ, and RQ for drain work requests
and completions.

allocate the CQs using \ :c:func:`ib_alloc_cq`\ .

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

.. This file was automatic generated / don't edit.

