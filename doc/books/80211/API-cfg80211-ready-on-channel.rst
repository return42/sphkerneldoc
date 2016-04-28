.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-ready-on-channel:

=========================
cfg80211_ready_on_channel
=========================

*man cfg80211_ready_on_channel(9)*

*4.6.0-rc5*

notification of remain_on_channel start


Synopsis
========

.. c:function:: void cfg80211_ready_on_channel( struct wireless_dev * wdev, u64 cookie, struct ieee80211_channel * chan, unsigned int duration, gfp_t gfp )

Arguments
=========

``wdev``
    wireless device

``cookie``
    the request cookie

``chan``
    The current channel (from remain_on_channel request)

``duration``
    Duration in milliseconds that the driver intents to remain on the
    channel

``gfp``
    allocation flags


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
