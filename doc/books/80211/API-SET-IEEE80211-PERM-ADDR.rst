
.. _API-SET-IEEE80211-PERM-ADDR:

=======================
SET_IEEE80211_PERM_ADDR
=======================

*man SET_IEEE80211_PERM_ADDR(9)*

*4.6.0-rc1*

set the permanent MAC address for 802.11 hardware


Synopsis
========

.. c:function:: void SET_IEEE80211_PERM_ADDR( struct ieee80211_hw * hw, const u8 * addr )

Arguments
=========

``hw``
    the ``struct ieee80211_hw`` to set the MAC address for

``addr``
    the address to set
