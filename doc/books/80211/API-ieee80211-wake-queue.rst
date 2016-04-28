.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-wake-queue:

====================
ieee80211_wake_queue
====================

*man ieee80211_wake_queue(9)*

*4.6.0-rc5*

wake specific queue


Synopsis
========

.. c:function:: void ieee80211_wake_queue( struct ieee80211_hw * hw, int queue )

Arguments
=========

``hw``
    pointer as obtained from ``ieee80211_alloc_hw``.

``queue``
    queue number (counted from zero).


Description
===========

Drivers should use this function instead of netif_wake_queue.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
