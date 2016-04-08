
.. _API-cfg80211-assoc-timeout:

======================
cfg80211_assoc_timeout
======================

*man cfg80211_assoc_timeout(9)*

*4.6.0-rc1*

notification of timed out association


Synopsis
========

.. c:function:: void cfg80211_assoc_timeout( struct net_device * dev, struct cfg80211_bss * bss )

Arguments
=========

``dev``
    network device

``bss``
    The BSS entry with which association timed out.


Description
===========

This function may sleep. The caller must hold the corresponding wdev's mutex.
