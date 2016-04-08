
.. _API-cfg80211-roamed:

===============
cfg80211_roamed
===============

*man cfg80211_roamed(9)*

*4.6.0-rc1*

notify cfg80211 of roaming


Synopsis
========

.. c:function:: void cfg80211_roamed( struct net_device * dev, struct ieee80211_channel * channel, const u8 * bssid, const u8 * req_ie, size_t req_ie_len, const u8 * resp_ie, size_t resp_ie_len, gfp_t gfp )

Arguments
=========

``dev``
    network device

``channel``
    the channel of the new AP

``bssid``
    the BSSID of the new AP

``req_ie``
    association request IEs (maybe be ``NULL``)

``req_ie_len``
    association request IEs length

``resp_ie``
    association response IEs (may be ``NULL``)

``resp_ie_len``
    assoc response IEs length

``gfp``
    allocation flags


Description
===========

It should be called by the underlying driver whenever it roamed from one AP to another while connected.
