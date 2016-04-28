.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-beacon-loss:

=====================
ieee80211_beacon_loss
=====================

*man ieee80211_beacon_loss(9)*

*4.6.0-rc5*

inform hardware does not receive beacons


Synopsis
========

.. c:function:: void ieee80211_beacon_loss( struct ieee80211_vif * vif )

Arguments
=========

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback.


Description
===========

When beacon filtering is enabled with ``IEEE80211_VIF_BEACON_FILTER``
and ``IEEE80211_CONF_PS`` is set, the driver needs to inform whenever
the hardware is not receiving beacons with this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
