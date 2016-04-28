.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-data-from-8023:

========================
ieee80211_data_from_8023
========================

*man ieee80211_data_from_8023(9)*

*4.6.0-rc5*

convert an 802.3 frame to 802.11


Synopsis
========

.. c:function:: int ieee80211_data_from_8023( struct sk_buff * skb, const u8 * addr, enum nl80211_iftype iftype, const u8 * bssid, bool qos )

Arguments
=========

``skb``
    the 802.3 frame

``addr``
    the device MAC address

``iftype``
    the virtual interface type

``bssid``
    the network bssid (used only for iftype STATION and ADHOC)

``qos``
    build 802.11 QoS data frame


Return
======

0 on success, or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
