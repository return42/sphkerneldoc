
.. _API-ieee80211-stop-queues:

=====================
ieee80211_stop_queues
=====================

*man ieee80211_stop_queues(9)*

*4.6.0-rc1*

stop all queues


Synopsis
========

.. c:function:: void ieee80211_stop_queues( struct ieee80211_hw * hw )

Arguments
=========

``hw``
    pointer as obtained from ``ieee80211_alloc_hw``.


Description
===========

Drivers should use this function instead of netif_stop_queue.
