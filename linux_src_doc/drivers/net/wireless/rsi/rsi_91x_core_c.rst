.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_core.c

.. _`rsi_determine_min_weight_queue`:

rsi_determine_min_weight_queue
==============================

.. c:function:: u8 rsi_determine_min_weight_queue(struct rsi_common *common)

    :param common:
        *undescribed*
    :type common: struct rsi_common \*

.. _`rsi_determine_min_weight_queue.description`:

Description
-----------

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

.. _`rsi_recalculate_weights`:

rsi_recalculate_weights
=======================

.. c:function:: bool rsi_recalculate_weights(struct rsi_common *common)

    This function recalculates the weights corresponding to each queue.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_recalculate_weights.return`:

Return
------

recontend_queue bool variable

.. _`rsi_get_num_pkts_dequeue`:

rsi_get_num_pkts_dequeue
========================

.. c:function:: u32 rsi_get_num_pkts_dequeue(struct rsi_common *common, u8 q_num)

    This function determines the number of packets to be dequeued based on the number of bytes calculated using txop.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param q_num:
        the queue from which pkts have to be dequeued
    :type q_num: u8

.. _`rsi_get_num_pkts_dequeue.return`:

Return
------

pkt_num: Number of pkts to be dequeued.

.. _`rsi_core_determine_hal_queue`:

rsi_core_determine_hal_queue
============================

.. c:function:: u8 rsi_core_determine_hal_queue(struct rsi_common *common)

    This function determines the queue from which packet has to be dequeued.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_core_determine_hal_queue.return`:

Return
------

q_num: Corresponding queue number on success.

.. _`rsi_core_queue_pkt`:

rsi_core_queue_pkt
==================

.. c:function:: void rsi_core_queue_pkt(struct rsi_common *common, struct sk_buff *skb)

    This functions enqueues the packet to the queue specified by the queue number.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param skb:
        Pointer to the socket buffer structure.
    :type skb: struct sk_buff \*

.. _`rsi_core_queue_pkt.return`:

Return
------

None.

.. _`rsi_core_dequeue_pkt`:

rsi_core_dequeue_pkt
====================

.. c:function:: struct sk_buff *rsi_core_dequeue_pkt(struct rsi_common *common, u8 q_num)

    This functions dequeues the packet from the queue specified by the queue number.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param q_num:
        Queue number.
    :type q_num: u8

.. _`rsi_core_dequeue_pkt.return`:

Return
------

Pointer to sk_buff structure.

.. _`rsi_core_qos_processor`:

rsi_core_qos_processor
======================

.. c:function:: void rsi_core_qos_processor(struct rsi_common *common)

    This function is used to determine the wmm queue based on the backoff procedure. Data packets are dequeued from the selected hal queue and sent to the below layers.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_core_qos_processor.return`:

Return
------

None.

.. _`rsi_core_xmit`:

rsi_core_xmit
=============

.. c:function:: void rsi_core_xmit(struct rsi_common *common, struct sk_buff *skb)

    This function transmits the packets received from mac80211

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param skb:
        Pointer to the socket buffer structure.
    :type skb: struct sk_buff \*

.. _`rsi_core_xmit.return`:

Return
------

None.

.. This file was automatic generated / don't edit.

