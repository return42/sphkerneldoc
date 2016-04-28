.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-inform-bss-data:

========================
cfg80211_inform_bss_data
========================

*man cfg80211_inform_bss_data(9)*

*4.6.0-rc5*

inform cfg80211 of a new BSS


Synopsis
========

.. c:function:: struct cfg80211_bss * cfg80211_inform_bss_data( struct wiphy * wiphy, struct cfg80211_inform_bss * data, enum cfg80211_bss_frame_type ftype, const u8 * bssid, u64 tsf, u16 capability, u16 beacon_interval, const u8 * ie, size_t ielen, gfp_t gfp )

Arguments
=========

``wiphy``
    the wiphy reporting the BSS

``data``
    the BSS metadata

``ftype``
    frame type (if known)

``bssid``
    the BSSID of the BSS

``tsf``
    the TSF sent by the peer in the beacon/probe response (or 0)

``capability``
    the capability field sent by the peer

``beacon_interval``
    the beacon interval announced by the peer

``ie``
    additional IEs sent by the peer

``ielen``
    length of the additional IEs

``gfp``
    context flags


Description
===========

This informs cfg80211 that BSS information was found and the BSS should
be updated/added.


Return
======

A referenced struct, must be released with ``cfg80211_put_bss``! Or
``NULL`` on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
