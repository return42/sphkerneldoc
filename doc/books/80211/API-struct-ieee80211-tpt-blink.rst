
.. _API-struct-ieee80211-tpt-blink:

==========================
struct ieee80211_tpt_blink
==========================

*man struct ieee80211_tpt_blink(9)*

*4.6.0-rc1*

throughput blink description


Synopsis
========

.. code-block:: c

    struct ieee80211_tpt_blink {
      int throughput;
      int blink_time;
    };


Members
=======

throughput
    throughput in Kbit/sec

blink_time
    blink time in milliseconds (full cycle, ie. one off + one on period)
