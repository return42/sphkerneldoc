.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_qp.c

.. _`alloc_sq_skb_arr`:

alloc_sq_skb_arr
================

.. c:function:: int alloc_sq_skb_arr(struct hinic_sq *sq)

    allocate sq array for saved skb

    :param sq:
        HW Send Queue
    :type sq: struct hinic_sq \*

.. _`alloc_sq_skb_arr.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_sq_skb_arr`:

free_sq_skb_arr
===============

.. c:function:: void free_sq_skb_arr(struct hinic_sq *sq)

    free sq array for saved skb

    :param sq:
        HW Send Queue
    :type sq: struct hinic_sq \*

.. _`alloc_rq_skb_arr`:

alloc_rq_skb_arr
================

.. c:function:: int alloc_rq_skb_arr(struct hinic_rq *rq)

    allocate rq array for saved skb

    :param rq:
        HW Receive Queue
    :type rq: struct hinic_rq \*

.. _`alloc_rq_skb_arr.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_rq_skb_arr`:

free_rq_skb_arr
===============

.. c:function:: void free_rq_skb_arr(struct hinic_rq *rq)

    free rq array for saved skb

    :param rq:
        HW Receive Queue
    :type rq: struct hinic_rq \*

.. _`hinic_init_sq`:

hinic_init_sq
=============

.. c:function:: int hinic_init_sq(struct hinic_sq *sq, struct hinic_hwif *hwif, struct hinic_wq *wq, struct msix_entry *entry, void *ci_addr, dma_addr_t ci_dma_addr, void __iomem *db_base)

    Initialize HW Send Queue

    :param sq:
        HW Send Queue
    :type sq: struct hinic_sq \*

    :param hwif:
        HW Interface for accessing HW
    :type hwif: struct hinic_hwif \*

    :param wq:
        Work Queue for the data of the SQ
    :type wq: struct hinic_wq \*

    :param entry:
        msix entry for sq
    :type entry: struct msix_entry \*

    :param ci_addr:
        address for reading the current HW consumer index
    :type ci_addr: void \*

    :param ci_dma_addr:
        dma address for reading the current HW consumer index
    :type ci_dma_addr: dma_addr_t

    :param db_base:
        doorbell base address
    :type db_base: void __iomem \*

.. _`hinic_init_sq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_clean_sq`:

hinic_clean_sq
==============

.. c:function:: void hinic_clean_sq(struct hinic_sq *sq)

    Clean HW Send Queue's Resources

    :param sq:
        Send Queue
    :type sq: struct hinic_sq \*

.. _`alloc_rq_cqe`:

alloc_rq_cqe
============

.. c:function:: int alloc_rq_cqe(struct hinic_rq *rq)

    allocate rq completion queue elements

    :param rq:
        HW Receive Queue
    :type rq: struct hinic_rq \*

.. _`alloc_rq_cqe.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_rq_cqe`:

free_rq_cqe
===========

.. c:function:: void free_rq_cqe(struct hinic_rq *rq)

    free rq completion queue elements

    :param rq:
        HW Receive Queue
    :type rq: struct hinic_rq \*

.. _`hinic_init_rq`:

hinic_init_rq
=============

.. c:function:: int hinic_init_rq(struct hinic_rq *rq, struct hinic_hwif *hwif, struct hinic_wq *wq, struct msix_entry *entry)

    Initialize HW Receive Queue

    :param rq:
        HW Receive Queue
    :type rq: struct hinic_rq \*

    :param hwif:
        HW Interface for accessing HW
    :type hwif: struct hinic_hwif \*

    :param wq:
        Work Queue for the data of the RQ
    :type wq: struct hinic_wq \*

    :param entry:
        msix entry for rq
    :type entry: struct msix_entry \*

.. _`hinic_init_rq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_clean_rq`:

hinic_clean_rq
==============

.. c:function:: void hinic_clean_rq(struct hinic_rq *rq)

    Clean HW Receive Queue's Resources

    :param rq:
        HW Receive Queue
    :type rq: struct hinic_rq \*

.. _`hinic_get_sq_free_wqebbs`:

hinic_get_sq_free_wqebbs
========================

.. c:function:: int hinic_get_sq_free_wqebbs(struct hinic_sq *sq)

    return number of free wqebbs for use

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

.. _`hinic_get_sq_free_wqebbs.description`:

Description
-----------

Return number of free wqebbs

.. _`hinic_get_rq_free_wqebbs`:

hinic_get_rq_free_wqebbs
========================

.. c:function:: int hinic_get_rq_free_wqebbs(struct hinic_rq *rq)

    return number of free wqebbs for use

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

.. _`hinic_get_rq_free_wqebbs.description`:

Description
-----------

Return number of free wqebbs

.. _`hinic_sq_prepare_wqe`:

hinic_sq_prepare_wqe
====================

.. c:function:: void hinic_sq_prepare_wqe(struct hinic_sq *sq, u16 prod_idx, struct hinic_sq_wqe *sq_wqe, struct hinic_sge *sges, int nr_sges)

    prepare wqe before insert to the queue

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param prod_idx:
        pi value
    :type prod_idx: u16

    :param sq_wqe:
        wqe to prepare
    :type sq_wqe: struct hinic_sq_wqe \*

    :param sges:
        sges for use by the wqe for send for buf addresses
    :type sges: struct hinic_sge \*

    :param nr_sges:
        number of sges
    :type nr_sges: int

.. _`sq_prepare_db`:

sq_prepare_db
=============

.. c:function:: u32 sq_prepare_db(struct hinic_sq *sq, u16 prod_idx, unsigned int cos)

    prepare doorbell to write

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param prod_idx:
        pi value for the doorbell
    :type prod_idx: u16

    :param cos:
        cos of the doorbell
    :type cos: unsigned int

.. _`sq_prepare_db.description`:

Description
-----------

Return db value

.. _`hinic_sq_write_db`:

hinic_sq_write_db
=================

.. c:function:: void hinic_sq_write_db(struct hinic_sq *sq, u16 prod_idx, unsigned int wqe_size, unsigned int cos)

    write doorbell

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param prod_idx:
        pi value for the doorbell
    :type prod_idx: u16

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

    :param cos:
        cos of the wqe
    :type cos: unsigned int

.. _`hinic_sq_get_wqe`:

hinic_sq_get_wqe
================

.. c:function:: struct hinic_sq_wqe *hinic_sq_get_wqe(struct hinic_sq *sq, unsigned int wqe_size, u16 *prod_idx)

    get wqe ptr in the current pi and update the pi

    :param sq:
        sq to get wqe from
    :type sq: struct hinic_sq \*

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

    :param prod_idx:
        returned pi
    :type prod_idx: u16 \*

.. _`hinic_sq_get_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_sq_return_wqe`:

hinic_sq_return_wqe
===================

.. c:function:: void hinic_sq_return_wqe(struct hinic_sq *sq, unsigned int wqe_size)

    return the wqe to the sq

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param wqe_size:
        the size of the wqe
    :type wqe_size: unsigned int

.. _`hinic_sq_write_wqe`:

hinic_sq_write_wqe
==================

.. c:function:: void hinic_sq_write_wqe(struct hinic_sq *sq, u16 prod_idx, struct hinic_sq_wqe *sq_wqe, struct sk_buff *skb, unsigned int wqe_size)

    write the wqe to the sq

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param prod_idx:
        pi of the wqe
    :type prod_idx: u16

    :param sq_wqe:
        the wqe to write
    :type sq_wqe: struct hinic_sq_wqe \*

    :param skb:
        skb to save
    :type skb: struct sk_buff \*

    :param wqe_size:
        the size of the wqe
    :type wqe_size: unsigned int

.. _`hinic_sq_read_wqebb`:

hinic_sq_read_wqebb
===================

.. c:function:: struct hinic_sq_wqe *hinic_sq_read_wqebb(struct hinic_sq *sq, struct sk_buff **skb, unsigned int *wqe_size, u16 *cons_idx)

    read wqe ptr in the current ci and update the ci, the wqe only have one wqebb

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param skb:
        return skb that was saved
    :type skb: struct sk_buff \*\*

    :param wqe_size:
        the wqe size ptr
    :type wqe_size: unsigned int \*

    :param cons_idx:
        consumer index of the wqe
    :type cons_idx: u16 \*

.. _`hinic_sq_read_wqebb.description`:

Description
-----------

Return wqe in ci position

.. _`hinic_sq_read_wqe`:

hinic_sq_read_wqe
=================

.. c:function:: struct hinic_sq_wqe *hinic_sq_read_wqe(struct hinic_sq *sq, struct sk_buff **skb, unsigned int wqe_size, u16 *cons_idx)

    read wqe ptr in the current ci and update the ci

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param skb:
        return skb that was saved
    :type skb: struct sk_buff \*\*

    :param wqe_size:
        the size of the wqe
    :type wqe_size: unsigned int

    :param cons_idx:
        consumer index of the wqe
    :type cons_idx: u16 \*

.. _`hinic_sq_read_wqe.description`:

Description
-----------

Return wqe in ci position

.. _`hinic_sq_put_wqe`:

hinic_sq_put_wqe
================

.. c:function:: void hinic_sq_put_wqe(struct hinic_sq *sq, unsigned int wqe_size)

    release the ci for new wqes

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param wqe_size:
        the size of the wqe
    :type wqe_size: unsigned int

.. _`hinic_sq_get_sges`:

hinic_sq_get_sges
=================

.. c:function:: void hinic_sq_get_sges(struct hinic_sq_wqe *sq_wqe, struct hinic_sge *sges, int nr_sges)

    get sges from the wqe

    :param sq_wqe:
        wqe to get the sges from its buffer addresses
    :type sq_wqe: struct hinic_sq_wqe \*

    :param sges:
        returned sges
    :type sges: struct hinic_sge \*

    :param nr_sges:
        number sges to return
    :type nr_sges: int

.. _`hinic_rq_get_wqe`:

hinic_rq_get_wqe
================

.. c:function:: struct hinic_rq_wqe *hinic_rq_get_wqe(struct hinic_rq *rq, unsigned int wqe_size, u16 *prod_idx)

    get wqe ptr in the current pi and update the pi

    :param rq:
        rq to get wqe from
    :type rq: struct hinic_rq \*

    :param wqe_size:
        wqe size
    :type wqe_size: unsigned int

    :param prod_idx:
        returned pi
    :type prod_idx: u16 \*

.. _`hinic_rq_get_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_rq_write_wqe`:

hinic_rq_write_wqe
==================

.. c:function:: void hinic_rq_write_wqe(struct hinic_rq *rq, u16 prod_idx, struct hinic_rq_wqe *rq_wqe, struct sk_buff *skb)

    write the wqe to the rq

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

    :param prod_idx:
        pi of the wqe
    :type prod_idx: u16

    :param rq_wqe:
        the wqe to write
    :type rq_wqe: struct hinic_rq_wqe \*

    :param skb:
        skb to save
    :type skb: struct sk_buff \*

.. _`hinic_rq_read_wqe`:

hinic_rq_read_wqe
=================

.. c:function:: struct hinic_rq_wqe *hinic_rq_read_wqe(struct hinic_rq *rq, unsigned int wqe_size, struct sk_buff **skb, u16 *cons_idx)

    read wqe ptr in the current ci and update the ci

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

    :param wqe_size:
        the size of the wqe
    :type wqe_size: unsigned int

    :param skb:
        return saved skb
    :type skb: struct sk_buff \*\*

    :param cons_idx:
        consumer index of the wqe
    :type cons_idx: u16 \*

.. _`hinic_rq_read_wqe.description`:

Description
-----------

Return wqe in ci position

.. _`hinic_rq_read_next_wqe`:

hinic_rq_read_next_wqe
======================

.. c:function:: struct hinic_rq_wqe *hinic_rq_read_next_wqe(struct hinic_rq *rq, unsigned int wqe_size, struct sk_buff **skb, u16 *cons_idx)

    increment ci and read the wqe in ci position

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

    :param wqe_size:
        the size of the wqe
    :type wqe_size: unsigned int

    :param skb:
        return saved skb
    :type skb: struct sk_buff \*\*

    :param cons_idx:
        consumer index in the wq
    :type cons_idx: u16 \*

.. _`hinic_rq_read_next_wqe.description`:

Description
-----------

Return wqe in incremented ci position

.. _`hinic_rq_put_wqe`:

hinic_rq_put_wqe
================

.. c:function:: void hinic_rq_put_wqe(struct hinic_rq *rq, u16 cons_idx, unsigned int wqe_size)

    release the ci for new wqes

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

    :param cons_idx:
        consumer index of the wqe
    :type cons_idx: u16

    :param wqe_size:
        the size of the wqe
    :type wqe_size: unsigned int

.. _`hinic_rq_get_sge`:

hinic_rq_get_sge
================

.. c:function:: void hinic_rq_get_sge(struct hinic_rq *rq, struct hinic_rq_wqe *rq_wqe, u16 cons_idx, struct hinic_sge *sge)

    get sge from the wqe

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

    :param rq_wqe:
        wqe to get the sge from its buf address
    :type rq_wqe: struct hinic_rq_wqe \*

    :param cons_idx:
        consumer index
    :type cons_idx: u16

    :param sge:
        returned sge
    :type sge: struct hinic_sge \*

.. _`hinic_rq_prepare_wqe`:

hinic_rq_prepare_wqe
====================

.. c:function:: void hinic_rq_prepare_wqe(struct hinic_rq *rq, u16 prod_idx, struct hinic_rq_wqe *rq_wqe, struct hinic_sge *sge)

    prepare wqe before insert to the queue

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

    :param prod_idx:
        pi value
    :type prod_idx: u16

    :param rq_wqe:
        the wqe
    :type rq_wqe: struct hinic_rq_wqe \*

    :param sge:
        sge for use by the wqe for recv buf address
    :type sge: struct hinic_sge \*

.. _`hinic_rq_update`:

hinic_rq_update
===============

.. c:function:: void hinic_rq_update(struct hinic_rq *rq, u16 prod_idx)

    update pi of the rq

    :param rq:
        recv queue
    :type rq: struct hinic_rq \*

    :param prod_idx:
        pi value
    :type prod_idx: u16

.. This file was automatic generated / don't edit.

