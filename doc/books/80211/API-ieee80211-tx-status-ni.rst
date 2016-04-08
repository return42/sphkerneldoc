
.. _API-ieee80211-tx-status-ni:

======================
ieee80211_tx_status_ni
======================

*man ieee80211_tx_status_ni(9)*

*4.6.0-rc1*

transmit status callback (in process context)


Synopsis
========

.. c:function:: void ieee80211_tx_status_ni( struct ieee80211_hw * hw, struct sk_buff * skb )

Arguments
=========

``hw``
    the hardware the frame was transmitted by

``skb``
    the frame that was transmitted, owned by mac80211 after this call


Description
===========

Like ``ieee80211_tx_status`` but can be called in process context.

Calls to this function, ``ieee80211_tx_status`` and ``ieee80211_tx_status_irqsafe`` may not be mixed for a single hardware.
