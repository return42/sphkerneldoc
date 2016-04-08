
.. _API-struct-cfg80211-auth-request:

============================
struct cfg80211_auth_request
============================

*man struct cfg80211_auth_request(9)*

*4.6.0-rc1*

Authentication request data


Synopsis
========

.. code-block:: c

    struct cfg80211_auth_request {
      struct cfg80211_bss * bss;
      const u8 * ie;
      size_t ie_len;
      enum nl80211_auth_type auth_type;
      const u8 * key;
      u8 key_len;
      u8 key_idx;
      const u8 * sae_data;
      size_t sae_data_len;
    };


Members
=======

bss
    The BSS to authenticate with, the callee must obtain a reference to it if it needs to keep it.

ie
    Extra IEs to add to Authentication frame or ``NULL``

ie_len
    Length of ie buffer in octets

auth_type
    Authentication type (algorithm)

key
    WEP key for shared key authentication

key_len
    length of WEP key for shared key authentication

key_idx
    index of WEP key for shared key authentication

sae_data
    Non-IE data to use with SAE or ``NULL``. This starts with Authentication transaction sequence number field.

sae_data_len
    Length of sae_data buffer in octets


Description
===========

This structure provides information needed to complete IEEE 802.11 authentication.
