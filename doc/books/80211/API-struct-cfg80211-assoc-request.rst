
.. _API-struct-cfg80211-assoc-request:

=============================
struct cfg80211_assoc_request
=============================

*man struct cfg80211_assoc_request(9)*

*4.6.0-rc1*

(Re)Association request data


Synopsis
========

.. code-block:: c

    struct cfg80211_assoc_request {
      struct cfg80211_bss * bss;
      const u8 * ie;
      const u8 * prev_bssid;
      size_t ie_len;
      struct cfg80211_crypto_settings crypto;
      bool use_mfp;
      u32 flags;
      struct ieee80211_ht_cap ht_capa;
      struct ieee80211_ht_cap ht_capa_mask;
      struct ieee80211_vht_cap vht_capa;
      struct ieee80211_vht_cap vht_capa_mask;
    };


Members
=======

bss
    The BSS to associate with. If the call is successful the driver is given a reference that it must give back to ``cfg80211_send_rx_assoc`` or to ``cfg80211_assoc_timeout``. To
    ensure proper refcounting, new association requests while already associating must be rejected.

ie
    Extra IEs to add to (Re)Association Request frame or ``NULL``

prev_bssid
    previous BSSID, if not ``NULL`` use reassociate frame

ie_len
    Length of ie buffer in octets

crypto
    crypto settings

use_mfp
    Use management frame protection (IEEE 802.11w) in this association

flags
    See ``enum`` cfg80211_assoc_req_flags

ht_capa
    HT Capabilities over-rides. Values set in ht_capa_mask will be used in ht_capa. Un-supported values will be ignored.

ht_capa_mask
    The bits of ht_capa which are to be used.

vht_capa
    VHT capability override

vht_capa_mask
    VHT capability mask indicating which fields to use


Description
===========

This structure provides information needed to complete IEEE 802.11 (re)association.
