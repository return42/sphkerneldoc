
.. _API-cfg80211-testmode-alloc-event-skb:

=================================
cfg80211_testmode_alloc_event_skb
=================================

*man cfg80211_testmode_alloc_event_skb(9)*

*4.6.0-rc1*

allocate testmode event


Synopsis
========

.. c:function:: struct sk_buff ⋆ cfg80211_testmode_alloc_event_skb( struct wiphy * wiphy, int approxlen, gfp_t gfp )

Arguments
=========

``wiphy``
    the wiphy

``approxlen``
    an upper bound of the length of the data that will be put into the skb

``gfp``
    allocation flags


Description
===========

This function allocates and pre-fills an skb for an event on the testmode multicast group.

The returned skb is set up in the same way as with ``cfg80211_testmode_alloc_reply_skb`` but prepared for an event. As there, you should simply add data to it that will then end up
in the ``NL80211_ATTR_TESTDATA`` attribute. Again, you must not modify the skb in any other way.

When done filling the skb, call ``cfg80211_testmode_event`` with the skb to send the event.


Return
======

An allocated and pre-filled skb. ``NULL`` if any errors happen.
