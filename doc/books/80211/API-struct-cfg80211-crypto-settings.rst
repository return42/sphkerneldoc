.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-crypto-settings:

===============================
struct cfg80211_crypto_settings
===============================

*man struct cfg80211_crypto_settings(9)*

*4.6.0-rc5*

Crypto settings


Synopsis
========

.. code-block:: c

    struct cfg80211_crypto_settings {
      u32 wpa_versions;
      u32 cipher_group;
      int n_ciphers_pairwise;
      u32 ciphers_pairwise[NL80211_MAX_NR_CIPHER_SUITES];
      int n_akm_suites;
      u32 akm_suites[NL80211_MAX_NR_AKM_SUITES];
      bool control_port;
      __be16 control_port_ethertype;
      bool control_port_no_encrypt;
    };


Members
=======

wpa_versions
    indicates which, if any, WPA versions are enabled (from enum
    nl80211_wpa_versions)

cipher_group
    group key cipher suite (or 0 if unset)

n_ciphers_pairwise
    number of AP supported unicast ciphers

ciphers_pairwise[NL80211_MAX_NR_CIPHER_SUITES]
    unicast key cipher suites

n_akm_suites
    number of AKM suites

akm_suites[NL80211_MAX_NR_AKM_SUITES]
    AKM suites

control_port
    Whether user space controls IEEE 802.1X port, i.e., sets/clears
    ``NL80211_STA_FLAG_AUTHORIZED``. If true, the driver is required to
    assume that the port is unauthorized until authorized by user space.
    Otherwise, port is marked authorized by default.

control_port_ethertype
    the control port protocol that should be allowed through even on
    unauthorized ports

control_port_no_encrypt
    TRUE to prevent encryption of control port protocol frames.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
