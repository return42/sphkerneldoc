
.. _API-ieee80211-tx-status-irqsafe:

===========================
ieee80211_tx_status_irqsafe
===========================

*man ieee80211_tx_status_irqsafe(9)*

*4.6.0-rc1*

IRQ-safe transmit status callback


Synopsis
========

.. c:function:: void ieee80211_tx_status_irqsafe( struct ieee80211_hw * hw, struct sk_buff * skb )

Arguments
=========

``hw``
    the hardware the frame was transmitted by

``skb``
    the frame that was transmitted, owned by mac80211 after this call


Description
===========

Like ``ieee80211_tx_status`` but can be called in IRQ context (internally defers to a tasklet.)

Calls to this function, ``ieee80211_tx_status`` and ``ieee80211_tx_status_ni`` may not be mixed for a single hardware.
