.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_mgt.c

.. _`nes_mgt_rq_wqes_timeout`:

nes_mgt_rq_wqes_timeout
=======================

.. c:function:: void nes_mgt_rq_wqes_timeout(unsigned long parm)

    :param unsigned long parm:
        *undescribed*

.. _`nes_mgt_free_skb`:

nes_mgt_free_skb
================

.. c:function:: void nes_mgt_free_skb(struct nes_device *nesdev, struct sk_buff *skb, u32 dir)

    unmap and free skb

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param u32 dir:
        *undescribed*

.. _`nes_download_callback`:

nes_download_callback
=====================

.. c:function:: void nes_download_callback(struct nes_device *nesdev, struct nes_cqp_request *cqp_request)

    handle download completions

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_cqp_request \*cqp_request:
        *undescribed*

.. _`nes_get_seq`:

nes_get_seq
===========

.. c:function:: u32 nes_get_seq(struct sk_buff *skb, u32 *ack, u16 *wnd, u32 *fin_rcvd, u32 *rst_rcvd)

    Get the seq, ack_seq and window from the packet

    :param struct sk_buff \*skb:
        *undescribed*

    :param u32 \*ack:
        *undescribed*

    :param u16 \*wnd:
        *undescribed*

    :param u32 \*fin_rcvd:
        *undescribed*

    :param u32 \*rst_rcvd:
        *undescribed*

.. _`nes_get_next_skb`:

nes_get_next_skb
================

.. c:function:: struct sk_buff *nes_get_next_skb(struct nes_device *nesdev, struct nes_qp *nesqp, struct sk_buff *skb, u32 nextseq, u32 *ack, u16 *wnd, u32 *fin_rcvd, u32 *rst_rcvd)

    Get the next skb based on where current skb is in the queue

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param u32 nextseq:
        *undescribed*

    :param u32 \*ack:
        *undescribed*

    :param u16 \*wnd:
        *undescribed*

    :param u32 \*fin_rcvd:
        *undescribed*

    :param u32 \*rst_rcvd:
        *undescribed*

.. _`get_fpdu_info`:

get_fpdu_info
=============

.. c:function:: int get_fpdu_info(struct nes_device *nesdev, struct nes_qp *nesqp, struct pau_fpdu_info **pau_fpdu_info)

    Find the next complete fpdu and return its fragments.

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param struct pau_fpdu_info \*\*pau_fpdu_info:
        *undescribed*

.. _`forward_fpdus`:

forward_fpdus
=============

.. c:function:: int forward_fpdus(struct nes_vnic *nesvnic, struct nes_qp *nesqp)

    send complete fpdus, one at a time

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

.. _`queue_fpdus`:

queue_fpdus
===========

.. c:function:: void queue_fpdus(struct sk_buff *skb, struct nes_vnic *nesvnic, struct nes_qp *nesqp)

    Handle fpdu's that hw passed up to sw

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

.. _`mgt_thread`:

mgt_thread
==========

.. c:function:: int mgt_thread(void *context)

    Handle mgt skbs in a safe context

    :param void \*context:
        *undescribed*

.. _`nes_queue_mgt_skbs`:

nes_queue_mgt_skbs
==================

.. c:function:: void nes_queue_mgt_skbs(struct sk_buff *skb, struct nes_vnic *nesvnic, struct nes_qp *nesqp)

    Queue skb so it can be handled in a thread context

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

.. _`nes_change_quad_hash`:

nes_change_quad_hash
====================

.. c:function:: int nes_change_quad_hash(struct nes_device *nesdev, struct nes_vnic *nesvnic, struct nes_qp *nesqp)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

.. _`nes_mgt_ce_handler`:

nes_mgt_ce_handler
==================

.. c:function:: void nes_mgt_ce_handler(struct nes_device *nesdev, struct nes_hw_nic_cq *cq)

    This management code deals with any packed and unaligned (pau) fpdu's that the hardware cannot handle.

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_hw_nic_cq \*cq:
        *undescribed*

.. _`nes_init_mgt_qp`:

nes_init_mgt_qp
===============

.. c:function:: int nes_init_mgt_qp(struct nes_device *nesdev, struct net_device *netdev, struct nes_vnic *nesvnic)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct net_device \*netdev:
        *undescribed*

    :param struct nes_vnic \*nesvnic:
        *undescribed*

.. This file was automatic generated / don't edit.

