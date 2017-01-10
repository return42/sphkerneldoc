.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_puda.c

.. _`i40iw_puda_get_listbuf`:

i40iw_puda_get_listbuf
======================

.. c:function:: struct i40iw_puda_buf *i40iw_puda_get_listbuf(struct list_head *list)

    get buffer from puda list

    :param struct list_head \*list:
        list to use for buffers (ILQ or IEQ)

.. _`i40iw_puda_get_bufpool`:

i40iw_puda_get_bufpool
======================

.. c:function:: struct i40iw_puda_buf *i40iw_puda_get_bufpool(struct i40iw_puda_rsrc *rsrc)

    return buffer from resource

    :param struct i40iw_puda_rsrc \*rsrc:
        resource to use for buffer

.. _`i40iw_puda_ret_bufpool`:

i40iw_puda_ret_bufpool
======================

.. c:function:: void i40iw_puda_ret_bufpool(struct i40iw_puda_rsrc *rsrc, struct i40iw_puda_buf *buf)

    return buffer to rsrc list

    :param struct i40iw_puda_rsrc \*rsrc:
        resource to use for buffer

    :param struct i40iw_puda_buf \*buf:
        buffe to return to resouce

.. _`i40iw_puda_post_recvbuf`:

i40iw_puda_post_recvbuf
=======================

.. c:function:: void i40iw_puda_post_recvbuf(struct i40iw_puda_rsrc *rsrc, u32 wqe_idx, struct i40iw_puda_buf *buf, bool initial)

    set wqe for rcv buffer

    :param struct i40iw_puda_rsrc \*rsrc:
        resource ptr

    :param u32 wqe_idx:
        wqe index to use

    :param struct i40iw_puda_buf \*buf:
        puda buffer for rcv q

    :param bool initial:
        flag if during init time

.. _`i40iw_puda_replenish_rq`:

i40iw_puda_replenish_rq
=======================

.. c:function:: enum i40iw_status_code i40iw_puda_replenish_rq(struct i40iw_puda_rsrc *rsrc, bool initial)

    post rcv buffers

    :param struct i40iw_puda_rsrc \*rsrc:
        resource to use for buffer

    :param bool initial:
        flag if during init time

.. _`i40iw_puda_alloc_buf`:

i40iw_puda_alloc_buf
====================

.. c:function:: struct i40iw_puda_buf *i40iw_puda_alloc_buf(struct i40iw_sc_dev *dev, u32 length)

    allocate mem for buffer

    :param struct i40iw_sc_dev \*dev:
        iwarp device

    :param u32 length:
        length of buffer

.. _`i40iw_puda_dele_buf`:

i40iw_puda_dele_buf
===================

.. c:function:: void i40iw_puda_dele_buf(struct i40iw_sc_dev *dev, struct i40iw_puda_buf *buf)

    delete buffer back to system

    :param struct i40iw_sc_dev \*dev:
        iwarp device

    :param struct i40iw_puda_buf \*buf:
        buffer to free

.. _`i40iw_puda_get_next_send_wqe`:

i40iw_puda_get_next_send_wqe
============================

.. c:function:: u64 *i40iw_puda_get_next_send_wqe(struct i40iw_qp_uk *qp, u32 *wqe_idx)

    return next wqe for processing

    :param struct i40iw_qp_uk \*qp:
        puda qp for wqe

    :param u32 \*wqe_idx:
        wqe index for caller

.. _`i40iw_puda_poll_info`:

i40iw_puda_poll_info
====================

.. c:function:: enum i40iw_status_code i40iw_puda_poll_info(struct i40iw_sc_cq *cq, struct i40iw_puda_completion_info *info)

    poll cq for completion

    :param struct i40iw_sc_cq \*cq:
        cq for poll

    :param struct i40iw_puda_completion_info \*info:
        info return for successful completion

.. _`i40iw_puda_poll_completion`:

i40iw_puda_poll_completion
==========================

.. c:function:: enum i40iw_status_code i40iw_puda_poll_completion(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq, u32 *compl_err)

    processes completion for cq

    :param struct i40iw_sc_dev \*dev:
        iwarp device

    :param struct i40iw_sc_cq \*cq:
        cq getting interrupt

    :param u32 \*compl_err:
        return any completion err

.. _`i40iw_puda_send`:

i40iw_puda_send
===============

.. c:function:: enum i40iw_status_code i40iw_puda_send(struct i40iw_sc_qp *qp, struct i40iw_puda_send_info *info)

    complete send wqe for transmit

    :param struct i40iw_sc_qp \*qp:
        puda qp for send

    :param struct i40iw_puda_send_info \*info:
        buffer information for transmit

.. _`i40iw_puda_send_buf`:

i40iw_puda_send_buf
===================

.. c:function:: void i40iw_puda_send_buf(struct i40iw_puda_rsrc *rsrc, struct i40iw_puda_buf *buf)

    transmit puda buffer

    :param struct i40iw_puda_rsrc \*rsrc:
        resource to use for buffer

    :param struct i40iw_puda_buf \*buf:
        puda buffer to transmit

.. _`i40iw_puda_qp_setctx`:

i40iw_puda_qp_setctx
====================

.. c:function:: void i40iw_puda_qp_setctx(struct i40iw_puda_rsrc *rsrc)

    during init, set qp's context

    :param struct i40iw_puda_rsrc \*rsrc:
        qp's resource

.. _`i40iw_puda_qp_wqe`:

i40iw_puda_qp_wqe
=================

.. c:function:: enum i40iw_status_code i40iw_puda_qp_wqe(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    setup wqe for qp create

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

    :param struct i40iw_sc_qp \*qp:
        *undescribed*

.. _`i40iw_puda_qp_create`:

i40iw_puda_qp_create
====================

.. c:function:: enum i40iw_status_code i40iw_puda_qp_create(struct i40iw_puda_rsrc *rsrc)

    create qp for resource

    :param struct i40iw_puda_rsrc \*rsrc:
        resource to use for buffer

.. _`i40iw_puda_cq_wqe`:

i40iw_puda_cq_wqe
=================

.. c:function:: enum i40iw_status_code i40iw_puda_cq_wqe(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq)

    setup wqe for cq create

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

    :param struct i40iw_sc_cq \*cq:
        *undescribed*

.. _`i40iw_puda_cq_create`:

i40iw_puda_cq_create
====================

.. c:function:: enum i40iw_status_code i40iw_puda_cq_create(struct i40iw_puda_rsrc *rsrc)

    create cq for resource

    :param struct i40iw_puda_rsrc \*rsrc:
        resource for which cq to create

.. _`i40iw_puda_free_qp`:

i40iw_puda_free_qp
==================

.. c:function:: void i40iw_puda_free_qp(struct i40iw_puda_rsrc *rsrc)

    free qp for resource

    :param struct i40iw_puda_rsrc \*rsrc:
        resource for which qp to free

.. _`i40iw_puda_free_cq`:

i40iw_puda_free_cq
==================

.. c:function:: void i40iw_puda_free_cq(struct i40iw_puda_rsrc *rsrc)

    free cq for resource

    :param struct i40iw_puda_rsrc \*rsrc:
        resource for which cq to free

.. _`i40iw_puda_dele_resources`:

i40iw_puda_dele_resources
=========================

.. c:function:: void i40iw_puda_dele_resources(struct i40iw_sc_vsi *vsi, enum puda_resource_type type, bool reset)

    delete all resources during close

    :param struct i40iw_sc_vsi \*vsi:
        *undescribed*

    :param enum puda_resource_type type:
        type of resource to dele

    :param bool reset:
        true if reset chip

.. _`i40iw_puda_allocbufs`:

i40iw_puda_allocbufs
====================

.. c:function:: enum i40iw_status_code i40iw_puda_allocbufs(struct i40iw_puda_rsrc *rsrc, u32 count)

    allocate buffers for resource

    :param struct i40iw_puda_rsrc \*rsrc:
        resource for buffer allocation

    :param u32 count:
        number of buffers to create

.. _`i40iw_puda_create_rsrc`:

i40iw_puda_create_rsrc
======================

.. c:function:: enum i40iw_status_code i40iw_puda_create_rsrc(struct i40iw_sc_vsi *vsi, struct i40iw_puda_rsrc_info *info)

    create resouce (ilq or ieq)

    :param struct i40iw_sc_vsi \*vsi:
        *undescribed*

    :param struct i40iw_puda_rsrc_info \*info:
        resource information

.. _`i40iw_ilq_putback_rcvbuf`:

i40iw_ilq_putback_rcvbuf
========================

.. c:function:: void i40iw_ilq_putback_rcvbuf(struct i40iw_sc_qp *qp, u32 wqe_idx)

    ilq buffer to put back on rq

    :param struct i40iw_sc_qp \*qp:
        ilq's qp resource

    :param u32 wqe_idx:
        wqe index of completed rcvbuf

.. _`i40iw_ieq_get_fpdu_length`:

i40iw_ieq_get_fpdu_length
=========================

.. c:function:: u16 i40iw_ieq_get_fpdu_length(u16 length)

    given length return fpdu length

    :param u16 length:
        length if fpdu

.. _`i40iw_ieq_copy_to_txbuf`:

i40iw_ieq_copy_to_txbuf
=======================

.. c:function:: void i40iw_ieq_copy_to_txbuf(struct i40iw_puda_buf *buf, struct i40iw_puda_buf *txbuf, u16 buf_offset, u32 txbuf_offset, u32 length)

    copydata from rcv buf to tx buf

    :param struct i40iw_puda_buf \*buf:
        rcv buffer with partial

    :param struct i40iw_puda_buf \*txbuf:
        tx buffer for sendign back

    :param u16 buf_offset:
        rcv buffer offset to copy from

    :param u32 txbuf_offset:
        at offset in tx buf to copy

    :param u32 length:
        length of data to copy

.. _`i40iw_ieq_setup_tx_buf`:

i40iw_ieq_setup_tx_buf
======================

.. c:function:: void i40iw_ieq_setup_tx_buf(struct i40iw_puda_buf *buf, struct i40iw_puda_buf *txbuf)

    setup tx buffer for partial handling

    :param struct i40iw_puda_buf \*buf:
        reeive buffer with partial

    :param struct i40iw_puda_buf \*txbuf:
        buffer to prepare

.. _`i40iw_ieq_check_first_buf`:

i40iw_ieq_check_first_buf
=========================

.. c:function:: void i40iw_ieq_check_first_buf(struct i40iw_puda_buf *buf, u32 fps)

    check if rcv buffer's seq is in range

    :param struct i40iw_puda_buf \*buf:
        receive exception buffer

    :param u32 fps:
        first partial sequence number

.. _`i40iw_ieq_compl_pfpdu`:

i40iw_ieq_compl_pfpdu
=====================

.. c:function:: void i40iw_ieq_compl_pfpdu(struct i40iw_puda_rsrc *ieq, struct list_head *rxlist, struct list_head *pbufl, struct i40iw_puda_buf *txbuf, u16 fpdu_len)

    write txbuf with full fpdu

    :param struct i40iw_puda_rsrc \*ieq:
        ieq resource

    :param struct list_head \*rxlist:
        ieq's received buffer list

    :param struct list_head \*pbufl:
        temporary list for buffers for fpddu

    :param struct i40iw_puda_buf \*txbuf:
        tx buffer for fpdu

    :param u16 fpdu_len:
        total length of fpdu

.. _`i40iw_ieq_create_pbufl`:

i40iw_ieq_create_pbufl
======================

.. c:function:: enum i40iw_status_code i40iw_ieq_create_pbufl(struct i40iw_pfpdu *pfpdu, struct list_head *rxlist, struct list_head *pbufl, struct i40iw_puda_buf *buf, u16 fpdu_len)

    create buffer list for single fpdu

    :param struct i40iw_pfpdu \*pfpdu:
        *undescribed*

    :param struct list_head \*rxlist:
        resource list for receive ieq buffes

    :param struct list_head \*pbufl:
        temp. list for buffers for fpddu

    :param struct i40iw_puda_buf \*buf:
        first receive buffer

    :param u16 fpdu_len:
        total length of fpdu

.. _`i40iw_ieq_handle_partial`:

i40iw_ieq_handle_partial
========================

.. c:function:: enum i40iw_status_code i40iw_ieq_handle_partial(struct i40iw_puda_rsrc *ieq, struct i40iw_pfpdu *pfpdu, struct i40iw_puda_buf *buf, u16 fpdu_len)

    process partial fpdu buffer

    :param struct i40iw_puda_rsrc \*ieq:
        ieq resource

    :param struct i40iw_pfpdu \*pfpdu:
        partial management per user qp

    :param struct i40iw_puda_buf \*buf:
        receive buffer

    :param u16 fpdu_len:
        fpdu len in the buffer

.. _`i40iw_ieq_process_buf`:

i40iw_ieq_process_buf
=====================

.. c:function:: enum i40iw_status_code i40iw_ieq_process_buf(struct i40iw_puda_rsrc *ieq, struct i40iw_pfpdu *pfpdu, struct i40iw_puda_buf *buf)

    process buffer rcvd for ieq

    :param struct i40iw_puda_rsrc \*ieq:
        ieq resource

    :param struct i40iw_pfpdu \*pfpdu:
        partial management per user qp

    :param struct i40iw_puda_buf \*buf:
        receive buffer

.. _`i40iw_ieq_process_fpdus`:

i40iw_ieq_process_fpdus
=======================

.. c:function:: void i40iw_ieq_process_fpdus(struct i40iw_sc_qp *qp, struct i40iw_puda_rsrc *ieq)

    process fpdu's buffers on its list

    :param struct i40iw_sc_qp \*qp:
        qp for which partial fpdus

    :param struct i40iw_puda_rsrc \*ieq:
        ieq resource

.. _`i40iw_ieq_handle_exception`:

i40iw_ieq_handle_exception
==========================

.. c:function:: void i40iw_ieq_handle_exception(struct i40iw_puda_rsrc *ieq, struct i40iw_sc_qp *qp, struct i40iw_puda_buf *buf)

    handle qp's exception

    :param struct i40iw_puda_rsrc \*ieq:
        ieq resource

    :param struct i40iw_sc_qp \*qp:
        qp receiving excpetion

    :param struct i40iw_puda_buf \*buf:
        receive buffer

.. _`i40iw_ieq_receive`:

i40iw_ieq_receive
=================

.. c:function:: void i40iw_ieq_receive(struct i40iw_sc_vsi *vsi, struct i40iw_puda_buf *buf)

    received exception buffer

    :param struct i40iw_sc_vsi \*vsi:
        *undescribed*

    :param struct i40iw_puda_buf \*buf:
        exception buffer received

.. _`i40iw_ieq_tx_compl`:

i40iw_ieq_tx_compl
==================

.. c:function:: void i40iw_ieq_tx_compl(struct i40iw_sc_vsi *vsi, void *sqwrid)

    put back after sending completed exception buffer

    :param struct i40iw_sc_vsi \*vsi:
        pointer to the vsi structure

    :param void \*sqwrid:
        pointer to puda buffer

.. _`i40iw_ieq_cleanup_qp`:

i40iw_ieq_cleanup_qp
====================

.. c:function:: void i40iw_ieq_cleanup_qp(struct i40iw_puda_rsrc *ieq, struct i40iw_sc_qp *qp)

    qp is being destroyed

    :param struct i40iw_puda_rsrc \*ieq:
        ieq resource

    :param struct i40iw_sc_qp \*qp:
        all pending fpdu buffers

.. This file was automatic generated / don't edit.

