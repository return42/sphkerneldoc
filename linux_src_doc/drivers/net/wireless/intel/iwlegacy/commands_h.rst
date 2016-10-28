.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlegacy/commands.h

.. _`il_cmd_header`:

struct il_cmd_header
====================

.. c:type:: struct il_cmd_header


.. _`il_cmd_header.definition`:

Definition
----------

.. code-block:: c

    struct il_cmd_header {
        u8 cmd;
        u8 flags;
        __le16 sequence;
        u8 data[0];
    }

.. _`il_cmd_header.members`:

Members
-------

cmd
    *undescribed*

flags
    *undescribed*

sequence
    *undescribed*

.. _`il_cmd_header.description`:

Description
-----------

This header format appears in the beginning of each command sent from the
driver, and each response/notification received from uCode.

.. _`il3945_tx_power`:

struct il3945_tx_power
======================

.. c:type:: struct il3945_tx_power


.. _`il3945_tx_power.definition`:

Definition
----------

.. code-block:: c

    struct il3945_tx_power {
        u8 tx_gain;
        u8 dsp_atten;
    }

.. _`il3945_tx_power.members`:

Members
-------

tx_gain
    *undescribed*

dsp_atten
    *undescribed*

.. _`il3945_tx_power.description`:

Description
-----------

Used in C_TX_PWR_TBL, C_SCAN, C_CHANNEL_SWITCH

.. _`il3945_tx_power.each-entry-contains-two-values`:

Each entry contains two values
------------------------------

1)  DSP gain (or sometimes called DSP attenuation).  This is a fine-grained
linear value that multiplies the output of the digital signal processor,
before being sent to the analog radio.
2)  Radio gain.  This sets the analog gain of the radio Tx path.
It is a coarser setting, and behaves in a logarithmic (dB) fashion.

Driver obtains values from struct il3945_tx_power power_gain_table[][].

.. _`il3945_power_per_rate`:

struct il3945_power_per_rate
============================

.. c:type:: struct il3945_power_per_rate


.. _`il3945_power_per_rate.definition`:

Definition
----------

.. code-block:: c

    struct il3945_power_per_rate {
        u8 rate;
        struct il3945_tx_power tpc;
        u8 reserved;
    }

.. _`il3945_power_per_rate.members`:

Members
-------

rate
    *undescribed*

tpc
    *undescribed*

reserved
    *undescribed*

.. _`il3945_power_per_rate.description`:

Description
-----------

Used in C_TX_PWR_TBL, C_CHANNEL_SWITCH

.. _`rate_mcs_code_msk`:

RATE_MCS_CODE_MSK
=================

.. c:function::  RATE_MCS_CODE_MSK()

.. _`rate_mcs_code_msk.rate_n_flags-format-is-used-in-following-iwl4965-commands`:

rate_n_flags format is used in following iwl4965 commands
---------------------------------------------------------

N_RX (response only)
N_RX_MPDU (response only)
C_TX (both command and response)
C_TX_LINK_QUALITY_CMD

High-throughput (HT) rate format for bits 7:0 (bit 8 must be "1"):
2-0:  0)   6 Mbps
1)  12 Mbps
2)  18 Mbps
3)  24 Mbps
4)  36 Mbps
5)  48 Mbps
6)  54 Mbps
7)  60 Mbps

4-3:  0)  Single stream (SISO)
1)  Dual stream (MIMO)
2)  Triple stream (MIMO)

5:  Value of 0x20 in bits 7:0 indicates 6 Mbps HT40 duplicate data

Legacy OFDM rate format for bits 7:0 (bit 8 must be "0", bit 9 "0"):
3-0:  0xD)   6 Mbps
0xF)   9 Mbps
0x5)  12 Mbps
0x7)  18 Mbps
0x9)  24 Mbps
0xB)  36 Mbps
0x1)  48 Mbps
0x3)  54 Mbps

Legacy CCK rate format for bits 7:0 (bit 8 must be "0", bit 9 "1"):
6-0:   10)  1 Mbps
20)  2 Mbps
55)  5.5 Mbps
110)  11 Mbps

.. _`rate_mcs_ant_pos`:

RATE_MCS_ANT_POS
================

.. c:function::  RATE_MCS_ANT_POS()

    4965 has 2 transmitters bit14:16

.. _`il4965_tx_power_dual_stream`:

union il4965_tx_power_dual_stream
=================================

.. c:type:: struct il4965_tx_power_dual_stream


.. _`il4965_tx_power_dual_stream.definition`:

Definition
----------

.. code-block:: c

    union il4965_tx_power_dual_stream {
        struct s;
        u32 dw;
    }

.. _`il4965_tx_power_dual_stream.members`:

Members
-------

s
    *undescribed*

dw
    *undescribed*

.. _`il4965_tx_power_dual_stream.description`:

Description
-----------

Host format used for C_TX_PWR_TBL, C_CHANNEL_SWITCH
Use \__le32 version (struct tx_power_dual_stream) when building command.

Driver provides radio gain and DSP attenuation settings to device in pairs,
one value for each transmitter chain.  The first value is for transmitter A,
second for transmitter B.

For SISO bit rates, both values in a pair should be identical.
For MIMO rates, one value may be different from the other,
in order to balance the Tx output between the two transmitters.

See more details in doc for TXPOWER in 4965.h.

.. _`tx_power_dual_stream`:

struct tx_power_dual_stream
===========================

.. c:type:: struct tx_power_dual_stream


.. _`tx_power_dual_stream.definition`:

Definition
----------

.. code-block:: c

    struct tx_power_dual_stream {
        __le32 dw;
    }

.. _`tx_power_dual_stream.members`:

Members
-------

dw
    *undescribed*

.. _`tx_power_dual_stream.description`:

Description
-----------

Table entries in C_TX_PWR_TBL, C_CHANNEL_SWITCH

Same format as il_tx_power_dual_stream, but \__le32

.. _`il4965_tx_power_db`:

struct il4965_tx_power_db
=========================

.. c:type:: struct il4965_tx_power_db


.. _`il4965_tx_power_db.definition`:

Definition
----------

.. code-block:: c

    struct il4965_tx_power_db {
        struct tx_power_dual_stream power_tbl[POWER_TBL_NUM_ENTRIES];
    }

.. _`il4965_tx_power_db.members`:

Members
-------

.. _`il4965_tx_power_db.description`:

Description
-----------

Entire table within C_TX_PWR_TBL, C_CHANNEL_SWITCH

.. _`il_ac_qos`:

struct il_ac_qos
================

.. c:type:: struct il_ac_qos

    - QOS timing params for C_QOS_PARAM One for each of 4 EDCA access categories in struct il_qosparam_cmd

.. _`il_ac_qos.definition`:

Definition
----------

.. code-block:: c

    struct il_ac_qos {
        __le16 cw_min;
        __le16 cw_max;
        u8 aifsn;
        u8 reserved1;
        __le16 edca_txop;
    }

.. _`il_ac_qos.members`:

Members
-------

cw_min
    Contention win, start value in numbers of slots.
    Should be a power-of-2, minus 1.  Device's default is 0x0f.

cw_max
    Contention win, max value in numbers of slots.
    Should be a power-of-2, minus 1.  Device's default is 0x3f.

aifsn
    Number of slots in Arbitration Interframe Space (before
    performing random backoff timing prior to Tx).  Device default 1.

reserved1
    *undescribed*

edca_txop
    Length of Tx opportunity, in uSecs.  Device default is 0.

.. _`il_ac_qos.description`:

Description
-----------

Device will automatically increase contention win by (2\*CW) + 1 for each
transmission retry.  Device uses cw_max as a bit mask, ANDed with new CW
value, to cap the CW value.

.. _`sta_id_modify`:

struct sta_id_modify
====================

.. c:type:: struct sta_id_modify


.. _`sta_id_modify.definition`:

Definition
----------

.. code-block:: c

    struct sta_id_modify {
        u8 addr[ETH_ALEN];
        __le16 reserved1;
        u8 sta_id;
        u8 modify_mask;
        __le16 reserved2;
    }

.. _`sta_id_modify.members`:

Members
-------

addr
    station's MAC address

reserved1
    *undescribed*

sta_id
    idx of station in uCode's station table

modify_mask
    STA_MODIFY\_\*, 1: modify, 0: don't change

reserved2
    *undescribed*

.. _`sta_id_modify.description`:

Description
-----------

Driver selects unused table idx when adding new station,
or the idx to a pre-existing station entry when modifying that station.
Some idxes have special purposes (IL_AP_ID, idx 0, is for AP).

modify_mask flags select which parameters to modify vs. leave alone.

.. _`il3945_rate_scaling_info`:

struct il3945_rate_scaling_info
===============================

.. c:type:: struct il3945_rate_scaling_info

    Rate Scaling Command & Response

.. _`il3945_rate_scaling_info.definition`:

Definition
----------

.. code-block:: c

    struct il3945_rate_scaling_info {
        __le16 rate_n_flags;
        u8 try_cnt;
        u8 next_rate_idx;
    }

.. _`il3945_rate_scaling_info.members`:

Members
-------

rate_n_flags
    *undescribed*

try_cnt
    *undescribed*

next_rate_idx
    *undescribed*

.. _`il3945_rate_scaling_info.description`:

Description
-----------

C_RATE_SCALE = 0x47 (command, has simple generic response)

.. _`il3945_rate_scaling_info.note`:

NOTE
----

The table of rates passed to the uCode via the
RATE_SCALE command sets up the corresponding order of
rates used for all related commands, including rate
masks, etc.

For example, if you set 9MB (PLCP 0x0f) as the first
rate in the rate table, the bit mask for that rate
when passed through ofdm_basic_rates on the C_RXON
command would be bit 0 (1 << 0)

.. _`il_link_qual_general_params`:

struct il_link_qual_general_params
==================================

.. c:type:: struct il_link_qual_general_params


.. _`il_link_qual_general_params.definition`:

Definition
----------

.. code-block:: c

    struct il_link_qual_general_params {
        u8 flags;
        u8 mimo_delimiter;
        u8 single_stream_ant_msk;
        u8 dual_stream_ant_msk;
        u8 start_rate_idx[LINK_QUAL_AC_NUM];
    }

.. _`il_link_qual_general_params.members`:

Members
-------

flags
    *undescribed*

mimo_delimiter
    *undescribed*

single_stream_ant_msk
    *undescribed*

dual_stream_ant_msk
    *undescribed*

.. _`il_link_qual_general_params.description`:

Description
-----------

Used in C_TX_LINK_QUALITY_CMD

.. _`il_link_qual_agg_params`:

struct il_link_qual_agg_params
==============================

.. c:type:: struct il_link_qual_agg_params


.. _`il_link_qual_agg_params.definition`:

Definition
----------

.. code-block:: c

    struct il_link_qual_agg_params {
        __le16 agg_time_limit;
        u8 agg_dis_start_th;
        u8 agg_frame_cnt_limit;
        __le32 reserved;
    }

.. _`il_link_qual_agg_params.members`:

Members
-------

agg_time_limit
    *undescribed*

agg_dis_start_th
    *undescribed*

agg_frame_cnt_limit
    *undescribed*

reserved
    *undescribed*

.. _`il_link_qual_agg_params.description`:

Description
-----------

Used in C_TX_LINK_QUALITY_CMD

.. _`il3945_scan_channel`:

struct il3945_scan_channel
==========================

.. c:type:: struct il3945_scan_channel

    entry in C_SCAN channel table

.. _`il3945_scan_channel.definition`:

Definition
----------

.. code-block:: c

    struct il3945_scan_channel {
        u8 type;
        u8 channel;
        struct il3945_tx_power tpc;
        __le16 active_dwell;
        __le16 passive_dwell;
    }

.. _`il3945_scan_channel.members`:

Members
-------

type
    *undescribed*

channel
    *undescribed*

tpc
    *undescribed*

active_dwell
    *undescribed*

passive_dwell
    *undescribed*

.. _`il3945_scan_channel.description`:

Description
-----------

One for each channel in the scan list.

.. _`il3945_scan_channel.each-channel-can-independently-select`:

Each channel can independently select
-------------------------------------

1)  SSID for directed active scans
2)  Txpower setting (for rate specified within Tx command)
3)  How long to stay on-channel (behavior may be modified by quiet_time,
quiet_plcp_th, good_CRC_th)

To avoid uCode errors, make sure the following are true (see comments
under struct il_scan_cmd about max_out_time and quiet_time):
1)  If using passive_dwell (i.e. passive_dwell != 0):
active_dwell <= passive_dwell (< max_out_time if max_out_time != 0)
2)  quiet_time <= active_dwell
3)  If restricting off-channel time (i.e. max_out_time !=0):
passive_dwell < max_out_time
active_dwell < max_out_time

.. _`il_ssid_ie`:

struct il_ssid_ie
=================

.. c:type:: struct il_ssid_ie

    directed scan network information element

.. _`il_ssid_ie.definition`:

Definition
----------

.. code-block:: c

    struct il_ssid_ie {
        u8 id;
        u8 len;
        u8 ssid[32];
    }

.. _`il_ssid_ie.members`:

Members
-------

id
    *undescribed*

len
    *undescribed*

.. _`il_ssid_ie.description`:

Description
-----------

Up to 20 of these may appear in C_SCAN (Note: Only 4 are in
3945 SCAN api), selected by "type" bit field in struct il_scan_channel;
each channel may select different ssids from among the 20 (4) entries.
SSID IEs get transmitted in reverse order of entry.

.. _`stats_tx_power`:

struct stats_tx_power
=====================

.. c:type:: struct stats_tx_power

    current tx power

.. _`stats_tx_power.definition`:

Definition
----------

.. code-block:: c

    struct stats_tx_power {
        u8 ant_a;
        u8 ant_b;
        u8 ant_c;
        u8 reserved;
    }

.. _`stats_tx_power.members`:

Members
-------

ant_a
    current tx power on chain a in 1/2 dB step

ant_b
    current tx power on chain b in 1/2 dB step

ant_c
    current tx power on chain c in 1/2 dB step

reserved
    *undescribed*

.. _`hd_tbl_size`:

HD_TBL_SIZE
===========

.. c:function::  HD_TBL_SIZE()

.. _`hd_tbl_size.description`:

Description
-----------

This command sets up the Rx signal detector for a sensitivity level that
is high enough to lock onto all signals within the associated network,
but low enough to ignore signals that are below a certain threshold, so as
not to have too many "false alarms".  False alarms are signals that the
Rx DSP tries to lock onto, but then discards after determining that they
are noise.

The optimum number of false alarms is between 5 and 50 per 200 TUs
(200 \* 1024 uSecs, i.e. 204.8 milliseconds) of actual Rx time (i.e.
time listening, not transmitting).  Driver must adjust sensitivity so that
the ratio of actual false alarms to actual Rx time falls within this range.

While associated, uCode delivers N_STATSs after each
received beacon.  These provide information to the driver to analyze the
sensitivity.  Don't analyze stats that come in from scanning, or any
other non-associated-network source.  Pertinent stats include:

From "general" stats (struct stats_rx_non_phy):

(beacon_energy_[abc] & 0x0FF00) >> 8 (unsigned, higher value is lower level)
Measure of energy of desired signal.  Used for establishing a level
below which the device does not detect signals.

(beacon_silence_rssi_[abc] & 0x0FF00) >> 8 (unsigned, units in dB)
Measure of background noise in silent period after beacon.

channel_load
uSecs of actual Rx time during beacon period (varies according to
how much time was spent transmitting).

From "cck" and "ofdm" stats (struct stats_rx_phy), separately:

false_alarm_cnt
Signal locks abandoned early (before phy-level header).

plcp_err
Signal locks abandoned late (during phy-level header).

.. _`hd_tbl_size.note`:

NOTE
----

Both false_alarm_cnt and plcp_err increment monotonically from
beacon to beacon, i.e. each value is an accumulation of all errors
before and including the latest beacon.  Values will wrap around to 0
after counting up to 2^32 - 1.  Driver must differentiate vs.
previous beacon's values to determine # false alarms in the current
beacon period.

Total number of false alarms = false_alarms + plcp_errs

For OFDM, adjust the following table entries in struct il_sensitivity_cmd
(notice that the start points for OFDM are at or close to settings for
maximum sensitivity):

START  /  MIN  /  MAX
HD_AUTO_CORR32_X1_TH_ADD_MIN_IDX          90   /   85  /  120
HD_AUTO_CORR32_X1_TH_ADD_MIN_MRC_IDX     170   /  170  /  210
HD_AUTO_CORR32_X4_TH_ADD_MIN_IDX         105   /  105  /  140
HD_AUTO_CORR32_X4_TH_ADD_MIN_MRC_IDX     220   /  220  /  270

If actual rate of OFDM false alarms (+ plcp_errors) is too high
(greater than 50 for each 204.8 msecs listening), reduce sensitivity
by \*adding\* 1 to all 4 of the table entries above, up to the max for
each entry.  Conversely, if false alarm rate is too low (less than 5
for each 204.8 msecs listening), \*subtract\* 1 from each entry to
increase sensitivity.

For CCK sensitivity, keep track of the following:

1).  20-beacon history of maximum background noise, indicated by
(beacon_silence_rssi_[abc] & 0x0FF00), units in dB, across the
3 receivers.  For any given beacon, the "silence reference" is
the maximum of last 60 samples (20 beacons \* 3 receivers).

2).  10-beacon history of strongest signal level, as indicated
by (beacon_energy_[abc] & 0x0FF00) >> 8, across the 3 receivers,
i.e. the strength of the signal through the best receiver at the
moment.  These measurements are "upside down", with lower values
for stronger signals, so max energy will be \*minimum\* value.

Then for any given beacon, the driver must determine the \*weakest\*
of the strongest signals; this is the minimum level that needs to be
successfully detected, when using the best receiver at the moment.
"Max cck energy" is the maximum (higher value means lower energy!)
of the last 10 minima.  Once this is determined, driver must add
a little margin by adding "6" to it.

3).  Number of consecutive beacon periods with too few false alarms.
Reset this to 0 at the first beacon period that falls within the
"good" range (5 to 50 false alarms per 204.8 milliseconds rx).

Then, adjust the following CCK table entries in struct il_sensitivity_cmd
(notice that the start points for CCK are at maximum sensitivity):

START  /  MIN  /  MAX
HD_AUTO_CORR40_X4_TH_ADD_MIN_IDX         125   /  125  /  200
HD_AUTO_CORR40_X4_TH_ADD_MIN_MRC_IDX     200   /  200  /  400
HD_MIN_ENERGY_CCK_DET_IDX                100   /    0  /  100

If actual rate of CCK false alarms (+ plcp_errors) is too high
(greater than 50 for each 204.8 msecs listening), method for reducing

.. _`hd_tbl_size.sensitivity-is`:

sensitivity is
--------------


1)  \*Add\* 3 to value in HD_AUTO_CORR40_X4_TH_ADD_MIN_MRC_IDX,
up to max 400.

2)  If current value in HD_AUTO_CORR40_X4_TH_ADD_MIN_IDX is < 160,
sensitivity has been reduced a significant amount; bring it up to
a moderate 161.  Otherwise, \*add\* 3, up to max 200.

3)  a)  If current value in HD_AUTO_CORR40_X4_TH_ADD_MIN_IDX is > 160,
sensitivity has been reduced only a moderate or small amount;
\*subtract\* 2 from value in HD_MIN_ENERGY_CCK_DET_IDX,
down to min 0.  Otherwise (if gain has been significantly reduced),
don't change the HD_MIN_ENERGY_CCK_DET_IDX value.

b)  Save a snapshot of the "silence reference".

If actual rate of CCK false alarms (+ plcp_errors) is too low
(less than 5 for each 204.8 msecs listening), method for increasing

.. _`hd_tbl_size.sensitivity-is-used-only-if`:

sensitivity is used only if
---------------------------


1a)  Previous beacon did not have too many false alarms
1b)  AND difference between previous "silence reference" and current
"silence reference" (prev - current) is 2 or more,
OR 2)  100 or more consecutive beacon periods have had rate of
less than 5 false alarms per 204.8 milliseconds rx time.

.. _`hd_tbl_size.method-for-increasing-sensitivity`:

Method for increasing sensitivity
---------------------------------


1)  \*Subtract\* 3 from value in HD_AUTO_CORR40_X4_TH_ADD_MIN_IDX,
down to min 125.

2)  \*Subtract\* 3 from value in HD_AUTO_CORR40_X4_TH_ADD_MIN_MRC_IDX,
down to min 200.

3)  \*Add\* 2 to value in HD_MIN_ENERGY_CCK_DET_IDX, up to max 100.

If actual rate of CCK false alarms (+ plcp_errors) is within good range
(between 5 and 50 for each 204.8 msecs listening):

1)  Save a snapshot of the silence reference.

2)  If previous beacon had too many CCK false alarms (+ plcp_errors),
give some extra margin to energy threshold by \*subtracting\* 8
from value in HD_MIN_ENERGY_CCK_DET_IDX.

For all cases (too few, too many, good range), make sure that the CCK
detection threshold (energy) is below the energy level for robust
detection over the past 10 beacon periods, the "Max cck energy".
Lower values mean higher energy; this means making sure that the value
in HD_MIN_ENERGY_CCK_DET_IDX is at or \*above\* "Max cck energy".

.. _`il_sensitivity_cmd`:

struct il_sensitivity_cmd
=========================

.. c:type:: struct il_sensitivity_cmd


.. _`il_sensitivity_cmd.definition`:

Definition
----------

.. code-block:: c

    struct il_sensitivity_cmd {
        __le16 control;
        __le16 table[HD_TBL_SIZE];
    }

.. _`il_sensitivity_cmd.members`:

Members
-------

control
    (1) updates working table, (0) updates default table

table
    energy threshold values, use HD\_\* as idx into table

.. _`il_sensitivity_cmd.description`:

Description
-----------

Always use "1" in "control" to update uCode's working table and DSP.

.. _`il_default_standard_phy_calibrate_tbl_size`:

IL_DEFAULT_STANDARD_PHY_CALIBRATE_TBL_SIZE
==========================================

.. c:function::  IL_DEFAULT_STANDARD_PHY_CALIBRATE_TBL_SIZE()

.. _`il_default_standard_phy_calibrate_tbl_size.description`:

Description
-----------

This command sets the relative gains of 4965 device's 3 radio receiver chains.

After the first association, driver should accumulate signal and noise
stats from the N_STATSs that follow the first 20
beacons from the associated network (don't collect stats that come
in from scanning, or any other non-network source).

.. _`il_default_standard_phy_calibrate_tbl_size.disconnected-antenna`:

DISCONNECTED ANTENNA
--------------------


Driver should determine which antennas are actually connected, by comparing
average beacon signal levels for the 3 Rx chains.  Accumulate (add) the
following values over 20 beacons, one accumulator for each of the chains
a/b/c, from struct stats_rx_non_phy:

beacon_rssi_[abc] & 0x0FF (unsigned, units in dB)

Find the strongest signal from among a/b/c.  Compare the other two to the
strongest.  If any signal is more than 15 dB (times 20, unless you
divide the accumulated values by 20) below the strongest, the driver
considers that antenna to be disconnected, and should not try to use that
antenna/chain for Rx or Tx.  If both A and B seem to be disconnected,
driver should declare the stronger one as connected, and attempt to use it
(A and B are the only 2 Tx chains!).

.. _`il_default_standard_phy_calibrate_tbl_size.rx-balance`:

RX BALANCE
----------


Driver should balance the 3 receivers (but just the ones that are connected
to antennas, see above) for gain, by comparing the average signal levels
detected during the silence after each beacon (background noise).
Accumulate (add) the following values over 20 beacons, one accumulator for
each of the chains a/b/c, from struct stats_rx_non_phy:

beacon_silence_rssi_[abc] & 0x0FF (unsigned, units in dB)

Find the weakest background noise level from among a/b/c.  This Rx chain
will be the reference, with 0 gain adjustment.  Attenuate other channels by

.. _`il_default_standard_phy_calibrate_tbl_size.finding-noise-difference`:

finding noise difference
------------------------


(accum_noise[i] - accum_noise[reference]) / 30

The "30" adjusts the dB in the 20 accumulated samples to units of 1.5 dB.
For use in diff_gain_[abc] fields of struct il_calibration_cmd, the
driver should limit the difference results to a range of 0-3 (0-4.5 dB),
and set bit 2 to indicate "reduce gain".  The value for the reference
(weakest) chain should be "0".

diff_gain_[abc] bit fields:
2: (1) reduce gain, (0) increase gain
1-0: amount of gain, units of 1.5 dB

.. This file was automatic generated / don't edit.

