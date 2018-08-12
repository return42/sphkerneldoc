.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath10k/wow.c

.. _`ath10k_wow_convert_8023_to_80211`:

ath10k_wow_convert_8023_to_80211
================================

.. c:function:: void ath10k_wow_convert_8023_to_80211(struct cfg80211_pkt_pattern *new, const struct cfg80211_pkt_pattern *old)

    +------------+-----------+--------+----------------+ 802.3:  \|dest mac(6B)\|src mac(6B)\|type(2B)\|     body...    \| +------------+-----------+--------+----------------+ \|_\_         \|______\_    \|___________\_  \|_______\_ \|                \|                \|          \| +--+------------+----+-----------+---------------+-----------+ 802.11: \|4B\|dest mac(6B)\| 6B \|src mac(6B)\|  8B  \|type(2B)\|  body...  \| +--+------------+----+-----------+---------------+-----------+

    :param struct cfg80211_pkt_pattern \*new:
        *undescribed*

    :param const struct cfg80211_pkt_pattern \*old:
        *undescribed*

.. This file was automatic generated / don't edit.

