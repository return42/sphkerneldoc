
.. _API-struct-cfg80211-ap-settings:

===========================
struct cfg80211_ap_settings
===========================

*man struct cfg80211_ap_settings(9)*

*4.6.0-rc1*

AP configuration


Synopsis
========

.. code-block:: c

    struct cfg80211_ap_settings {
      struct cfg80211_chan_def chandef;
      struct cfg80211_beacon_data beacon;
      int beacon_interval;
      int dtim_period;
      const u8 * ssid;
      size_t ssid_len;
      enum nl80211_hidden_ssid hidden_ssid;
      struct cfg80211_crypto_settings crypto;
      bool privacy;
      enum nl80211_auth_type auth_type;
      enum nl80211_smps_mode smps_mode;
      int inactivity_timeout;
      u8 p2p_ctwindow;
      bool p2p_opp_ps;
      const struct cfg80211_acl_data * acl;
      bool pbss;
    };


Members
=======

chandef
    defines the channel to use

beacon
    beacon data

beacon_interval
    beacon interval

dtim_period
    DTIM period

ssid
    SSID to be used in the BSS (note: may be ``NULL`` if not provided from user space)

ssid_len
    length of ``ssid``

hidden_ssid
    whether to hide the SSID in Beacon/Probe Response frames

crypto
    crypto settings

privacy
    the BSS uses privacy

auth_type
    Authentication type (algorithm)

smps_mode
    SMPS mode

inactivity_timeout
    time in seconds to determine station's inactivity.

p2p_ctwindow
    P2P CT Window

p2p_opp_ps
    P2P opportunistic PS

acl
    ACL configuration used by the drivers which has support for MAC address based access control

pbss
    If set, start as a PCP instead of AP. Relevant for DMG networks.


Description
===========

Used to configure an AP interface.
