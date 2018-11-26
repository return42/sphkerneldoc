.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/iowait.h

.. _`iowait_schedule`:

iowait_schedule
===============

.. c:function:: bool iowait_schedule(struct iowait *wait, struct workqueue_struct *wq, int cpu)

    schedule the default send engine work

    :param wait:
        wait struct to schedule
    :type wait: struct iowait \*

    :param wq:
        workqueue for schedule
    :type wq: struct workqueue_struct \*

    :param cpu:
        cpu
    :type cpu: int

.. _`iowait_sdma_drain`:

iowait_sdma_drain
=================

.. c:function:: void iowait_sdma_drain(struct iowait *wait)

    wait for DMAs to drain

    :param wait:
        iowait structure
    :type wait: struct iowait \*

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

    :param wait:
        iowait structure
    :type wait: struct iowait \*

.. _`iowait_sdma_inc`:

iowait_sdma_inc
===============

.. c:function:: void iowait_sdma_inc(struct iowait *wait)

    note sdma io pending

    :param wait:
        iowait structure
    :type wait: struct iowait \*

.. _`iowait_sdma_add`:

iowait_sdma_add
===============

.. c:function:: void iowait_sdma_add(struct iowait *wait, int count)

    add count to pending

    :param wait:
        iowait structure
    :type wait: struct iowait \*

    :param count:
        *undescribed*
    :type count: int

.. _`iowait_sdma_dec`:

iowait_sdma_dec
===============

.. c:function:: int iowait_sdma_dec(struct iowait *wait)

    note sdma complete

    :param wait:
        iowait structure
    :type wait: struct iowait \*

.. _`iowait_pio_drain`:

iowait_pio_drain
================

.. c:function:: void iowait_pio_drain(struct iowait *wait)

    wait for pios to drain

    :param wait:
        iowait structure
    :type wait: struct iowait \*

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

    :param wait:
        iowait structure
    :type wait: struct iowait \*

.. _`iowait_pio_inc`:

iowait_pio_inc
==============

.. c:function:: void iowait_pio_inc(struct iowait *wait)

    note pio pending

    :param wait:
        iowait structure
    :type wait: struct iowait \*

.. _`iowait_pio_dec`:

iowait_pio_dec
==============

.. c:function:: int iowait_pio_dec(struct iowait *wait)

    note pio complete

    :param wait:
        iowait structure
    :type wait: struct iowait \*

.. _`iowait_drain_wakeup`:

iowait_drain_wakeup
===================

.. c:function:: void iowait_drain_wakeup(struct iowait *wait)

    trigger \ :c:func:`iowait_drain`\  waiter

    :param wait:
        iowait structure
    :type wait: struct iowait \*

.. _`iowait_drain_wakeup.description`:

Description
-----------

This will trigger any waiters.

.. _`iowait_get_txhead`:

iowait_get_txhead
=================

.. c:function:: struct sdma_txreq *iowait_get_txhead(struct iowait_work *wait)

    get packet off of iowait list

    :param wait:
        *undescribed*
    :type wait: struct iowait_work \*

.. _`iowait_get_txhead.description`:

Description
-----------

\ ``wait``\  iowait_work struture

.. _`iowait_queue`:

iowait_queue
============

.. c:function:: void iowait_queue(bool pkts_sent, struct iowait *w, struct list_head *wait_head)

    Put the iowait on a wait queue

    :param pkts_sent:
        have some packets been sent before queuing?
    :type pkts_sent: bool

    :param w:
        the iowait struct
    :type w: struct iowait \*

    :param wait_head:
        the wait queue
    :type wait_head: struct list_head \*

.. _`iowait_queue.description`:

Description
-----------

This function is called to insert an iowait struct into a
wait queue after a resource (eg, sdma decriptor or pio
buffer) is run out.

.. _`iowait_starve_clear`:

iowait_starve_clear
===================

.. c:function:: void iowait_starve_clear(bool pkts_sent, struct iowait *w)

    clear the wait queue's starve count

    :param pkts_sent:
        have some packets been sent?
    :type pkts_sent: bool

    :param w:
        the iowait struct
    :type w: struct iowait \*

.. _`iowait_starve_clear.description`:

Description
-----------

This function is called to clear the starve count. If no
packets have been sent, the starve count will not be cleared.

.. _`iowait_starve_find_max`:

iowait_starve_find_max
======================

.. c:function:: void iowait_starve_find_max(struct iowait *w, u8 *max, uint idx, uint *max_idx)

    Find the maximum of the starve count

    :param w:
        the iowait struct
    :type w: struct iowait \*

    :param max:
        a variable containing the max starve count
    :type max: u8 \*

    :param idx:
        the index of the current iowait in an array
    :type idx: uint

    :param max_idx:
        a variable containing the array index for the
        iowait entry that has the max starve count
    :type max_idx: uint \*

.. _`iowait_starve_find_max.description`:

Description
-----------

This function is called to compare the starve count of a
given iowait with the given max starve count. The max starve
count and the index will be updated if the iowait's start
count is larger.

.. _`iowait_packet_queued`:

iowait_packet_queued
====================

.. c:function:: bool iowait_packet_queued(struct iowait_work *wait)

    determine if a packet is queued

    :param wait:
        the iowait_work structure
    :type wait: struct iowait_work \*

.. _`iowait_inc_wait_count`:

iowait_inc_wait_count
=====================

.. c:function:: void iowait_inc_wait_count(struct iowait_work *w, u16 n)

    increment wait counts

    :param w:
        the log work struct
    :type w: struct iowait_work \*

    :param n:
        the count
    :type n: u16

.. _`iowait_get_tid_work`:

iowait_get_tid_work
===================

.. c:function:: struct iowait_work *iowait_get_tid_work(struct iowait *w)

    return iowait_work for tid SE

    :param w:
        the iowait struct
    :type w: struct iowait \*

.. _`iowait_get_ib_work`:

iowait_get_ib_work
==================

.. c:function:: struct iowait_work *iowait_get_ib_work(struct iowait *w)

    return iowait_work for ib SE

    :param w:
        the iowait struct
    :type w: struct iowait \*

.. _`iowait_ioww_to_iow`:

iowait_ioww_to_iow
==================

.. c:function:: struct iowait *iowait_ioww_to_iow(struct iowait_work *w)

    return iowait given iowait_work

    :param w:
        the iowait_work struct
    :type w: struct iowait_work \*

.. This file was automatic generated / don't edit.

