.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-mac80211-rate-control-flags:

================================
enum mac80211_rate_control_flags
================================

*man enum mac80211_rate_control_flags(9)*

*4.6.0-rc5*

per-rate flags set by the Rate Control algorithm.


Synopsis
========

.. code-block:: c

    enum mac80211_rate_control_flags {
      IEEE80211_TX_RC_USE_RTS_CTS,
      IEEE80211_TX_RC_USE_CTS_PROTECT,
      IEEE80211_TX_RC_USE_SHORT_PREAMBLE,
      IEEE80211_TX_RC_MCS,
      IEEE80211_TX_RC_GREEN_FIELD,
      IEEE80211_TX_RC_40_MHZ_WIDTH,
      IEEE80211_TX_RC_DUP_DATA,
      IEEE80211_TX_RC_SHORT_GI,
      IEEE80211_TX_RC_VHT_MCS,
      IEEE80211_TX_RC_80_MHZ_WIDTH,
      IEEE80211_TX_RC_160_MHZ_WIDTH
    };


Constants
=========

IEEE80211_TX_RC_USE_RTS_CTS
    Use RTS/CTS exchange for this rate.

IEEE80211_TX_RC_USE_CTS_PROTECT
    CTS-to-self protection is required. This is set if the current BSS
    requires ERP protection.

IEEE80211_TX_RC_USE_SHORT_PREAMBLE
    Use short preamble.

IEEE80211_TX_RC_MCS
    HT rate.

IEEE80211_TX_RC_GREEN_FIELD
    Indicates whether this rate should be used in Greenfield mode.

IEEE80211_TX_RC_40_MHZ_WIDTH
    Indicates if the Channel Width should be 40 MHz.

IEEE80211_TX_RC_DUP_DATA
    The frame should be transmitted on both of the adjacent 20 MHz
    channels, if the current channel type is NL80211_CHAN_HT40MINUS or
    NL80211_CHAN_HT40PLUS.

IEEE80211_TX_RC_SHORT_GI
    Short Guard interval should be used for this rate.

IEEE80211_TX_RC_VHT_MCS
    VHT MCS rate, in this case the idx field is split into a higher 4
    bits (Nss) and lower 4 bits (MCS number)

IEEE80211_TX_RC_80_MHZ_WIDTH
    Indicates 80 MHz transmission

IEEE80211_TX_RC_160_MHZ_WIDTH
    Indicates 160 MHz transmission (80+80 isn't supported yet)


Description
===========

These flags are set by the Rate control algorithm for each rate during
tx, in the ``flags`` member of struct ieee80211_tx_rate.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
