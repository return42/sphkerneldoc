.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/commands.h

.. _`rate_mcs_code_msk`:

RATE_MCS_CODE_MSK
=================

.. c:function::  RATE_MCS_CODE_MSK()

.. _`rate_mcs_code_msk.rate_n_flags-format-is-used-in-following-iwlagn-commands`:

rate_n_flags format is used in following iwlagn commands
--------------------------------------------------------

REPLY_RX (response only)
REPLY_RX_MPDU (response only)
REPLY_TX (both command and response)
REPLY_TX_LINK_QUALITY_CMD

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

    4965 has 2 transmitters 5100 has 1 transmitter B 5150 has 1 transmitter A 5300 has 3 transmitters 5350 has 3 transmitters bit14:16

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

Table entries in REPLY_TX_PWR_TABLE_CMD, REPLY_CHANNEL_SWITCH

Same format as iwl_tx_power_dual_stream, but \__le32

.. _`iwlagn_tx_power_auto`:

IWLAGN_TX_POWER_AUTO
====================

.. c:function::  IWLAGN_TX_POWER_AUTO()

    struct iwlagn_tx_power_dbm_cmd

.. _`iwl5000_channel_switch_cmd`:

struct iwl5000_channel_switch_cmd
=================================

.. c:type:: struct iwl5000_channel_switch_cmd


.. _`iwl5000_channel_switch_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl5000_channel_switch_cmd {
        u8 band;
        u8 expect_beacon;
        __le16 channel;
        __le32 rxon_flags;
        __le32 rxon_filter_flags;
        __le32 switch_time;
        __le32 reserved[2][IWL_PWR_NUM_HT_OFDM_ENTRIES + IWL_PWR_CCK_ENTRIES];
    }

.. _`iwl5000_channel_switch_cmd.members`:

Members
-------

band
    0- 5.2GHz, 1- 2.4GHz

expect_beacon
    0- resume transmits after channel switch
    1- wait for beacon to resume transmits

channel
    new channel number

rxon_flags
    Rx on flags

rxon_filter_flags
    filtering parameters

switch_time
    switch time in extended beacon format

reserved
    reserved bytes

.. _`iwl6000_channel_switch_cmd`:

struct iwl6000_channel_switch_cmd
=================================

.. c:type:: struct iwl6000_channel_switch_cmd


.. _`iwl6000_channel_switch_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl6000_channel_switch_cmd {
        u8 band;
        u8 expect_beacon;
        __le16 channel;
        __le32 rxon_flags;
        __le32 rxon_filter_flags;
        __le32 switch_time;
        __le32 reserved[3][IWL_PWR_NUM_HT_OFDM_ENTRIES + IWL_PWR_CCK_ENTRIES];
    }

.. _`iwl6000_channel_switch_cmd.members`:

Members
-------

band
    0- 5.2GHz, 1- 2.4GHz

expect_beacon
    0- resume transmits after channel switch
    1- wait for beacon to resume transmits

channel
    new channel number

rxon_flags
    Rx on flags

rxon_filter_flags
    filtering parameters

switch_time
    switch time in extended beacon format

reserved
    reserved bytes

.. _`iwl_ac_qos`:

struct iwl_ac_qos
=================

.. c:type:: struct iwl_ac_qos

    - QOS timing params for REPLY_QOS_PARAM One for each of 4 EDCA access categories in struct iwl_qosparam_cmd

.. _`iwl_ac_qos.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ac_qos {
        __le16 cw_min;
        __le16 cw_max;
        u8 aifsn;
        u8 reserved1;
        __le16 edca_txop;
    }

.. _`iwl_ac_qos.members`:

Members
-------

cw_min
    Contention window, start value in numbers of slots.
    Should be a power-of-2, minus 1.  Device's default is 0x0f.

cw_max
    Contention window, max value in numbers of slots.
    Should be a power-of-2, minus 1.  Device's default is 0x3f.

aifsn
    Number of slots in Arbitration Interframe Space (before
    performing random backoff timing prior to Tx).  Device default 1.

reserved1
    *undescribed*

edca_txop
    Length of Tx opportunity, in uSecs.  Device default is 0.

.. _`iwl_ac_qos.description`:

Description
-----------

Device will automatically increase contention window by (2\*CW) + 1 for each
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
    index of station in uCode's station table

modify_mask
    STA_MODIFY\_\*, 1: modify, 0: don't change

reserved2
    *undescribed*

.. _`sta_id_modify.description`:

Description
-----------

Driver selects unused table index when adding new station,
or the index to a pre-existing station entry when modifying that station.
Some indexes have special purposes (IWL_AP_ID, index 0, is for AP).

modify_mask flags select which parameters to modify vs. leave alone.

.. _`iwl_link_qual_general_params`:

struct iwl_link_qual_general_params
===================================

.. c:type:: struct iwl_link_qual_general_params


.. _`iwl_link_qual_general_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_link_qual_general_params {
        u8 flags;
        u8 mimo_delimiter;
        u8 single_stream_ant_msk;
        u8 dual_stream_ant_msk;
        u8 start_rate_index[LINK_QUAL_AC_NUM];
    }

.. _`iwl_link_qual_general_params.members`:

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

.. _`iwl_link_qual_general_params.description`:

Description
-----------

Used in REPLY_TX_LINK_QUALITY_CMD

.. _`iwl_link_qual_agg_params`:

struct iwl_link_qual_agg_params
===============================

.. c:type:: struct iwl_link_qual_agg_params


.. _`iwl_link_qual_agg_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_link_qual_agg_params {
        __le16 agg_time_limit;
        u8 agg_dis_start_th;
        u8 agg_frame_cnt_limit;
        __le32 reserved;
    }

.. _`iwl_link_qual_agg_params.members`:

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

.. _`iwl_link_qual_agg_params.description`:

Description
-----------

Used in REPLY_TX_LINK_QUALITY_CMD

.. _`iwl_scan_channel`:

struct iwl_scan_channel
=======================

.. c:type:: struct iwl_scan_channel

    entry in REPLY_SCAN_CMD channel table

.. _`iwl_scan_channel.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_channel {
        __le32 type;
        __le16 channel;
        u8 tx_gain;
        u8 dsp_atten;
        __le16 active_dwell;
        __le16 passive_dwell;
    }

.. _`iwl_scan_channel.members`:

Members
-------

type
    *undescribed*

channel
    *undescribed*

tx_gain
    *undescribed*

dsp_atten
    *undescribed*

active_dwell
    *undescribed*

passive_dwell
    *undescribed*

.. _`iwl_scan_channel.description`:

Description
-----------

One for each channel in the scan list.

.. _`iwl_scan_channel.each-channel-can-independently-select`:

Each channel can independently select
-------------------------------------

1)  SSID for directed active scans
2)  Txpower setting (for rate specified within Tx command)
3)  How long to stay on-channel (behavior may be modified by quiet_time,
quiet_plcp_th, good_CRC_th)

To avoid uCode errors, make sure the following are true (see comments
under struct iwl_scan_cmd about max_out_time and quiet_time):
1)  If using passive_dwell (i.e. passive_dwell != 0):
active_dwell <= passive_dwell (< max_out_time if max_out_time != 0)
2)  quiet_time <= active_dwell
3)  If restricting off-channel time (i.e. max_out_time !=0):
passive_dwell < max_out_time
active_dwell < max_out_time

.. _`iwl_ssid_ie`:

struct iwl_ssid_ie
==================

.. c:type:: struct iwl_ssid_ie

    directed scan network information element

.. _`iwl_ssid_ie.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ssid_ie {
        u8 id;
        u8 len;
        u8 ssid[32];
    }

.. _`iwl_ssid_ie.members`:

Members
-------

id
    *undescribed*

len
    *undescribed*

.. _`iwl_ssid_ie.description`:

Description
-----------

Up to 20 of these may appear in REPLY_SCAN_CMD,
selected by "type" bit field in struct iwl_scan_channel;
each channel may select different ssids from among the 20 entries.
SSID IEs get transmitted in reverse order of entry.

.. _`statistics_tx_power`:

struct statistics_tx_power
==========================

.. c:type:: struct statistics_tx_power

    current tx power

.. _`statistics_tx_power.definition`:

Definition
----------

.. code-block:: c

    struct statistics_tx_power {
        u8 ant_a;
        u8 ant_b;
        u8 ant_c;
        u8 reserved;
    }

.. _`statistics_tx_power.members`:

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

.. _`hd_table_size`:

HD_TABLE_SIZE
=============

.. c:function::  HD_TABLE_SIZE()

.. _`hd_table_size.description`:

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

While associated, uCode delivers STATISTICS_NOTIFICATIONs after each
received beacon.  These provide information to the driver to analyze the
sensitivity.  Don't analyze statistics that come in from scanning, or any
other non-associated-network source.  Pertinent statistics include:

From "general" statistics (struct statistics_rx_non_phy):

(beacon_energy_[abc] & 0x0FF00) >> 8 (unsigned, higher value is lower level)
Measure of energy of desired signal.  Used for establishing a level
below which the device does not detect signals.

(beacon_silence_rssi_[abc] & 0x0FF00) >> 8 (unsigned, units in dB)
Measure of background noise in silent period after beacon.

channel_load
uSecs of actual Rx time during beacon period (varies according to
how much time was spent transmitting).

From "cck" and "ofdm" statistics (struct statistics_rx_phy), separately:

false_alarm_cnt
Signal locks abandoned early (before phy-level header).

plcp_err
Signal locks abandoned late (during phy-level header).

.. _`hd_table_size.note`:

NOTE
----

Both false_alarm_cnt and plcp_err increment monotonically from
beacon to beacon, i.e. each value is an accumulation of all errors
before and including the latest beacon.  Values will wrap around to 0
after counting up to 2^32 - 1.  Driver must differentiate vs.
previous beacon's values to determine # false alarms in the current
beacon period.

Total number of false alarms = false_alarms + plcp_errs

For OFDM, adjust the following table entries in struct iwl_sensitivity_cmd
(notice that the start points for OFDM are at or close to settings for
maximum sensitivity):

START  /  MIN  /  MAX
HD_AUTO_CORR32_X1_TH_ADD_MIN_INDEX          90   /   85  /  120
HD_AUTO_CORR32_X1_TH_ADD_MIN_MRC_INDEX     170   /  170  /  210
HD_AUTO_CORR32_X4_TH_ADD_MIN_INDEX         105   /  105  /  140
HD_AUTO_CORR32_X4_TH_ADD_MIN_MRC_INDEX     220   /  220  /  270

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

Then, adjust the following CCK table entries in struct iwl_sensitivity_cmd
(notice that the start points for CCK are at maximum sensitivity):

START  /  MIN  /  MAX
HD_AUTO_CORR40_X4_TH_ADD_MIN_INDEX         125   /  125  /  200
HD_AUTO_CORR40_X4_TH_ADD_MIN_MRC_INDEX     200   /  200  /  400
HD_MIN_ENERGY_CCK_DET_INDEX                100   /    0  /  100

If actual rate of CCK false alarms (+ plcp_errors) is too high
(greater than 50 for each 204.8 msecs listening), method for reducing

.. _`hd_table_size.sensitivity-is`:

sensitivity is
--------------


1)  \*Add\* 3 to value in HD_AUTO_CORR40_X4_TH_ADD_MIN_MRC_INDEX,
up to max 400.

2)  If current value in HD_AUTO_CORR40_X4_TH_ADD_MIN_INDEX is < 160,
sensitivity has been reduced a significant amount; bring it up to
a moderate 161.  Otherwise, \*add\* 3, up to max 200.

3)  a)  If current value in HD_AUTO_CORR40_X4_TH_ADD_MIN_INDEX is > 160,
sensitivity has been reduced only a moderate or small amount;
\*subtract\* 2 from value in HD_MIN_ENERGY_CCK_DET_INDEX,
down to min 0.  Otherwise (if gain has been significantly reduced),
don't change the HD_MIN_ENERGY_CCK_DET_INDEX value.

b)  Save a snapshot of the "silence reference".

If actual rate of CCK false alarms (+ plcp_errors) is too low
(less than 5 for each 204.8 msecs listening), method for increasing

.. _`hd_table_size.sensitivity-is-used-only-if`:

sensitivity is used only if
---------------------------


1a)  Previous beacon did not have too many false alarms
1b)  AND difference between previous "silence reference" and current
"silence reference" (prev - current) is 2 or more,
OR 2)  100 or more consecutive beacon periods have had rate of
less than 5 false alarms per 204.8 milliseconds rx time.

.. _`hd_table_size.method-for-increasing-sensitivity`:

Method for increasing sensitivity
---------------------------------


1)  \*Subtract\* 3 from value in HD_AUTO_CORR40_X4_TH_ADD_MIN_INDEX,
down to min 125.

2)  \*Subtract\* 3 from value in HD_AUTO_CORR40_X4_TH_ADD_MIN_MRC_INDEX,
down to min 200.

3)  \*Add\* 2 to value in HD_MIN_ENERGY_CCK_DET_INDEX, up to max 100.

If actual rate of CCK false alarms (+ plcp_errors) is within good range
(between 5 and 50 for each 204.8 msecs listening):

1)  Save a snapshot of the silence reference.

2)  If previous beacon had too many CCK false alarms (+ plcp_errors),
give some extra margin to energy threshold by \*subtracting\* 8
from value in HD_MIN_ENERGY_CCK_DET_INDEX.

For all cases (too few, too many, good range), make sure that the CCK
detection threshold (energy) is below the energy level for robust
detection over the past 10 beacon periods, the "Max cck energy".
Lower values mean higher energy; this means making sure that the value
in HD_MIN_ENERGY_CCK_DET_INDEX is at or \*above\* "Max cck energy".

.. _`iwl_sensitivity_cmd`:

struct iwl_sensitivity_cmd
==========================

.. c:type:: struct iwl_sensitivity_cmd


.. _`iwl_sensitivity_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_sensitivity_cmd {
        __le16 control;
        __le16 table[HD_TABLE_SIZE];
    }

.. _`iwl_sensitivity_cmd.members`:

Members
-------

control
    (1) updates working table, (0) updates default table

table
    energy threshold values, use HD\_\* as index into table

.. _`iwl_sensitivity_cmd.description`:

Description
-----------

Always use "1" in "control" to update uCode's working table and DSP.

.. _`iwl_wipan_slot`:

struct iwl_wipan_slot
=====================

.. c:type:: struct iwl_wipan_slot


.. _`iwl_wipan_slot.definition`:

Definition
----------

.. code-block:: c

    struct iwl_wipan_slot {
        __le16 width;
        u8 type;
        u8 reserved;
    }

.. _`iwl_wipan_slot.members`:

Members
-------

width
    Time in TU

type
    0 - BSS
    1 - PAN

reserved
    *undescribed*

.. _`iwl_wipan_params_cmd`:

struct iwl_wipan_params_cmd
===========================

.. c:type:: struct iwl_wipan_params_cmd


.. _`iwl_wipan_params_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_wipan_params_cmd {
        __le16 flags;
        u8 reserved;
        u8 num_slots;
        struct iwl_wipan_slot slots[10];
    }

.. _`iwl_wipan_params_cmd.members`:

Members
-------

flags
    *undescribed*

reserved
    *undescribed*

num_slots
    1 - 10

.. _`iwl_wipan_params_cmd.bit0`:

bit0
----

reserved

.. _`iwl_wipan_params_cmd.bit1`:

bit1
----

CP leave channel with CTS

.. _`iwl_wipan_params_cmd.bit2`:

bit2
----

CP leave channel qith Quiet

.. _`iwl_wipan_params_cmd.bit3`:

bit3
----

slotted mode
1 - work in slotted mode
0 - work in non slotted mode

.. _`iwl_wipan_params_cmd.bit4`:

bit4
----

filter beacon notification

.. _`iwl_wipan_params_cmd.bit5`:

bit5
----

full tx slotted mode. if this flag is set,
uCode will perform leaving channel methods in context switch
also when working in same channel mode

.. This file was automatic generated / don't edit.

