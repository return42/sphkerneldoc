.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-queue-work:

====================
ieee80211_queue_work
====================

*man ieee80211_queue_work(9)*

*4.6.0-rc5*

add work onto the mac80211 workqueue


Synopsis
========

.. c:function:: void ieee80211_queue_work( struct ieee80211_hw * hw, struct work_struct * work )

Arguments
=========

``hw``
    the hardware struct for the interface we are adding work for

``work``
    the work we want to add onto the mac80211 workqueue


Description
===========

Drivers and mac80211 use this to add work onto the mac80211 workqueue.
This helper ensures drivers are not queueing work when they should not
be.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
