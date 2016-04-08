
.. _API-ieee80211-get-hdrlen-from-skb:

=============================
ieee80211_get_hdrlen_from_skb
=============================

*man ieee80211_get_hdrlen_from_skb(9)*

*4.6.0-rc1*

get header length from data


Synopsis
========

.. c:function:: unsigned int ieee80211_get_hdrlen_from_skb( const struct sk_buff * skb )

Arguments
=========

``skb``
    the frame


Description
===========

Given an skb with a raw 802.11 header at the data pointer this function returns the 802.11 header length.


Return
======

The 802.11 header length in bytes (not including encryption headers). Or 0 if the data in the sk_buff is too short to contain a valid 802.11 header.
