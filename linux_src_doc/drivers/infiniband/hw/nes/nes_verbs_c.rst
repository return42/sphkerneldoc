.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_verbs.c

.. _`nes_alloc_mw`:

nes_alloc_mw
============

.. c:function:: struct ib_mw *nes_alloc_mw(struct ib_pd *ibpd, enum ib_mw_type type, struct ib_udata *udata)

    :param ibpd:
        *undescribed*
    :type ibpd: struct ib_pd \*

    :param type:
        *undescribed*
    :type type: enum ib_mw_type

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`nes_dealloc_mw`:

nes_dealloc_mw
==============

.. c:function:: int nes_dealloc_mw(struct ib_mw *ibmw)

    :param ibmw:
        *undescribed*
    :type ibmw: struct ib_mw \*

.. _`nes_query_device`:

nes_query_device
================

.. c:function:: int nes_query_device(struct ib_device *ibdev, struct ib_device_attr *props, struct ib_udata *uhw)

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

    :param props:
        *undescribed*
    :type props: struct ib_device_attr \*

    :param uhw:
        *undescribed*
    :type uhw: struct ib_udata \*

.. _`nes_query_port`:

nes_query_port
==============

.. c:function:: int nes_query_port(struct ib_device *ibdev, u8 port, struct ib_port_attr *props)

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

    :param port:
        *undescribed*
    :type port: u8

    :param props:
        *undescribed*
    :type props: struct ib_port_attr \*

.. _`nes_query_pkey`:

nes_query_pkey
==============

.. c:function:: int nes_query_pkey(struct ib_device *ibdev, u8 port, u16 index, u16 *pkey)

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

    :param port:
        *undescribed*
    :type port: u8

    :param index:
        *undescribed*
    :type index: u16

    :param pkey:
        *undescribed*
    :type pkey: u16 \*

.. _`nes_query_gid`:

nes_query_gid
=============

.. c:function:: int nes_query_gid(struct ib_device *ibdev, u8 port, int index, union ib_gid *gid)

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

    :param port:
        *undescribed*
    :type port: u8

    :param index:
        *undescribed*
    :type index: int

    :param gid:
        *undescribed*
    :type gid: union ib_gid \*

.. _`nes_alloc_ucontext`:

nes_alloc_ucontext
==================

.. c:function:: struct ib_ucontext *nes_alloc_ucontext(struct ib_device *ibdev, struct ib_udata *udata)

    Allocate the user context data structure. This keeps track of all objects associated with a particular user-mode client.

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`nes_dealloc_ucontext`:

nes_dealloc_ucontext
====================

.. c:function:: int nes_dealloc_ucontext(struct ib_ucontext *context)

    :param context:
        *undescribed*
    :type context: struct ib_ucontext \*

.. _`nes_mmap`:

nes_mmap
========

.. c:function:: int nes_mmap(struct ib_ucontext *context, struct vm_area_struct *vma)

    :param context:
        *undescribed*
    :type context: struct ib_ucontext \*

    :param vma:
        *undescribed*
    :type vma: struct vm_area_struct \*

.. _`nes_alloc_pd`:

nes_alloc_pd
============

.. c:function:: struct ib_pd *nes_alloc_pd(struct ib_device *ibdev, struct ib_ucontext *context, struct ib_udata *udata)

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

    :param context:
        *undescribed*
    :type context: struct ib_ucontext \*

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`nes_dealloc_pd`:

nes_dealloc_pd
==============

.. c:function:: int nes_dealloc_pd(struct ib_pd *ibpd)

    :param ibpd:
        *undescribed*
    :type ibpd: struct ib_pd \*

.. _`nes_get_encoded_size`:

nes_get_encoded_size
====================

.. c:function:: u8 nes_get_encoded_size(int *size)

    :param size:
        *undescribed*
    :type size: int \*

.. _`nes_setup_virt_qp`:

nes_setup_virt_qp
=================

.. c:function:: int nes_setup_virt_qp(struct nes_qp *nesqp, struct nes_pbl *nespbl, struct nes_vnic *nesvnic, int sq_size, int rq_size)

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param nespbl:
        *undescribed*
    :type nespbl: struct nes_pbl \*

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param sq_size:
        *undescribed*
    :type sq_size: int

    :param rq_size:
        *undescribed*
    :type rq_size: int

.. _`nes_setup_mmap_qp`:

nes_setup_mmap_qp
=================

.. c:function:: int nes_setup_mmap_qp(struct nes_qp *nesqp, struct nes_vnic *nesvnic, int sq_size, int rq_size)

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param sq_size:
        *undescribed*
    :type sq_size: int

    :param rq_size:
        *undescribed*
    :type rq_size: int

.. _`nes_free_qp_mem`:

nes_free_qp_mem
===============

.. c:function:: void nes_free_qp_mem(struct nes_device *nesdev, struct nes_qp *nesqp, int virt_wqs)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param virt_wqs:
        *undescribed*
    :type virt_wqs: int

.. _`nes_create_qp`:

nes_create_qp
=============

.. c:function:: struct ib_qp *nes_create_qp(struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    :param ibpd:
        *undescribed*
    :type ibpd: struct ib_pd \*

    :param init_attr:
        *undescribed*
    :type init_attr: struct ib_qp_init_attr \*

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`nes_clean_cq`:

nes_clean_cq
============

.. c:function:: void nes_clean_cq(struct nes_qp *nesqp, struct nes_cq *nescq)

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param nescq:
        *undescribed*
    :type nescq: struct nes_cq \*

.. _`nes_destroy_qp`:

nes_destroy_qp
==============

.. c:function:: int nes_destroy_qp(struct ib_qp *ibqp)

    :param ibqp:
        *undescribed*
    :type ibqp: struct ib_qp \*

.. _`nes_create_cq`:

nes_create_cq
=============

.. c:function:: struct ib_cq *nes_create_cq(struct ib_device *ibdev, const struct ib_cq_init_attr *attr, struct ib_ucontext *context, struct ib_udata *udata)

    :param ibdev:
        *undescribed*
    :type ibdev: struct ib_device \*

    :param attr:
        *undescribed*
    :type attr: const struct ib_cq_init_attr \*

    :param context:
        *undescribed*
    :type context: struct ib_ucontext \*

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`nes_destroy_cq`:

nes_destroy_cq
==============

.. c:function:: int nes_destroy_cq(struct ib_cq *ib_cq)

    :param ib_cq:
        *undescribed*
    :type ib_cq: struct ib_cq \*

.. _`root_256`:

root_256
========

.. c:function:: u32 root_256(struct nes_device *nesdev, struct nes_root_vpbl *root_vpbl, struct nes_root_vpbl *new_root, u16 pbl_count_4k)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param root_vpbl:
        *undescribed*
    :type root_vpbl: struct nes_root_vpbl \*

    :param new_root:
        *undescribed*
    :type new_root: struct nes_root_vpbl \*

    :param pbl_count_4k:
        *undescribed*
    :type pbl_count_4k: u16

.. _`nes_reg_mr`:

nes_reg_mr
==========

.. c:function:: int nes_reg_mr(struct nes_device *nesdev, struct nes_pd *nespd, u32 stag, u64 region_length, struct nes_root_vpbl *root_vpbl, dma_addr_t single_buffer, u16 pbl_count_4k, u16 residual_page_count_4k, int acc, u64 *iova_start, u16 *actual_pbl_cnt, u8 *used_4k_pbls)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param nespd:
        *undescribed*
    :type nespd: struct nes_pd \*

    :param stag:
        *undescribed*
    :type stag: u32

    :param region_length:
        *undescribed*
    :type region_length: u64

    :param root_vpbl:
        *undescribed*
    :type root_vpbl: struct nes_root_vpbl \*

    :param single_buffer:
        *undescribed*
    :type single_buffer: dma_addr_t

    :param pbl_count_4k:
        *undescribed*
    :type pbl_count_4k: u16

    :param residual_page_count_4k:
        *undescribed*
    :type residual_page_count_4k: u16

    :param acc:
        *undescribed*
    :type acc: int

    :param iova_start:
        *undescribed*
    :type iova_start: u64 \*

    :param actual_pbl_cnt:
        *undescribed*
    :type actual_pbl_cnt: u16 \*

    :param used_4k_pbls:
        *undescribed*
    :type used_4k_pbls: u8 \*

.. _`nes_reg_phys_mr`:

nes_reg_phys_mr
===============

.. c:function:: struct ib_mr *nes_reg_phys_mr(struct ib_pd *ib_pd, u64 addr, u64 size, int acc, u64 *iova_start)

    :param ib_pd:
        *undescribed*
    :type ib_pd: struct ib_pd \*

    :param addr:
        *undescribed*
    :type addr: u64

    :param size:
        *undescribed*
    :type size: u64

    :param acc:
        *undescribed*
    :type acc: int

    :param iova_start:
        *undescribed*
    :type iova_start: u64 \*

.. _`nes_get_dma_mr`:

nes_get_dma_mr
==============

.. c:function:: struct ib_mr *nes_get_dma_mr(struct ib_pd *pd, int acc)

    :param pd:
        *undescribed*
    :type pd: struct ib_pd \*

    :param acc:
        *undescribed*
    :type acc: int

.. _`nes_reg_user_mr`:

nes_reg_user_mr
===============

.. c:function:: struct ib_mr *nes_reg_user_mr(struct ib_pd *pd, u64 start, u64 length, u64 virt, int acc, struct ib_udata *udata)

    :param pd:
        *undescribed*
    :type pd: struct ib_pd \*

    :param start:
        *undescribed*
    :type start: u64

    :param length:
        *undescribed*
    :type length: u64

    :param virt:
        *undescribed*
    :type virt: u64

    :param acc:
        *undescribed*
    :type acc: int

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`nes_dereg_mr`:

nes_dereg_mr
============

.. c:function:: int nes_dereg_mr(struct ib_mr *ib_mr)

    :param ib_mr:
        *undescribed*
    :type ib_mr: struct ib_mr \*

.. _`hw_rev_show`:

hw_rev_show
===========

.. c:function:: ssize_t hw_rev_show(struct device *dev, struct device_attribute *attr, char *buf)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`hca_type_show`:

hca_type_show
=============

.. c:function:: ssize_t hca_type_show(struct device *dev, struct device_attribute *attr, char *buf)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`board_id_show`:

board_id_show
=============

.. c:function:: ssize_t board_id_show(struct device *dev, struct device_attribute *attr, char *buf)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`nes_query_qp`:

nes_query_qp
============

.. c:function:: int nes_query_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    :param ibqp:
        *undescribed*
    :type ibqp: struct ib_qp \*

    :param attr:
        *undescribed*
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        *undescribed*
    :type attr_mask: int

    :param init_attr:
        *undescribed*
    :type init_attr: struct ib_qp_init_attr \*

.. _`nes_hw_modify_qp`:

nes_hw_modify_qp
================

.. c:function:: int nes_hw_modify_qp(struct nes_device *nesdev, struct nes_qp *nesqp, u32 next_iwarp_state, u32 termlen, u32 wait_completion)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param next_iwarp_state:
        *undescribed*
    :type next_iwarp_state: u32

    :param termlen:
        *undescribed*
    :type termlen: u32

    :param wait_completion:
        *undescribed*
    :type wait_completion: u32

.. _`nes_modify_qp`:

nes_modify_qp
=============

.. c:function:: int nes_modify_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    :param ibqp:
        *undescribed*
    :type ibqp: struct ib_qp \*

    :param attr:
        *undescribed*
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        *undescribed*
    :type attr_mask: int

    :param udata:
        *undescribed*
    :type udata: struct ib_udata \*

.. _`nes_post_send`:

nes_post_send
=============

.. c:function:: int nes_post_send(struct ib_qp *ibqp, const struct ib_send_wr *ib_wr, const struct ib_send_wr **bad_wr)

    :param ibqp:
        *undescribed*
    :type ibqp: struct ib_qp \*

    :param ib_wr:
        *undescribed*
    :type ib_wr: const struct ib_send_wr \*

    :param bad_wr:
        *undescribed*
    :type bad_wr: const struct ib_send_wr \*\*

.. _`nes_post_recv`:

nes_post_recv
=============

.. c:function:: int nes_post_recv(struct ib_qp *ibqp, const struct ib_recv_wr *ib_wr, const struct ib_recv_wr **bad_wr)

    :param ibqp:
        *undescribed*
    :type ibqp: struct ib_qp \*

    :param ib_wr:
        *undescribed*
    :type ib_wr: const struct ib_recv_wr \*

    :param bad_wr:
        *undescribed*
    :type bad_wr: const struct ib_recv_wr \*\*

.. _`nes_drain_sq`:

nes_drain_sq
============

.. c:function:: void nes_drain_sq(struct ib_qp *ibqp)

    drain sq

    :param ibqp:
        pointer to ibqp
    :type ibqp: struct ib_qp \*

.. _`nes_drain_rq`:

nes_drain_rq
============

.. c:function:: void nes_drain_rq(struct ib_qp *ibqp)

    drain rq

    :param ibqp:
        pointer to ibqp
    :type ibqp: struct ib_qp \*

.. _`nes_poll_cq`:

nes_poll_cq
===========

.. c:function:: int nes_poll_cq(struct ib_cq *ibcq, int num_entries, struct ib_wc *entry)

    :param ibcq:
        *undescribed*
    :type ibcq: struct ib_cq \*

    :param num_entries:
        *undescribed*
    :type num_entries: int

    :param entry:
        *undescribed*
    :type entry: struct ib_wc \*

.. _`nes_req_notify_cq`:

nes_req_notify_cq
=================

.. c:function:: int nes_req_notify_cq(struct ib_cq *ibcq, enum ib_cq_notify_flags notify_flags)

    :param ibcq:
        *undescribed*
    :type ibcq: struct ib_cq \*

    :param notify_flags:
        *undescribed*
    :type notify_flags: enum ib_cq_notify_flags

.. _`nes_init_ofa_device`:

nes_init_ofa_device
===================

.. c:function:: struct nes_ib_device *nes_init_ofa_device(struct net_device *netdev)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_handle_delayed_event`:

nes_handle_delayed_event
========================

.. c:function:: void nes_handle_delayed_event(struct timer_list *t)

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`nes_destroy_ofa_device`:

nes_destroy_ofa_device
======================

.. c:function:: void nes_destroy_ofa_device(struct nes_ib_device *nesibdev)

    :param nesibdev:
        *undescribed*
    :type nesibdev: struct nes_ib_device \*

.. _`nes_register_ofa_device`:

nes_register_ofa_device
=======================

.. c:function:: int nes_register_ofa_device(struct nes_ib_device *nesibdev)

    :param nesibdev:
        *undescribed*
    :type nesibdev: struct nes_ib_device \*

.. _`nes_unregister_ofa_device`:

nes_unregister_ofa_device
=========================

.. c:function:: void nes_unregister_ofa_device(struct nes_ib_device *nesibdev)

    :param nesibdev:
        *undescribed*
    :type nesibdev: struct nes_ib_device \*

.. This file was automatic generated / don't edit.

