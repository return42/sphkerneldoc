
.. _API-ieee80211-rts-duration:

======================
ieee80211_rts_duration
======================

*man ieee80211_rts_duration(9)*

*4.6.0-rc1*

Get the duration field for an RTS frame


Synopsis
========

.. c:function:: __le16 ieee80211_rts_duration( struct ieee80211_hw * hw, struct ieee80211_vif * vif, size_t frame_len, const struct ieee80211_tx_info * frame_txctl )

Arguments
=========

``hw``
    pointer obtained from ``ieee80211_alloc_hw``.

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback.

``frame_len``
    the length of the frame that is going to be protected by the RTS.

``frame_txctl``
    ``struct ieee80211_tx_info`` of the frame.


Description
===========

If the RTS is generated in firmware, but the host system must provide the duration field, the low-level driver uses this function to receive the duration field value in
little-endian byteorder.


Return
======

The duration.
