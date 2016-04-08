
.. _API-struct-ieee80211-sta-ht-cap:

===========================
struct ieee80211_sta_ht_cap
===========================

*man struct ieee80211_sta_ht_cap(9)*

*4.6.0-rc1*

STA's HT capabilities


Synopsis
========

.. code-block:: c

    struct ieee80211_sta_ht_cap {
      u16 cap;
      bool ht_supported;
      u8 ampdu_factor;
      u8 ampdu_density;
      struct ieee80211_mcs_info mcs;
    };


Members
=======

cap
    HT capabilities map as described in 802.11n spec

ht_supported
    is HT supported by the STA

ampdu_factor
    Maximum A-MPDU length factor

ampdu_density
    Minimum A-MPDU spacing

mcs
    Supported MCS rates


Description
===========

This structure describes most essential parameters needed to describe 802.11n HT capabilities for an STA.
