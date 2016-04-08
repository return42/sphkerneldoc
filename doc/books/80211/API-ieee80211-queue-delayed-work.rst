
.. _API-ieee80211-queue-delayed-work:

============================
ieee80211_queue_delayed_work
============================

*man ieee80211_queue_delayed_work(9)*

*4.6.0-rc1*

add work onto the mac80211 workqueue


Synopsis
========

.. c:function:: void ieee80211_queue_delayed_work( struct ieee80211_hw * hw, struct delayed_work * dwork, unsigned long delay )

Arguments
=========

``hw``
    the hardware struct for the interface we are adding work for

``dwork``
    delayable work to queue onto the mac80211 workqueue

``delay``
    number of jiffies to wait before queueing


Description
===========

Drivers and mac80211 use this to queue delayed work onto the mac80211 workqueue.
