
.. _API-cfg80211-cqm-rssi-notify:

========================
cfg80211_cqm_rssi_notify
========================

*man cfg80211_cqm_rssi_notify(9)*

*4.6.0-rc1*

connection quality monitoring rssi event


Synopsis
========

.. c:function:: void cfg80211_cqm_rssi_notify( struct net_device * dev, enum nl80211_cqm_rssi_threshold_event rssi_event, gfp_t gfp )

Arguments
=========

``dev``
    network device

``rssi_event``
    the triggered RSSI event

``gfp``
    context flags


Description
===========

This function is called when a configured connection quality monitoring rssi threshold reached event occurs.
