
.. _API-cfg80211-remain-on-channel-expired:

==================================
cfg80211_remain_on_channel_expired
==================================

*man cfg80211_remain_on_channel_expired(9)*

*4.6.0-rc1*

remain_on_channel duration expired


Synopsis
========

.. c:function:: void cfg80211_remain_on_channel_expired( struct wireless_dev * wdev, u64 cookie, struct ieee80211_channel * chan, gfp_t gfp )

Arguments
=========

``wdev``
    wireless device

``cookie``
    the request cookie

``chan``
    The current channel (from remain_on_channel request)

``gfp``
    allocation flags
