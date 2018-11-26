.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_puda.c

.. _`i40iw_puda_get_listbuf`:

i40iw_puda_get_listbuf
======================

.. c:function:: struct i40iw_puda_buf *i40iw_puda_get_listbuf(struct list_head *list)

    get buffer from puda list

    :param list:
        list to use for buffers (ILQ or IEQ)
    :type list: struct list_head \*

.. _`i40iw_puda_get_bufpool`:

i40iw_puda_get_bufpool
======================

.. c:function:: struct i40iw_puda_buf *i40iw_puda_get_bufpool(struct i40iw_puda_rsrc *rsrc)

    return buffer from resource

    :param rsrc:
        resource to use for buffer
    :type rsrc: struct i40iw_puda_rsrc \*

.. _`i40iw_puda_ret_bufpool`:

i40iw_puda_ret_bufpool
======================

.. c:function:: void i40iw_puda_ret_bufpool(struct i40iw_puda_rsrc *rsrc, struct i40iw_puda_buf *buf)

    return buffer to rsrc list

    :param rsrc:
        resource to use for buffer
    :type rsrc: struct i40iw_puda_rsrc \*

    :param buf:
        buffe to return to resouce
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_puda_post_recvbuf`:

i40iw_puda_post_recvbuf
=======================

.. c:function:: void i40iw_puda_post_recvbuf(struct i40iw_puda_rsrc *rsrc, u32 wqe_idx, struct i40iw_puda_buf *buf, bool initial)

    set wqe for rcv buffer

    :param rsrc:
        resource ptr
    :type rsrc: struct i40iw_puda_rsrc \*

    :param wqe_idx:
        wqe index to use
    :type wqe_idx: u32

    :param buf:
        puda buffer for rcv q
    :type buf: struct i40iw_puda_buf \*

    :param initial:
        flag if during init time
    :type initial: bool

.. _`i40iw_puda_replenish_rq`:

i40iw_puda_replenish_rq
=======================

.. c:function:: enum i40iw_status_code i40iw_puda_replenish_rq(struct i40iw_puda_rsrc *rsrc, bool initial)

    post rcv buffers

    :param rsrc:
        resource to use for buffer
    :type rsrc: struct i40iw_puda_rsrc \*

    :param initial:
        flag if during init time
    :type initial: bool

.. _`i40iw_puda_alloc_buf`:

i40iw_puda_alloc_buf
====================

.. c:function:: struct i40iw_puda_buf *i40iw_puda_alloc_buf(struct i40iw_sc_dev *dev, u32 length)

    allocate mem for buffer

    :param dev:
        iwarp device
    :type dev: struct i40iw_sc_dev \*

    :param length:
        length of buffer
    :type length: u32

.. _`i40iw_puda_dele_buf`:

i40iw_puda_dele_buf
===================

.. c:function:: void i40iw_puda_dele_buf(struct i40iw_sc_dev *dev, struct i40iw_puda_buf *buf)

    delete buffer back to system

    :param dev:
        iwarp device
    :type dev: struct i40iw_sc_dev \*

    :param buf:
        buffer to free
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_puda_get_next_send_wqe`:

i40iw_puda_get_next_send_wqe
============================

.. c:function:: u64 *i40iw_puda_get_next_send_wqe(struct i40iw_qp_uk *qp, u32 *wqe_idx)

    return next wqe for processing

    :param qp:
        puda qp for wqe
    :type qp: struct i40iw_qp_uk \*

    :param wqe_idx:
        wqe index for caller
    :type wqe_idx: u32 \*

.. _`i40iw_puda_poll_info`:

i40iw_puda_poll_info
====================

.. c:function:: enum i40iw_status_code i40iw_puda_poll_info(struct i40iw_sc_cq *cq, struct i40iw_puda_completion_info *info)

    poll cq for completion

    :param cq:
        cq for poll
    :type cq: struct i40iw_sc_cq \*

    :param info:
        info return for successful completion
    :type info: struct i40iw_puda_completion_info \*

.. _`i40iw_puda_poll_completion`:

i40iw_puda_poll_completion
==========================

.. c:function:: enum i40iw_status_code i40iw_puda_poll_completion(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq, u32 *compl_err)

    processes completion for cq

    :param dev:
        iwarp device
    :type dev: struct i40iw_sc_dev \*

    :param cq:
        cq getting interrupt
    :type cq: struct i40iw_sc_cq \*

    :param compl_err:
        return any completion err
    :type compl_err: u32 \*

.. _`i40iw_puda_send`:

i40iw_puda_send
===============

.. c:function:: enum i40iw_status_code i40iw_puda_send(struct i40iw_sc_qp *qp, struct i40iw_puda_send_info *info)

    complete send wqe for transmit

    :param qp:
        puda qp for send
    :type qp: struct i40iw_sc_qp \*

    :param info:
        buffer information for transmit
    :type info: struct i40iw_puda_send_info \*

.. _`i40iw_puda_send_buf`:

i40iw_puda_send_buf
===================

.. c:function:: void i40iw_puda_send_buf(struct i40iw_puda_rsrc *rsrc, struct i40iw_puda_buf *buf)

    transmit puda buffer

    :param rsrc:
        resource to use for buffer
    :type rsrc: struct i40iw_puda_rsrc \*

    :param buf:
        puda buffer to transmit
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_puda_qp_setctx`:

i40iw_puda_qp_setctx
====================

.. c:function:: void i40iw_puda_qp_setctx(struct i40iw_puda_rsrc *rsrc)

    during init, set qp's context

    :param rsrc:
        qp's resource
    :type rsrc: struct i40iw_puda_rsrc \*

.. _`i40iw_puda_qp_wqe`:

i40iw_puda_qp_wqe
=================

.. c:function:: enum i40iw_status_code i40iw_puda_qp_wqe(struct i40iw_sc_dev *dev, struct i40iw_sc_qp *qp)

    setup wqe for qp create

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param qp:
        *undescribed*
    :type qp: struct i40iw_sc_qp \*

.. _`i40iw_puda_qp_create`:

i40iw_puda_qp_create
====================

.. c:function:: enum i40iw_status_code i40iw_puda_qp_create(struct i40iw_puda_rsrc *rsrc)

    create qp for resource

    :param rsrc:
        resource to use for buffer
    :type rsrc: struct i40iw_puda_rsrc \*

.. _`i40iw_puda_cq_wqe`:

i40iw_puda_cq_wqe
=================

.. c:function:: enum i40iw_status_code i40iw_puda_cq_wqe(struct i40iw_sc_dev *dev, struct i40iw_sc_cq *cq)

    setup wqe for cq create

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param cq:
        *undescribed*
    :type cq: struct i40iw_sc_cq \*

.. _`i40iw_puda_cq_create`:

i40iw_puda_cq_create
====================

.. c:function:: enum i40iw_status_code i40iw_puda_cq_create(struct i40iw_puda_rsrc *rsrc)

    create cq for resource

    :param rsrc:
        resource for which cq to create
    :type rsrc: struct i40iw_puda_rsrc \*

.. _`i40iw_puda_free_qp`:

i40iw_puda_free_qp
==================

.. c:function:: void i40iw_puda_free_qp(struct i40iw_puda_rsrc *rsrc)

    free qp for resource

    :param rsrc:
        resource for which qp to free
    :type rsrc: struct i40iw_puda_rsrc \*

.. _`i40iw_puda_free_cq`:

i40iw_puda_free_cq
==================

.. c:function:: void i40iw_puda_free_cq(struct i40iw_puda_rsrc *rsrc)

    free cq for resource

    :param rsrc:
        resource for which cq to free
    :type rsrc: struct i40iw_puda_rsrc \*

.. _`i40iw_puda_dele_resources`:

i40iw_puda_dele_resources
=========================

.. c:function:: void i40iw_puda_dele_resources(struct i40iw_sc_vsi *vsi, enum puda_resource_type type, bool reset)

    delete all resources during close

    :param vsi:
        *undescribed*
    :type vsi: struct i40iw_sc_vsi \*

    :param type:
        type of resource to dele
    :type type: enum puda_resource_type

    :param reset:
        true if reset chip
    :type reset: bool

.. _`i40iw_puda_allocbufs`:

i40iw_puda_allocbufs
====================

.. c:function:: enum i40iw_status_code i40iw_puda_allocbufs(struct i40iw_puda_rsrc *rsrc, u32 count)

    allocate buffers for resource

    :param rsrc:
        resource for buffer allocation
    :type rsrc: struct i40iw_puda_rsrc \*

    :param count:
        number of buffers to create
    :type count: u32

.. _`i40iw_puda_create_rsrc`:

i40iw_puda_create_rsrc
======================

.. c:function:: enum i40iw_status_code i40iw_puda_create_rsrc(struct i40iw_sc_vsi *vsi, struct i40iw_puda_rsrc_info *info)

    create resouce (ilq or ieq)

    :param vsi:
        *undescribed*
    :type vsi: struct i40iw_sc_vsi \*

    :param info:
        resource information
    :type info: struct i40iw_puda_rsrc_info \*

.. _`i40iw_ilq_putback_rcvbuf`:

i40iw_ilq_putback_rcvbuf
========================

.. c:function:: void i40iw_ilq_putback_rcvbuf(struct i40iw_sc_qp *qp, u32 wqe_idx)

    ilq buffer to put back on rq

    :param qp:
        ilq's qp resource
    :type qp: struct i40iw_sc_qp \*

    :param wqe_idx:
        wqe index of completed rcvbuf
    :type wqe_idx: u32

.. _`i40iw_ieq_get_fpdu_length`:

i40iw_ieq_get_fpdu_length
=========================

.. c:function:: u16 i40iw_ieq_get_fpdu_length(u16 length)

    given length return fpdu length

    :param length:
        length if fpdu
    :type length: u16

.. _`i40iw_ieq_copy_to_txbuf`:

i40iw_ieq_copy_to_txbuf
=======================

.. c:function:: void i40iw_ieq_copy_to_txbuf(struct i40iw_puda_buf *buf, struct i40iw_puda_buf *txbuf, u16 buf_offset, u32 txbuf_offset, u32 length)

    copydata from rcv buf to tx buf

    :param buf:
        rcv buffer with partial
    :type buf: struct i40iw_puda_buf \*

    :param txbuf:
        tx buffer for sendign back
    :type txbuf: struct i40iw_puda_buf \*

    :param buf_offset:
        rcv buffer offset to copy from
    :type buf_offset: u16

    :param txbuf_offset:
        at offset in tx buf to copy
    :type txbuf_offset: u32

    :param length:
        length of data to copy
    :type length: u32

.. _`i40iw_ieq_setup_tx_buf`:

i40iw_ieq_setup_tx_buf
======================

.. c:function:: void i40iw_ieq_setup_tx_buf(struct i40iw_puda_buf *buf, struct i40iw_puda_buf *txbuf)

    setup tx buffer for partial handling

    :param buf:
        reeive buffer with partial
    :type buf: struct i40iw_puda_buf \*

    :param txbuf:
        buffer to prepare
    :type txbuf: struct i40iw_puda_buf \*

.. _`i40iw_ieq_check_first_buf`:

i40iw_ieq_check_first_buf
=========================

.. c:function:: void i40iw_ieq_check_first_buf(struct i40iw_puda_buf *buf, u32 fps)

    check if rcv buffer's seq is in range

    :param buf:
        receive exception buffer
    :type buf: struct i40iw_puda_buf \*

    :param fps:
        first partial sequence number
    :type fps: u32

.. _`i40iw_ieq_compl_pfpdu`:

i40iw_ieq_compl_pfpdu
=====================

.. c:function:: void i40iw_ieq_compl_pfpdu(struct i40iw_puda_rsrc *ieq, struct list_head *rxlist, struct list_head *pbufl, struct i40iw_puda_buf *txbuf, u16 fpdu_len)

    write txbuf with full fpdu

    :param ieq:
        ieq resource
    :type ieq: struct i40iw_puda_rsrc \*

    :param rxlist:
        ieq's received buffer list
    :type rxlist: struct list_head \*

    :param pbufl:
        temporary list for buffers for fpddu
    :type pbufl: struct list_head \*

    :param txbuf:
        tx buffer for fpdu
    :type txbuf: struct i40iw_puda_buf \*

    :param fpdu_len:
        total length of fpdu
    :type fpdu_len: u16

.. _`i40iw_ieq_create_pbufl`:

i40iw_ieq_create_pbufl
======================

.. c:function:: enum i40iw_status_code i40iw_ieq_create_pbufl(struct i40iw_pfpdu *pfpdu, struct list_head *rxlist, struct list_head *pbufl, struct i40iw_puda_buf *buf, u16 fpdu_len)

    create buffer list for single fpdu

    :param pfpdu:
        *undescribed*
    :type pfpdu: struct i40iw_pfpdu \*

    :param rxlist:
        resource list for receive ieq buffes
    :type rxlist: struct list_head \*

    :param pbufl:
        temp. list for buffers for fpddu
    :type pbufl: struct list_head \*

    :param buf:
        first receive buffer
    :type buf: struct i40iw_puda_buf \*

    :param fpdu_len:
        total length of fpdu
    :type fpdu_len: u16

.. _`i40iw_ieq_handle_partial`:

i40iw_ieq_handle_partial
========================

.. c:function:: enum i40iw_status_code i40iw_ieq_handle_partial(struct i40iw_puda_rsrc *ieq, struct i40iw_pfpdu *pfpdu, struct i40iw_puda_buf *buf, u16 fpdu_len)

    process partial fpdu buffer

    :param ieq:
        ieq resource
    :type ieq: struct i40iw_puda_rsrc \*

    :param pfpdu:
        partial management per user qp
    :type pfpdu: struct i40iw_pfpdu \*

    :param buf:
        receive buffer
    :type buf: struct i40iw_puda_buf \*

    :param fpdu_len:
        fpdu len in the buffer
    :type fpdu_len: u16

.. _`i40iw_ieq_process_buf`:

i40iw_ieq_process_buf
=====================

.. c:function:: enum i40iw_status_code i40iw_ieq_process_buf(struct i40iw_puda_rsrc *ieq, struct i40iw_pfpdu *pfpdu, struct i40iw_puda_buf *buf)

    process buffer rcvd for ieq

    :param ieq:
        ieq resource
    :type ieq: struct i40iw_puda_rsrc \*

    :param pfpdu:
        partial management per user qp
    :type pfpdu: struct i40iw_pfpdu \*

    :param buf:
        receive buffer
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_ieq_process_fpdus`:

i40iw_ieq_process_fpdus
=======================

.. c:function:: void i40iw_ieq_process_fpdus(struct i40iw_sc_qp *qp, struct i40iw_puda_rsrc *ieq)

    process fpdu's buffers on its list

    :param qp:
        qp for which partial fpdus
    :type qp: struct i40iw_sc_qp \*

    :param ieq:
        ieq resource
    :type ieq: struct i40iw_puda_rsrc \*

.. _`i40iw_ieq_handle_exception`:

i40iw_ieq_handle_exception
==========================

.. c:function:: void i40iw_ieq_handle_exception(struct i40iw_puda_rsrc *ieq, struct i40iw_sc_qp *qp, struct i40iw_puda_buf *buf)

    handle qp's exception

    :param ieq:
        ieq resource
    :type ieq: struct i40iw_puda_rsrc \*

    :param qp:
        qp receiving excpetion
    :type qp: struct i40iw_sc_qp \*

    :param buf:
        receive buffer
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_ieq_receive`:

i40iw_ieq_receive
=================

.. c:function:: void i40iw_ieq_receive(struct i40iw_sc_vsi *vsi, struct i40iw_puda_buf *buf)

    received exception buffer

    :param vsi:
        *undescribed*
    :type vsi: struct i40iw_sc_vsi \*

    :param buf:
        exception buffer received
    :type buf: struct i40iw_puda_buf \*

.. _`i40iw_ieq_tx_compl`:

i40iw_ieq_tx_compl
==================

.. c:function:: void i40iw_ieq_tx_compl(struct i40iw_sc_vsi *vsi, void *sqwrid)

    put back after sending completed exception buffer

    :param vsi:
        pointer to the vsi structure
    :type vsi: struct i40iw_sc_vsi \*

    :param sqwrid:
        pointer to puda buffer
    :type sqwrid: void \*

.. _`i40iw_ieq_cleanup_qp`:

i40iw_ieq_cleanup_qp
====================

.. c:function:: void i40iw_ieq_cleanup_qp(struct i40iw_puda_rsrc *ieq, struct i40iw_sc_qp *qp)

    qp is being destroyed

    :param ieq:
        ieq resource
    :type ieq: struct i40iw_puda_rsrc \*

    :param qp:
        all pending fpdu buffers
    :type qp: struct i40iw_sc_qp \*

.. This file was automatic generated / don't edit.

