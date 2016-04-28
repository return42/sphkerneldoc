.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-sta-eosp:

==================
ieee80211_sta_eosp
==================

*man ieee80211_sta_eosp(9)*

*4.6.0-rc5*

notify mac80211 about end of SP


Synopsis
========

.. c:function:: void ieee80211_sta_eosp( struct ieee80211_sta * pubsta )

Arguments
=========

``pubsta``
    the station


Description
===========

When a device transmits frames in a way that it can't tell mac80211 in
the TX status about the EOSP, it must clear the
``IEEE80211_TX_STATUS_EOSP`` bit and call this function instead. This
applies for PS-Poll as well as uAPSD.

Note that just like with ``_tx_status`` and ``_rx`` drivers must not mix
calls to irqsafe/non-irqsafe versions, this function must not be mixed
with those either. Use the all irqsafe, or all non-irqsafe, don't mix!


NB
==

the _irqsafe version of this function doesn't exist, no driver needs it
right now. Don't call this function if you'd need the _irqsafe version,
look at the git history and restore the _irqsafe version!


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
