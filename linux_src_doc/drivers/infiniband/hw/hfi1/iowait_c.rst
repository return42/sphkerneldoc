.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/iowait.c

.. _`iowait_init`:

iowait_init
===========

.. c:function:: void iowait_init(struct iowait *wait, u32 tx_limit, void (*func)(struct work_struct *work), void (*tidfunc)(struct work_struct *work), int (*sleep)(struct sdma_engine *sde, struct iowait_work *wait, struct sdma_txreq *tx, uint seq, bool pkts_sent), void (*wakeup)(struct iowait *wait, int reason), void (*sdma_drained)(struct iowait *wait))

    initialize wait structure

    :param wait:
        wait struct to initialize
    :type wait: struct iowait \*

    :param tx_limit:
        limit for overflow queuing
    :type tx_limit: u32

    :param void (\*func)(struct work_struct \*work):
        restart function for workqueue

    :param void (\*tidfunc)(struct work_struct \*work):
        *undescribed*

    :param int (\*sleep)(struct sdma_engine \*sde, struct iowait_work \*wait, struct sdma_txreq \*tx, uint seq, bool pkts_sent):
        sleep function for no space

    :param void (\*wakeup)(struct iowait \*wait, int reason):
        *undescribed*

    :param void (\*sdma_drained)(struct iowait \*wait):
        *undescribed*

.. _`iowait_init.description`:

Description
-----------

This function initializes the iowait
structure embedded in the QP or PQ.

.. _`iowait_cancel_work`:

iowait_cancel_work
==================

.. c:function:: void iowait_cancel_work(struct iowait *w)

    cancel all work in iowait

    :param w:
        the iowait struct
    :type w: struct iowait \*

.. _`iowait_set_work_flag`:

iowait_set_work_flag
====================

.. c:function:: int iowait_set_work_flag(struct iowait_work *w)

    set work flag based on leg \ ``w``\  - the iowait work struct

    :param w:
        *undescribed*
    :type w: struct iowait_work \*

.. This file was automatic generated / don't edit.

