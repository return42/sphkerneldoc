.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-rx-ni:

===============
ieee80211_rx_ni
===============

*man ieee80211_rx_ni(9)*

*4.6.0-rc5*

receive frame (in process context)


Synopsis
========

.. c:function:: void ieee80211_rx_ni( struct ieee80211_hw * hw, struct sk_buff * skb )

Arguments
=========

``hw``
    the hardware this frame came in on

``skb``
    the buffer to receive, owned by mac80211 after this call


Description
===========

Like ``ieee80211_rx`` but can be called in process context (internally
disables bottom halves).

Calls to this function, ``ieee80211_rx`` and ``ieee80211_rx_irqsafe``
may not be mixed for a single hardware. Must not run concurrently with
``ieee80211_tx_status`` or ``ieee80211_tx_status_ni``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
