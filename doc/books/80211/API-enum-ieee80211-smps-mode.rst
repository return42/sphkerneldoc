
.. _API-enum-ieee80211-smps-mode:

========================
enum ieee80211_smps_mode
========================

*man enum ieee80211_smps_mode(9)*

*4.6.0-rc1*

spatial multiplexing power save mode


Synopsis
========

.. code-block:: c

    enum ieee80211_smps_mode {
      IEEE80211_SMPS_AUTOMATIC,
      IEEE80211_SMPS_OFF,
      IEEE80211_SMPS_STATIC,
      IEEE80211_SMPS_DYNAMIC,
      IEEE80211_SMPS_NUM_MODES
    };


Constants
=========

IEEE80211_SMPS_AUTOMATIC
    automatic

IEEE80211_SMPS_OFF
    off

IEEE80211_SMPS_STATIC
    static

IEEE80211_SMPS_DYNAMIC
    dynamic

IEEE80211_SMPS_NUM_MODES
    internal, don't use
