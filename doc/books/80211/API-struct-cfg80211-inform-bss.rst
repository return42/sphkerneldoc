
.. _API-struct-cfg80211-inform-bss:

==========================
struct cfg80211_inform_bss
==========================

*man struct cfg80211_inform_bss(9)*

*4.6.0-rc1*

BSS inform data


Synopsis
========

.. code-block:: c

    struct cfg80211_inform_bss {
      struct ieee80211_channel * chan;
      enum nl80211_bss_scan_width scan_width;
      s32 signal;
      u64 boottime_ns;
    };


Members
=======

chan
    channel the frame was received on

scan_width
    scan width that was used

signal
    signal strength value, according to the wiphy's signal type

boottime_ns
    timestamp (CLOCK_BOOTTIME) when the information was received; should match the time when the frame was actually received by the device (not just by the host, in case it was
    buffered on the device) and be accurate to about 10ms. If the frame isn't buffered, just passing the return value of ``ktime_get_boot_ns`` is likely appropriate.
