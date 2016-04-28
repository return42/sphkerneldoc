.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-queue-stopped:

=======================
ieee80211_queue_stopped
=======================

*man ieee80211_queue_stopped(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
