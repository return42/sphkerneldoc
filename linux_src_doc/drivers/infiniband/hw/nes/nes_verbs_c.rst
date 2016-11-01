.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_verbs.c

.. _`nes_alloc_mw`:

nes_alloc_mw
============

.. c:function:: struct ib_mw *nes_alloc_mw(struct ib_pd *ibpd, enum ib_mw_type type, struct ib_udata *udata)

    :param struct ib_pd \*ibpd:
        *undescribed*

    :param enum ib_mw_type type:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`nes_dealloc_mw`:

nes_dealloc_mw
==============

.. c:function:: int nes_dealloc_mw(struct ib_mw *ibmw)

    :param struct ib_mw \*ibmw:
        *undescribed*

.. _`nes_query_device`:

nes_query_device
================

.. c:function:: int nes_query_device(struct ib_device *ibdev, struct ib_device_attr *props, struct ib_udata *uhw)

    :param struct ib_device \*ibdev:
        *undescribed*

    :param struct ib_device_attr \*props:
        *undescribed*

    :param struct ib_udata \*uhw:
        *undescribed*

.. _`nes_query_port`:

nes_query_port
==============

.. c:function:: int nes_query_port(struct ib_device *ibdev, u8 port, struct ib_port_attr *props)

    :param struct ib_device \*ibdev:
        *undescribed*

    :param u8 port:
        *undescribed*

    :param struct ib_port_attr \*props:
        *undescribed*

.. _`nes_query_pkey`:

nes_query_pkey
==============

.. c:function:: int nes_query_pkey(struct ib_device *ibdev, u8 port, u16 index, u16 *pkey)

    :param struct ib_device \*ibdev:
        *undescribed*

    :param u8 port:
        *undescribed*

    :param u16 index:
        *undescribed*

    :param u16 \*pkey:
        *undescribed*

.. _`nes_query_gid`:

nes_query_gid
=============

.. c:function:: int nes_query_gid(struct ib_device *ibdev, u8 port, int index, union ib_gid *gid)

    :param struct ib_device \*ibdev:
        *undescribed*

    :param u8 port:
        *undescribed*

    :param int index:
        *undescribed*

    :param union ib_gid \*gid:
        *undescribed*

.. _`nes_alloc_ucontext`:

nes_alloc_ucontext
==================

.. c:function:: struct ib_ucontext *nes_alloc_ucontext(struct ib_device *ibdev, struct ib_udata *udata)

    Allocate the user context data structure. This keeps track of all objects associated with a particular user-mode client.

    :param struct ib_device \*ibdev:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`nes_dealloc_ucontext`:

nes_dealloc_ucontext
====================

.. c:function:: int nes_dealloc_ucontext(struct ib_ucontext *context)

    :param struct ib_ucontext \*context:
        *undescribed*

.. _`nes_mmap`:

nes_mmap
========

.. c:function:: int nes_mmap(struct ib_ucontext *context, struct vm_area_struct *vma)

    :param struct ib_ucontext \*context:
        *undescribed*

    :param struct vm_area_struct \*vma:
        *undescribed*

.. _`nes_alloc_pd`:

nes_alloc_pd
============

.. c:function:: struct ib_pd *nes_alloc_pd(struct ib_device *ibdev, struct ib_ucontext *context, struct ib_udata *udata)

    :param struct ib_device \*ibdev:
        *undescribed*

    :param struct ib_ucontext \*context:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`nes_dealloc_pd`:

nes_dealloc_pd
==============

.. c:function:: int nes_dealloc_pd(struct ib_pd *ibpd)

    :param struct ib_pd \*ibpd:
        *undescribed*

.. _`nes_create_ah`:

nes_create_ah
=============

.. c:function:: struct ib_ah *nes_create_ah(struct ib_pd *pd, struct ib_ah_attr *ah_attr)

    :param struct ib_pd \*pd:
        *undescribed*

    :param struct ib_ah_attr \*ah_attr:
        *undescribed*

.. _`nes_destroy_ah`:

nes_destroy_ah
==============

.. c:function:: int nes_destroy_ah(struct ib_ah *ah)

    :param struct ib_ah \*ah:
        *undescribed*

.. _`nes_get_encoded_size`:

nes_get_encoded_size
====================

.. c:function:: u8 nes_get_encoded_size(int *size)

    :param int \*size:
        *undescribed*

.. _`nes_setup_virt_qp`:

nes_setup_virt_qp
=================

.. c:function:: int nes_setup_virt_qp(struct nes_qp *nesqp, struct nes_pbl *nespbl, struct nes_vnic *nesvnic, int sq_size, int rq_size)

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param struct nes_pbl \*nespbl:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param int sq_size:
        *undescribed*

    :param int rq_size:
        *undescribed*

.. _`nes_setup_mmap_qp`:

nes_setup_mmap_qp
=================

.. c:function:: int nes_setup_mmap_qp(struct nes_qp *nesqp, struct nes_vnic *nesvnic, int sq_size, int rq_size)

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param int sq_size:
        *undescribed*

    :param int rq_size:
        *undescribed*

.. _`nes_free_qp_mem`:

nes_free_qp_mem
===============

.. c:function:: void nes_free_qp_mem(struct nes_device *nesdev, struct nes_qp *nesqp, int virt_wqs)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param int virt_wqs:
        *undescribed*

.. _`nes_create_qp`:

nes_create_qp
=============

.. c:function:: struct ib_qp *nes_create_qp(struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    :param struct ib_pd \*ibpd:
        *undescribed*

    :param struct ib_qp_init_attr \*init_attr:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`nes_clean_cq`:

nes_clean_cq
============

.. c:function:: void nes_clean_cq(struct nes_qp *nesqp, struct nes_cq *nescq)

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param struct nes_cq \*nescq:
        *undescribed*

.. _`nes_destroy_qp`:

nes_destroy_qp
==============

.. c:function:: int nes_destroy_qp(struct ib_qp *ibqp)

    :param struct ib_qp \*ibqp:
        *undescribed*

.. _`nes_create_cq`:

nes_create_cq
=============

.. c:function:: struct ib_cq *nes_create_cq(struct ib_device *ibdev, const struct ib_cq_init_attr *attr, struct ib_ucontext *context, struct ib_udata *udata)

    :param struct ib_device \*ibdev:
        *undescribed*

    :param const struct ib_cq_init_attr \*attr:
        *undescribed*

    :param struct ib_ucontext \*context:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`nes_destroy_cq`:

nes_destroy_cq
==============

.. c:function:: int nes_destroy_cq(struct ib_cq *ib_cq)

    :param struct ib_cq \*ib_cq:
        *undescribed*

.. _`root_256`:

root_256
========

.. c:function:: u32 root_256(struct nes_device *nesdev, struct nes_root_vpbl *root_vpbl, struct nes_root_vpbl *new_root, u16 pbl_count_4k)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_root_vpbl \*root_vpbl:
        *undescribed*

    :param struct nes_root_vpbl \*new_root:
        *undescribed*

    :param u16 pbl_count_4k:
        *undescribed*

.. _`nes_reg_mr`:

nes_reg_mr
==========

.. c:function:: int nes_reg_mr(struct nes_device *nesdev, struct nes_pd *nespd, u32 stag, u64 region_length, struct nes_root_vpbl *root_vpbl, dma_addr_t single_buffer, u16 pbl_count_4k, u16 residual_page_count_4k, int acc, u64 *iova_start, u16 *actual_pbl_cnt, u8 *used_4k_pbls)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_pd \*nespd:
        *undescribed*

    :param u32 stag:
        *undescribed*

    :param u64 region_length:
        *undescribed*

    :param struct nes_root_vpbl \*root_vpbl:
        *undescribed*

    :param dma_addr_t single_buffer:
        *undescribed*

    :param u16 pbl_count_4k:
        *undescribed*

    :param u16 residual_page_count_4k:
        *undescribed*

    :param int acc:
        *undescribed*

    :param u64 \*iova_start:
        *undescribed*

    :param u16 \*actual_pbl_cnt:
        *undescribed*

    :param u8 \*used_4k_pbls:
        *undescribed*

.. _`nes_reg_phys_mr`:

nes_reg_phys_mr
===============

.. c:function:: struct ib_mr *nes_reg_phys_mr(struct ib_pd *ib_pd, u64 addr, u64 size, int acc, u64 *iova_start)

    :param struct ib_pd \*ib_pd:
        *undescribed*

    :param u64 addr:
        *undescribed*

    :param u64 size:
        *undescribed*

    :param int acc:
        *undescribed*

    :param u64 \*iova_start:
        *undescribed*

.. _`nes_get_dma_mr`:

nes_get_dma_mr
==============

.. c:function:: struct ib_mr *nes_get_dma_mr(struct ib_pd *pd, int acc)

    :param struct ib_pd \*pd:
        *undescribed*

    :param int acc:
        *undescribed*

.. _`nes_reg_user_mr`:

nes_reg_user_mr
===============

.. c:function:: struct ib_mr *nes_reg_user_mr(struct ib_pd *pd, u64 start, u64 length, u64 virt, int acc, struct ib_udata *udata)

    :param struct ib_pd \*pd:
        *undescribed*

    :param u64 start:
        *undescribed*

    :param u64 length:
        *undescribed*

    :param u64 virt:
        *undescribed*

    :param int acc:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`nes_dereg_mr`:

nes_dereg_mr
============

.. c:function:: int nes_dereg_mr(struct ib_mr *ib_mr)

    :param struct ib_mr \*ib_mr:
        *undescribed*

.. _`show_rev`:

show_rev
========

.. c:function:: ssize_t show_rev(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_hca`:

show_hca
========

.. c:function:: ssize_t show_hca(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_board`:

show_board
==========

.. c:function:: ssize_t show_board(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`nes_query_qp`:

nes_query_qp
============

.. c:function:: int nes_query_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    :param struct ib_qp \*ibqp:
        *undescribed*

    :param struct ib_qp_attr \*attr:
        *undescribed*

    :param int attr_mask:
        *undescribed*

    :param struct ib_qp_init_attr \*init_attr:
        *undescribed*

.. _`nes_hw_modify_qp`:

nes_hw_modify_qp
================

.. c:function:: int nes_hw_modify_qp(struct nes_device *nesdev, struct nes_qp *nesqp, u32 next_iwarp_state, u32 termlen, u32 wait_completion)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param u32 next_iwarp_state:
        *undescribed*

    :param u32 termlen:
        *undescribed*

    :param u32 wait_completion:
        *undescribed*

.. _`nes_modify_qp`:

nes_modify_qp
=============

.. c:function:: int nes_modify_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    :param struct ib_qp \*ibqp:
        *undescribed*

    :param struct ib_qp_attr \*attr:
        *undescribed*

    :param int attr_mask:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`nes_multicast_attach`:

nes_multicast_attach
====================

.. c:function:: int nes_multicast_attach(struct ib_qp *ibqp, union ib_gid *gid, u16 lid)

    :param struct ib_qp \*ibqp:
        *undescribed*

    :param union ib_gid \*gid:
        *undescribed*

    :param u16 lid:
        *undescribed*

.. _`nes_multicast_detach`:

nes_multicast_detach
====================

.. c:function:: int nes_multicast_detach(struct ib_qp *ibqp, union ib_gid *gid, u16 lid)

    :param struct ib_qp \*ibqp:
        *undescribed*

    :param union ib_gid \*gid:
        *undescribed*

    :param u16 lid:
        *undescribed*

.. _`nes_process_mad`:

nes_process_mad
===============

.. c:function:: int nes_process_mad(struct ib_device *ibdev, int mad_flags, u8 port_num, const struct ib_wc *in_wc, const struct ib_grh *in_grh, const struct ib_mad_hdr *in, size_t in_mad_size, struct ib_mad_hdr *out, size_t *out_mad_size, u16 *out_mad_pkey_index)

    :param struct ib_device \*ibdev:
        *undescribed*

    :param int mad_flags:
        *undescribed*

    :param u8 port_num:
        *undescribed*

    :param const struct ib_wc \*in_wc:
        *undescribed*

    :param const struct ib_grh \*in_grh:
        *undescribed*

    :param const struct ib_mad_hdr \*in:
        *undescribed*

    :param size_t in_mad_size:
        *undescribed*

    :param struct ib_mad_hdr \*out:
        *undescribed*

    :param size_t \*out_mad_size:
        *undescribed*

    :param u16 \*out_mad_pkey_index:
        *undescribed*

.. _`nes_post_send`:

nes_post_send
=============

.. c:function:: int nes_post_send(struct ib_qp *ibqp, struct ib_send_wr *ib_wr, struct ib_send_wr **bad_wr)

    :param struct ib_qp \*ibqp:
        *undescribed*

    :param struct ib_send_wr \*ib_wr:
        *undescribed*

    :param struct ib_send_wr \*\*bad_wr:
        *undescribed*

.. _`nes_post_recv`:

nes_post_recv
=============

.. c:function:: int nes_post_recv(struct ib_qp *ibqp, struct ib_recv_wr *ib_wr, struct ib_recv_wr **bad_wr)

    :param struct ib_qp \*ibqp:
        *undescribed*

    :param struct ib_recv_wr \*ib_wr:
        *undescribed*

    :param struct ib_recv_wr \*\*bad_wr:
        *undescribed*

.. _`nes_drain_sq`:

nes_drain_sq
============

.. c:function:: void nes_drain_sq(struct ib_qp *ibqp)

    drain sq

    :param struct ib_qp \*ibqp:
        pointer to ibqp

.. _`nes_drain_rq`:

nes_drain_rq
============

.. c:function:: void nes_drain_rq(struct ib_qp *ibqp)

    drain rq

    :param struct ib_qp \*ibqp:
        pointer to ibqp

.. _`nes_poll_cq`:

nes_poll_cq
===========

.. c:function:: int nes_poll_cq(struct ib_cq *ibcq, int num_entries, struct ib_wc *entry)

    :param struct ib_cq \*ibcq:
        *undescribed*

    :param int num_entries:
        *undescribed*

    :param struct ib_wc \*entry:
        *undescribed*

.. _`nes_req_notify_cq`:

nes_req_notify_cq
=================

.. c:function:: int nes_req_notify_cq(struct ib_cq *ibcq, enum ib_cq_notify_flags notify_flags)

    :param struct ib_cq \*ibcq:
        *undescribed*

    :param enum ib_cq_notify_flags notify_flags:
        *undescribed*

.. _`nes_init_ofa_device`:

nes_init_ofa_device
===================

.. c:function:: struct nes_ib_device *nes_init_ofa_device(struct net_device *netdev)

    :param struct net_device \*netdev:
        *undescribed*

.. _`nes_handle_delayed_event`:

nes_handle_delayed_event
========================

.. c:function:: void nes_handle_delayed_event(unsigned long data)

    :param unsigned long data:
        *undescribed*

.. _`nes_destroy_ofa_device`:

nes_destroy_ofa_device
======================

.. c:function:: void nes_destroy_ofa_device(struct nes_ib_device *nesibdev)

    :param struct nes_ib_device \*nesibdev:
        *undescribed*

.. _`nes_register_ofa_device`:

nes_register_ofa_device
=======================

.. c:function:: int nes_register_ofa_device(struct nes_ib_device *nesibdev)

    :param struct nes_ib_device \*nesibdev:
        *undescribed*

.. _`nes_unregister_ofa_device`:

nes_unregister_ofa_device
=========================

.. c:function:: void nes_unregister_ofa_device(struct nes_ib_device *nesibdev)

    :param struct nes_ib_device \*nesibdev:
        *undescribed*

.. This file was automatic generated / don't edit.

