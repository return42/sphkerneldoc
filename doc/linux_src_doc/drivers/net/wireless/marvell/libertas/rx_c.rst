.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/rx.c

.. _`lbs_process_rxed_packet`:

lbs_process_rxed_packet
=======================

.. c:function:: int lbs_process_rxed_packet(struct lbs_private *priv, struct sk_buff *skb)

    processes received packet and forwards it to kernel/upper layer

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\ 

    :param struct sk_buff \*skb:
        A pointer to skb which includes the received packet

.. _`lbs_process_rxed_packet.return`:

Return
------

0 or -1

.. _`convert_mv_rate_to_radiotap`:

convert_mv_rate_to_radiotap
===========================

.. c:function:: u8 convert_mv_rate_to_radiotap(u8 rate)

    converts Tx/Rx rates from Marvell WLAN format (see Table 2 in Section 3.1) to IEEE80211_RADIOTAP_RATE units (500 Kb/s)

    :param u8 rate:
        Input rate

.. _`convert_mv_rate_to_radiotap.return`:

Return
------

Output Rate (0 if invalid)

.. _`process_rxed_802_11_packet`:

process_rxed_802_11_packet
==========================

.. c:function:: int process_rxed_802_11_packet(struct lbs_private *priv, struct sk_buff *skb)

    processes a received 802.11 packet and forwards it to kernel/upper layer

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\ 

    :param struct sk_buff \*skb:
        A pointer to skb which includes the received packet

.. _`process_rxed_802_11_packet.return`:

Return
------

0 or -1

.. This file was automatic generated / don't edit.

