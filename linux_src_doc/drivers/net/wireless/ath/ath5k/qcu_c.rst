.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/qcu.c

.. _`queue-control-unit--qcu--dcf-control-unit--dcu--functions`:

Queue Control Unit (QCU)/DCF Control Unit (DCU) functions
=========================================================

Here we setup parameters for the 12 available TX queues. Note that
on the various registers we can usually only map the first 10 of them so
basically we have 10 queues to play with. Each queue has a matching
QCU that controls when the queue will get triggered and multiple QCUs
can be mapped to a single DCU that controls the various DFS parameters
for the various queues. In our setup we have a 1:1 mapping between QCUs
and DCUs allowing us to have different DFS settings for each queue.

When a frame goes into a TX queue, QCU decides when it'll trigger a
transmission based on various criteria (such as how many data we have inside
it's buffer or -if it's a beacon queue- if it's time to fire up the queue
based on TSF etc), DCU adds backoff, IFSes etc and then a scheduler
(arbitrator) decides the priority of each QCU based on it's configuration
(e.g. beacons are always transmitted when they leave DCU bypassing all other
frames from other queues waiting to be transmitted). After a frame leaves
the DCU it goes to PCU for further processing and then to PHY for
the actual transmission.

.. _`ath5k_hw_num_tx_pending`:

ath5k_hw_num_tx_pending
=======================

.. c:function:: u32 ath5k_hw_num_tx_pending(struct ath5k_hw *ah, unsigned int queue)

    Get number of pending frames for a  given queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        One of enum ath5k_tx_queue_id
    :type queue: unsigned int

.. _`ath5k_hw_release_tx_queue`:

ath5k_hw_release_tx_queue
=========================

.. c:function:: void ath5k_hw_release_tx_queue(struct ath5k_hw *ah, unsigned int queue)

    Set a transmit queue inactive

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        One of enum ath5k_tx_queue_id
    :type queue: unsigned int

.. _`ath5k_cw_validate`:

ath5k_cw_validate
=================

.. c:function:: u16 ath5k_cw_validate(u16 cw_req)

    Make sure the given cw is valid

    :param cw_req:
        The contention window value to check
    :type cw_req: u16

.. _`ath5k_cw_validate.description`:

Description
-----------

Make sure cw is a power of 2 minus 1 and smaller than 1024

.. _`ath5k_hw_get_tx_queueprops`:

ath5k_hw_get_tx_queueprops
==========================

.. c:function:: int ath5k_hw_get_tx_queueprops(struct ath5k_hw *ah, int queue, struct ath5k_txq_info *queue_info)

    Get properties for a transmit queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        One of enum ath5k_tx_queue_id
    :type queue: int

    :param queue_info:
        The \ :c:type:`struct ath5k_txq_info <ath5k_txq_info>`\  to fill
    :type queue_info: struct ath5k_txq_info \*

.. _`ath5k_hw_set_tx_queueprops`:

ath5k_hw_set_tx_queueprops
==========================

.. c:function:: int ath5k_hw_set_tx_queueprops(struct ath5k_hw *ah, int queue, const struct ath5k_txq_info *qinfo)

    Set properties for a transmit queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        One of enum ath5k_tx_queue_id
    :type queue: int

    :param qinfo:
        The \ :c:type:`struct ath5k_txq_info <ath5k_txq_info>`\  to use
    :type qinfo: const struct ath5k_txq_info \*

.. _`ath5k_hw_set_tx_queueprops.description`:

Description
-----------

Returns 0 on success or -EIO if queue is inactive

.. _`ath5k_hw_setup_tx_queue`:

ath5k_hw_setup_tx_queue
=======================

.. c:function:: int ath5k_hw_setup_tx_queue(struct ath5k_hw *ah, enum ath5k_tx_queue queue_type, struct ath5k_txq_info *queue_info)

    Initialize a transmit queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue_type:
        One of enum ath5k_tx_queue
    :type queue_type: enum ath5k_tx_queue

    :param queue_info:
        The \ :c:type:`struct ath5k_txq_info <ath5k_txq_info>`\  to use
    :type queue_info: struct ath5k_txq_info \*

.. _`ath5k_hw_setup_tx_queue.description`:

Description
-----------

Returns 0 on success, -EINVAL on invalid arguments

.. _`ath5k_hw_set_tx_retry_limits`:

ath5k_hw_set_tx_retry_limits
============================

.. c:function:: void ath5k_hw_set_tx_retry_limits(struct ath5k_hw *ah, unsigned int queue)

    Set tx retry limits on DCU

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        One of enum ath5k_tx_queue_id
    :type queue: unsigned int

.. _`ath5k_hw_set_tx_retry_limits.description`:

Description
-----------

This function is used when initializing a queue, to set
retry limits based on ah->ah_retry\_\* and the chipset used.

.. _`ath5k_hw_reset_tx_queue`:

ath5k_hw_reset_tx_queue
=======================

.. c:function:: int ath5k_hw_reset_tx_queue(struct ath5k_hw *ah, unsigned int queue)

    Initialize a single hw queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        One of enum ath5k_tx_queue_id
    :type queue: unsigned int

.. _`ath5k_hw_reset_tx_queue.description`:

Description
-----------

Set DCF properties for the given transmit queue on DCU
and configures all queue-specific parameters.

.. _`ath5k_hw_set_ifs_intervals`:

ath5k_hw_set_ifs_intervals
==========================

.. c:function:: int ath5k_hw_set_ifs_intervals(struct ath5k_hw *ah, unsigned int slot_time)

    Set global inter-frame spaces on DCU

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param slot_time:
        Slot time in us
    :type slot_time: unsigned int

.. _`ath5k_hw_set_ifs_intervals.description`:

Description
-----------

Sets the global IFS intervals on DCU (also works on AR5210) for
the given slot time and the current bwmode.

.. _`ath5k_hw_init_queues`:

ath5k_hw_init_queues
====================

.. c:function:: int ath5k_hw_init_queues(struct ath5k_hw *ah)

    Initialize tx queues

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_init_queues.description`:

Description
-----------

Initializes all tx queues based on information on
ah->ah_txq\* set by the driver

.. This file was automatic generated / don't edit.

