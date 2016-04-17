.. -*- coding: utf-8; mode: rst -*-

========
dynack.c
========


.. _`ath_dynack_ewma`:

ath_dynack_ewma
===============

.. c:function:: u32 ath_dynack_ewma (u32 old, u32 new)

    EWMA (Exponentially Weighted Moving Average) calculation

    :param u32 old:

        *undescribed*

    :param u32 new:

        *undescribed*



.. _`ath_dynack_get_sifs`:

ath_dynack_get_sifs
===================

.. c:function:: u32 ath_dynack_get_sifs (struct ath_hw *ah, int phy)

    get sifs time based on phy used

    :param struct ath_hw \*ah:
        ath hw

    :param int phy:
        phy used



.. _`ath_dynack_bssidmask`:

ath_dynack_bssidmask
====================

.. c:function:: bool ath_dynack_bssidmask (struct ath_hw *ah, const u8 *mac)

    filter out ACK frames based on BSSID mask

    :param struct ath_hw \*ah:
        ath hw

    :param const u8 \*mac:
        receiver address



.. _`ath_dynack_compute_ackto`:

ath_dynack_compute_ackto
========================

.. c:function:: void ath_dynack_compute_ackto (struct ath_hw *ah)

    compute ACK timeout as the maximum STA timeout

    :param struct ath_hw \*ah:
        ath hw



.. _`ath_dynack_compute_ackto.description`:

Description
-----------

should be called while holding qlock



.. _`ath_dynack_compute_to`:

ath_dynack_compute_to
=====================

.. c:function:: void ath_dynack_compute_to (struct ath_hw *ah)

    compute STA ACK timeout

    :param struct ath_hw \*ah:
        ath hw



.. _`ath_dynack_compute_to.description`:

Description
-----------

should be called while holding qlock



.. _`ath_dynack_sample_tx_ts`:

ath_dynack_sample_tx_ts
=======================

.. c:function:: void ath_dynack_sample_tx_ts (struct ath_hw *ah, struct sk_buff *skb, struct ath_tx_status *ts)

    status timestamp sampling method

    :param struct ath_hw \*ah:
        ath hw

    :param struct sk_buff \*skb:
        socket buffer

    :param struct ath_tx_status \*ts:
        tx status info



.. _`ath_dynack_sample_ack_ts`:

ath_dynack_sample_ack_ts
========================

.. c:function:: void ath_dynack_sample_ack_ts (struct ath_hw *ah, struct sk_buff *skb, u32 ts)

    ACK timestamp sampling method

    :param struct ath_hw \*ah:
        ath hw

    :param struct sk_buff \*skb:
        socket buffer

    :param u32 ts:
        rx timestamp



.. _`ath_dynack_node_init`:

ath_dynack_node_init
====================

.. c:function:: void ath_dynack_node_init (struct ath_hw *ah, struct ath_node *an)

    init ath_node related info

    :param struct ath_hw \*ah:
        ath hw

    :param struct ath_node \*an:
        ath node



.. _`ath_dynack_node_deinit`:

ath_dynack_node_deinit
======================

.. c:function:: void ath_dynack_node_deinit (struct ath_hw *ah, struct ath_node *an)

    deinit ath_node related info

    :param struct ath_hw \*ah:
        ath hw

    :param struct ath_node \*an:
        ath node



.. _`ath_dynack_reset`:

ath_dynack_reset
================

.. c:function:: void ath_dynack_reset (struct ath_hw *ah)

    reset dynack processing

    :param struct ath_hw \*ah:
        ath hw



.. _`ath_dynack_init`:

ath_dynack_init
===============

.. c:function:: void ath_dynack_init (struct ath_hw *ah)

    init dynack data structure

    :param struct ath_hw \*ah:
        ath hw

