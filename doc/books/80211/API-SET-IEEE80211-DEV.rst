
.. _API-SET-IEEE80211-DEV:

=================
SET_IEEE80211_DEV
=================

*man SET_IEEE80211_DEV(9)*

*4.6.0-rc1*

set device for 802.11 hardware


Synopsis
========

.. c:function:: void SET_IEEE80211_DEV( struct ieee80211_hw * hw, struct device * dev )

Arguments
=========

``hw``
    the ``struct ieee80211_hw`` to set the device for

``dev``
    the ``struct device`` of this 802.11 device
