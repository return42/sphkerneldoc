.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-auth-timeout:

=====================
cfg80211_auth_timeout
=====================

*man cfg80211_auth_timeout(9)*

*4.6.0-rc5*

notification of timed out authentication


Synopsis
========

.. c:function:: void cfg80211_auth_timeout( struct net_device * dev, const u8 * addr )

Arguments
=========

``dev``
    network device

``addr``
    The MAC address of the device with which the authentication timed
    out


Description
===========

This function may sleep. The caller must hold the corresponding wdev's
mutex.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
