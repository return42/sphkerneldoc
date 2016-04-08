
.. _API-struct-ieee80211-rate:

=====================
struct ieee80211_rate
=====================

*man struct ieee80211_rate(9)*

*4.6.0-rc1*

bitrate definition


Synopsis
========

.. code-block:: c

    struct ieee80211_rate {
      u32 flags;
      u16 bitrate;
      u16 hw_value;
      u16 hw_value_short;
    };


Members
=======

flags
    rate-specific flags

bitrate
    bitrate in units of 100 Kbps

hw_value
    driver/hardware value for this rate

hw_value_short
    driver/hardware value for this rate when short preamble is used


Description
===========

This structure describes a bitrate that an 802.11 PHY can operate with. The two values ``hw_value`` and ``hw_value_short`` are only for driver use when pointers to this structure
are passed around.
