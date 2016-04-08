
.. _API-struct-ieee80211-conf:

=====================
struct ieee80211_conf
=====================

*man struct ieee80211_conf(9)*

*4.6.0-rc1*

configuration of the device


Synopsis
========

.. code-block:: c

    struct ieee80211_conf {
      u32 flags;
      int power_level;
      int dynamic_ps_timeout;
      u16 listen_interval;
      u8 ps_dtim_period;
      u8 long_frame_max_tx_count;
      u8 short_frame_max_tx_count;
      struct cfg80211_chan_def chandef;
      bool radar_enabled;
      enum ieee80211_smps_mode smps_mode;
    };


Members
=======

flags
    configuration flags defined above

power_level
    requested transmit power (in dBm), backward compatibility value only that is set to the minimum of all interfaces

dynamic_ps_timeout
    The dynamic powersave timeout (in ms), see the powersave documentation below. This variable is valid only when the CONF_PS flag is set.

listen_interval
    listen interval in units of beacon interval

ps_dtim_period
    The DTIM period of the AP we're connected to, for use in power saving. Power saving will not be enabled until a beacon has been received and the DTIM period is known.

long_frame_max_tx_count
    Maximum number of transmissions for a “long” frame (a frame not RTS protected), called “dot11LongRetryLimit” in 802.11, but actually means the number of transmissions not the
    number of retries

short_frame_max_tx_count
    Maximum number of transmissions for a “short” frame, called “dot11ShortRetryLimit” in 802.11, but actually means the number of transmissions not the number of retries

chandef
    the channel definition to tune to

radar_enabled
    whether radar detection is enabled

smps_mode
    spatial multiplexing powersave mode; note that ``IEEE80211_SMPS_STATIC`` is used when the device is not configured for an HT channel. Note that this is only valid if channel
    contexts are not used, otherwise each channel context has the number of chains listed.


Description
===========

This struct indicates how the driver shall configure the hardware.
