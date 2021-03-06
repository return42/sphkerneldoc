.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ralink/rt2x00/rt2x00lib.h

.. _`queue-handlers`:

Queue handlers
==============



.. _`rt2x00queue_alloc_rxskb`:

rt2x00queue_alloc_rxskb
=======================

.. c:function:: struct sk_buff *rt2x00queue_alloc_rxskb(struct queue_entry *entry, gfp_t gfp)

    allocate a skb for RX purposes.

    :param entry:
        The entry for which the skb will be applicable.
    :type entry: struct queue_entry \*

    :param gfp:
        *undescribed*
    :type gfp: gfp_t

.. _`rt2x00queue_free_skb`:

rt2x00queue_free_skb
====================

.. c:function:: void rt2x00queue_free_skb(struct queue_entry *entry)

    free a skb

    :param entry:
        The entry for which the skb will be applicable.
    :type entry: struct queue_entry \*

.. _`rt2x00queue_align_frame`:

rt2x00queue_align_frame
=======================

.. c:function:: void rt2x00queue_align_frame(struct sk_buff *skb)

    Align 802.11 frame to 4-byte boundary

    :param skb:
        The skb to align
    :type skb: struct sk_buff \*

.. _`rt2x00queue_align_frame.description`:

Description
-----------

Align the start of the 802.11 frame to a 4-byte boundary, this could
mean the payload is not aligned properly though.

.. _`rt2x00queue_insert_l2pad`:

rt2x00queue_insert_l2pad
========================

.. c:function:: void rt2x00queue_insert_l2pad(struct sk_buff *skb, unsigned int header_length)

    Align 802.11 header & payload to 4-byte boundary

    :param skb:
        The skb to align
    :type skb: struct sk_buff \*

    :param header_length:
        Length of 802.11 header
    :type header_length: unsigned int

.. _`rt2x00queue_insert_l2pad.description`:

Description
-----------

Apply L2 padding to align both header and payload to 4-byte boundary

.. _`rt2x00queue_remove_l2pad`:

rt2x00queue_remove_l2pad
========================

.. c:function:: void rt2x00queue_remove_l2pad(struct sk_buff *skb, unsigned int header_length)

    Remove L2 padding from 802.11 frame

    :param skb:
        The skb to align
    :type skb: struct sk_buff \*

    :param header_length:
        Length of 802.11 header
    :type header_length: unsigned int

.. _`rt2x00queue_remove_l2pad.description`:

Description
-----------

Remove L2 padding used to align both header and payload to 4-byte boundary,
by removing the L2 padding the header will no longer be 4-byte aligned.

.. _`rt2x00queue_write_tx_frame`:

rt2x00queue_write_tx_frame
==========================

.. c:function:: int rt2x00queue_write_tx_frame(struct data_queue *queue, struct sk_buff *skb, struct ieee80211_sta *sta, bool local)

    Write TX frame to hardware

    :param queue:
        Queue over which the frame should be send
    :type queue: struct data_queue \*

    :param skb:
        The skb to send
    :type skb: struct sk_buff \*

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

    :param local:
        frame is not from mac80211
    :type local: bool

.. _`rt2x00queue_update_beacon`:

rt2x00queue_update_beacon
=========================

.. c:function:: int rt2x00queue_update_beacon(struct rt2x00_dev *rt2x00dev, struct ieee80211_vif *vif)

    Send new beacon from mac80211 to hardware. Handles locking by itself (mutex).

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param vif:
        Interface for which the beacon should be updated.
    :type vif: struct ieee80211_vif \*

.. _`rt2x00queue_update_beacon_locked`:

rt2x00queue_update_beacon_locked
================================

.. c:function:: int rt2x00queue_update_beacon_locked(struct rt2x00_dev *rt2x00dev, struct ieee80211_vif *vif)

    Send new beacon from mac80211 to hardware. Caller needs to ensure locking.

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param vif:
        Interface for which the beacon should be updated.
    :type vif: struct ieee80211_vif \*

.. _`rt2x00queue_clear_beacon`:

rt2x00queue_clear_beacon
========================

.. c:function:: int rt2x00queue_clear_beacon(struct rt2x00_dev *rt2x00dev, struct ieee80211_vif *vif)

    Clear beacon in hardware

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param vif:
        Interface for which the beacon should be updated.
    :type vif: struct ieee80211_vif \*

.. _`rt2x00queue_index_inc`:

rt2x00queue_index_inc
=====================

.. c:function:: void rt2x00queue_index_inc(struct queue_entry *entry, enum queue_index index)

    Index incrementation function

    :param entry:
        Queue entry (&struct queue_entry) to perform the action on.
    :type entry: struct queue_entry \*

    :param index:
        Index type (&enum queue_index) to perform the action on.
    :type index: enum queue_index

.. _`rt2x00queue_index_inc.description`:

Description
-----------

This function will increase the requested index on the entry's queue,
it will grab the appropriate locks and handle queue overflow events by
resetting the index to the start of the queue.

.. _`rt2x00queue_init_queues`:

rt2x00queue_init_queues
=======================

.. c:function:: void rt2x00queue_init_queues(struct rt2x00_dev *rt2x00dev)

    Initialize all data queues

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00queue_init_queues.description`:

Description
-----------

This function will loop through all available queues to clear all
index numbers and set the queue entry to the correct initialization
state.

.. _`rt2x00link_update_stats`:

rt2x00link_update_stats
=======================

.. c:function:: void rt2x00link_update_stats(struct rt2x00_dev *rt2x00dev, struct sk_buff *skb, struct rxdone_entry_desc *rxdesc)

    Update link statistics from RX frame

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param skb:
        Received frame
    :type skb: struct sk_buff \*

    :param rxdesc:
        Received frame descriptor
    :type rxdesc: struct rxdone_entry_desc \*

.. _`rt2x00link_update_stats.description`:

Description
-----------

Update link statistics based on the information from the
received frame descriptor.

.. _`rt2x00link_start_tuner`:

rt2x00link_start_tuner
======================

.. c:function:: void rt2x00link_start_tuner(struct rt2x00_dev *rt2x00dev)

    Start periodic link tuner work

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00link_start_tuner.description`:

Description
-----------

This start the link tuner periodic work, this work will
be executed periodically until \ :c:type:`struct rt2x00link_stop_tuner <rt2x00link_stop_tuner>`\  has
been called.

.. _`rt2x00link_stop_tuner`:

rt2x00link_stop_tuner
=====================

.. c:function:: void rt2x00link_stop_tuner(struct rt2x00_dev *rt2x00dev)

    Stop periodic link tuner work

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00link_stop_tuner.description`:

Description
-----------

After this function completed the link tuner will not
be running until \ :c:type:`struct rt2x00link_start_tuner <rt2x00link_start_tuner>`\  is called.

.. _`rt2x00link_reset_tuner`:

rt2x00link_reset_tuner
======================

.. c:function:: void rt2x00link_reset_tuner(struct rt2x00_dev *rt2x00dev, bool antenna)

    Reset periodic link tuner work

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param antenna:
        Should the antenna tuning also be reset
    :type antenna: bool

.. _`rt2x00link_reset_tuner.description`:

Description
-----------

The VGC limit configured in the hardware will be reset to 0
which forces the driver to rediscover the correct value for
the current association. This is needed when configuration
options have changed which could drastically change the
SNR level or link quality (i.e. changing the antenna setting).

Resetting the link tuner will also cause the periodic work counter
to be reset. Any driver which has a fixed limit on the number
of rounds the link tuner is supposed to work will accept the
tuner actions again if this limit was previously reached.

If \ ``antenna``\  is set to true a the software antenna diversity
tuning will also be reset.

.. _`rt2x00link_start_watchdog`:

rt2x00link_start_watchdog
=========================

.. c:function:: void rt2x00link_start_watchdog(struct rt2x00_dev *rt2x00dev)

    Start periodic watchdog monitoring

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00link_start_watchdog.description`:

Description
-----------

This start the watchdog periodic work, this work will
be executed periodically until \ :c:type:`struct rt2x00link_stop_watchdog <rt2x00link_stop_watchdog>`\  has
been called.

.. _`rt2x00link_stop_watchdog`:

rt2x00link_stop_watchdog
========================

.. c:function:: void rt2x00link_stop_watchdog(struct rt2x00_dev *rt2x00dev)

    Stop periodic watchdog monitoring

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00link_stop_watchdog.description`:

Description
-----------

After this function completed the watchdog monitoring will not
be running until \ :c:type:`struct rt2x00link_start_watchdog <rt2x00link_start_watchdog>`\  is called.

.. _`rt2x00link_register`:

rt2x00link_register
===================

.. c:function:: void rt2x00link_register(struct rt2x00_dev *rt2x00dev)

    Initialize link tuning & watchdog functionality

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00link_register.description`:

Description
-----------

Initialize work structure and all link tuning and watchdog related
parameters. This will not start the periodic work itself.

.. This file was automatic generated / don't edit.

