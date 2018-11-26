.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/rs.h

.. _`iwl_rate_scale_data`:

struct iwl_rate_scale_data
==========================

.. c:type:: struct iwl_rate_scale_data

    - tx success history for one rate

.. _`iwl_rate_scale_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rate_scale_data {
        u64 data;
        s32 success_counter;
        s32 success_ratio;
        s32 counter;
        s32 average_tpt;
        unsigned long stamp;
    }

.. _`iwl_rate_scale_data.members`:

Members
-------

data
    *undescribed*

success_counter
    *undescribed*

success_ratio
    *undescribed*

counter
    *undescribed*

average_tpt
    *undescribed*

stamp
    *undescribed*

.. _`iwl_scale_tbl_info`:

struct iwl_scale_tbl_info
=========================

.. c:type:: struct iwl_scale_tbl_info

    - tx params and success history for all rates

.. _`iwl_scale_tbl_info.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scale_tbl_info {
        enum iwl_table_type lq_type;
        u8 ant_type;
        u8 is_SGI;
        u8 is_ht40;
        u8 is_dup;
        u8 action;
        u8 max_search;
        const u16 *expected_tpt;
        u32 current_rate;
        struct iwl_rate_scale_data win[IWL_RATE_COUNT];
    }

.. _`iwl_scale_tbl_info.members`:

Members
-------

lq_type
    *undescribed*

ant_type
    *undescribed*

is_SGI
    *undescribed*

is_ht40
    *undescribed*

is_dup
    *undescribed*

action
    *undescribed*

max_search
    *undescribed*

expected_tpt
    *undescribed*

current_rate
    *undescribed*

win
    *undescribed*

.. _`iwl_scale_tbl_info.description`:

Description
-----------

There are two of these in struct iwl_lq_sta,
one for "active", and one for "search".

.. _`iwl_lq_sta`:

struct iwl_lq_sta
=================

.. c:type:: struct iwl_lq_sta

    - driver's rate scaling private structure

.. _`iwl_lq_sta.definition`:

Definition
----------

.. code-block:: c

    struct iwl_lq_sta {
        u8 active_tbl;
        u8 enable_counter;
        u8 stay_in_tbl;
        u8 search_better_tbl;
        s32 last_tpt;
        u32 table_count_limit;
        u32 max_failure_limit;
        u32 max_success_limit;
        u32 table_count;
        u32 total_failed;
        u32 total_success;
        u64 flush_timer;
        u8 action_counter;
        u8 is_green;
        u8 is_dup;
        enum nl80211_band band;
        u32 supp_rates;
        u16 active_legacy_rate;
        u16 active_siso_rate;
        u16 active_mimo2_rate;
        u16 active_mimo3_rate;
        s8 max_rate_idx;
        u8 missed_rate_counter;
        struct iwl_link_quality_cmd lq;
        struct iwl_scale_tbl_info lq_info[LQ_SIZE];
        struct iwl_traffic_load load[IWL_MAX_TID_COUNT];
        u8 tx_agg_tid_en;
    #ifdef CONFIG_MAC80211_DEBUGFS
        struct dentry *rs_sta_dbgfs_scale_table_file;
        struct dentry *rs_sta_dbgfs_stats_table_file;
        struct dentry *rs_sta_dbgfs_rate_scale_data_file;
        struct dentry *rs_sta_dbgfs_tx_agg_tid_en_file;
        u32 dbg_fixed_rate;
    #endif
        struct iwl_priv *drv;
        int last_txrate_idx;
        u32 last_rate_n_flags;
        u8 is_agg;
        u8 last_bt_traffic;
    }

.. _`iwl_lq_sta.members`:

Members
-------

active_tbl
    *undescribed*

enable_counter
    *undescribed*

stay_in_tbl
    *undescribed*

search_better_tbl
    *undescribed*

last_tpt
    *undescribed*

table_count_limit
    *undescribed*

max_failure_limit
    *undescribed*

max_success_limit
    *undescribed*

table_count
    *undescribed*

total_failed
    *undescribed*

total_success
    *undescribed*

flush_timer
    *undescribed*

action_counter
    *undescribed*

is_green
    *undescribed*

is_dup
    *undescribed*

band
    *undescribed*

supp_rates
    *undescribed*

active_legacy_rate
    *undescribed*

active_siso_rate
    *undescribed*

active_mimo2_rate
    *undescribed*

active_mimo3_rate
    *undescribed*

max_rate_idx
    *undescribed*

missed_rate_counter
    *undescribed*

lq
    *undescribed*

lq_info
    *undescribed*

load
    *undescribed*

tx_agg_tid_en
    *undescribed*

rs_sta_dbgfs_scale_table_file
    *undescribed*

rs_sta_dbgfs_stats_table_file
    *undescribed*

rs_sta_dbgfs_rate_scale_data_file
    *undescribed*

rs_sta_dbgfs_tx_agg_tid_en_file
    *undescribed*

dbg_fixed_rate
    *undescribed*

drv
    *undescribed*

last_txrate_idx
    *undescribed*

last_rate_n_flags
    *undescribed*

is_agg
    *undescribed*

last_bt_traffic
    *undescribed*

.. _`iwl_lq_sta.description`:

Description
-----------

Pointer to this gets passed back and forth between driver and mac80211.

.. _`iwlagn_rate_control_register`:

iwlagn_rate_control_register
============================

.. c:function:: int iwlagn_rate_control_register( void)

    Register the rate control algorithm callbacks

    :param void:
        no arguments
    :type void: 

.. _`iwlagn_rate_control_register.description`:

Description
-----------

Since the rate control algorithm is hardware specific, there is no need
or reason to place it as a stand alone module.  The driver can call
iwl_rate_control_register in order to register the rate control callbacks
with the mac80211 subsystem.  This should be performed prior to calling
ieee80211_register_hw

.. _`iwlagn_rate_control_unregister`:

iwlagn_rate_control_unregister
==============================

.. c:function:: void iwlagn_rate_control_unregister( void)

    Unregister the rate control callbacks

    :param void:
        no arguments
    :type void: 

.. _`iwlagn_rate_control_unregister.description`:

Description
-----------

This should be called after calling ieee80211_unregister_hw, but before
the driver is unloaded.

.. This file was automatic generated / don't edit.

