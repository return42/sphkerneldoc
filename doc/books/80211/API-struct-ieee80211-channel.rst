.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-channel:

========================
struct ieee80211_channel
========================

*man struct ieee80211_channel(9)*

*4.6.0-rc5*

channel definition


Synopsis
========

.. code-block:: c

    struct ieee80211_channel {
      enum ieee80211_band band;
      u16 center_freq;
      u16 hw_value;
      u32 flags;
      int max_antenna_gain;
      int max_power;
      int max_reg_power;
      bool beacon_found;
      u32 orig_flags;
      int orig_mag;
      int orig_mpwr;
      enum nl80211_dfs_state dfs_state;
      unsigned long dfs_state_entered;
      unsigned int dfs_cac_ms;
    };


Members
=======

band
    band this channel belongs to.

center_freq
    center frequency in MHz

hw_value
    hardware-specific value for the channel

flags
    channel flags from ``enum`` ieee80211_channel_flags.

max_antenna_gain
    maximum antenna gain in dBi

max_power
    maximum transmission power (in dBm)

max_reg_power
    maximum regulatory transmission power (in dBm)

beacon_found
    helper to regulatory code to indicate when a beacon has been found
    on this channel. Use ``regulatory_hint_found_beacon`` to enable
    this, this is useful only on 5 GHz band.

orig_flags
    channel flags at registration time, used by regulatory code to
    support devices with additional restrictions

orig_mag
    internal use

orig_mpwr
    internal use

dfs_state
    current state of this channel. Only relevant if radar is required on
    this channel.

dfs_state_entered
    timestamp (jiffies) when the dfs state was entered.

dfs_cac_ms
    DFS CAC time in milliseconds, this is valid for DFS channels.


Description
===========

This structure describes a single channel for use with cfg80211.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
