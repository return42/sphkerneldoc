.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-connect-params:

==============================
struct cfg80211_connect_params
==============================

*man struct cfg80211_connect_params(9)*

*4.6.0-rc5*

Connection parameters


Synopsis
========

.. code-block:: c

    struct cfg80211_connect_params {
      struct ieee80211_channel * channel;
      struct ieee80211_channel * channel_hint;
      const u8 * bssid;
      const u8 * bssid_hint;
      const u8 * ssid;
      size_t ssid_len;
      enum nl80211_auth_type auth_type;
      const u8 * ie;
      size_t ie_len;
      bool privacy;
      enum nl80211_mfp mfp;
      struct cfg80211_crypto_settings crypto;
      const u8 * key;
      u8 key_len;
      u8 key_idx;
      u32 flags;
      int bg_scan_period;
      struct ieee80211_ht_cap ht_capa;
      struct ieee80211_ht_cap ht_capa_mask;
      struct ieee80211_vht_cap vht_capa;
      struct ieee80211_vht_cap vht_capa_mask;
      bool pbss;
    };


Members
=======

channel
    The channel to use or ``NULL`` if not specified (auto-select based
    on scan results)

channel_hint
    The channel of the recommended BSS for initial connection or
    ``NULL`` if not specified

bssid
    The AP BSSID or ``NULL`` if not specified (auto-select based on scan
    results)

bssid_hint
    The recommended AP BSSID for initial connection to the BSS or
    ``NULL`` if not specified. Unlike the ``bssid`` parameter, the
    driver is allowed to ignore this ``bssid_hint`` if it has knowledge
    of a better BSS to use.

ssid
    SSID

ssid_len
    Length of ssid in octets

auth_type
    Authentication type (algorithm)

ie
    IEs for association request

ie_len
    Length of assoc_ie in octets

privacy
    indicates whether privacy-enabled APs should be used

mfp
    indicate whether management frame protection is used

crypto
    crypto settings

key
    WEP key for shared key authentication

key_len
    length of WEP key for shared key authentication

key_idx
    index of WEP key for shared key authentication

flags
    See ``enum`` cfg80211_assoc_req_flags

bg_scan_period
    Background scan period in seconds or -1 to indicate that default
    value is to be used.

ht_capa
    HT Capabilities over-rides. Values set in ht_capa_mask will be
    used in ht_capa. Un-supported values will be ignored.

ht_capa_mask
    The bits of ht_capa which are to be used.

vht_capa
    VHT Capability overrides

vht_capa_mask
    The bits of vht_capa which are to be used.

pbss
    if set, connect to a PCP instead of AP. Valid for DMG networks.


Description
===========

This structure provides information needed to complete IEEE 802.11
authentication and association.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
