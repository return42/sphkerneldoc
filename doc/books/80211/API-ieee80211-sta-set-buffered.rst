.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-sta-set-buffered:

==========================
ieee80211_sta_set_buffered
==========================

*man ieee80211_sta_set_buffered(9)*

*4.6.0-rc5*

inform mac80211 about driver-buffered frames


Synopsis
========

.. c:function:: void ieee80211_sta_set_buffered( struct ieee80211_sta * sta, u8 tid, bool buffered )

Arguments
=========

``sta``
    ``struct ieee80211_sta`` pointer for the sleeping station

``tid``
    the TID that has buffered frames

``buffered``
    indicates whether or not frames are buffered for this TID


Description
===========

If a driver buffers frames for a powersave station instead of passing
them back to mac80211 for retransmission, the station may still need to
be told that there are buffered frames via the TIM bit.

This function informs mac80211 whether or not there are frames that are
buffered in the driver for a given TID; mac80211 can then use this data
to set the TIM bit (NOTE: This may call back into the driver's set_tim
call! Beware of the locking!)

If all frames are released to the station (due to PS-poll or uAPSD) then
the driver needs to inform mac80211 that there no longer are frames
buffered. However, when the station wakes up mac80211 assumes that all
buffered frames will be transmitted and clears this data, drivers need
to make sure they inform mac80211 about all buffered frames on the sleep
transition (``sta_notify`` with ``STA_NOTIFY_SLEEP``).

Note that technically mac80211 only needs to know this per AC, not per
TID, but since driver buffering will inevitably happen per TID (since it
is related to aggregation) it is easier to make mac80211 map the TID to
the AC as required instead of keeping track in all drivers that use this
API.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
