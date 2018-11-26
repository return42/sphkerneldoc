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
        IWL_TLC_MNG_CFG_FLAGS_STBC_MSK,
        IWL_TLC_MNG_CFG_FLAGS_LDPC_MSK,
        IWL_TLC_MNG_CFG_FLAGS_HE_STBC_160MHZ_MSK,
        IWL_TLC_MNG_CFG_FLAGS_HE_DCM_NSS_1_MSK,
        IWL_TLC_MNG_CFG_FLAGS_HE_DCM_NSS_2_MSK
    };

.. _`iwl_tlc_mng_cfg_flags.constants`:

Constants
---------

IWL_TLC_MNG_CFG_FLAGS_STBC_MSK
    enable STBC. For HE this enables STBC for
    bandwidths <= 80MHz

IWL_TLC_MNG_CFG_FLAGS_LDPC_MSK
    enable LDPC

IWL_TLC_MNG_CFG_FLAGS_HE_STBC_160MHZ_MSK
    enable STBC in HE at 160MHz
    bandwidth

IWL_TLC_MNG_CFG_FLAGS_HE_DCM_NSS_1_MSK
    enable HE Dual Carrier Modulation
    for BPSK (MCS 0) with 1 spatial
    stream

IWL_TLC_MNG_CFG_FLAGS_HE_DCM_NSS_2_MSK
    enable HE Dual Carrier Modulation
    for BPSK (MCS 0) with 2 spatial
    streams

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
        IWL_TLC_MNG_CH_WIDTH_20MHZ,
        IWL_TLC_MNG_CH_WIDTH_40MHZ,
        IWL_TLC_MNG_CH_WIDTH_80MHZ,
        IWL_TLC_MNG_CH_WIDTH_160MHZ,
        IWL_TLC_MNG_CH_WIDTH_LAST
    };

.. _`iwl_tlc_mng_cfg_cw.constants`:

Constants
---------

IWL_TLC_MNG_CH_WIDTH_20MHZ
    20MHZ channel

IWL_TLC_MNG_CH_WIDTH_40MHZ
    40MHZ channel

IWL_TLC_MNG_CH_WIDTH_80MHZ
    80MHZ channel

IWL_TLC_MNG_CH_WIDTH_160MHZ
    160MHZ channel

IWL_TLC_MNG_CH_WIDTH_LAST
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
        IWL_TLC_MNG_CHAIN_B_MSK
    };

.. _`iwl_tlc_mng_cfg_chains.constants`:

Constants
---------

IWL_TLC_MNG_CHAIN_A_MSK
    chain A

IWL_TLC_MNG_CHAIN_B_MSK
    chain B

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

.. _`iwl_tlc_mng_ht_rates`:

enum iwl_tlc_mng_ht_rates
=========================

.. c:type:: enum iwl_tlc_mng_ht_rates

    HT/VHT/HE rates

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
        IWL_TLC_MNG_HT_RATE_MCS10,
        IWL_TLC_MNG_HT_RATE_MCS11,
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

IWL_TLC_MNG_HT_RATE_MCS10
    index of MCS10

IWL_TLC_MNG_HT_RATE_MCS11
    index of MCS11

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
        u8 max_ch_width;
        u8 mode;
        u8 chains;
        u8 amsdu;
        __le16 flags;
        __le16 non_ht_rates;
        __le16 ht_rates[MAX_NSS][2];
        __le16 max_mpdu_len;
        u8 sgi_ch_width_supp;
        u8 reserved2[1];
    }

.. _`iwl_tlc_config_cmd.members`:

Members
-------

sta_id
    station id

reserved1
    reserved

max_ch_width
    max supported channel width from \ ``enum``\  iwl_tlc_mng_cfg_cw

mode
    \ :c:type:`enum iwl_tlc_mng_cfg_mode <iwl_tlc_mng_cfg_mode>`\ 

chains
    bitmask of \ :c:type:`enum iwl_tlc_mng_cfg_chains <iwl_tlc_mng_cfg_chains>`\ 

amsdu
    TX amsdu is supported

flags
    bitmask of \ :c:type:`enum iwl_tlc_mng_cfg_flags <iwl_tlc_mng_cfg_flags>`\ 

non_ht_rates
    bitmap of supported legacy rates

ht_rates
    bitmap of \ :c:type:`enum iwl_tlc_mng_ht_rates <iwl_tlc_mng_ht_rates>`\ , per <nss, channel-width>
    pair (0 - 80mhz width and below, 1 - 160mhz).

max_mpdu_len
    max MPDU length, in bytes

sgi_ch_width_supp
    bitmap of SGI support per channel width
    use BIT(@enum iwl_tlc_mng_cfg_cw)

reserved2
    reserved

.. _`iwl_tlc_update_flags`:

enum iwl_tlc_update_flags
=========================

.. c:type:: enum iwl_tlc_update_flags

    updated fields

.. _`iwl_tlc_update_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tlc_update_flags {
        IWL_TLC_NOTIF_FLAG_RATE,
        IWL_TLC_NOTIF_FLAG_AMSDU
    };

.. _`iwl_tlc_update_flags.constants`:

Constants
---------

IWL_TLC_NOTIF_FLAG_RATE
    last initial rate update

IWL_TLC_NOTIF_FLAG_AMSDU
    umsdu parameters update

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
        u8 reserved[3];
        __le32 flags;
        __le32 rate;
        __le32 amsdu_size;
        __le32 amsdu_enabled;
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

rate
    current initial rate

amsdu_size
    Max AMSDU size, in bytes

amsdu_enabled
    bitmap for per-TID AMSDU enablement

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

