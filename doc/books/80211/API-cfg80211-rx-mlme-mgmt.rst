
.. _API-cfg80211-rx-mlme-mgmt:

=====================
cfg80211_rx_mlme_mgmt
=====================

*man cfg80211_rx_mlme_mgmt(9)*

*4.6.0-rc1*

notification of processed MLME management frame


Synopsis
========

.. c:function:: void cfg80211_rx_mlme_mgmt( struct net_device * dev, const u8 * buf, size_t len )

Arguments
=========

``dev``
    network device

``buf``
    authentication frame (header + body)

``len``
    length of the frame data


Description
===========

This function is called whenever an authentication, disassociation or deauthentication frame has been received and processed in station mode.


After being asked to authenticate via cfg80211_ops
==================================================

:``auth`` the driver must call either this function or ``cfg80211_auth_timeout``.


After being asked to associate via cfg80211_ops
===============================================

:``assoc`` the driver must call either this function or ``cfg80211_auth_timeout``. While connected, the driver must calls this for received and processed disassociation and
deauthentication frames. If the frame couldn't be used because it was unprotected, the driver must call the function ``cfg80211_rx_unprot_mlme_mgmt`` instead.

This function may sleep. The caller must hold the corresponding wdev's mutex.
