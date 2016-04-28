.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-data-to-8023:

======================
ieee80211_data_to_8023
======================

*man ieee80211_data_to_8023(9)*

*4.6.0-rc5*

convert an 802.11 data frame to 802.3


Synopsis
========

.. c:function:: int ieee80211_data_to_8023( struct sk_buff * skb, const u8 * addr, enum nl80211_iftype iftype )

Arguments
=========

``skb``
    the 802.11 data frame

``addr``
    the device MAC address

``iftype``
    the virtual interface type


Return
======

0 on success. Non-zero on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
