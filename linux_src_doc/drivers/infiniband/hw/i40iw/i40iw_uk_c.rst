.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_uk.c

.. _`i40iw_nop_1`:

i40iw_nop_1
===========

.. c:function:: enum i40iw_status_code i40iw_nop_1(struct i40iw_qp_uk *qp)

    insert a nop wqe and move head. no post work

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

.. _`i40iw_qp_post_wr`:

i40iw_qp_post_wr
================

.. c:function:: void i40iw_qp_post_wr(struct i40iw_qp_uk *qp)

    post wr to hrdware

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

.. _`i40iw_qp_ring_push_db`:

i40iw_qp_ring_push_db
=====================

.. c:function:: void i40iw_qp_ring_push_db(struct i40iw_qp_uk *qp, u32 wqe_idx)

    ring qp doorbell

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param wqe_idx:
        wqe index
    :type wqe_idx: u32

.. _`i40iw_qp_get_next_send_wqe`:

i40iw_qp_get_next_send_wqe
==========================

.. c:function:: u64 *i40iw_qp_get_next_send_wqe(struct i40iw_qp_uk *qp, u32 *wqe_idx, u8 wqe_size, u32 total_size, u64 wr_id)

    return next wqe ptr

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param wqe_idx:
        return wqe index
    :type wqe_idx: u32 \*

    :param wqe_size:
        size of sq wqe
    :type wqe_size: u8

    :param total_size:
        *undescribed*
    :type total_size: u32

    :param wr_id:
        *undescribed*
    :type wr_id: u64

.. _`i40iw_set_fragment`:

i40iw_set_fragment
==================

.. c:function:: void i40iw_set_fragment(u64 *wqe, u32 offset, struct i40iw_sge *sge)

    set fragment in wqe

    :param wqe:
        wqe for setting fragment
    :type wqe: u64 \*

    :param offset:
        offset value
    :type offset: u32

    :param sge:
        sge length and stag
    :type sge: struct i40iw_sge \*

.. _`i40iw_qp_get_next_recv_wqe`:

i40iw_qp_get_next_recv_wqe
==========================

.. c:function:: u64 *i40iw_qp_get_next_recv_wqe(struct i40iw_qp_uk *qp, u32 *wqe_idx)

    get next qp's rcv wqe

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param wqe_idx:
        return wqe index
    :type wqe_idx: u32 \*

.. _`i40iw_rdma_write`:

i40iw_rdma_write
================

.. c:function:: enum i40iw_status_code i40iw_rdma_write(struct i40iw_qp_uk *qp, struct i40iw_post_sq_info *info, bool post_sq)

    rdma write operation

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post sq information
    :type info: struct i40iw_post_sq_info \*

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_rdma_read`:

i40iw_rdma_read
===============

.. c:function:: enum i40iw_status_code i40iw_rdma_read(struct i40iw_qp_uk *qp, struct i40iw_post_sq_info *info, bool inv_stag, bool post_sq)

    rdma read command

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post sq information
    :type info: struct i40iw_post_sq_info \*

    :param inv_stag:
        flag for inv_stag
    :type inv_stag: bool

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_send`:

i40iw_send
==========

.. c:function:: enum i40iw_status_code i40iw_send(struct i40iw_qp_uk *qp, struct i40iw_post_sq_info *info, u32 stag_to_inv, bool post_sq)

    rdma send command

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post sq information
    :type info: struct i40iw_post_sq_info \*

    :param stag_to_inv:
        stag_to_inv value
    :type stag_to_inv: u32

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_inline_rdma_write`:

i40iw_inline_rdma_write
=======================

.. c:function:: enum i40iw_status_code i40iw_inline_rdma_write(struct i40iw_qp_uk *qp, struct i40iw_post_sq_info *info, bool post_sq)

    inline rdma write operation

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post sq information
    :type info: struct i40iw_post_sq_info \*

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_inline_send`:

i40iw_inline_send
=================

.. c:function:: enum i40iw_status_code i40iw_inline_send(struct i40iw_qp_uk *qp, struct i40iw_post_sq_info *info, u32 stag_to_inv, bool post_sq)

    inline send operation

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post sq information
    :type info: struct i40iw_post_sq_info \*

    :param stag_to_inv:
        remote stag
    :type stag_to_inv: u32

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_stag_local_invalidate`:

i40iw_stag_local_invalidate
===========================

.. c:function:: enum i40iw_status_code i40iw_stag_local_invalidate(struct i40iw_qp_uk *qp, struct i40iw_post_sq_info *info, bool post_sq)

    stag invalidate operation

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post sq information
    :type info: struct i40iw_post_sq_info \*

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_mw_bind`:

i40iw_mw_bind
=============

.. c:function:: enum i40iw_status_code i40iw_mw_bind(struct i40iw_qp_uk *qp, struct i40iw_post_sq_info *info, bool post_sq)

    Memory Window bind operation

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post sq information
    :type info: struct i40iw_post_sq_info \*

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_post_receive`:

i40iw_post_receive
==================

.. c:function:: enum i40iw_status_code i40iw_post_receive(struct i40iw_qp_uk *qp, struct i40iw_post_rq_info *info)

    post receive wqe

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param info:
        post rq information
    :type info: struct i40iw_post_rq_info \*

.. _`i40iw_cq_request_notification`:

i40iw_cq_request_notification
=============================

.. c:function:: void i40iw_cq_request_notification(struct i40iw_cq_uk *cq, enum i40iw_completion_notify cq_notify)

    cq notification request (door bell)

    :param cq:
        hw cq
    :type cq: struct i40iw_cq_uk \*

    :param cq_notify:
        notification type
    :type cq_notify: enum i40iw_completion_notify

.. _`i40iw_cq_post_entries`:

i40iw_cq_post_entries
=====================

.. c:function:: enum i40iw_status_code i40iw_cq_post_entries(struct i40iw_cq_uk *cq, u8 count)

    update tail in shadow memory

    :param cq:
        hw cq
    :type cq: struct i40iw_cq_uk \*

    :param count:
        # of entries processed
    :type count: u8

.. _`i40iw_cq_poll_completion`:

i40iw_cq_poll_completion
========================

.. c:function:: enum i40iw_status_code i40iw_cq_poll_completion(struct i40iw_cq_uk *cq, struct i40iw_cq_poll_info *info)

    get cq completion info

    :param cq:
        hw cq
    :type cq: struct i40iw_cq_uk \*

    :param info:
        cq poll information returned
    :type info: struct i40iw_cq_poll_info \*

.. _`i40iw_get_wqe_shift`:

i40iw_get_wqe_shift
===================

.. c:function:: void i40iw_get_wqe_shift(u32 sge, u32 inline_data, u8 *shift)

    get shift count for maximum wqe size

    :param sge:
        Maximum Scatter Gather Elements wqe
    :type sge: u32

    :param inline_data:
        Maximum inline data size
    :type inline_data: u32

    :param shift:
        Returns the shift needed based on sge
    :type shift: u8 \*

.. _`i40iw_get_wqe_shift.description`:

Description
-----------

Shift can be used to left shift the wqe size based on number of SGEs and inlind data size.
For 1 SGE or inline data <= 16, shift = 0 (wqe size of 32 bytes).
For 2 or 3 SGEs or inline data <= 48, shift = 1 (wqe size of 64 bytes).
Shift of 2 otherwise (wqe size of 128 bytes).

.. _`i40iw_qp_uk_init`:

i40iw_qp_uk_init
================

.. c:function:: enum i40iw_status_code i40iw_qp_uk_init(struct i40iw_qp_uk *qp, struct i40iw_qp_uk_init_info *info)

    initialize shared qp

    :param qp:
        hw qp (user and kernel)
    :type qp: struct i40iw_qp_uk \*

    :param info:
        qp initialization info
    :type info: struct i40iw_qp_uk_init_info \*

.. _`i40iw_qp_uk_init.description`:

Description
-----------

initializes the vars used in both user and kernel mode.
size of the wqe depends on numbers of max. fragements
allowed. Then size of wqe \* the number of wqes should be the
amount of memory allocated for sq and rq. If srq is used,
then rq_base will point to one rq wqe only (not the whole
array of wqes)

.. _`i40iw_cq_uk_init`:

i40iw_cq_uk_init
================

.. c:function:: enum i40iw_status_code i40iw_cq_uk_init(struct i40iw_cq_uk *cq, struct i40iw_cq_uk_init_info *info)

    initialize shared cq (user and kernel)

    :param cq:
        hw cq
    :type cq: struct i40iw_cq_uk \*

    :param info:
        hw cq initialization info
    :type info: struct i40iw_cq_uk_init_info \*

.. _`i40iw_device_init_uk`:

i40iw_device_init_uk
====================

.. c:function:: void i40iw_device_init_uk(struct i40iw_dev_uk *dev)

    setup routines for iwarp shared device

    :param dev:
        iwarp shared (user and kernel)
    :type dev: struct i40iw_dev_uk \*

.. _`i40iw_clean_cq`:

i40iw_clean_cq
==============

.. c:function:: void i40iw_clean_cq(void *queue, struct i40iw_cq_uk *cq)

    clean cq entries \ ````\  queue completion context

    :param queue:
        *undescribed*
    :type queue: void \*

    :param cq:
        cq to clean
    :type cq: struct i40iw_cq_uk \*

.. _`i40iw_nop`:

i40iw_nop
=========

.. c:function:: enum i40iw_status_code i40iw_nop(struct i40iw_qp_uk *qp, u64 wr_id, bool signaled, bool post_sq)

    send a nop

    :param qp:
        hw qp ptr
    :type qp: struct i40iw_qp_uk \*

    :param wr_id:
        work request id
    :type wr_id: u64

    :param signaled:
        flag if signaled for completion
    :type signaled: bool

    :param post_sq:
        flag to post sq
    :type post_sq: bool

.. _`i40iw_fragcnt_to_wqesize_sq`:

i40iw_fragcnt_to_wqesize_sq
===========================

.. c:function:: enum i40iw_status_code i40iw_fragcnt_to_wqesize_sq(u32 frag_cnt, u8 *wqe_size)

    calculate wqe size based on fragment count for SQ

    :param frag_cnt:
        number of fragments
    :type frag_cnt: u32

    :param wqe_size:
        size of sq wqe returned
    :type wqe_size: u8 \*

.. _`i40iw_fragcnt_to_wqesize_rq`:

i40iw_fragcnt_to_wqesize_rq
===========================

.. c:function:: enum i40iw_status_code i40iw_fragcnt_to_wqesize_rq(u32 frag_cnt, u8 *wqe_size)

    calculate wqe size based on fragment count for RQ

    :param frag_cnt:
        number of fragments
    :type frag_cnt: u32

    :param wqe_size:
        size of rq wqe returned
    :type wqe_size: u8 \*

.. _`i40iw_inline_data_size_to_wqesize`:

i40iw_inline_data_size_to_wqesize
=================================

.. c:function:: enum i40iw_status_code i40iw_inline_data_size_to_wqesize(u32 data_size, u8 *wqe_size)

    based on inline data, wqe size

    :param data_size:
        data size for inline
    :type data_size: u32

    :param wqe_size:
        size of sq wqe returned
    :type wqe_size: u8 \*

.. This file was automatic generated / don't edit.

