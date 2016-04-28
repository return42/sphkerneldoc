.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-generic-frame-duration:

================================
ieee80211_generic_frame_duration
================================

*man ieee80211_generic_frame_duration(9)*

*4.6.0-rc5*

Calculate the duration field for a frame


Synopsis
========

.. c:function:: __le16 ieee80211_generic_frame_duration( struct ieee80211_hw * hw, struct ieee80211_vif * vif, enum ieee80211_band band, size_t frame_len, struct ieee80211_rate * rate )

Arguments
=========

``hw``
    pointer obtained from ``ieee80211_alloc_hw``.

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback.

``band``
    the band to calculate the frame duration on

``frame_len``
    the length of the frame.

``rate``
    the rate at which the frame is going to be transmitted.


Description
===========

Calculate the duration field of some generic frame, given its length and
transmission rate (in 100kbps).


Return
======

The duration.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
