
.. _API-struct-ieee80211-supported-band:

===============================
struct ieee80211_supported_band
===============================

*man struct ieee80211_supported_band(9)*

*4.6.0-rc1*

frequency band definition


Synopsis
========

.. code-block:: c

    struct ieee80211_supported_band {
      struct ieee80211_channel * channels;
      struct ieee80211_rate * bitrates;
      enum ieee80211_band band;
      int n_channels;
      int n_bitrates;
      struct ieee80211_sta_ht_cap ht_cap;
      struct ieee80211_sta_vht_cap vht_cap;
    };


Members
=======

channels
    Array of channels the hardware can operate in in this band.

bitrates
    Array of bitrates the hardware can operate with in this band. Must be sorted to give a valid “supported rates” IE, i.e. CCK rates first, then OFDM.

band
    the band this structure represents

n_channels
    Number of channels in ``channels``

n_bitrates
    Number of bitrates in ``bitrates``

ht_cap
    HT capabilities in this band

vht_cap
    VHT capabilities in this band


Description
===========

This structure describes a frequency band a wiphy is able to operate in.
