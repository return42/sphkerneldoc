.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-michael-mic-failure:

============================
cfg80211_michael_mic_failure
============================

*man cfg80211_michael_mic_failure(9)*

*4.6.0-rc5*

notification of Michael MIC failure (TKIP)


Synopsis
========

.. c:function:: void cfg80211_michael_mic_failure( struct net_device * dev, const u8 * addr, enum nl80211_key_type key_type, int key_id, const u8 * tsc, gfp_t gfp )

Arguments
=========

``dev``
    network device

``addr``
    The source MAC address of the frame

``key_type``
    The key type that the received frame used

``key_id``
    Key identifier (0..3). Can be -1 if missing.

``tsc``
    The TSC value of the frame that generated the MIC failure (6 octets)

``gfp``
    allocation flags


Description
===========

This function is called whenever the local MAC detects a MIC failure in
a received frame. This matches with
MLME-MICHAELMICFAILURE.\ ``indication`` primitive.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
