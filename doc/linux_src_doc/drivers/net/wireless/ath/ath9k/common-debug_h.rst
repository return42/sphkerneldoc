.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/common-debug.h

.. _`ath_rx_stats`:

struct ath_rx_stats
===================

.. c:type:: struct ath_rx_stats

    RX Statistics

.. _`ath_rx_stats.definition`:

Definition
----------

.. code-block:: c

    struct ath_rx_stats {
        u32 rx_pkts_all;
        u32 rx_bytes_all;
        u32 crc_err;
        u32 decrypt_crc_err;
        u32 phy_err;
        u32 mic_err;
        u32 pre_delim_crc_err;
        u32 post_delim_crc_err;
        u32 decrypt_busy_err;
        u32 phy_err_stats[ATH9K_PHYERR_MAX];
        u32 rx_len_err;
        u32 rx_oom_err;
        u32 rx_rate_err;
        u32 rx_too_many_frags_err;
        u32 rx_beacons;
        u32 rx_frags;
        u32 rx_spectral;
    }

.. _`ath_rx_stats.members`:

Members
-------

rx_pkts_all
    No. of total frames received, including ones that

rx_bytes_all
    No. of total bytes received, including ones that

crc_err
    No. of frames with incorrect CRC value

decrypt_crc_err
    No. of frames whose CRC check failed after

phy_err
    No. of frames whose reception failed because the PHY

mic_err
    No. of frames with incorrect TKIP MIC verification failure

pre_delim_crc_err
    Pre-Frame delimiter CRC error detections

post_delim_crc_err
    Post-Frame delimiter CRC error detections

decrypt_busy_err
    Decryption interruptions counter

phy_err_stats
    Individual PHY error statistics

rx_len_err
    No. of frames discarded due to bad length.

rx_oom_err
    No. of frames dropped due to OOM issues.

rx_rate_err
    No. of frames dropped due to rate errors.

rx_too_many_frags_err
    Frames dropped due to too-many-frags received.

rx_beacons
    No. of beacons received.

rx_frags
    No. of rx-fragements received.

rx_spectral
    No of spectral packets received.

.. This file was automatic generated / don't edit.

