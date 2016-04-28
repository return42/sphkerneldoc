.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-wake-queues:

=====================
ieee80211_wake_queues
=====================

*man ieee80211_wake_queues(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
