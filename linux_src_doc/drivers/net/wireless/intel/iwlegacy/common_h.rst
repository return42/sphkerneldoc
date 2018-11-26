.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlegacy/common.h

.. _`il_device_cmd`:

struct il_device_cmd
====================

.. c:type:: struct il_device_cmd


.. _`il_device_cmd.definition`:

Definition
----------

.. code-block:: c

    struct il_device_cmd {
        struct il_cmd_header hdr;
        union {
            u32 flags;
            u8 val8;
            u16 val16;
            u32 val32;
            struct il_tx_cmd tx;
            u8 payload[DEF_CMD_PAYLOAD_SIZE];
        } __packed cmd;
    }

.. _`il_device_cmd.members`:

Members
-------

hdr
    *undescribed*

cmd
    *undescribed*

.. _`il_device_cmd.description`:

Description
-----------

For allocation of the command and tx queues, this establishes the overall
size of the largest command we send to uCode, except for a scan command
(which is relatively huge; space is allocated separately).

.. _`il_rx_queue`:

struct il_rx_queue
==================

.. c:type:: struct il_rx_queue

    Rx queue

.. _`il_rx_queue.definition`:

Definition
----------

.. code-block:: c

    struct il_rx_queue {
        __le32 *bd;
        dma_addr_t bd_dma;
        struct il_rx_buf pool[RX_QUEUE_SIZE + RX_FREE_BUFFERS];
        struct il_rx_buf *queue[RX_QUEUE_SIZE];
        u32 read;
        u32 write;
        u32 free_count;
        u32 write_actual;
        struct list_head rx_free;
        struct list_head rx_used;
        int need_update;
        struct il_rb_status *rb_stts;
        dma_addr_t rb_stts_dma;
        spinlock_t lock;
    }

.. _`il_rx_queue.members`:

Members
-------

bd
    driver's pointer to buffer of receive buffer descriptors (rbd)

bd_dma
    bus address of buffer of receive buffer descriptors (rbd)

pool
    *undescribed*

queue
    *undescribed*

read
    Shared idx to newest available Rx buffer

write
    Shared idx to oldest written Rx packet

free_count
    Number of pre-allocated buffers in rx_free

write_actual
    *undescribed*

rx_free
    list of free SKBs for use

rx_used
    List of Rx buffers with no SKB

need_update
    flag to indicate we need to update read/write idx

rb_stts
    driver's pointer to receive buffer status

rb_stts_dma
    bus address of receive buffer status

lock
    *undescribed*

.. _`il_rx_queue.note`:

NOTE
----

rx_free and rx_used are used as a FIFO for il_rx_bufs

.. _`il_ht_agg`:

struct il_ht_agg
================

.. c:type:: struct il_ht_agg

    - aggregation status while waiting for block-ack

.. _`il_ht_agg.definition`:

Definition
----------

.. code-block:: c

    struct il_ht_agg {
        u16 txq_id;
        u16 frame_count;
        u16 wait_for_ba;
        u16 start_idx;
        u64 bitmap;
        u32 rate_n_flags;
    #define IL_AGG_OFF 0
    #define IL_AGG_ON 1
    #define IL_EMPTYING_HW_QUEUE_ADDBA 2
    #define IL_EMPTYING_HW_QUEUE_DELBA 3
        u8 state;
    }

.. _`il_ht_agg.members`:

Members
-------

txq_id
    Tx queue used for Tx attempt

frame_count
    # frames attempted by Tx command

wait_for_ba
    Expect block-ack before next Tx reply

start_idx
    Index of 1st Transmit Frame Descriptor (TFD) in Tx win

bitmap
    *undescribed*

rate_n_flags
    Rate at which Tx was attempted

state
    *undescribed*

.. _`il_ht_agg.description`:

Description
-----------

If C_TX indicates that aggregation was attempted, driver must wait
for block ack (N_COMPRESSED_BA).  This struct stores tx reply info
until block ack arrives.

.. _`il_vif_priv`:

struct il_vif_priv
==================

.. c:type:: struct il_vif_priv

    driver's ilate per-interface information

.. _`il_vif_priv.definition`:

Definition
----------

.. code-block:: c

    struct il_vif_priv {
        u8 ibss_bssid_sta_id;
    }

.. _`il_vif_priv.members`:

Members
-------

ibss_bssid_sta_id
    *undescribed*

.. _`il_vif_priv.description`:

Description
-----------

When mac80211 allocates a virtual interface, it can allocate
space for us to put data into.

.. _`il_hw_params`:

struct il_hw_params
===================

.. c:type:: struct il_hw_params


.. _`il_hw_params.definition`:

Definition
----------

.. code-block:: c

    struct il_hw_params {
        u8 bcast_id;
        u8 max_txq_num;
        u8 dma_chnl_num;
        u16 scd_bc_tbls_size;
        u32 tfd_size;
        u8 tx_chains_num;
        u8 rx_chains_num;
        u8 valid_tx_ant;
        u8 valid_rx_ant;
        u16 max_rxq_size;
        u16 max_rxq_log;
        u32 rx_page_order;
        u32 rx_wrt_ptr_reg;
        u8 max_stations;
        u8 ht40_channel;
        u8 max_beacon_itrvl;
        u32 max_inst_size;
        u32 max_data_size;
        u32 max_bsm_size;
        u32 ct_kill_threshold;
        u16 beacon_time_tsf_bits;
        const struct il_sensitivity_ranges *sens;
    }

.. _`il_hw_params.members`:

Members
-------

bcast_id
    f/w broadcast station ID

max_txq_num
    Max # Tx queues supported

dma_chnl_num
    Number of Tx DMA/FIFO channels

scd_bc_tbls_size
    size of scheduler byte count tables

tfd_size
    TFD size

tx_chains_num
    *undescribed*

rx_chains_num
    *undescribed*

valid_tx_ant
    *undescribed*

valid_rx_ant
    *undescribed*

max_rxq_size
    Max # Rx frames in Rx queue (must be power-of-2)

max_rxq_log
    Log-base-2 of max_rxq_size

rx_page_order
    Rx buffer page order

rx_wrt_ptr_reg
    FH{39}_RSCSR_CHNL0_WPTR

max_stations
    *undescribed*

ht40_channel
    is 40MHz width possible in band 2.4
    BIT(NL80211_BAND_5GHZ) BIT(NL80211_BAND_5GHZ)

max_beacon_itrvl
    *undescribed*

max_inst_size
    *undescribed*

max_data_size
    *undescribed*

max_bsm_size
    *undescribed*

ct_kill_threshold
    temperature threshold

beacon_time_tsf_bits
    number of valid tsf bits for beacon time

sens
    *undescribed*

.. _`il_cfg`:

struct il_cfg
=============

.. c:type:: struct il_cfg


.. _`il_cfg.definition`:

Definition
----------

.. code-block:: c

    struct il_cfg {
        const char *name;
        const char *fw_name_pre;
        const unsigned int ucode_api_max;
        const unsigned int ucode_api_min;
        u8 valid_tx_ant;
        u8 valid_rx_ant;
        unsigned int sku;
        u16 eeprom_ver;
        u16 eeprom_calib_ver;
        const struct il_mod_params *mod_params;
        struct il_base_params *base_params;
        u8 scan_rx_antennas[NUM_NL80211_BANDS];
        enum il_led_mode led_mode;
        int eeprom_size;
        int num_of_queues;
        int num_of_ampdu_queues;
        u32 pll_cfg_val;
        bool set_l0s;
        bool use_bsm;
        u16 led_compensation;
        int chain_noise_num_beacons;
        unsigned int wd_timeout;
        bool temperature_kelvin;
        const bool ucode_tracing;
        const bool sensitivity_calib_by_driver;
        const bool chain_noise_calib_by_driver;
        const u32 regulatory_bands[7];
    }

.. _`il_cfg.members`:

Members
-------

name
    *undescribed*

fw_name_pre
    Firmware filename prefix. The api version and extension
    (.ucode) will be added to filename before loading from disk. The
    filename is constructed as fw_name_pre<api>.ucode.

ucode_api_max
    Highest version of uCode API supported by driver.

ucode_api_min
    Lowest version of uCode API supported by driver.

valid_tx_ant
    *undescribed*

valid_rx_ant
    *undescribed*

sku
    *undescribed*

eeprom_ver
    *undescribed*

eeprom_calib_ver
    *undescribed*

mod_params
    *undescribed*

base_params
    *undescribed*

scan_rx_antennas
    *undescribed*

led_mode
    0=blinking, 1=On(RF On)/Off(RF Off)

eeprom_size
    *undescribed*

num_of_queues
    *undescribed*

num_of_ampdu_queues
    *undescribed*

pll_cfg_val
    *undescribed*

set_l0s
    *undescribed*

use_bsm
    *undescribed*

led_compensation
    *undescribed*

chain_noise_num_beacons
    *undescribed*

wd_timeout
    *undescribed*

temperature_kelvin
    *undescribed*

ucode_tracing
    *undescribed*

sensitivity_calib_by_driver
    *undescribed*

chain_noise_calib_by_driver
    *undescribed*

regulatory_bands
    *undescribed*

.. _`il_cfg.description`:

Description
-----------

We enable the driver to be backward compatible wrt API version. The
driver specifies which APIs it supports (with \ ``ucode_api_max``\  being the
highest and \ ``ucode_api_min``\  the lowest). Firmware will only be loaded if
it has a supported API version. The firmware's API version will be
stored in \ ``il_priv``\ , enabling the driver to make runtime changes based
on firmware version used.

For example,
if (IL_UCODE_API(il->ucode_ver) >= 2) {
Driver interacts with Firmware API version >= 2.
} else {
Driver interacts with Firmware API version 1.
}

The ideal usage of this infrastructure is to treat a new ucode API
release as a new hardware revision. That is, through utilizing the
il_hcmd_utils_ops etc. we accommodate different command structures
and flows between hardware versions as well as their API
versions.

.. _`il_clear_driver_stations`:

il_clear_driver_stations
========================

.. c:function:: void il_clear_driver_stations(struct il_priv *il)

    clear knowledge of all stations from driver

    :param il:
        iwl il struct
    :type il: struct il_priv \*

.. _`il_clear_driver_stations.description`:

Description
-----------

This is called during \ :c:func:`il_down`\  to make sure that in the case
we're coming there from a hardware restart mac80211 will be
able to reconfigure stations -- if we're getting there in the
normal down flow then the stations will already be cleared.

.. _`il_sta_id_or_broadcast`:

il_sta_id_or_broadcast
======================

.. c:function:: int il_sta_id_or_broadcast(struct il_priv *il, struct ieee80211_sta *sta)

    return sta_id or broadcast sta

    :param il:
        iwl il
    :type il: struct il_priv \*

    :param sta:
        mac80211 station
    :type sta: struct ieee80211_sta \*

.. _`il_sta_id_or_broadcast.description`:

Description
-----------

In certain circumstances mac80211 passes a station pointer
that may be \ ``NULL``\ , for example during TX or key setup. In
that case, we need to use the broadcast station, so this
inline wraps that pattern.

.. _`il_queue_inc_wrap`:

il_queue_inc_wrap
=================

.. c:function:: int il_queue_inc_wrap(int idx, int n_bd)

    increment queue idx, wrap back to beginning \ ``idx``\  -- current idx \ ``n_bd``\  -- total number of entries in queue (must be power of 2)

    :param idx:
        *undescribed*
    :type idx: int

    :param n_bd:
        *undescribed*
    :type n_bd: int

.. _`il_queue_dec_wrap`:

il_queue_dec_wrap
=================

.. c:function:: int il_queue_dec_wrap(int idx, int n_bd)

    decrement queue idx, wrap back to end \ ``idx``\  -- current idx \ ``n_bd``\  -- total number of entries in queue (must be power of 2)

    :param idx:
        *undescribed*
    :type idx: int

    :param n_bd:
        *undescribed*
    :type n_bd: int

.. _`il_beacon_time_mask_low`:

il_beacon_time_mask_low
=======================

.. c:function:: u32 il_beacon_time_mask_low(struct il_priv *il, u16 tsf_bits)

    mask of lower 32 bit of beacon time \ ``il``\  -- pointer to il_priv data structure \ ``tsf_bits``\  -- number of bits need to shift for masking)

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param tsf_bits:
        *undescribed*
    :type tsf_bits: u16

.. _`il_beacon_time_mask_high`:

il_beacon_time_mask_high
========================

.. c:function:: u32 il_beacon_time_mask_high(struct il_priv *il, u16 tsf_bits)

    mask of higher 32 bit of beacon time \ ``il``\  -- pointer to il_priv data structure \ ``tsf_bits``\  -- number of bits need to shift for masking)

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param tsf_bits:
        *undescribed*
    :type tsf_bits: u16

.. _`il_rb_status`:

struct il_rb_status
===================

.. c:type:: struct il_rb_status

    reseve buffer status host memory mapped FH registers

.. _`il_rb_status.definition`:

Definition
----------

.. code-block:: c

    struct il_rb_status {
        __le16 closed_rb_num;
        __le16 closed_fr_num;
        __le16 finished_rb_num;
        __le16 finished_fr_nam;
        __le32 __unused;
    }

.. _`il_rb_status.members`:

Members
-------

closed_rb_num
    11] - Indicates the idx of the RB which was closed

closed_fr_num
    11] - Indicates the idx of the RX Frame which was closed

finished_rb_num
    11] - Indicates the idx of the current RB
    in which the last frame was written to

finished_fr_nam
    *undescribed*

\__unused
    *undescribed*

.. _`il_tfd_tb`:

struct il_tfd_tb
================

.. c:type:: struct il_tfd_tb


.. _`il_tfd_tb.definition`:

Definition
----------

.. code-block:: c

    struct il_tfd_tb {
        __le32 lo;
        __le16 hi_n_len;
    }

.. _`il_tfd_tb.members`:

Members
-------

lo
    low [31:0] portion of the dma address of TX buffer every even is
    unaligned on 16 bit boundary

hi_n_len
    0-3 [35:32] portion of dma
    4-15 length of the tx buffer

.. _`il_tfd_tb.description`:

Description
-----------

This structure contains dma address and length of transmission address

.. _`il_tfd`:

struct il_tfd
=============

.. c:type:: struct il_tfd


.. _`il_tfd.definition`:

Definition
----------

.. code-block:: c

    struct il_tfd {
        u8 __reserved1[3];
        u8 num_tbs;
        struct il_tfd_tb tbs[IL_NUM_OF_TBS];
        __le32 __pad;
    }

.. _`il_tfd.members`:

Members
-------

\__reserved1
    *undescribed*

num_tbs
    *undescribed*

tbs
    *undescribed*

\__pad
    *undescribed*

.. _`il_tfd.description`:

Description
-----------

Transmit Frame Descriptor (TFD)

\ ````\  \__reserved1[3] reserved
\ ````\  num_tbs 0-4 number of active tbs
5   reserved
6-7 padding (not used)
\ ````\  tbs[20]    transmit frame buffer descriptors
\ ````\  \__pad      padding

Each Tx queue uses a circular buffer of 256 TFDs stored in host DRAM.
Both driver and device share these circular buffers, each of which must be
contiguous 256 TFDs x 128 bytes-per-TFD = 32 KBytes

Driver must indicate the physical address of the base of each
circular buffer via the FH49_MEM_CBBC_QUEUE registers.

Each TFD contains pointer/size information for up to 20 data buffers
in host DRAM.  These buffers collectively contain the (one) frame described
by the TFD.  Each buffer must be a single contiguous block of memory within
itself, but buffers may be scattered in host DRAM.  Each buffer has max size
of (4K - 4).  The concatenates all of a TFD's buffers into a single
Tx frame, up to 8 KBytes in size.

A maximum of 255 (not 256!) TFDs may be on a queue waiting for Tx.

.. _`il_rate_scale_data`:

struct il_rate_scale_data
=========================

.. c:type:: struct il_rate_scale_data

    - tx success history for one rate

.. _`il_rate_scale_data.definition`:

Definition
----------

.. code-block:: c

    struct il_rate_scale_data {
        u64 data;
        s32 success_counter;
        s32 success_ratio;
        s32 counter;
        s32 average_tpt;
        unsigned long stamp;
    }

.. _`il_rate_scale_data.members`:

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

.. _`il_scale_tbl_info`:

struct il_scale_tbl_info
========================

.. c:type:: struct il_scale_tbl_info

    - tx params and success history for all rates

.. _`il_scale_tbl_info.definition`:

Definition
----------

.. code-block:: c

    struct il_scale_tbl_info {
        enum il_table_type lq_type;
        u8 ant_type;
        u8 is_SGI;
        u8 is_ht40;
        u8 is_dup;
        u8 action;
        u8 max_search;
        s32 *expected_tpt;
        u32 current_rate;
        struct il_rate_scale_data win[RATE_COUNT];
    }

.. _`il_scale_tbl_info.members`:

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

.. _`il_scale_tbl_info.description`:

Description
-----------

There are two of these in struct il_lq_sta,
one for "active", and one for "search".

.. _`il_lq_sta`:

struct il_lq_sta
================

.. c:type:: struct il_lq_sta

    - driver's rate scaling ilate structure

.. _`il_lq_sta.definition`:

Definition
----------

.. code-block:: c

    struct il_lq_sta {
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
        s8 max_rate_idx;
        u8 missed_rate_counter;
        struct il_link_quality_cmd lq;
        struct il_scale_tbl_info lq_info[LQ_SIZE];
        struct il_traffic_load load[TID_MAX_LOAD_COUNT];
        u8 tx_agg_tid_en;
    #ifdef CONFIG_MAC80211_DEBUGFS
        struct dentry *rs_sta_dbgfs_scale_table_file;
        struct dentry *rs_sta_dbgfs_stats_table_file;
        struct dentry *rs_sta_dbgfs_rate_scale_data_file;
        struct dentry *rs_sta_dbgfs_tx_agg_tid_en_file;
        u32 dbg_fixed_rate;
    #endif
        struct il_priv *drv;
        int last_txrate_idx;
        u32 last_rate_n_flags;
        u8 is_agg;
    }

.. _`il_lq_sta.members`:

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

.. _`il_lq_sta.description`:

Description
-----------

Pointer to this gets passed back and forth between driver and mac80211.

.. _`il3945_rate_scale_init`:

il3945_rate_scale_init
======================

.. c:function:: void il3945_rate_scale_init(struct ieee80211_hw *hw, s32 sta_id)

    Initialize the rate scale table based on assoc info

    :param hw:
        *undescribed*
    :type hw: struct ieee80211_hw \*

    :param sta_id:
        *undescribed*
    :type sta_id: s32

.. _`il3945_rate_scale_init.description`:

Description
-----------

The specific throughput table used is based on the type of network
the associated with, including A, B, G, and G w/ TGG protection

.. _`il4965_rate_control_register`:

il4965_rate_control_register
============================

.. c:function:: int il4965_rate_control_register( void)

    Register the rate control algorithm callbacks

    :param void:
        no arguments
    :type void: 

.. _`il4965_rate_control_register.description`:

Description
-----------

Since the rate control algorithm is hardware specific, there is no need
or reason to place it as a stand alone module.  The driver can call
il_rate_control_register in order to register the rate control callbacks
with the mac80211 subsystem.  This should be performed prior to calling
ieee80211_register_hw

.. _`il4965_rate_control_unregister`:

il4965_rate_control_unregister
==============================

.. c:function:: void il4965_rate_control_unregister( void)

    Unregister the rate control callbacks

    :param void:
        no arguments
    :type void: 

.. _`il4965_rate_control_unregister.description`:

Description
-----------

This should be called after calling ieee80211_unregister_hw, but before
the driver is unloaded.

.. This file was automatic generated / don't edit.

