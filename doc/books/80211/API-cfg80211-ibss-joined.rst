.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-ibss-joined:

====================
cfg80211_ibss_joined
====================

*man cfg80211_ibss_joined(9)*

*4.6.0-rc5*

notify cfg80211 that device joined an IBSS


Synopsis
========

.. c:function:: void cfg80211_ibss_joined( struct net_device * dev, const u8 * bssid, struct ieee80211_channel * channel, gfp_t gfp )

Arguments
=========

``dev``
    network device

``bssid``
    the BSSID of the IBSS joined

``channel``
    the channel of the IBSS joined

``gfp``
    allocation flags


Description
===========

This function notifies cfg80211 that the device joined an IBSS or
switched to a different BSSID. Before this function can be called,
either a beacon has to have been received from the IBSS, or one of the
cfg80211_inform_bss{,_frame} functions must have been called with the
locally generated beacon -- this guarantees that there is always a scan
result for this IBSS. cfg80211 will handle the rest.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
