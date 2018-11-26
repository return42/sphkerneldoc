.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/tx.c

.. _`convert_radiotap_rate_to_mv`:

convert_radiotap_rate_to_mv
===========================

.. c:function:: u32 convert_radiotap_rate_to_mv(u8 rate)

    converts Tx/Rx rates from IEEE80211_RADIOTAP_RATE units (500 Kb/s) into Marvell WLAN format (see Table 8 in Section 3.2.1)

    :param rate:
        Input rate
    :type rate: u8

.. _`convert_radiotap_rate_to_mv.return`:

Return
------

Output Rate (0 if invalid)

.. _`lbs_hard_start_xmit`:

lbs_hard_start_xmit
===================

.. c:function:: netdev_tx_t lbs_hard_start_xmit(struct sk_buff *skb, struct net_device *dev)

    checks the conditions and sends packet to IF layer if everything is ok

    :param skb:
        A pointer to skb which includes TX packet
    :type skb: struct sk_buff \*

    :param dev:
        A pointer to the \ :c:type:`struct net_device <net_device>`\ 
    :type dev: struct net_device \*

.. _`lbs_hard_start_xmit.return`:

Return
------

0 or -1

.. _`lbs_send_tx_feedback`:

lbs_send_tx_feedback
====================

.. c:function:: void lbs_send_tx_feedback(struct lbs_private *priv, u32 try_count)

    sends to the host the last transmitted packet, filling the radiotap headers with transmission information.

    :param priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure
    :type priv: struct lbs_private \*

    :param try_count:
        A 32-bit value containing transmission retry status.
    :type try_count: u32

.. _`lbs_send_tx_feedback.return`:

Return
------

void

.. This file was automatic generated / don't edit.

