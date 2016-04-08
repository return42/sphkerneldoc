
.. _API-enum-ieee80211-conf-flags:

=========================
enum ieee80211_conf_flags
=========================

*man enum ieee80211_conf_flags(9)*

*4.6.0-rc1*

configuration flags


Synopsis
========

.. code-block:: c

    enum ieee80211_conf_flags {
      IEEE80211_CONF_MONITOR,
      IEEE80211_CONF_PS,
      IEEE80211_CONF_IDLE,
      IEEE80211_CONF_OFFCHANNEL
    };


Constants
=========

IEEE80211_CONF_MONITOR
    there's a monitor interface present -- use this to determine for example whether to calculate timestamps for packets or not, do not use instead of filter flags!

IEEE80211_CONF_PS
    Enable 802.11 power save mode (managed mode only). This is the power save mode defined by IEEE 802.11-2007 section 11.2, meaning that the hardware still wakes up for beacons,
    is able to transmit frames and receive the possible acknowledgment frames. Not to be confused with hardware specific wakeup/sleep states, driver is responsible for that. See
    the section “Powersave support” for more.

IEEE80211_CONF_IDLE
    The device is running, but idle; if the flag is set the driver should be prepared to handle configuration requests but may turn the device off as much as possible. Typically,
    this flag will be set when an interface is set UP but not associated or scanning, but it can also be unset in that case when monitor interfaces are active.

IEEE80211_CONF_OFFCHANNEL
    The device is currently not on its main operating channel.


Description
===========

Flags to define PHY configuration options
