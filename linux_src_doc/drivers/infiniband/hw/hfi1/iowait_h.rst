.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/iowait.h

.. _`iowait`:

struct iowait
=============

.. c:type:: struct iowait

    linkage for delayed progress/waiting

.. _`iowait.definition`:

Definition
----------

.. code-block:: c

    struct iowait {
        struct list_head list;
        struct list_head tx_head;
        int (*sleep)(struct sdma_engine *sde,struct iowait *wait,struct sdma_txreq *tx, unsigned seq);
        void (*wakeup)(struct iowait *wait, int reason);
        void (*sdma_drained)(struct iowait *wait);
        seqlock_t *lock;
        struct work_struct iowork;
        wait_queue_head_t wait_dma;
        wait_queue_head_t wait_pio;
        atomic_t sdma_busy;
        atomic_t pio_busy;
        u32 count;
        u32 tx_limit;
        u32 tx_count;
    }

.. _`iowait.members`:

Members
-------

list
    used to add/insert into QP/PQ wait lists

tx_head
    overflow list of sdma_txreq's

sleep
    no space callback

wakeup
    space callback wakeup

sdma_drained
    sdma count drained

lock
    uses to record the list head lock

iowork
    workqueue overhead

wait_dma
    wait for sdma_busy == 0

wait_pio
    wait for pio_busy == 0

sdma_busy
    # of packets in flight

pio_busy
    *undescribed*

count
    total number of descriptors in tx_head'ed list

tx_limit
    limit for overflow queuing

tx_count
    number of tx entry's in tx_head'ed list

.. _`iowait.description`:

Description
-----------

This is to be embedded in user's state structure
(QP or PQ).

The sleep and wakeup members are a
bit misnamed.   They do not strictly
speaking sleep or wake up, but they
are callbacks for the ULP to implement
what ever queuing/dequeuing of
the embedded iowait and its containing struct
when a resource shortage like SDMA ring space is seen.

Both potentially have locks help
so sleeping is not allowed.

The wait_dma member along with the iow

The lock field is used by waiters to record
the seqlock_t that guards the list head.
Waiters explicity know that, but the destroy
code that unwaits QPs does not.

.. _`iowait_init`:

iowait_init
===========

.. c:function:: void iowait_init(struct iowait *wait, u32 tx_limit, void (*func)(struct work_struct *work), int (*sleep)( struct sdma_engine *sde, struct iowait *wait, struct sdma_txreq *tx, unsigned seq), void (*wakeup)(struct iowait *wait, int reason), void (*sdma_drained)(struct iowait *wait))

    initialize wait structure

    :param struct iowait \*wait:
        wait struct to initialize

    :param u32 tx_limit:
        limit for overflow queuing

    :param void (\*func)(struct work_struct \*work):
        restart function for workqueue

    :param int (\*sleep)( struct sdma_engine \*sde, struct iowait \*wait, struct sdma_txreq \*tx, unsigned seq):
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

.. _`iowait_schedule`:

iowait_schedule
===============

.. c:function:: void iowait_schedule(struct iowait *wait, struct workqueue_struct *wq, int cpu)

    initialize wait structure

    :param struct iowait \*wait:
        wait struct to schedule

    :param struct workqueue_struct \*wq:
        workqueue for schedule

    :param int cpu:
        cpu

.. _`iowait_sdma_drain`:

iowait_sdma_drain
=================

.. c:function:: void iowait_sdma_drain(struct iowait *wait)

    wait for DMAs to drain

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_sdma_drain.description`:

Description
-----------

This will delay until the iowait sdmas have
completed.

.. _`iowait_sdma_pending`:

iowait_sdma_pending
===================

.. c:function:: int iowait_sdma_pending(struct iowait *wait)

    return sdma pending count

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_sdma_inc`:

iowait_sdma_inc
===============

.. c:function:: void iowait_sdma_inc(struct iowait *wait)

    note sdma io pending

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_sdma_add`:

iowait_sdma_add
===============

.. c:function:: void iowait_sdma_add(struct iowait *wait, int count)

    add count to pending

    :param struct iowait \*wait:
        iowait structure

    :param int count:
        *undescribed*

.. _`iowait_sdma_dec`:

iowait_sdma_dec
===============

.. c:function:: int iowait_sdma_dec(struct iowait *wait)

    note sdma complete

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_pio_drain`:

iowait_pio_drain
================

.. c:function:: void iowait_pio_drain(struct iowait *wait)

    wait for pios to drain

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_pio_drain.description`:

Description
-----------

This will delay until the iowait pios have
completed.

.. _`iowait_pio_pending`:

iowait_pio_pending
==================

.. c:function:: int iowait_pio_pending(struct iowait *wait)

    return pio pending count

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_pio_inc`:

iowait_pio_inc
==============

.. c:function:: void iowait_pio_inc(struct iowait *wait)

    note pio pending

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_pio_dec`:

iowait_pio_dec
==============

.. c:function:: int iowait_pio_dec(struct iowait *wait)

    note pio complete

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_drain_wakeup`:

iowait_drain_wakeup
===================

.. c:function:: void iowait_drain_wakeup(struct iowait *wait)

    trigger \ :c:func:`iowait_drain`\  waiter

    :param struct iowait \*wait:
        iowait structure

.. _`iowait_drain_wakeup.description`:

Description
-----------

This will trigger any waiters.

.. _`iowait_get_txhead`:

iowait_get_txhead
=================

.. c:function:: struct sdma_txreq *iowait_get_txhead(struct iowait *wait)

    get packet off of iowait list

    :param struct iowait \*wait:
        *undescribed*

.. _`iowait_get_txhead.description`:

Description
-----------

@wait wait struture

.. This file was automatic generated / don't edit.

