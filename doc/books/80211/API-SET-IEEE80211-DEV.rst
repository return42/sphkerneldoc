.. -*- coding: utf-8; mode: rst -*-

.. _API-SET-IEEE80211-DEV:

=================
SET_IEEE80211_DEV
=================

*man SET_IEEE80211_DEV(9)*

*4.6.0-rc5*

set device for 802.11 hardware


Synopsis
========

.. c:function:: void SET_IEEE80211_DEV( struct ieee80211_hw * hw, struct device * dev )

Arguments
=========

``hw``
    the ``struct ieee80211_hw`` to set the device for

``dev``
    the ``struct device`` of this 802.11 device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
