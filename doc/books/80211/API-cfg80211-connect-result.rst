
.. _API-cfg80211-connect-result:

=======================
cfg80211_connect_result
=======================

*man cfg80211_connect_result(9)*

*4.6.0-rc1*

notify cfg80211 of connection result


Synopsis
========

.. c:function:: void cfg80211_connect_result( struct net_device * dev, const u8 * bssid, const u8 * req_ie, size_t req_ie_len, const u8 * resp_ie, size_t resp_ie_len, u16 status, gfp_t gfp )

Arguments
=========

``dev``
    network device

``bssid``
    the BSSID of the AP

``req_ie``
    association request IEs (maybe be ``NULL``)

``req_ie_len``
    association request IEs length

``resp_ie``
    association response IEs (may be ``NULL``)

``resp_ie_len``
    assoc response IEs length

``status``
    status code, 0 for successful connection, use ``WLAN_STATUS_UNSPECIFIED_FAILURE`` if your device cannot give you the real status code for failures.

``gfp``
    allocation flags


Description
===========

It should be called by the underlying driver whenever ``connect`` has succeeded.
