
.. _API-enum-cfg80211-signal-type:

=========================
enum cfg80211_signal_type
=========================

*man enum cfg80211_signal_type(9)*

*4.6.0-rc1*

signal type


Synopsis
========

.. code-block:: c

    enum cfg80211_signal_type {
      CFG80211_SIGNAL_TYPE_NONE,
      CFG80211_SIGNAL_TYPE_MBM,
      CFG80211_SIGNAL_TYPE_UNSPEC
    };


Constants
=========

CFG80211_SIGNAL_TYPE_NONE
    no signal strength information available

CFG80211_SIGNAL_TYPE_MBM
    signal strength in mBm (100⋆dBm)

CFG80211_SIGNAL_TYPE_UNSPEC
    signal strength, increasing from 0 through 100
