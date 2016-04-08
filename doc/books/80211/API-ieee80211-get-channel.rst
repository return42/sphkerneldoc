
.. _API-ieee80211-get-channel:

=====================
ieee80211_get_channel
=====================

*man ieee80211_get_channel(9)*

*4.6.0-rc1*

get channel struct from wiphy for specified frequency


Synopsis
========

.. c:function:: struct ieee80211_channel ⋆ ieee80211_get_channel( struct wiphy * wiphy, int freq )

Arguments
=========

``wiphy``
    the struct wiphy to get the channel for

``freq``
    the center frequency of the channel


Return
======

The channel struct from ``wiphy`` at ``freq``.
