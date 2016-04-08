
.. _API-ieee80211-get-buffered-bc:

=========================
ieee80211_get_buffered_bc
=========================

*man ieee80211_get_buffered_bc(9)*

*4.6.0-rc1*

accessing buffered broadcast and multicast frames


Synopsis
========

.. c:function:: struct sk_buff ⋆ ieee80211_get_buffered_bc( struct ieee80211_hw * hw, struct ieee80211_vif * vif )

Arguments
=========

``hw``
    pointer as obtained from ``ieee80211_alloc_hw``.

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback.


Description
===========

Function for accessing buffered broadcast and multicast frames. If hardware/firmware does not implement buffering of broadcast/multicast frames when power saving is used, 802.11
code buffers them in the host memory. The low-level driver uses this function to fetch next buffered frame. In most cases, this is used when generating beacon frame.


Return
======

A pointer to the next buffered skb or NULL if no more buffered frames are available.


Note
====

buffered frames are returned only after DTIM beacon frame was generated with ``ieee80211_beacon_get`` and the low-level driver must thus call ``ieee80211_beacon_get`` first.
``ieee80211_get_buffered_bc`` returns NULL if the previous generated beacon was not DTIM, so the low-level driver does not need to check for DTIM beacons separately and should be
able to use common code for all beacons.
