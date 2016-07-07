.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/dfs_debug.h

.. _`ath_dfs_stats`:

struct ath_dfs_stats
====================

.. c:type:: struct ath_dfs_stats

    DFS Statistics per wiphy

.. _`ath_dfs_stats.definition`:

Definition
----------

.. code-block:: c

    struct ath_dfs_stats {
        u32 pulses_total;
        u32 pulses_no_dfs;
        u32 pulses_detected;
        u32 datalen_discards;
        u32 rssi_discards;
        u32 bwinfo_discards;
        u32 pri_phy_errors;
        u32 ext_phy_errors;
        u32 dc_phy_errors;
        u32 pulses_processed;
        u32 radar_detected;
    }

.. _`ath_dfs_stats.members`:

Members
-------

pulses_total
    pulses reported by HW

pulses_no_dfs
    pulses wrongly reported as DFS

pulses_detected
    pulses detected so far

datalen_discards
    pulses discarded due to invalid datalen

rssi_discards
    pulses discarded due to invalid RSSI

bwinfo_discards
    pulses discarded due to invalid BW info

pri_phy_errors
    pulses reported for primary channel

ext_phy_errors
    pulses reported for extension channel

dc_phy_errors
    pulses reported for primary + extension channel

pulses_processed
    pulses forwarded to detector

radar_detected
    radars detected

.. This file was automatic generated / don't edit.

