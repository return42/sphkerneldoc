.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-new-sta:

================
cfg80211_new_sta
================

*man cfg80211_new_sta(9)*

*4.6.0-rc5*

notify userspace about station


Synopsis
========

.. c:function:: void cfg80211_new_sta( struct net_device * dev, const u8 * mac_addr, struct station_info * sinfo, gfp_t gfp )

Arguments
=========

``dev``
    the netdev

``mac_addr``
    the station's address

``sinfo``
    the station information

``gfp``
    allocation flags


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
