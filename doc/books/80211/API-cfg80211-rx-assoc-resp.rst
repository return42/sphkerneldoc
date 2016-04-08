
.. _API-cfg80211-rx-assoc-resp:

======================
cfg80211_rx_assoc_resp
======================

*man cfg80211_rx_assoc_resp(9)*

*4.6.0-rc1*

notification of processed association response


Synopsis
========

.. c:function:: void cfg80211_rx_assoc_resp( struct net_device * dev, struct cfg80211_bss * bss, const u8 * buf, size_t len, int uapsd_queues )

Arguments
=========

``dev``
    network device

``bss``
    the BSS that association was requested with, ownership of the pointer moves to cfg80211 in this call

``buf``
    authentication frame (header + body)

``len``
    length of the frame data

``uapsd_queues``
    bitmap of ACs configured to uapsd. -1 if n/a.


After being asked to associate via cfg80211_ops
===============================================

:``assoc`` the driver must call either this function or ``cfg80211_auth_timeout``.

This function may sleep. The caller must hold the corresponding wdev's mutex.
