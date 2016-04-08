
.. _API-cfg80211-testmode-event:

=======================
cfg80211_testmode_event
=======================

*man cfg80211_testmode_event(9)*

*4.6.0-rc1*

send the event


Synopsis
========

.. c:function:: void cfg80211_testmode_event( struct sk_buff * skb, gfp_t gfp )

Arguments
=========

``skb``
    The skb, must have been allocated with ``cfg80211_testmode_alloc_event_skb``

``gfp``
    allocation flags


Description
===========

This function sends the given ``skb``, which must have been allocated by ``cfg80211_testmode_alloc_event_skb``, as an event. It always consumes it.
