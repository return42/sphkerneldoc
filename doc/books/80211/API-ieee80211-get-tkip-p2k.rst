.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-get-tkip-p2k:

======================
ieee80211_get_tkip_p2k
======================

*man ieee80211_get_tkip_p2k(9)*

*4.6.0-rc5*

get a TKIP phase 2 key


Synopsis
========

.. c:function:: void ieee80211_get_tkip_p2k( struct ieee80211_key_conf * keyconf, struct sk_buff * skb, u8 * p2k )

Arguments
=========

``keyconf``
    the parameter passed with the set key

``skb``
    the packet to take the IV32/IV16 values from that will be encrypted
    with this key

``p2k``
    a buffer to which the key will be written, 16 bytes


Description
===========

This function computes the TKIP RC4 key for the IV values in the packet.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
