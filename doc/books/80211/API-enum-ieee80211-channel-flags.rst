
.. _API-enum-ieee80211-channel-flags:

============================
enum ieee80211_channel_flags
============================

*man enum ieee80211_channel_flags(9)*

*4.6.0-rc1*

channel flags


Synopsis
========

.. code-block:: c

    enum ieee80211_channel_flags {
      IEEE80211_CHAN_DISABLED,
      IEEE80211_CHAN_NO_IR,
      IEEE80211_CHAN_RADAR,
      IEEE80211_CHAN_NO_HT40PLUS,
      IEEE80211_CHAN_NO_HT40MINUS,
      IEEE80211_CHAN_NO_OFDM,
      IEEE80211_CHAN_NO_80MHZ,
      IEEE80211_CHAN_NO_160MHZ,
      IEEE80211_CHAN_INDOOR_ONLY,
      IEEE80211_CHAN_IR_CONCURRENT,
      IEEE80211_CHAN_NO_20MHZ,
      IEEE80211_CHAN_NO_10MHZ
    };


Constants
=========

IEEE80211_CHAN_DISABLED
    This channel is disabled.

IEEE80211_CHAN_NO_IR
    do not initiate radiation, this includes sending probe requests or beaconing.

IEEE80211_CHAN_RADAR
    Radar detection is required on this channel.

IEEE80211_CHAN_NO_HT40PLUS
    extension channel above this channel is not permitted.

IEEE80211_CHAN_NO_HT40MINUS
    extension channel below this channel is not permitted.

IEEE80211_CHAN_NO_OFDM
    OFDM is not allowed on this channel.

IEEE80211_CHAN_NO_80MHZ
    If the driver supports 80 MHz on the band, this flag indicates that an 80 MHz channel cannot use this channel as the control or any of the secondary channels. This may be due
    to the driver or due to regulatory bandwidth restrictions.

IEEE80211_CHAN_NO_160MHZ
    If the driver supports 160 MHz on the band, this flag indicates that an 160 MHz channel cannot use this channel as the control or any of the secondary channels. This may be due
    to the driver or due to regulatory bandwidth restrictions.

IEEE80211_CHAN_INDOOR_ONLY
    see ``NL80211_FREQUENCY_ATTR_INDOOR_ONLY``

IEEE80211_CHAN_IR_CONCURRENT
    see ``NL80211_FREQUENCY_ATTR_IR_CONCURRENT``

IEEE80211_CHAN_NO_20MHZ
    20 MHz bandwidth is not permitted on this channel.

IEEE80211_CHAN_NO_10MHZ
    10 MHz bandwidth is not permitted on this channel.


Description
===========

Channel flags set by the regulatory control code.
