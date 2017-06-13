.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/rs.h

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
        struct rs_rate rate;
        enum rs_column column;
        const u16 *expected_tpt;
        struct iwl_rate_scale_data win;
        struct iwl_rate_scale_data tpc_win;
    }

.. _`iwl_scale_tbl_info.members`:

Members
-------

rate
    *undescribed*

column
    *undescribed*

expected_tpt
    *undescribed*

win
    *undescribed*

tpc_win
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
        u8 rs_state;
        u8 search_better_tbl;
        s32 last_tpt;
        u32 table_count_limit;
        u32 max_failure_limit;
        u32 max_success_limit;
        u32 table_count;
        u32 total_failed;
        u32 total_success;
        u64 flush_timer;
        u32 visited_columns;
        u64 last_tx;
        bool is_vht;
        bool ldpc;
        bool stbc_capable;
        bool bfer_capable;
        enum nl80211_band band;
        unsigned long active_legacy_rate;
        unsigned long active_siso_rate;
        unsigned long active_mimo2_rate;
        u8 max_legacy_rate_idx;
        u8 max_siso_rate_idx;
        u8 max_mimo2_rate_idx;
        struct rs_rate optimal_rate;
        unsigned long optimal_rate_mask;
        const struct rs_init_rate_info *optimal_rates;
        int optimal_nentries;
        u8 missed_rate_counter;
        struct iwl_lq_cmd lq;
        struct iwl_scale_tbl_info lq_info;
        u8 tx_agg_tid_en;
        u32 last_rate_n_flags;
        u8 is_agg;
        int tpc_reduce;
        struct lq_sta_pers pers;
    }

.. _`iwl_lq_sta.members`:

Members
-------

active_tbl
    *undescribed*

rs_state
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

visited_columns
    *undescribed*

last_tx
    *undescribed*

is_vht
    *undescribed*

ldpc
    *undescribed*

stbc_capable
    *undescribed*

bfer_capable
    *undescribed*

band
    *undescribed*

active_legacy_rate
    *undescribed*

active_siso_rate
    *undescribed*

active_mimo2_rate
    *undescribed*

max_legacy_rate_idx
    *undescribed*

max_siso_rate_idx
    *undescribed*

max_mimo2_rate_idx
    *undescribed*

optimal_rate
    *undescribed*

optimal_rate_mask
    *undescribed*

optimal_rates
    *undescribed*

optimal_nentries
    *undescribed*

missed_rate_counter
    *undescribed*

lq
    *undescribed*

lq_info
    *undescribed*

tx_agg_tid_en
    *undescribed*

last_rate_n_flags
    *undescribed*

is_agg
    *undescribed*

tpc_reduce
    *undescribed*

pers
    *undescribed*

.. _`iwl_lq_sta.description`:

Description
-----------

Pointer to this gets passed back and forth between driver and mac80211.

.. _`iwl_mvm_rate_control_register`:

iwl_mvm_rate_control_register
=============================

.. c:function:: int iwl_mvm_rate_control_register( void)

    Register the rate control algorithm callbacks

    :param  void:
        no arguments

.. _`iwl_mvm_rate_control_register.description`:

Description
-----------

Since the rate control algorithm is hardware specific, there is no need
or reason to place it as a stand alone module.  The driver can call
iwl_rate_control_register in order to register the rate control callbacks
with the mac80211 subsystem.  This should be performed prior to calling
ieee80211_register_hw

.. _`iwl_mvm_rate_control_unregister`:

iwl_mvm_rate_control_unregister
===============================

.. c:function:: void iwl_mvm_rate_control_unregister( void)

    Unregister the rate control callbacks

    :param  void:
        no arguments

.. _`iwl_mvm_rate_control_unregister.description`:

Description
-----------

This should be called after calling ieee80211_unregister_hw, but before
the driver is unloaded.

.. This file was automatic generated / don't edit.

