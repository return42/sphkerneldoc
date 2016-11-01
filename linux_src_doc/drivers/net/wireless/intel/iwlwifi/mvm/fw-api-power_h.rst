.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-power.h

.. _`iwl_ltr_config_flags`:

enum iwl_ltr_config_flags
=========================

.. c:type:: enum iwl_ltr_config_flags

    masks for LTR config command flags

.. _`iwl_ltr_config_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_ltr_config_flags {
        LTR_CFG_FLAG_FEATURE_ENABLE,
        LTR_CFG_FLAG_HW_DIS_ON_SHADOW_REG_ACCESS,
        LTR_CFG_FLAG_HW_EN_SHRT_WR_THROUGH,
        LTR_CFG_FLAG_HW_DIS_ON_D0_2_D3,
        LTR_CFG_FLAG_SW_SET_SHORT,
        LTR_CFG_FLAG_SW_SET_LONG,
        LTR_CFG_FLAG_DENIE_C10_ON_PD
    };

.. _`iwl_ltr_config_flags.constants`:

Constants
---------

LTR_CFG_FLAG_FEATURE_ENABLE
    Feature operational status

LTR_CFG_FLAG_HW_DIS_ON_SHADOW_REG_ACCESS
    allow LTR change on shadow
    memory access

LTR_CFG_FLAG_HW_EN_SHRT_WR_THROUGH
    allow LTR msg send on ANY LTR
    reg change

LTR_CFG_FLAG_HW_DIS_ON_D0_2_D3
    allow LTR msg send on transition from
    D0 to D3

LTR_CFG_FLAG_SW_SET_SHORT
    fixed static short LTR register

LTR_CFG_FLAG_SW_SET_LONG
    fixed static short LONG register

LTR_CFG_FLAG_DENIE_C10_ON_PD
    allow going into C10 on PD

.. _`iwl_ltr_config_cmd_v1`:

struct iwl_ltr_config_cmd_v1
============================

.. c:type:: struct iwl_ltr_config_cmd_v1

    configures the LTR

.. _`iwl_ltr_config_cmd_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ltr_config_cmd_v1 {
        __le32 flags;
        __le32 static_long;
        __le32 static_short;
    }

.. _`iwl_ltr_config_cmd_v1.members`:

Members
-------

flags
    See \ ``enum``\  iwl_ltr_config_flags

static_long
    *undescribed*

static_short
    *undescribed*

.. _`iwl_ltr_config_cmd`:

struct iwl_ltr_config_cmd
=========================

.. c:type:: struct iwl_ltr_config_cmd

    configures the LTR

.. _`iwl_ltr_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ltr_config_cmd {
        __le32 flags;
        __le32 static_long;
        __le32 static_short;
        __le32 ltr_cfg_values[LTR_VALID_STATES_NUM];
        __le32 ltr_short_idle_timeout;
    }

.. _`iwl_ltr_config_cmd.members`:

Members
-------

flags
    See \ ``enum``\  iwl_ltr_config_flags

static_long
    *undescribed*

static_short
    *undescribed*

ltr_short_idle_timeout
    *undescribed*

.. _`iwl_power_flags`:

enum iwl_power_flags
====================

.. c:type:: enum iwl_power_flags

    masks for power table command flags

.. _`iwl_power_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_power_flags {
        POWER_FLAGS_POWER_SAVE_ENA_MSK,
        POWER_FLAGS_POWER_MANAGEMENT_ENA_MSK,
        POWER_FLAGS_SKIP_OVER_DTIM_MSK,
        POWER_FLAGS_SNOOZE_ENA_MSK,
        POWER_FLAGS_BT_SCO_ENA,
        POWER_FLAGS_ADVANCE_PM_ENA_MSK,
        POWER_FLAGS_LPRX_ENA_MSK,
        POWER_FLAGS_UAPSD_MISBEHAVING_ENA_MSK
    };

.. _`iwl_power_flags.constants`:

Constants
---------

POWER_FLAGS_POWER_SAVE_ENA_MSK
    '1' Allow to save power by turning off
    receiver and transmitter. '0' - does not allow.

POWER_FLAGS_POWER_MANAGEMENT_ENA_MSK
    '0' Driver disables power management,
    '1' Driver enables PM (use rest of parameters)

POWER_FLAGS_SKIP_OVER_DTIM_MSK
    '0' PM have to walk up every DTIM,
    '1' PM could sleep over DTIM till listen Interval.

POWER_FLAGS_SNOOZE_ENA_MSK
    Enable snoozing only if uAPSD is enabled and all
    access categories are both delivery and trigger enabled.

POWER_FLAGS_BT_SCO_ENA
    Enable BT SCO coex only if uAPSD and
    PBW Snoozing enabled

POWER_FLAGS_ADVANCE_PM_ENA_MSK
    Advanced PM (uAPSD) enable mask

POWER_FLAGS_LPRX_ENA_MSK
    Low Power RX enable.

POWER_FLAGS_UAPSD_MISBEHAVING_ENA_MSK
    *undescribed*

.. _`iwl_powertable_cmd`:

struct iwl_powertable_cmd
=========================

.. c:type:: struct iwl_powertable_cmd

    legacy power command. Beside old API support this is used also with a new power API for device wide power settings. POWER_TABLE_CMD = 0x77 (command, has simple generic response)

.. _`iwl_powertable_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_powertable_cmd {
        __le16 flags;
        u8 keep_alive_seconds;
        u8 debug_flags;
        __le32 rx_data_timeout;
        __le32 tx_data_timeout;
        __le32 sleep_interval[IWL_POWER_VEC_SIZE];
        __le32 skip_dtim_periods;
        __le32 lprx_rssi_threshold;
    }

.. _`iwl_powertable_cmd.members`:

Members
-------

flags
    Power table command flags from POWER_FLAGS\_\*

keep_alive_seconds
    Keep alive period in seconds. Default - 25 sec.
    Minimum allowed:- 3 \* DTIM. Keep alive period must be
    set regardless of power scheme or current power state.
    FW use this value also when PM is disabled.

debug_flags
    *undescribed*

rx_data_timeout
    Minimum time (usec) from last Rx packet for AM to
    PSM transition - legacy PM

tx_data_timeout
    Minimum time (usec) from last Tx packet for AM to
    PSM transition - legacy PM

sleep_interval
    not in use

skip_dtim_periods
    Number of DTIM periods to skip if Skip over DTIM flag
    is set. For example, if it is required to skip over
    one DTIM, this value need to be set to 2 (DTIM periods).

lprx_rssi_threshold
    Signal strength up to which LP RX can be enabled.
    Default: 80dbm

.. _`iwl_device_power_flags`:

enum iwl_device_power_flags
===========================

.. c:type:: enum iwl_device_power_flags

    masks for device power command flags

.. _`iwl_device_power_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_device_power_flags {
        DEVICE_POWER_FLAGS_POWER_SAVE_ENA_MSK
    };

.. _`iwl_device_power_flags.constants`:

Constants
---------

DEVICE_POWER_FLAGS_POWER_SAVE_ENA_MSK
    *undescribed*

.. _`iwl_device_power_cmd`:

struct iwl_device_power_cmd
===========================

.. c:type:: struct iwl_device_power_cmd

    device wide power command. DEVICE_POWER_CMD = 0x77 (command, has simple generic response)

.. _`iwl_device_power_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_device_power_cmd {
        __le16 flags;
        __le16 reserved;
    }

.. _`iwl_device_power_cmd.members`:

Members
-------

flags
    Power table command flags from DEVICE_POWER_FLAGS\_\*

reserved
    *undescribed*

.. _`iwl_mac_power_cmd`:

struct iwl_mac_power_cmd
========================

.. c:type:: struct iwl_mac_power_cmd

    New power command containing uAPSD support MAC_PM_POWER_TABLE = 0xA9 (command, has simple generic response)

.. _`iwl_mac_power_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_power_cmd {
        __le32 id_and_color;
        __le16 flags;
        __le16 keep_alive_seconds;
        __le32 rx_data_timeout;
        __le32 tx_data_timeout;
        __le32 rx_data_timeout_uapsd;
        __le32 tx_data_timeout_uapsd;
        u8 lprx_rssi_threshold;
        u8 skip_dtim_periods;
        __le16 snooze_interval;
        __le16 snooze_window;
        u8 snooze_step;
        u8 qndp_tid;
        u8 uapsd_ac_flags;
        u8 uapsd_max_sp;
        u8 heavy_tx_thld_packets;
        u8 heavy_rx_thld_packets;
        u8 heavy_tx_thld_percentage;
        u8 heavy_rx_thld_percentage;
        u8 limited_ps_threshold;
        u8 reserved;
    }

.. _`iwl_mac_power_cmd.members`:

Members
-------

id_and_color
    MAC contex identifier

flags
    Power table command flags from POWER_FLAGS\_\*

keep_alive_seconds
    Keep alive period in seconds. Default - 25 sec.
    Minimum allowed:- 3 \* DTIM. Keep alive period must be
    set regardless of power scheme or current power state.
    FW use this value also when PM is disabled.

rx_data_timeout
    Minimum time (usec) from last Rx packet for AM to
    PSM transition - legacy PM

tx_data_timeout
    Minimum time (usec) from last Tx packet for AM to
    PSM transition - legacy PM

rx_data_timeout_uapsd
    Minimum time (usec) from last Rx packet for AM to
    PSM transition - uAPSD

tx_data_timeout_uapsd
    Minimum time (usec) from last Tx packet for AM to
    PSM transition - uAPSD

lprx_rssi_threshold
    Signal strength up to which LP RX can be enabled.
    Default: 80dbm

skip_dtim_periods
    Number of DTIM periods to skip if Skip over DTIM flag
    is set. For example, if it is required to skip over
    one DTIM, this value need to be set to 2 (DTIM periods).

snooze_interval
    Maximum time between attempts to retrieve buffered data
    from the AP [msec]

snooze_window
    A window of time in which PBW snoozing insures that all
    packets received. It is also the minimum time from last
    received unicast RX packet, before client stops snoozing
    for data. [msec]

snooze_step
    TBD

qndp_tid
    TID client shall use for uAPSD QNDP triggers

uapsd_ac_flags
    Set trigger-enabled and delivery-enabled indication for
    each corresponding AC.
    Use IEEE80211_WMM_IE_STA_QOSINFO_AC\* for correct values.

uapsd_max_sp
    Use IEEE80211_WMM_IE_STA_QOSINFO_SP\_\* for correct
    values.

heavy_tx_thld_packets
    TX threshold measured in number of packets

heavy_rx_thld_packets
    RX threshold measured in number of packets

heavy_tx_thld_percentage
    TX threshold measured in load's percentage

heavy_rx_thld_percentage
    RX threshold measured in load's percentage

limited_ps_threshold
    *undescribed*

reserved
    *undescribed*

.. _`iwl_reduce_tx_power_cmd`:

struct iwl_reduce_tx_power_cmd
==============================

.. c:type:: struct iwl_reduce_tx_power_cmd

    TX power reduction command REDUCE_TX_POWER_CMD = 0x9f

.. _`iwl_reduce_tx_power_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_reduce_tx_power_cmd {
        u8 flags;
        u8 mac_context_id;
        __le16 pwr_restriction;
    }

.. _`iwl_reduce_tx_power_cmd.members`:

Members
-------

flags
    (reserved for future implementation)

mac_context_id
    id of the mac ctx for which we are reducing TX power.

pwr_restriction
    TX power restriction in dBms.

.. _`iwl_dev_tx_power_cmd_v3`:

struct iwl_dev_tx_power_cmd_v3
==============================

.. c:type:: struct iwl_dev_tx_power_cmd_v3

    TX power reduction command

.. _`iwl_dev_tx_power_cmd_v3.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dev_tx_power_cmd_v3 {
        __le32 set_mode;
        __le32 mac_context_id;
        __le16 pwr_restriction;
        __le16 dev_24;
        __le16 dev_52_low;
        __le16 dev_52_high;
        __le16 per_chain_restriction[IWL_NUM_CHAIN_LIMITS][IWL_NUM_SUB_BANDS];
    }

.. _`iwl_dev_tx_power_cmd_v3.members`:

Members
-------

set_mode
    see \ :c:type:`enum iwl_dev_tx_power_cmd_mode <iwl_dev_tx_power_cmd_mode>`\ 

mac_context_id
    id of the mac ctx for which we are reducing TX power.

pwr_restriction
    TX power restriction in 1/8 dBms.

dev_24
    device TX power restriction in 1/8 dBms

dev_52_low
    device TX power restriction upper band - low

dev_52_high
    device TX power restriction upper band - high

per_chain_restriction
    per chain restrictions

.. _`iwl_dev_tx_power_cmd`:

struct iwl_dev_tx_power_cmd
===========================

.. c:type:: struct iwl_dev_tx_power_cmd

    TX power reduction command

.. _`iwl_dev_tx_power_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dev_tx_power_cmd {
        struct iwl_dev_tx_power_cmd_v3 v3;
        u8 enable_ack_reduction;
        u8 reserved[3];
    }

.. _`iwl_dev_tx_power_cmd.members`:

Members
-------

v3
    version 3 of the command, embedded here for easier software handling

enable_ack_reduction
    enable or disable close range ack TX power
    reduction.

.. _`iwl_beacon_filter_cmd`:

struct iwl_beacon_filter_cmd
============================

.. c:type:: struct iwl_beacon_filter_cmd

    REPLY_BEACON_FILTERING_CMD = 0xd2 (command)

.. _`iwl_beacon_filter_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_beacon_filter_cmd {
        __le32 bf_energy_delta;
        __le32 bf_roaming_energy_delta;
        __le32 bf_roaming_state;
        __le32 bf_temp_threshold;
        __le32 bf_temp_fast_filter;
        __le32 bf_temp_slow_filter;
        __le32 bf_enable_beacon_filter;
        __le32 bf_debug_flag;
        __le32 bf_escape_timer;
        __le32 ba_escape_timer;
        __le32 ba_enable_beacon_abort;
    }

.. _`iwl_beacon_filter_cmd.members`:

Members
-------

bf_energy_delta
    Used for RSSI filtering, if in 'normal' state. Send beacon
    to driver if delta in Energy values calculated for this and last
    passed beacon is greater than this threshold. Zero value means that
    the Energy change is ignored for beacon filtering, and beacon will
    not be forced to be sent to driver regardless of this delta. Typical
    energy delta 5dB.

bf_roaming_energy_delta
    Used for RSSI filtering, if in 'roaming' state.
    Send beacon to driver if delta in Energy values calculated for this
    and last passed beacon is greater than this threshold. Zero value
    means that the Energy change is ignored for beacon filtering while in
    Roaming state, typical energy delta 1dB.

bf_roaming_state
    Used for RSSI filtering. If absolute Energy values
    calculated for current beacon is less than the threshold, use
    Roaming Energy Delta Threshold, otherwise use normal Energy Delta
    Threshold. Typical energy threshold is -72dBm.

bf_temp_threshold
    This threshold determines the type of temperature
    filtering (Slow or Fast) that is selected (Units are in Celsuis):
    If the current temperature is above this threshold - Fast filter
    will be used, If the current temperature is below this threshold -
    Slow filter will be used.

bf_temp_fast_filter
    Send Beacon to driver if delta in temperature values
    calculated for this and the last passed beacon is greater than this
    threshold. Zero value means that the temperature change is ignored for
    beacon filtering; beacons will not be  forced to be sent to driver
    regardless of whether its temerature has been changed.

bf_temp_slow_filter
    Send Beacon to driver if delta in temperature values
    calculated for this and the last passed beacon is greater than this
    threshold. Zero value means that the temperature change is ignored for
    beacon filtering; beacons will not be forced to be sent to driver
    regardless of whether its temerature has been changed.

bf_enable_beacon_filter
    1, beacon filtering is enabled; 0, disabled.

bf_debug_flag
    *undescribed*

bf_escape_timer
    *undescribed*

ba_escape_timer
    Fully receive and parse beacon if no beacons were passed
    for a longer period of time then this escape-timeout. Units: Beacons.

ba_enable_beacon_abort
    1, beacon abort is enabled; 0, disabled.

.. This file was automatic generated / don't edit.

