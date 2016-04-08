
.. _API-cfg80211-tx-mlme-mgmt:

=====================
cfg80211_tx_mlme_mgmt
=====================

*man cfg80211_tx_mlme_mgmt(9)*

*4.6.0-rc1*

notification of transmitted deauth/disassoc frame


Synopsis
========

.. c:function:: void cfg80211_tx_mlme_mgmt( struct net_device * dev, const u8 * buf, size_t len )

Arguments
=========

``dev``
    network device

``buf``
    802.11 frame (header + body)

``len``
    length of the frame data


Description
===========

This function is called whenever deauthentication has been processed in station mode. This includes both received deauthentication frames and locally generated ones. This function
may sleep. The caller must hold the corresponding wdev's mutex.
