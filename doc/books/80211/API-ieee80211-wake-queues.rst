
.. _API-ieee80211-wake-queues:

=====================
ieee80211_wake_queues
=====================

*man ieee80211_wake_queues(9)*

*4.6.0-rc1*

wake all queues


Synopsis
========

.. c:function:: void ieee80211_wake_queues( struct ieee80211_hw * hw )

Arguments
=========

``hw``
    pointer as obtained from ``ieee80211_alloc_hw``.


Description
===========

Drivers should use this function instead of netif_wake_queue.
