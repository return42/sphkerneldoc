
.. _API-ieee80211-get-response-rate:

===========================
ieee80211_get_response_rate
===========================

*man ieee80211_get_response_rate(9)*

*4.6.0-rc1*

get basic rate for a given rate


Synopsis
========

.. c:function:: struct ieee80211_rate ⋆ ieee80211_get_response_rate( struct ieee80211_supported_band * sband, u32 basic_rates, int bitrate )

Arguments
=========

``sband``
    the band to look for rates in

``basic_rates``
    bitmap of basic rates

``bitrate``
    the bitrate for which to find the basic rate


Return
======

The basic rate corresponding to a given bitrate, that is the next lower bitrate contained in the basic rate map, which is, for this function, given as a bitmap of indices of rates
in the band's bitrate table.
