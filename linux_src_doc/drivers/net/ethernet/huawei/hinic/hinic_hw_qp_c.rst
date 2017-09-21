.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_qp.c

.. _`alloc_sq_skb_arr`:

alloc_sq_skb_arr
================

.. c:function:: int alloc_sq_skb_arr(struct hinic_sq *sq)

    allocate sq array for saved skb

    :param struct hinic_sq \*sq:
        HW Send Queue

.. _`alloc_sq_skb_arr.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_sq_skb_arr`:

free_sq_skb_arr
===============

.. c:function:: void free_sq_skb_arr(struct hinic_sq *sq)

    free sq array for saved skb

    :param struct hinic_sq \*sq:
        HW Send Queue

.. _`alloc_rq_skb_arr`:

alloc_rq_skb_arr
================

.. c:function:: int alloc_rq_skb_arr(struct hinic_rq *rq)

    allocate rq array for saved skb

    :param struct hinic_rq \*rq:
        HW Receive Queue

.. _`alloc_rq_skb_arr.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_rq_skb_arr`:

free_rq_skb_arr
===============

.. c:function:: void free_rq_skb_arr(struct hinic_rq *rq)

    free rq array for saved skb

    :param struct hinic_rq \*rq:
        HW Receive Queue

.. _`hinic_init_sq`:

hinic_init_sq
=============

.. c:function:: int hinic_init_sq(struct hinic_sq *sq, struct hinic_hwif *hwif, struct hinic_wq *wq, struct msix_entry *entry, void *ci_addr, dma_addr_t ci_dma_addr, void __iomem *db_base)

    Initialize HW Send Queue

    :param struct hinic_sq \*sq:
        HW Send Queue

    :param struct hinic_hwif \*hwif:
        HW Interface for accessing HW

    :param struct hinic_wq \*wq:
        Work Queue for the data of the SQ

    :param struct msix_entry \*entry:
        msix entry for sq

    :param void \*ci_addr:
        address for reading the current HW consumer index

    :param dma_addr_t ci_dma_addr:
        dma address for reading the current HW consumer index

    :param void __iomem \*db_base:
        doorbell base address

.. _`hinic_init_sq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_clean_sq`:

hinic_clean_sq
==============

.. c:function:: void hinic_clean_sq(struct hinic_sq *sq)

    Clean HW Send Queue's Resources

    :param struct hinic_sq \*sq:
        Send Queue

.. _`alloc_rq_cqe`:

alloc_rq_cqe
============

.. c:function:: int alloc_rq_cqe(struct hinic_rq *rq)

    allocate rq completion queue elements

    :param struct hinic_rq \*rq:
        HW Receive Queue

.. _`alloc_rq_cqe.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_rq_cqe`:

free_rq_cqe
===========

.. c:function:: void free_rq_cqe(struct hinic_rq *rq)

    free rq completion queue elements

    :param struct hinic_rq \*rq:
        HW Receive Queue

.. _`hinic_init_rq`:

hinic_init_rq
=============

.. c:function:: int hinic_init_rq(struct hinic_rq *rq, struct hinic_hwif *hwif, struct hinic_wq *wq, struct msix_entry *entry)

    Initialize HW Receive Queue

    :param struct hinic_rq \*rq:
        HW Receive Queue

    :param struct hinic_hwif \*hwif:
        HW Interface for accessing HW

    :param struct hinic_wq \*wq:
        Work Queue for the data of the RQ

    :param struct msix_entry \*entry:
        msix entry for rq

.. _`hinic_init_rq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_clean_rq`:

hinic_clean_rq
==============

.. c:function:: void hinic_clean_rq(struct hinic_rq *rq)

    Clean HW Receive Queue's Resources

    :param struct hinic_rq \*rq:
        HW Receive Queue

.. _`hinic_get_sq_free_wqebbs`:

hinic_get_sq_free_wqebbs
========================

.. c:function:: int hinic_get_sq_free_wqebbs(struct hinic_sq *sq)

    return number of free wqebbs for use

    :param struct hinic_sq \*sq:
        send queue

.. _`hinic_get_sq_free_wqebbs.description`:

Description
-----------

Return number of free wqebbs

.. _`hinic_get_rq_free_wqebbs`:

hinic_get_rq_free_wqebbs
========================

.. c:function:: int hinic_get_rq_free_wqebbs(struct hinic_rq *rq)

    return number of free wqebbs for use

    :param struct hinic_rq \*rq:
        recv queue

.. _`hinic_get_rq_free_wqebbs.description`:

Description
-----------

Return number of free wqebbs

.. _`hinic_sq_prepare_wqe`:

hinic_sq_prepare_wqe
====================

.. c:function:: void hinic_sq_prepare_wqe(struct hinic_sq *sq, u16 prod_idx, struct hinic_sq_wqe *sq_wqe, struct hinic_sge *sges, int nr_sges)

    prepare wqe before insert to the queue

    :param struct hinic_sq \*sq:
        send queue

    :param u16 prod_idx:
        pi value

    :param struct hinic_sq_wqe \*sq_wqe:
        wqe to prepare

    :param struct hinic_sge \*sges:
        sges for use by the wqe for send for buf addresses

    :param int nr_sges:
        number of sges

.. _`sq_prepare_db`:

sq_prepare_db
=============

.. c:function:: u32 sq_prepare_db(struct hinic_sq *sq, u16 prod_idx, unsigned int cos)

    prepare doorbell to write

    :param struct hinic_sq \*sq:
        send queue

    :param u16 prod_idx:
        pi value for the doorbell

    :param unsigned int cos:
        cos of the doorbell

.. _`sq_prepare_db.description`:

Description
-----------

Return db value

.. _`hinic_sq_write_db`:

hinic_sq_write_db
=================

.. c:function:: void hinic_sq_write_db(struct hinic_sq *sq, u16 prod_idx, unsigned int wqe_size, unsigned int cos)

    write doorbell

    :param struct hinic_sq \*sq:
        send queue

    :param u16 prod_idx:
        pi value for the doorbell

    :param unsigned int wqe_size:
        wqe size

    :param unsigned int cos:
        cos of the wqe

.. _`hinic_sq_get_wqe`:

hinic_sq_get_wqe
================

.. c:function:: struct hinic_sq_wqe *hinic_sq_get_wqe(struct hinic_sq *sq, unsigned int wqe_size, u16 *prod_idx)

    get wqe ptr in the current pi and update the pi

    :param struct hinic_sq \*sq:
        sq to get wqe from

    :param unsigned int wqe_size:
        wqe size

    :param u16 \*prod_idx:
        returned pi

.. _`hinic_sq_get_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_sq_write_wqe`:

hinic_sq_write_wqe
==================

.. c:function:: void hinic_sq_write_wqe(struct hinic_sq *sq, u16 prod_idx, struct hinic_sq_wqe *sq_wqe, struct sk_buff *skb, unsigned int wqe_size)

    write the wqe to the sq

    :param struct hinic_sq \*sq:
        send queue

    :param u16 prod_idx:
        pi of the wqe

    :param struct hinic_sq_wqe \*sq_wqe:
        the wqe to write

    :param struct sk_buff \*skb:
        skb to save

    :param unsigned int wqe_size:
        the size of the wqe

.. _`hinic_sq_read_wqe`:

hinic_sq_read_wqe
=================

.. c:function:: struct hinic_sq_wqe *hinic_sq_read_wqe(struct hinic_sq *sq, struct sk_buff **skb, unsigned int *wqe_size, u16 *cons_idx)

    read wqe ptr in the current ci and update the ci

    :param struct hinic_sq \*sq:
        send queue

    :param struct sk_buff \*\*skb:
        return skb that was saved

    :param unsigned int \*wqe_size:
        the size of the wqe

    :param u16 \*cons_idx:
        consumer index of the wqe

.. _`hinic_sq_read_wqe.description`:

Description
-----------

Return wqe in ci position

.. _`hinic_sq_put_wqe`:

hinic_sq_put_wqe
================

.. c:function:: void hinic_sq_put_wqe(struct hinic_sq *sq, unsigned int wqe_size)

    release the ci for new wqes

    :param struct hinic_sq \*sq:
        send queue

    :param unsigned int wqe_size:
        the size of the wqe

.. _`hinic_sq_get_sges`:

hinic_sq_get_sges
=================

.. c:function:: void hinic_sq_get_sges(struct hinic_sq_wqe *sq_wqe, struct hinic_sge *sges, int nr_sges)

    get sges from the wqe

    :param struct hinic_sq_wqe \*sq_wqe:
        wqe to get the sges from its buffer addresses

    :param struct hinic_sge \*sges:
        returned sges

    :param int nr_sges:
        number sges to return

.. _`hinic_rq_get_wqe`:

hinic_rq_get_wqe
================

.. c:function:: struct hinic_rq_wqe *hinic_rq_get_wqe(struct hinic_rq *rq, unsigned int wqe_size, u16 *prod_idx)

    get wqe ptr in the current pi and update the pi

    :param struct hinic_rq \*rq:
        rq to get wqe from

    :param unsigned int wqe_size:
        wqe size

    :param u16 \*prod_idx:
        returned pi

.. _`hinic_rq_get_wqe.description`:

Description
-----------

Return wqe pointer

.. _`hinic_rq_write_wqe`:

hinic_rq_write_wqe
==================

.. c:function:: void hinic_rq_write_wqe(struct hinic_rq *rq, u16 prod_idx, struct hinic_rq_wqe *rq_wqe, struct sk_buff *skb)

    write the wqe to the rq

    :param struct hinic_rq \*rq:
        recv queue

    :param u16 prod_idx:
        pi of the wqe

    :param struct hinic_rq_wqe \*rq_wqe:
        the wqe to write

    :param struct sk_buff \*skb:
        skb to save

.. _`hinic_rq_read_wqe`:

hinic_rq_read_wqe
=================

.. c:function:: struct hinic_rq_wqe *hinic_rq_read_wqe(struct hinic_rq *rq, unsigned int wqe_size, struct sk_buff **skb, u16 *cons_idx)

    read wqe ptr in the current ci and update the ci

    :param struct hinic_rq \*rq:
        recv queue

    :param unsigned int wqe_size:
        the size of the wqe

    :param struct sk_buff \*\*skb:
        return saved skb

    :param u16 \*cons_idx:
        consumer index of the wqe

.. _`hinic_rq_read_wqe.description`:

Description
-----------

Return wqe in ci position

.. _`hinic_rq_read_next_wqe`:

hinic_rq_read_next_wqe
======================

.. c:function:: struct hinic_rq_wqe *hinic_rq_read_next_wqe(struct hinic_rq *rq, unsigned int wqe_size, struct sk_buff **skb, u16 *cons_idx)

    increment ci and read the wqe in ci position

    :param struct hinic_rq \*rq:
        recv queue

    :param unsigned int wqe_size:
        the size of the wqe

    :param struct sk_buff \*\*skb:
        return saved skb

    :param u16 \*cons_idx:
        consumer index in the wq

.. _`hinic_rq_read_next_wqe.description`:

Description
-----------

Return wqe in incremented ci position

.. _`hinic_rq_put_wqe`:

hinic_rq_put_wqe
================

.. c:function:: void hinic_rq_put_wqe(struct hinic_rq *rq, u16 cons_idx, unsigned int wqe_size)

    release the ci for new wqes

    :param struct hinic_rq \*rq:
        recv queue

    :param u16 cons_idx:
        consumer index of the wqe

    :param unsigned int wqe_size:
        the size of the wqe

.. _`hinic_rq_get_sge`:

hinic_rq_get_sge
================

.. c:function:: void hinic_rq_get_sge(struct hinic_rq *rq, struct hinic_rq_wqe *rq_wqe, u16 cons_idx, struct hinic_sge *sge)

    get sge from the wqe

    :param struct hinic_rq \*rq:
        recv queue

    :param struct hinic_rq_wqe \*rq_wqe:
        wqe to get the sge from its buf address

    :param u16 cons_idx:
        consumer index

    :param struct hinic_sge \*sge:
        returned sge

.. _`hinic_rq_prepare_wqe`:

hinic_rq_prepare_wqe
====================

.. c:function:: void hinic_rq_prepare_wqe(struct hinic_rq *rq, u16 prod_idx, struct hinic_rq_wqe *rq_wqe, struct hinic_sge *sge)

    prepare wqe before insert to the queue

    :param struct hinic_rq \*rq:
        recv queue

    :param u16 prod_idx:
        pi value

    :param struct hinic_rq_wqe \*rq_wqe:
        the wqe

    :param struct hinic_sge \*sge:
        sge for use by the wqe for recv buf address

.. _`hinic_rq_update`:

hinic_rq_update
===============

.. c:function:: void hinic_rq_update(struct hinic_rq *rq, u16 prod_idx)

    update pi of the rq

    :param struct hinic_rq \*rq:
        recv queue

    :param u16 prod_idx:
        pi value

.. This file was automatic generated / don't edit.

