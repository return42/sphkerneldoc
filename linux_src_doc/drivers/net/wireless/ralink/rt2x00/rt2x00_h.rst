.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ralink/rt2x00/rt2x00.h

.. _`hw_mode_spec`:

struct hw_mode_spec
===================

.. c:type:: struct hw_mode_spec

    Hardware specifications structure

.. _`hw_mode_spec.definition`:

Definition
----------

.. code-block:: c

    struct hw_mode_spec {
        unsigned int supported_bands;
    #define SUPPORT_BAND_2GHZ 0x00000001
    #define SUPPORT_BAND_5GHZ 0x00000002
        unsigned int supported_rates;
    #define SUPPORT_RATE_CCK 0x00000001
    #define SUPPORT_RATE_OFDM 0x00000002
        unsigned int num_channels;
        const struct rf_channel *channels;
        const struct channel_info *channels_info;
        struct ieee80211_sta_ht_cap ht;
    }

.. _`hw_mode_spec.members`:

Members
-------

supported_bands
    Bitmask contained the supported bands (2.4GHz, 5.2GHz).

supported_rates
    Rate types which are supported (CCK, OFDM).

num_channels
    Number of supported channels. This is used as array size
    for \ ``tx_power_a``\ , \ ``tx_power_bg``\  and \ ``channels``\ .

channels
    Device/chipset specific channel values (See \ :c:type:`struct rf_channel <rf_channel>`\ ).

channels_info
    Additional information for channels (See \ :c:type:`struct channel_info <channel_info>`\ ).

ht
    Driver HT Capabilities (See \ :c:type:`struct ieee80211_sta_ht_cap <ieee80211_sta_ht_cap>`\ ).

.. _`hw_mode_spec.description`:

Description
-----------

Details about the supported modes, rates and channels
of a particular chipset. This is used by rt2x00lib
to build the ieee80211_hw_mode array for mac80211.

.. _`rt2x00queue_map_txskb`:

rt2x00queue_map_txskb
=====================

.. c:function:: int rt2x00queue_map_txskb(struct queue_entry *entry)

    Map a skb into DMA for TX purposes.

    :param entry:
        Pointer to \ :c:type:`struct queue_entry <queue_entry>`\ 
    :type entry: struct queue_entry \*

.. _`rt2x00queue_map_txskb.description`:

Description
-----------

Returns -ENOMEM if mapping fail, 0 otherwise.

.. _`rt2x00queue_unmap_skb`:

rt2x00queue_unmap_skb
=====================

.. c:function:: void rt2x00queue_unmap_skb(struct queue_entry *entry)

    Unmap a skb from DMA.

    :param entry:
        Pointer to \ :c:type:`struct queue_entry <queue_entry>`\ 
    :type entry: struct queue_entry \*

.. _`rt2x00queue_get_tx_queue`:

rt2x00queue_get_tx_queue
========================

.. c:function:: struct data_queue *rt2x00queue_get_tx_queue(struct rt2x00_dev *rt2x00dev, const enum data_queue_qid queue)

    Convert tx queue index to queue pointer

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param queue:
        rt2x00 queue index (see \ :c:type:`enum data_queue_qid <data_queue_qid>`\ ).
    :type queue: const enum data_queue_qid

.. _`rt2x00queue_get_tx_queue.description`:

Description
-----------

Returns NULL for non tx queues.

.. _`rt2x00queue_get_entry`:

rt2x00queue_get_entry
=====================

.. c:function:: struct queue_entry *rt2x00queue_get_entry(struct data_queue *queue, enum queue_index index)

    Get queue entry where the given index points to.

    :param queue:
        Pointer to \ :c:type:`struct data_queue <data_queue>`\  from where we obtain the entry.
    :type queue: struct data_queue \*

    :param index:
        Index identifier for obtaining the correct index.
    :type index: enum queue_index

.. _`rt2x00queue_pause_queue`:

rt2x00queue_pause_queue
=======================

.. c:function:: void rt2x00queue_pause_queue(struct data_queue *queue)

    Pause a data queue

    :param queue:
        Pointer to \ :c:type:`struct data_queue <data_queue>`\ .
    :type queue: struct data_queue \*

.. _`rt2x00queue_pause_queue.description`:

Description
-----------

This function will pause the data queue locally, preventing
new frames to be added to the queue (while the hardware is
still allowed to run).

.. _`rt2x00queue_unpause_queue`:

rt2x00queue_unpause_queue
=========================

.. c:function:: void rt2x00queue_unpause_queue(struct data_queue *queue)

    unpause a data queue

    :param queue:
        Pointer to \ :c:type:`struct data_queue <data_queue>`\ .
    :type queue: struct data_queue \*

.. _`rt2x00queue_unpause_queue.description`:

Description
-----------

This function will unpause the data queue locally, allowing
new frames to be added to the queue again.

.. _`rt2x00queue_start_queue`:

rt2x00queue_start_queue
=======================

.. c:function:: void rt2x00queue_start_queue(struct data_queue *queue)

    Start a data queue

    :param queue:
        Pointer to \ :c:type:`struct data_queue <data_queue>`\ .
    :type queue: struct data_queue \*

.. _`rt2x00queue_start_queue.description`:

Description
-----------

This function will start handling all pending frames in the queue.

.. _`rt2x00queue_stop_queue`:

rt2x00queue_stop_queue
======================

.. c:function:: void rt2x00queue_stop_queue(struct data_queue *queue)

    Halt a data queue

    :param queue:
        Pointer to \ :c:type:`struct data_queue <data_queue>`\ .
    :type queue: struct data_queue \*

.. _`rt2x00queue_stop_queue.description`:

Description
-----------

This function will stop all pending frames in the queue.

.. _`rt2x00queue_flush_queue`:

rt2x00queue_flush_queue
=======================

.. c:function:: void rt2x00queue_flush_queue(struct data_queue *queue, bool drop)

    Flush a data queue

    :param queue:
        Pointer to \ :c:type:`struct data_queue <data_queue>`\ .
    :type queue: struct data_queue \*

    :param drop:
        True to drop all pending frames.
    :type drop: bool

.. _`rt2x00queue_flush_queue.description`:

Description
-----------

This function will flush the queue. After this call
the queue is guaranteed to be empty.

.. _`rt2x00queue_start_queues`:

rt2x00queue_start_queues
========================

.. c:function:: void rt2x00queue_start_queues(struct rt2x00_dev *rt2x00dev)

    Start all data queues

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00queue_start_queues.description`:

Description
-----------

This function will loop through all available queues to start them

.. _`rt2x00queue_stop_queues`:

rt2x00queue_stop_queues
=======================

.. c:function:: void rt2x00queue_stop_queues(struct rt2x00_dev *rt2x00dev)

    Halt all data queues

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00queue_stop_queues.description`:

Description
-----------

This function will loop through all available queues to stop
any pending frames.

.. _`rt2x00queue_flush_queues`:

rt2x00queue_flush_queues
========================

.. c:function:: void rt2x00queue_flush_queues(struct rt2x00_dev *rt2x00dev, bool drop)

    Flush all data queues

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param drop:
        True to drop all pending frames.
    :type drop: bool

.. _`rt2x00queue_flush_queues.description`:

Description
-----------

This function will loop through all available queues to flush
any pending frames.

.. _`rt2x00debug_dump_frame`:

rt2x00debug_dump_frame
======================

.. c:function:: void rt2x00debug_dump_frame(struct rt2x00_dev *rt2x00dev, enum rt2x00_dump_type type, struct queue_entry *entry)

    Dump a frame to userspace through debugfs.

    :param rt2x00dev:
        Pointer to \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param type:
        The type of frame that is being dumped.
    :type type: enum rt2x00_dump_type

    :param entry:
        The queue entry containing the frame to be dumped.
    :type entry: struct queue_entry \*

.. This file was automatic generated / don't edit.

