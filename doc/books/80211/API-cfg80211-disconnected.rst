.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-disconnected:

=====================
cfg80211_disconnected
=====================

*man cfg80211_disconnected(9)*

*4.6.0-rc5*

notify cfg80211 that connection was dropped


Synopsis
========

.. c:function:: void cfg80211_disconnected( struct net_device * dev, u16 reason, const u8 * ie, size_t ie_len, bool locally_generated, gfp_t gfp )

Arguments
=========

``dev``
    network device

``reason``
    reason code for the disconnection, set it to 0 if unknown

``ie``
    information elements of the deauth/disassoc frame (may be ``NULL``)

``ie_len``
    length of IEs

``locally_generated``
    disconnection was requested locally

``gfp``
    allocation flags


Description
===========

After it calls this function, the driver should enter an idle state and
not try to connect to any AP any more.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
