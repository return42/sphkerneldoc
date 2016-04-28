.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-assoc-timeout:

======================
cfg80211_assoc_timeout
======================

*man cfg80211_assoc_timeout(9)*

*4.6.0-rc5*

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

This function may sleep. The caller must hold the corresponding wdev's
mutex.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
