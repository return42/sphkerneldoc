.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-rs.h

.. _`iwl_lq_cmd`:

struct iwl_lq_cmd
=================

.. c:type:: struct iwl_lq_cmd

    link quality command

.. _`iwl_lq_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_lq_cmd {
        u8 sta_id;
        u8 reduced_tpc;
        u16 control;
        u8 flags;
        u8 mimo_delim;
        u8 single_stream_ant_msk;
        u8 dual_stream_ant_msk;
        u8 initial_rate_index;
        __le16 agg_time_limit;
        u8 agg_disable_start_th;
        u8 agg_frame_cnt_limit;
        __le32 reserved2;
        __le32 rs_table;
        __le32 ss_params;
    }

.. _`iwl_lq_cmd.members`:

Members
-------

sta_id
    station to update

reduced_tpc
    *undescribed*

control
    not used

flags
    combination of LQ_FLAG\_\*

mimo_delim
    the first SISO index in rs_table, which separates MIMO
    and SISO rates

single_stream_ant_msk
    best antenna for SISO (can be dual in CDD).
    Should be ANT_[ABC]

dual_stream_ant_msk
    best antennas for MIMO, combination of ANT_[ABC]

initial_rate_index
    first index from rs_table per AC category

agg_time_limit
    aggregation max time threshold in usec/100, meaning
    value of 100 is one usec. Range is 100 to 8000

agg_disable_start_th
    try-count threshold for starting aggregation.
    If a frame has higher try-count, it should not be selected for
    starting an aggregation sequence.

agg_frame_cnt_limit
    max frame count in an aggregation.
    0: no limit
    1: no aggregation (one frame per aggregation)
    2 - 0x3f: maximal number of frames (up to 3f == 63)

reserved2
    *undescribed*

rs_table
    array of rates for each TX try, each is rate_n_flags,
    meaning it is a combination of RATE_MCS\_\* and IWL_RATE\_\*\_PLCP

ss_params
    single stream features. declare whether STBC or BFER are allowed.

.. This file was automatic generated / don't edit.

