
.. _API-ieee80211-queue-stopped:

=======================
ieee80211_queue_stopped
=======================

*man ieee80211_queue_stopped(9)*

*4.6.0-rc1*

test status of the queue


Synopsis
========

.. c:function:: int ieee80211_queue_stopped( struct ieee80211_hw * hw, int queue )

Arguments
=========

``hw``
    pointer as obtained from ``ieee80211_alloc_hw``.

``queue``
    queue number (counted from zero).


Description
===========

Drivers should use this function instead of netif_stop_queue.


Return
======

``true`` if the queue is stopped. ``false`` otherwise.
