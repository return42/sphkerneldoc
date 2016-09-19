.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/dev.h

.. _`iwl_agg_state`:

enum iwl_agg_state
==================

.. c:type:: enum iwl_agg_state


.. _`iwl_agg_state.definition`:

Definition
----------

.. code-block:: c

    enum iwl_agg_state {
        IWL_AGG_OFF,
        IWL_AGG_STARTING,
        IWL_AGG_ON,
        IWL_EMPTYING_HW_QUEUE_ADDBA,
        IWL_EMPTYING_HW_QUEUE_DELBA
    };

.. _`iwl_agg_state.constants`:

Constants
---------

IWL_AGG_OFF
    aggregation is not used

IWL_AGG_STARTING
    aggregation are starting (between start and oper)

IWL_AGG_ON
    aggregation session is up

IWL_EMPTYING_HW_QUEUE_ADDBA
    establishing a BA session - waiting for the
    HW queue to be empty from packets for this RA /TID.

IWL_EMPTYING_HW_QUEUE_DELBA
    tearing down a BA session - waiting for the
    HW queue to be empty from packets for this RA /TID.

.. _`iwl_agg_state.description`:

Description
-----------

The state machine of the BA agreement establishment / tear down.
These states relate to a specific RA / TID.

.. _`iwl_ht_agg`:

struct iwl_ht_agg
=================

.. c:type:: struct iwl_ht_agg

    aggregation state machine This structs holds the states for the BA agreement establishment and tear down. It also holds the state during the BA session itself. This struct is duplicated for each RA / TID.

.. _`iwl_ht_agg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ht_agg {
        u32 rate_n_flags;
        enum iwl_agg_state state;
        u16 txq_id;
        u16 ssn;
        bool wait_for_ba;
    }

.. _`iwl_ht_agg.members`:

Members
-------

rate_n_flags
    Rate at which Tx was attempted. Holds the data between the
    Tx response (REPLY_TX), and the block ack notification
    (REPLY_COMPRESSED_BA).

state
    state of the BA agreement establishment / tear down.

txq_id
    Tx queue used by the BA session

ssn
    the first packet to be sent in AGG HW queue in Tx AGG start flow, or
    the first packet to be sent in legacy HW queue in Tx AGG stop flow.
    Basically when next_reclaimed reaches ssn, we can tell mac80211 that
    we are ready to finish the Tx AGG stop / start flow.

wait_for_ba
    Expect block-ack before next Tx reply

.. _`iwl_tid_data`:

struct iwl_tid_data
===================

.. c:type:: struct iwl_tid_data

    one for each RA / TID This structs holds the states for each RA / TID.

.. _`iwl_tid_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tid_data {
        u16 seq_number;
        u16 next_reclaimed;
        struct iwl_ht_agg agg;
    }

.. _`iwl_tid_data.members`:

Members
-------

seq_number
    the next WiFi sequence number to use

next_reclaimed
    the WiFi sequence number of the next packet to be acked.
    This is basically (last acked packet++).

agg
    aggregation state machine

.. _`iwl_vif_priv`:

struct iwl_vif_priv
===================

.. c:type:: struct iwl_vif_priv

    driver's private per-interface information

.. _`iwl_vif_priv.definition`:

Definition
----------

.. code-block:: c

    struct iwl_vif_priv {
        struct iwl_rxon_context *ctx;
        u8 ibss_bssid_sta_id;
    }

.. _`iwl_vif_priv.members`:

Members
-------

ctx
    *undescribed*

ibss_bssid_sta_id
    *undescribed*

.. _`iwl_vif_priv.description`:

Description
-----------

When mac80211 allocates a virtual interface, it can allocate
space for us to put data into.

.. _`iwl_hw_params`:

struct iwl_hw_params
====================

.. c:type:: struct iwl_hw_params


.. _`iwl_hw_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_hw_params {
        u8 tx_chains_num;
        u8 rx_chains_num;
        bool use_rts_for_aggregation;
        u32 ct_kill_threshold;
        u32 ct_kill_exit_threshold;
        const struct iwl_sensitivity_ranges *sens;
    }

.. _`iwl_hw_params.members`:

Members
-------

tx_chains_num
    Number of TX chains

rx_chains_num
    Number of RX chains

use_rts_for_aggregation
    use rts/cts protection for HT traffic

ct_kill_threshold
    temperature threshold - in hw dependent unit

ct_kill_exit_threshold
    when to reeable the device - in hw dependent unit
    relevant for 1000, 6000 and up

sens
    *undescribed*

.. _`iwl_hw_params.description`:

Description
-----------

Holds the module parameters

.. _`iwl_dvm_bt_params`:

struct iwl_dvm_bt_params
========================

.. c:type:: struct iwl_dvm_bt_params

    DVM specific BT (coex) parameters

.. _`iwl_dvm_bt_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dvm_bt_params {
        bool advanced_bt_coexist;
        u8 bt_init_traffic_load;
        u32 bt_prio_boost;
        u16 agg_time_limit;
        bool bt_sco_disable;
        bool bt_session_2;
    }

.. _`iwl_dvm_bt_params.members`:

Members
-------

advanced_bt_coexist
    support advanced bt coexist

bt_init_traffic_load
    specify initial bt traffic load

bt_prio_boost
    default bt priority boost value

agg_time_limit
    maximum number of uSec in aggregation

bt_sco_disable
    uCode should not response to BT in SCO/ESCO mode

bt_session_2
    *undescribed*

.. _`iwl_dvm_cfg`:

struct iwl_dvm_cfg
==================

.. c:type:: struct iwl_dvm_cfg

    DVM firmware specific device configuration

.. _`iwl_dvm_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dvm_cfg {
        void (*set_hw_params)(struct iwl_priv *priv);
        int (*set_channel_switch)(struct iwl_priv *priv,struct ieee80211_channel_switch *ch_switch);
        void (*nic_config)(struct iwl_priv *priv);
        void (*temperature)(struct iwl_priv *priv);
        const struct iwl_dvm_bt_params *bt_params;
        s32 chain_noise_scale;
        u8 plcp_delta_threshold;
        bool adv_thermal_throttle;
        bool support_ct_kill_exit;
        bool hd_v2;
        bool no_idle_support;
        bool need_temp_offset_calib;
        bool no_xtal_calib;
        bool temp_offset_v2;
        bool adv_pm;
    }

.. _`iwl_dvm_cfg.members`:

Members
-------

set_hw_params
    set hardware parameters

set_channel_switch
    send channel switch command

nic_config
    apply device specific configuration

temperature
    read temperature

bt_params
    pointer to BT parameters

chain_noise_scale
    default chain noise scale used for gain computation

plcp_delta_threshold
    plcp error rate threshold used to trigger
    radio tuning when there is a high receiving plcp error rate

adv_thermal_throttle
    support advance thermal throttle

support_ct_kill_exit
    support ct kill exit condition

hd_v2
    v2 of enhanced sensitivity value, used for 2000 series and up

no_idle_support
    do not support idle mode

need_temp_offset_calib
    need to perform temperature offset calibration

no_xtal_calib
    some devices do not need crystal calibration data,
    don't send it to those

temp_offset_v2
    support v2 of temperature offset calibration

adv_pm
    advanced power management

.. This file was automatic generated / don't edit.

