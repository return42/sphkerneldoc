
.. _API-cfg80211-testmode-reply:

=======================
cfg80211_testmode_reply
=======================

*man cfg80211_testmode_reply(9)*

*4.6.0-rc1*

send the reply skb


Synopsis
========

.. c:function:: int cfg80211_testmode_reply( struct sk_buff * skb )

Arguments
=========

``skb``
    The skb, must have been allocated with ``cfg80211_testmode_alloc_reply_skb``


Description
===========

Since calling this function will usually be the last thing before returning from the ``testmode_cmd`` you should return the error code. Note that this function consumes the skb
regardless of the return value.


Return
======

An error code or 0 on success.
