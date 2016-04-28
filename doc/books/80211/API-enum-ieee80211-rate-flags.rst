.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-ieee80211-rate-flags:

=========================
enum ieee80211_rate_flags
=========================

*man enum ieee80211_rate_flags(9)*

*4.6.0-rc5*

rate flags


Synopsis
========

.. code-block:: c

    enum ieee80211_rate_flags {
      IEEE80211_RATE_SHORT_PREAMBLE,
      IEEE80211_RATE_MANDATORY_A,
      IEEE80211_RATE_MANDATORY_B,
      IEEE80211_RATE_MANDATORY_G,
      IEEE80211_RATE_ERP_G,
      IEEE80211_RATE_SUPPORTS_5MHZ,
      IEEE80211_RATE_SUPPORTS_10MHZ
    };


Constants
=========

IEEE80211_RATE_SHORT_PREAMBLE
    Hardware can send with short preamble on this bitrate; only relevant
    in 2.4GHz band and with CCK rates.

IEEE80211_RATE_MANDATORY_A
    This bitrate is a mandatory rate when used with 802.11a (on the 5
    GHz band); filled by the core code when registering the wiphy.

IEEE80211_RATE_MANDATORY_B
    This bitrate is a mandatory rate when used with 802.11b (on the 2.4
    GHz band); filled by the core code when registering the wiphy.

IEEE80211_RATE_MANDATORY_G
    This bitrate is a mandatory rate when used with 802.11g (on the 2.4
    GHz band); filled by the core code when registering the wiphy.

IEEE80211_RATE_ERP_G
    This is an ERP rate in 802.11g mode.

IEEE80211_RATE_SUPPORTS_5MHZ
    Rate can be used in 5 MHz mode

IEEE80211_RATE_SUPPORTS_10MHZ
    Rate can be used in 10 MHz mode


Description
===========

Hardware/specification flags for rates. These are structured in a way
that allows using the same bitrate structure for different bands/PHY
modes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
