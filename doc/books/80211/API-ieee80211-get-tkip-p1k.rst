
.. _API-ieee80211-get-tkip-p1k:

======================
ieee80211_get_tkip_p1k
======================

*man ieee80211_get_tkip_p1k(9)*

*4.6.0-rc1*

get a TKIP phase 1 key


Synopsis
========

.. c:function:: void ieee80211_get_tkip_p1k( struct ieee80211_key_conf * keyconf, struct sk_buff * skb, u16 * p1k )

Arguments
=========

``keyconf``
    the parameter passed with the set key

``skb``
    the packet to take the IV32 value from that will be encrypted with this P1K

``p1k``
    a buffer to which the key will be written, as 5 u16 values


Description
===========

This function returns the TKIP phase 1 key for the IV32 taken from the given packet.
