
.. _API-ieee80211-stop-queue:

====================
ieee80211_stop_queue
====================

*man ieee80211_stop_queue(9)*

*4.6.0-rc1*

stop specific queue


Synopsis
========

.. c:function:: void ieee80211_stop_queue( struct ieee80211_hw * hw, int queue )

Arguments
=========

``hw``
    pointer as obtained from ``ieee80211_alloc_hw``.

``queue``
    queue number (counted from zero).


Description
===========

Drivers should use this function instead of netif_stop_queue.
