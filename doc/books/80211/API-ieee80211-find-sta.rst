
.. _API-ieee80211-find-sta:

==================
ieee80211_find_sta
==================

*man ieee80211_find_sta(9)*

*4.6.0-rc1*

find a station


Synopsis
========

.. c:function:: struct ieee80211_sta ⋆ ieee80211_find_sta( struct ieee80211_vif * vif, const u8 * addr )

Arguments
=========

``vif``
    virtual interface to look for station on

``addr``
    station's address


Return
======

The station, if found. ``NULL`` otherwise.


Note
====

This function must be called under RCU lock and the resulting pointer is only valid under RCU lock as well.
