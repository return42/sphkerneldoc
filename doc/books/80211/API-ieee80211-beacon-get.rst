.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-beacon-get:

====================
ieee80211_beacon_get
====================

*man ieee80211_beacon_get(9)*

*4.6.0-rc5*

beacon generation function


Synopsis
========

.. c:function:: struct sk_buff * ieee80211_beacon_get( struct ieee80211_hw * hw, struct ieee80211_vif * vif )

Arguments
=========

``hw``
    pointer obtained from ``ieee80211_alloc_hw``.

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback.


Description
===========

See ``ieee80211_beacon_get_tim``.


Return
======

See ``ieee80211_beacon_get_tim``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
