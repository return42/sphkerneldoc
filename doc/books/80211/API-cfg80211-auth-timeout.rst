
.. _API-cfg80211-auth-timeout:

=====================
cfg80211_auth_timeout
=====================

*man cfg80211_auth_timeout(9)*

*4.6.0-rc1*

notification of timed out authentication


Synopsis
========

.. c:function:: void cfg80211_auth_timeout( struct net_device * dev, const u8 * addr )

Arguments
=========

``dev``
    network device

``addr``
    The MAC address of the device with which the authentication timed out


Description
===========

This function may sleep. The caller must hold the corresponding wdev's mutex.
