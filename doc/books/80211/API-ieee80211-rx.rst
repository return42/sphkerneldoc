
.. _API-ieee80211-rx:

============
ieee80211_rx
============

*man ieee80211_rx(9)*

*4.6.0-rc1*

receive frame


Synopsis
========

.. c:function:: void ieee80211_rx( struct ieee80211_hw * hw, struct sk_buff * skb )

Arguments
=========

``hw``
    the hardware this frame came in on

``skb``
    the buffer to receive, owned by mac80211 after this call


Description
===========

Use this function to hand received frames to mac80211. The receive buffer in ``skb`` must start with an IEEE 802.11 header. In case of a paged ``skb`` is used, the driver is
recommended to put the ieee80211 header of the frame on the linear part of the ``skb`` to avoid memory allocation and/or memcpy by the stack.

This function may not be called in IRQ context. Calls to this function for a single hardware must be synchronized against each other. Calls to this function, ``ieee80211_rx_ni``
and ``ieee80211_rx_irqsafe`` may not be mixed for a single hardware. Must not run concurrently with ``ieee80211_tx_status`` or ``ieee80211_tx_status_ni``.

In process context use instead ``ieee80211_rx_ni``.
