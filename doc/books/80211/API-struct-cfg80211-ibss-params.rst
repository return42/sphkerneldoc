
.. _API-struct-cfg80211-ibss-params:

===========================
struct cfg80211_ibss_params
===========================

*man struct cfg80211_ibss_params(9)*

*4.6.0-rc1*

IBSS parameters


Synopsis
========

.. code-block:: c

    struct cfg80211_ibss_params {
      const u8 * ssid;
      const u8 * bssid;
      struct cfg80211_chan_def chandef;
      const u8 * ie;
      u8 ssid_len;
      u8 ie_len;
      u16 beacon_interval;
      u32 basic_rates;
      bool channel_fixed;
      bool privacy;
      bool control_port;
      bool userspace_handles_dfs;
      int mcast_rate[IEEE80211_NUM_BANDS];
      struct ieee80211_ht_cap ht_capa;
      struct ieee80211_ht_cap ht_capa_mask;
    };


Members
=======

ssid
    The SSID, will always be non-null.

bssid
    Fixed BSSID requested, maybe be ``NULL``, if set do not search for IBSSs with a different BSSID.

chandef
    defines the channel to use if no other IBSS to join can be found

ie
    information element(s) to include in the beacon

ssid_len
    The length of the SSID, will always be non-zero.

ie_len
    length of that

beacon_interval
    beacon interval to use

basic_rates
    bitmap of basic rates to use when creating the IBSS

channel_fixed
    The channel should be fixed -- do not search for IBSSs to join on other channels.

privacy
    this is a protected network, keys will be configured after joining

control_port
    whether user space controls IEEE 802.1X port, i.e., sets/clears ``NL80211_STA_FLAG_AUTHORIZED``. If true, the driver is required to assume that the port is unauthorized until
    authorized by user space. Otherwise, port is marked authorized by default.

userspace_handles_dfs
    whether user space controls DFS operation, i.e. changes the channel when a radar is detected. This is required to operate on DFS channels.

mcast_rate[IEEE80211_NUM_BANDS]
    per-band multicast rate index + 1 (0: disabled)

ht_capa
    HT Capabilities over-rides. Values set in ht_capa_mask will be used in ht_capa. Un-supported values will be ignored.

ht_capa_mask
    The bits of ht_capa which are to be used.


Description
===========

This structure defines the IBSS parameters for the ``join_ibss`` method.
