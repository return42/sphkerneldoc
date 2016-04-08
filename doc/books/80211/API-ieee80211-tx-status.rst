
.. _API-ieee80211-tx-status:

===================
ieee80211_tx_status
===================

*man ieee80211_tx_status(9)*

*4.6.0-rc1*

transmit status callback


Synopsis
========

.. c:function:: void ieee80211_tx_status( struct ieee80211_hw * hw, struct sk_buff * skb )

Arguments
=========

``hw``
    the hardware the frame was transmitted by

``skb``
    the frame that was transmitted, owned by mac80211 after this call


Description
===========

Call this function for all transmitted frames after they have been transmitted. It is permissible to not call this function for multicast frames but this can affect statistics.

This function may not be called in IRQ context. Calls to this function for a single hardware must be synchronized against each other. Calls to this function,
``ieee80211_tx_status_ni`` and ``ieee80211_tx_status_irqsafe`` may not be mixed for a single hardware. Must not run concurrently with ``ieee80211_rx`` or ``ieee80211_rx_ni``.
