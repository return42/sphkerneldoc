.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/rs.h

.. _`iwl_tlc_mng_cfg_flags`:

enum iwl_tlc_mng_cfg_flags
==========================

.. c:type:: enum iwl_tlc_mng_cfg_flags

    options for TLC config flags

.. _`iwl_tlc_mng_cfg_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_mng_cfg_flags {
        IWL_TLC_MNG_CFG_FLAGS_CCK_MSK,
        IWL_TLC_MNG_CFG_FLAGS_DD_MSK,
        IWL_TLC_MNG_CFG_FLAGS_STBC_MSK,
        IWL_TLC_MNG_CFG_FLAGS_LDPC_MSK,
        IWL_TLC_MNG_CFG_FLAGS_BF_MSK,
        IWL_TLC_MNG_CFG_FLAGS_DCM_MSK
    };

.. _`iwl_tlc_mng_cfg_flags.constants`:

Constants
---------

IWL_TLC_MNG_CFG_FLAGS_CCK_MSK
    CCK support

IWL_TLC_MNG_CFG_FLAGS_DD_MSK
    enable DD

IWL_TLC_MNG_CFG_FLAGS_STBC_MSK
    enable STBC

IWL_TLC_MNG_CFG_FLAGS_LDPC_MSK
    enable LDPC

IWL_TLC_MNG_CFG_FLAGS_BF_MSK
    enable BFER

IWL_TLC_MNG_CFG_FLAGS_DCM_MSK
    enable DCM

.. _`iwl_tlc_mng_cfg_cw`:

enum iwl_tlc_mng_cfg_cw
=======================

.. c:type:: enum iwl_tlc_mng_cfg_cw

    channel width options

.. _`iwl_tlc_mng_cfg_cw.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_mng_cfg_cw {
        IWL_TLC_MNG_MAX_CH_WIDTH_20MHZ,
        IWL_TLC_MNG_MAX_CH_WIDTH_40MHZ,
        IWL_TLC_MNG_MAX_CH_WIDTH_80MHZ,
        IWL_TLC_MNG_MAX_CH_WIDTH_160MHZ,
        IWL_TLC_MNG_MAX_CH_WIDTH_LAST
    };

.. _`iwl_tlc_mng_cfg_cw.constants`:

Constants
---------

IWL_TLC_MNG_MAX_CH_WIDTH_20MHZ
    20MHZ channel

IWL_TLC_MNG_MAX_CH_WIDTH_40MHZ
    40MHZ channel

IWL_TLC_MNG_MAX_CH_WIDTH_80MHZ
    80MHZ channel

IWL_TLC_MNG_MAX_CH_WIDTH_160MHZ
    160MHZ channel

IWL_TLC_MNG_MAX_CH_WIDTH_LAST
    maximum value

.. _`iwl_tlc_mng_cfg_chains`:

enum iwl_tlc_mng_cfg_chains
===========================

.. c:type:: enum iwl_tlc_mng_cfg_chains

    possible chains

.. _`iwl_tlc_mng_cfg_chains.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_mng_cfg_chains {
        IWL_TLC_MNG_CHAIN_A_MSK,
        IWL_TLC_MNG_CHAIN_B_MSK,
        IWL_TLC_MNG_CHAIN_C_MSK
    };

.. _`iwl_tlc_mng_cfg_chains.constants`:

Constants
---------

IWL_TLC_MNG_CHAIN_A_MSK
    chain A

IWL_TLC_MNG_CHAIN_B_MSK
    chain B

IWL_TLC_MNG_CHAIN_C_MSK
    chain C

.. _`iwl_tlc_mng_cfg_gi`:

enum iwl_tlc_mng_cfg_gi
=======================

.. c:type:: enum iwl_tlc_mng_cfg_gi

    guard interval options

.. _`iwl_tlc_mng_cfg_gi.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_mng_cfg_gi {
        IWL_TLC_MNG_SGI_20MHZ_MSK,
        IWL_TLC_MNG_SGI_40MHZ_MSK,
        IWL_TLC_MNG_SGI_80MHZ_MSK,
        IWL_TLC_MNG_SGI_160MHZ_MSK
    };

.. _`iwl_tlc_mng_cfg_gi.constants`:

Constants
---------

IWL_TLC_MNG_SGI_20MHZ_MSK
    enable short GI for 20MHZ

IWL_TLC_MNG_SGI_40MHZ_MSK
    enable short GI for 40MHZ

IWL_TLC_MNG_SGI_80MHZ_MSK
    enable short GI for 80MHZ

IWL_TLC_MNG_SGI_160MHZ_MSK
    enable short GI for 160MHZ

.. _`iwl_tlc_mng_cfg_mode`:

enum iwl_tlc_mng_cfg_mode
=========================

.. c:type:: enum iwl_tlc_mng_cfg_mode

    supported modes

.. _`iwl_tlc_mng_cfg_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_mng_cfg_mode {
        IWL_TLC_MNG_MODE_CCK,
        IWL_TLC_MNG_MODE_OFDM_NON_HT,
        IWL_TLC_MNG_MODE_NON_HT,
        IWL_TLC_MNG_MODE_HT,
        IWL_TLC_MNG_MODE_VHT,
        IWL_TLC_MNG_MODE_HE,
        IWL_TLC_MNG_MODE_INVALID,
        IWL_TLC_MNG_MODE_NUM
    };

.. _`iwl_tlc_mng_cfg_mode.constants`:

Constants
---------

IWL_TLC_MNG_MODE_CCK
    enable CCK

IWL_TLC_MNG_MODE_OFDM_NON_HT
    enable OFDM (non HT)

IWL_TLC_MNG_MODE_NON_HT
    enable non HT

IWL_TLC_MNG_MODE_HT
    enable HT

IWL_TLC_MNG_MODE_VHT
    enable VHT

IWL_TLC_MNG_MODE_HE
    enable HE

IWL_TLC_MNG_MODE_INVALID
    invalid value

IWL_TLC_MNG_MODE_NUM
    a count of possible modes

.. _`iwl_tlc_mng_vht_he_types`:

enum iwl_tlc_mng_vht_he_types
=============================

.. c:type:: enum iwl_tlc_mng_vht_he_types

    VHT HE types

.. _`iwl_tlc_mng_vht_he_types.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_mng_vht_he_types {
        IWL_TLC_MNG_VALID_VHT_HE_TYPES_SU,
        IWL_TLC_MNG_VALID_VHT_HE_TYPES_SU_EXT,
        IWL_TLC_MNG_VALID_VHT_HE_TYPES_MU,
        IWL_TLC_MNG_VALID_VHT_HE_TYPES_TRIG_BASED,
        IWL_TLC_MNG_VALID_VHT_HE_TYPES_NUM
    };

.. _`iwl_tlc_mng_vht_he_types.constants`:

Constants
---------

IWL_TLC_MNG_VALID_VHT_HE_TYPES_SU
    VHT HT single user

IWL_TLC_MNG_VALID_VHT_HE_TYPES_SU_EXT
    VHT HT single user extended

IWL_TLC_MNG_VALID_VHT_HE_TYPES_MU
    VHT HT multiple users

IWL_TLC_MNG_VALID_VHT_HE_TYPES_TRIG_BASED
    trigger based

IWL_TLC_MNG_VALID_VHT_HE_TYPES_NUM
    a count of possible types

.. _`iwl_tlc_mng_ht_rates`:

enum iwl_tlc_mng_ht_rates
=========================

.. c:type:: enum iwl_tlc_mng_ht_rates

    HT/VHT rates

.. _`iwl_tlc_mng_ht_rates.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_mng_ht_rates {
        IWL_TLC_MNG_HT_RATE_MCS0,
        IWL_TLC_MNG_HT_RATE_MCS1,
        IWL_TLC_MNG_HT_RATE_MCS2,
        IWL_TLC_MNG_HT_RATE_MCS3,
        IWL_TLC_MNG_HT_RATE_MCS4,
        IWL_TLC_MNG_HT_RATE_MCS5,
        IWL_TLC_MNG_HT_RATE_MCS6,
        IWL_TLC_MNG_HT_RATE_MCS7,
        IWL_TLC_MNG_HT_RATE_MCS8,
        IWL_TLC_MNG_HT_RATE_MCS9,
        IWL_TLC_MNG_HT_RATE_MAX
    };

.. _`iwl_tlc_mng_ht_rates.constants`:

Constants
---------

IWL_TLC_MNG_HT_RATE_MCS0
    index of MCS0

IWL_TLC_MNG_HT_RATE_MCS1
    index of MCS1

IWL_TLC_MNG_HT_RATE_MCS2
    index of MCS2

IWL_TLC_MNG_HT_RATE_MCS3
    index of MCS3

IWL_TLC_MNG_HT_RATE_MCS4
    index of MCS4

IWL_TLC_MNG_HT_RATE_MCS5
    index of MCS5

IWL_TLC_MNG_HT_RATE_MCS6
    index of MCS6

IWL_TLC_MNG_HT_RATE_MCS7
    index of MCS7

IWL_TLC_MNG_HT_RATE_MCS8
    index of MCS8

IWL_TLC_MNG_HT_RATE_MCS9
    index of MCS9

IWL_TLC_MNG_HT_RATE_MAX
    maximal rate for HT/VHT

.. _`iwl_tlc_config_cmd`:

struct iwl_tlc_config_cmd
=========================

.. c:type:: struct iwl_tlc_config_cmd

    TLC configuration

.. _`iwl_tlc_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tlc_config_cmd {
        u8 sta_id;
        u8 reserved1[3];
        u8 max_supp_ch_width;
        u8 chains;
        u8 max_supp_ss;
        u8 valid_vht_he_types;
        __le16 flags;
        __le16 non_ht_supp_rates;
        __le16 ht_supp_rates[MAX_RS_ANT_NUM];
        u8 mode;
        u8 reserved2;
        __le16 he_supp_rates;
        u8 sgi_ch_width_supp;
        u8 he_gi_support;
        __le32 max_ampdu_cnt;
    }

.. _`iwl_tlc_config_cmd.members`:

Members
-------

sta_id
    station id

reserved1
    reserved

max_supp_ch_width
    channel width

chains
    bitmask of \ :c:type:`enum iwl_tlc_mng_cfg_chains <iwl_tlc_mng_cfg_chains>`\ 

max_supp_ss
    valid values are 0-3, 0 - spatial streams are not supported

valid_vht_he_types
    bitmap of \ :c:type:`enum iwl_tlc_mng_vht_he_types <iwl_tlc_mng_vht_he_types>`\ 

flags
    bitmask of \ :c:type:`enum iwl_tlc_mng_cfg_flags <iwl_tlc_mng_cfg_flags>`\ 

non_ht_supp_rates
    bitmap of supported legacy rates

ht_supp_rates
    bitmap of supported HT/VHT rates, valid bits are 0-9

mode
    &enum iwl_tlc_mng_cfg_mode

reserved2
    reserved

he_supp_rates
    bitmap of supported HE rates

sgi_ch_width_supp
    bitmap of SGI support per channel width

he_gi_support
    11ax HE guard interval

max_ampdu_cnt
    max AMPDU size (frames count)

.. _`iwl_tlc_notif_req_config_cmd`:

struct iwl_tlc_notif_req_config_cmd
===================================

.. c:type:: struct iwl_tlc_notif_req_config_cmd

    request notif on specific changes

.. _`iwl_tlc_notif_req_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tlc_notif_req_config_cmd {
        u8 sta_id;
        u8 reserved1;
        __le16 flags;
        __le16 interval;
        __le16 reserved2;
    }

.. _`iwl_tlc_notif_req_config_cmd.members`:

Members
-------

sta_id
    relevant station

reserved1
    reserved

flags
    bitmap of requested notifications \ ``IWL_TLC_NOTIF_INIT_``\ \\*

interval
    minimum time between notifications from TLC to the driver (msec)

reserved2
    reserved

.. _`iwl_tlc_update_notif`:

struct iwl_tlc_update_notif
===========================

.. c:type:: struct iwl_tlc_update_notif

    TLC notification from FW

.. _`iwl_tlc_update_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tlc_update_notif {
        u8 sta_id;
        u8 reserved;
        __le16 flags;
        __le32 values[16];
    }

.. _`iwl_tlc_update_notif.members`:

Members
-------

sta_id
    station id

reserved
    reserved

flags
    bitmap of notifications reported

values
    field per flag in struct iwl_tlc_notif_req_config_cmd

.. _`iwl_tlc_debug_flags`:

enum iwl_tlc_debug_flags
========================

.. c:type:: enum iwl_tlc_debug_flags

    debug options

.. _`iwl_tlc_debug_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_debug_flags {
        IWL_TLC_DEBUG_FIXED_RATE,
        IWL_TLC_DEBUG_STATS_TH,
        IWL_TLC_DEBUG_STATS_TIME_TH,
        IWL_TLC_DEBUG_AGG_TIME_LIM,
        IWL_TLC_DEBUG_AGG_DIS_START_TH,
        IWL_TLC_DEBUG_AGG_FRAME_CNT_LIM,
        IWL_TLC_DEBUG_RENEW_ADDBA_DELAY,
        IWL_TLC_DEBUG_START_AC_RATE_IDX,
        IWL_TLC_DEBUG_NO_FAR_RANGE_TWEAK
    };

.. _`iwl_tlc_debug_flags.constants`:

Constants
---------

IWL_TLC_DEBUG_FIXED_RATE
    set fixed rate for rate scaling

IWL_TLC_DEBUG_STATS_TH
    threshold for sending statistics to the driver, in
    frames

IWL_TLC_DEBUG_STATS_TIME_TH
    threshold for sending statistics to the
    driver, in msec

IWL_TLC_DEBUG_AGG_TIME_LIM
    time limit for a BA session

IWL_TLC_DEBUG_AGG_DIS_START_TH
    frame with try-count greater than this
    threshold should not start an aggregation session

IWL_TLC_DEBUG_AGG_FRAME_CNT_LIM
    set max number of frames in an aggregation

IWL_TLC_DEBUG_RENEW_ADDBA_DELAY
    delay between retries of ADD BA

IWL_TLC_DEBUG_START_AC_RATE_IDX
    frames per second to start a BA session

IWL_TLC_DEBUG_NO_FAR_RANGE_TWEAK
    disable BW scaling

.. _`iwl_dhc_tlc_cmd`:

struct iwl_dhc_tlc_cmd
======================

.. c:type:: struct iwl_dhc_tlc_cmd

    fixed debug config

.. _`iwl_dhc_tlc_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dhc_tlc_cmd {
        u8 sta_id;
        u8 reserved1[3];
        __le32 flags;
        __le32 fixed_rate;
        __le16 stats_threshold;
        __le16 time_threshold;
        __le16 agg_time_lim;
        __le16 agg_dis_start_threshold;
        __le16 agg_frame_count_lim;
        __le16 addba_retry_delay;
        u8 start_ac_rate_idx[IEEE80211_NUM_ACS];
        u8 no_far_range_tweak;
        u8 reserved2[3];
    }

.. _`iwl_dhc_tlc_cmd.members`:

Members
-------

sta_id
    bit 0 - enable/disable, bits 1 - 7 hold station id

reserved1
    reserved

flags
    bitmap of \ ``IWL_TLC_DEBUG_``\ \\*

fixed_rate
    rate value

stats_threshold
    if number of tx-ed frames is greater, send statistics

time_threshold
    statistics threshold in usec

agg_time_lim
    max agg time

agg_dis_start_threshold
    frames with try-cont greater than this count will
    not be aggregated

agg_frame_count_lim
    agg size

addba_retry_delay
    delay between retries of ADD BA

start_ac_rate_idx
    frames per second to start a BA session

no_far_range_tweak
    disable BW scaling

reserved2
    reserved

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
        __le16 control;
        u8 flags;
        u8 mimo_delim;
        u8 single_stream_ant_msk;
        u8 dual_stream_ant_msk;
        u8 initial_rate_index[AC_NUM];
        __le16 agg_time_limit;
        u8 agg_disable_start_th;
        u8 agg_frame_cnt_limit;
        __le32 reserved2;
        __le32 rs_table[LQ_MAX_RETRY_NUM];
        __le32 ss_params;
    }

.. _`iwl_lq_cmd.members`:

Members
-------

sta_id
    station to update

reduced_tpc
    reduced transmit power control value

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
    reserved

rs_table
    array of rates for each TX try, each is rate_n_flags,
    meaning it is a combination of RATE_MCS\_\* and IWL_RATE\_\*\_PLCP

ss_params
    single stream features. declare whether STBC or BFER are allowed.

.. This file was automatic generated / don't edit.

