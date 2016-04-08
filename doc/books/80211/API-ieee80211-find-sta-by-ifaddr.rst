
.. _API-ieee80211-find-sta-by-ifaddr:

============================
ieee80211_find_sta_by_ifaddr
============================

*man ieee80211_find_sta_by_ifaddr(9)*

*4.6.0-rc1*

find a station on hardware


Synopsis
========

.. c:function:: struct ieee80211_sta ⋆ ieee80211_find_sta_by_ifaddr( struct ieee80211_hw * hw, const u8 * addr, const u8 * localaddr )

Arguments
=========

``hw``
    pointer as obtained from ``ieee80211_alloc_hw``

``addr``
    remote station's address

``localaddr``
    local address (vif->sdata->vif.addr). Use NULL for 'any'.


Return
======

The station, if found. ``NULL`` otherwise.


Note
====

This function must be called under RCU lock and the resulting pointer is only valid under RCU lock as well.


NOTE
====

You may pass NULL for localaddr, but then you will just get the first STA that matches the remote address 'addr'. We can have multiple STA associated with multiple logical stations
(e.g. consider a station connecting to another BSSID on the same AP hardware without disconnecting first). In this case, the result of this method with localaddr NULL is not
reliable.

DO NOT USE THIS FUNCTION with localaddr NULL if at all possible.
