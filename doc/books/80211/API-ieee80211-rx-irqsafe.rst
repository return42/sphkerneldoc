
.. _API-ieee80211-rx-irqsafe:

====================
ieee80211_rx_irqsafe
====================

*man ieee80211_rx_irqsafe(9)*

*4.6.0-rc1*

receive frame


Synopsis
========

.. c:function:: void ieee80211_rx_irqsafe( struct ieee80211_hw * hw, struct sk_buff * skb )

Arguments
=========

``hw``
    the hardware this frame came in on

``skb``
    the buffer to receive, owned by mac80211 after this call


Description
===========

Like ``ieee80211_rx`` but can be called in IRQ context (internally defers to a tasklet.)

Calls to this function, ``ieee80211_rx`` or ``ieee80211_rx_ni`` may not be mixed for a single hardware.Must not run concurrently with ``ieee80211_tx_status`` or
``ieee80211_tx_status_ni``.
