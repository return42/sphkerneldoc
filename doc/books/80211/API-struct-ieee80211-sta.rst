
.. _API-struct-ieee80211-sta:

====================
struct ieee80211_sta
====================

*man struct ieee80211_sta(9)*

*4.6.0-rc1*

station table entry


Synopsis
========

.. code-block:: c

    struct ieee80211_sta {
      u32 supp_rates[IEEE80211_NUM_BANDS];
      u8 addr[ETH_ALEN];
      u16 aid;
      struct ieee80211_sta_ht_cap ht_cap;
      struct ieee80211_sta_vht_cap vht_cap;
      bool wme;
      u8 uapsd_queues;
      u8 max_sp;
      u8 rx_nss;
      enum ieee80211_sta_rx_bandwidth bandwidth;
      enum ieee80211_smps_mode smps_mode;
      struct ieee80211_sta_rates __rcu * rates;
      bool tdls;
      bool tdls_initiator;
      bool mfp;
      u8 max_amsdu_subframes;
      u16 max_amsdu_len;
      struct ieee80211_txq * txq[IEEE80211_NUM_TIDS];
      u8 drv_priv[0];
    };


Members
=======

supp_rates[IEEE80211_NUM_BANDS]
    Bitmap of supported rates (per band)

addr[ETH_ALEN]
    MAC address

aid
    AID we assigned to the station if we're an AP

ht_cap
    HT capabilities of this STA; restricted to our own capabilities

vht_cap
    VHT capabilities of this STA; restricted to our own capabilities

wme
    indicates whether the STA supports QoS/WME (if local devices does, otherwise always false)

uapsd_queues
    bitmap of queues configured for uapsd. Only valid if wme is supported.

max_sp
    max Service Period. Only valid if wme is supported.

rx_nss
    in HT/VHT, the maximum number of spatial streams the station can receive at the moment, changed by operating mode notifications and capabilities. The value is only valid after
    the station moves to associated state.

bandwidth
    current bandwidth the station can receive with

smps_mode
    current SMPS mode (off, static or dynamic)

rates
    rate control selection table

tdls
    indicates whether the STA is a TDLS peer

tdls_initiator
    indicates the STA is an initiator of the TDLS link. Only valid if the STA is a TDLS peer in the first place.

mfp
    indicates whether the STA uses management frame protection or not.

max_amsdu_subframes
    indicates the maximal number of MSDUs in a single A-MSDU. Taken from the Extended Capabilities element. 0 means unlimited.

max_amsdu_len
    indicates the maximal length of an A-MSDU in bytes. This field is always valid for packets with a VHT preamble. For packets with a HT preamble, additional limits apply: + If
    the skb is transmitted as part of a BA agreement, the A-MSDU maximal size is min(max_amsdu_len, 4065) bytes. + If the skb is not part of a BA aggreement, the A-MSDU maximal
    size is min(max_amsdu_len, 7935) bytes. Both additional HT limits must be enforced by the low level driver. This is defined by the spec (IEEE 802.11-2012 section 8.3.2.2 NOTE
    2).

txq[IEEE80211_NUM_TIDS]
    per-TID data TX queues (if driver uses the TXQ abstraction)

drv_priv[0]
    data area for driver use, will always be aligned to sizeof(void ⋆), size is determined in hw information.


Description
===========

A station table entry represents a station we are possibly communicating with. Since stations are RCU-managed in mac80211, any ieee80211_sta pointer you get access to must either
be protected by ``rcu_read_lock`` explicitly or implicitly, or you must take good care to not use such a pointer after a call to your sta_remove callback that removed it.
