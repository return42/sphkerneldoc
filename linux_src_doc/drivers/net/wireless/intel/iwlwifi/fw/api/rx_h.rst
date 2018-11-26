.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/rx.h

.. _`iwl_rx_phy_info`:

struct iwl_rx_phy_info
======================

.. c:type:: struct iwl_rx_phy_info

    phy info (REPLY_RX_PHY_CMD = 0xc0)

.. _`iwl_rx_phy_info.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_phy_info {
        u8 non_cfg_phy_cnt;
        u8 cfg_phy_cnt;
        u8 stat_id;
        u8 reserved1;
        __le32 system_timestamp;
        __le64 timestamp;
        __le32 beacon_time_stamp;
        __le16 phy_flags;
        __le16 channel;
        __le32 non_cfg_phy[IWL_RX_INFO_PHY_CNT];
        __le32 rate_n_flags;
        __le32 byte_count;
        u8 mac_active_msk;
        u8 mac_context_info;
        __le16 frame_time;
    }

.. _`iwl_rx_phy_info.members`:

Members
-------

non_cfg_phy_cnt
    non configurable DSP phy data byte count

cfg_phy_cnt
    configurable DSP phy data byte count

stat_id
    configurable DSP phy data set ID

reserved1
    reserved

system_timestamp
    GP2  at on air rise

timestamp
    TSF at on air rise

beacon_time_stamp
    beacon at on-air rise

phy_flags
    general phy flags: band, modulation, ...

channel
    channel number

non_cfg_phy
    for various implementations of non_cfg_phy

rate_n_flags
    RATE_MCS\_\*

byte_count
    frame's byte-count

mac_active_msk
    what MACs were active when the frame was received

mac_context_info
    additional info on the context in which the frame was
    received as defined in \ :c:type:`enum iwl_mac_context_info <iwl_mac_context_info>`\ 

frame_time
    frame's time on the air, based on byte count and frame rate
    calculation

.. _`iwl_rx_phy_info.description`:

Description
-----------

Before each Rx, the device sends this data. It contains PHY information
about the reception of the packet.

.. _`iwl_rx_mpdu_res_start`:

struct iwl_rx_mpdu_res_start
============================

.. c:type:: struct iwl_rx_mpdu_res_start

    phy info

.. _`iwl_rx_mpdu_res_start.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_mpdu_res_start {
        __le16 byte_count;
        __le16 assist;
    }

.. _`iwl_rx_mpdu_res_start.members`:

Members
-------

byte_count
    byte count of the frame

assist
    see \ :c:type:`enum iwl_csum_rx_assist_info <iwl_csum_rx_assist_info>`\ 

.. _`iwl_rx_phy_flags`:

enum iwl_rx_phy_flags
=====================

.. c:type:: enum iwl_rx_phy_flags

    to parse \ ``iwl_rx_phy_info``\  phy_flags

.. _`iwl_rx_phy_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_rx_phy_flags {
        RX_RES_PHY_FLAGS_BAND_24,
        RX_RES_PHY_FLAGS_MOD_CCK,
        RX_RES_PHY_FLAGS_SHORT_PREAMBLE,
        RX_RES_PHY_FLAGS_NARROW_BAND,
        RX_RES_PHY_FLAGS_ANTENNA,
        RX_RES_PHY_FLAGS_ANTENNA_POS,
        RX_RES_PHY_FLAGS_AGG,
        RX_RES_PHY_FLAGS_OFDM_HT,
        RX_RES_PHY_FLAGS_OFDM_GF,
        RX_RES_PHY_FLAGS_OFDM_VHT
    };

.. _`iwl_rx_phy_flags.constants`:

Constants
---------

RX_RES_PHY_FLAGS_BAND_24
    true if the packet was received on 2.4 band

RX_RES_PHY_FLAGS_MOD_CCK
    modulation is CCK

RX_RES_PHY_FLAGS_SHORT_PREAMBLE
    true if packet's preamble was short

RX_RES_PHY_FLAGS_NARROW_BAND
    narrow band (<20 MHz) receive

RX_RES_PHY_FLAGS_ANTENNA
    antenna on which the packet was received

RX_RES_PHY_FLAGS_ANTENNA_POS
    antenna bit position

RX_RES_PHY_FLAGS_AGG
    set if the packet was part of an A-MPDU

RX_RES_PHY_FLAGS_OFDM_HT
    The frame was an HT frame

RX_RES_PHY_FLAGS_OFDM_GF
    The frame used GF preamble

RX_RES_PHY_FLAGS_OFDM_VHT
    The frame was a VHT frame

.. _`iwl_mvm_rx_status`:

enum iwl_mvm_rx_status
======================

.. c:type:: enum iwl_mvm_rx_status

    written by fw for each Rx packet

.. _`iwl_mvm_rx_status.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_rx_status {
        RX_MPDU_RES_STATUS_CRC_OK,
        RX_MPDU_RES_STATUS_OVERRUN_OK,
        RX_MPDU_RES_STATUS_SRC_STA_FOUND,
        RX_MPDU_RES_STATUS_KEY_VALID,
        RX_MPDU_RES_STATUS_KEY_PARAM_OK,
        RX_MPDU_RES_STATUS_ICV_OK,
        RX_MPDU_RES_STATUS_MIC_OK,
        RX_MPDU_RES_STATUS_TTAK_OK,
        RX_MPDU_RES_STATUS_MNG_FRAME_REPLAY_ERR,
        RX_MPDU_RES_STATUS_SEC_NO_ENC,
        RX_MPDU_RES_STATUS_SEC_WEP_ENC,
        RX_MPDU_RES_STATUS_SEC_CCM_ENC,
        RX_MPDU_RES_STATUS_SEC_TKIP_ENC,
        RX_MPDU_RES_STATUS_SEC_EXT_ENC,
        RX_MPDU_RES_STATUS_SEC_CCM_CMAC_ENC,
        RX_MPDU_RES_STATUS_SEC_ENC_ERR,
        RX_MPDU_RES_STATUS_SEC_ENC_MSK,
        RX_MPDU_RES_STATUS_DEC_DONE,
        RX_MPDU_RES_STATUS_EXT_IV_BIT_CMP,
        RX_MPDU_RES_STATUS_KEY_ID_CMP_BIT,
        RX_MPDU_RES_STATUS_ROBUST_MNG_FRAME,
        RX_MPDU_RES_STATUS_CSUM_DONE,
        RX_MPDU_RES_STATUS_CSUM_OK,
        RX_MDPU_RES_STATUS_STA_ID_SHIFT,
        RX_MPDU_RES_STATUS_STA_ID_MSK,
        RX_MPDU_RES_STATUS_FILTERING_MSK,
        RX_MPDU_RES_STATUS2_FILTERING_MSK
    };

.. _`iwl_mvm_rx_status.constants`:

Constants
---------

RX_MPDU_RES_STATUS_CRC_OK
    CRC is fine

RX_MPDU_RES_STATUS_OVERRUN_OK
    there was no RXE overflow

RX_MPDU_RES_STATUS_SRC_STA_FOUND
    station was found

RX_MPDU_RES_STATUS_KEY_VALID
    key was valid

RX_MPDU_RES_STATUS_KEY_PARAM_OK
    key parameters were usable

RX_MPDU_RES_STATUS_ICV_OK
    ICV is fine, if not, the packet is destroyed

RX_MPDU_RES_STATUS_MIC_OK
    used for CCM alg only. TKIP MIC is checked
    in the driver.

RX_MPDU_RES_STATUS_TTAK_OK
    TTAK is fine

RX_MPDU_RES_STATUS_MNG_FRAME_REPLAY_ERR
    valid for alg = CCM_CMAC or
    alg = CCM only. Checks replay attack for 11w frames. Relevant only if
    \ ``RX_MPDU_RES_STATUS_ROBUST_MNG_FRAME``\  is set.

RX_MPDU_RES_STATUS_SEC_NO_ENC
    this frame is not encrypted

RX_MPDU_RES_STATUS_SEC_WEP_ENC
    this frame is encrypted using WEP

RX_MPDU_RES_STATUS_SEC_CCM_ENC
    this frame is encrypted using CCM

RX_MPDU_RES_STATUS_SEC_TKIP_ENC
    this frame is encrypted using TKIP

RX_MPDU_RES_STATUS_SEC_EXT_ENC
    this frame is encrypted using extension
    algorithm

RX_MPDU_RES_STATUS_SEC_CCM_CMAC_ENC
    this frame is encrypted using CCM_CMAC

RX_MPDU_RES_STATUS_SEC_ENC_ERR
    this frame couldn't be decrypted

RX_MPDU_RES_STATUS_SEC_ENC_MSK
    bitmask of the encryption algorithm

RX_MPDU_RES_STATUS_DEC_DONE
    this frame has been successfully decrypted

RX_MPDU_RES_STATUS_EXT_IV_BIT_CMP
    extended IV (set with TKIP)

RX_MPDU_RES_STATUS_KEY_ID_CMP_BIT
    key ID comparison done

RX_MPDU_RES_STATUS_ROBUST_MNG_FRAME
    this frame is an 11w management frame

RX_MPDU_RES_STATUS_CSUM_DONE
    checksum was done by the hw

RX_MPDU_RES_STATUS_CSUM_OK
    checksum found no errors

RX_MDPU_RES_STATUS_STA_ID_SHIFT
    station ID bit shift

RX_MPDU_RES_STATUS_STA_ID_MSK
    station ID mask

RX_MPDU_RES_STATUS_FILTERING_MSK
    filter status

RX_MPDU_RES_STATUS2_FILTERING_MSK
    filter status 2

.. _`iwl_rx_mpdu_desc_v1`:

struct iwl_rx_mpdu_desc_v1
==========================

.. c:type:: struct iwl_rx_mpdu_desc_v1

    RX MPDU descriptor

.. _`iwl_rx_mpdu_desc_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_mpdu_desc_v1 {
        union {
            __le32 rss_hash;
            __le32 sigb_common0;
        } ;
        union {
            __le32 filter_match;
            __le32 sigb_common1;
        } ;
        __le32 rate_n_flags;
        u8 energy_a;
        u8 energy_b;
        u8 channel;
        u8 mac_context;
        __le32 gp2_on_air_rise;
        union {
            __le64 tsf_on_air_rise;
            __le64 he_phy_data;
        } ;
    }

.. _`iwl_rx_mpdu_desc_v1.members`:

Members
-------

{unnamed_union}
    anonymous

rss_hash
    RSS hash value

sigb_common0
    for HE sniffer, HE-SIG-B common part 0

{unnamed_union}
    anonymous

filter_match
    filter match value

sigb_common1
    for HE sniffer, HE-SIG-B common part 1

rate_n_flags
    RX rate/flags encoding

energy_a
    energy chain A

energy_b
    energy chain B

channel
    channel number

mac_context
    MAC context mask

gp2_on_air_rise
    GP2 timer value on air rise (INA)

{unnamed_union}
    anonymous

tsf_on_air_rise
    TSF value on air rise (INA), only valid if
    \ ``IWL_RX_MPDU_PHY_TSF_OVERLOAD``\  isn't set

he_phy_data
    HE PHY data, see \ :c:type:`enum iwl_rx_he_phy <iwl_rx_he_phy>`\ , valid
    only if \ ``IWL_RX_MPDU_PHY_TSF_OVERLOAD``\  is set

.. _`iwl_rx_mpdu_desc_v3`:

struct iwl_rx_mpdu_desc_v3
==========================

.. c:type:: struct iwl_rx_mpdu_desc_v3

    RX MPDU descriptor

.. _`iwl_rx_mpdu_desc_v3.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_mpdu_desc_v3 {
        union {
            __le32 filter_match;
            __le32 sigb_common0;
        } ;
        union {
            __le32 rss_hash;
            __le32 sigb_common1;
        } ;
        __le32 partial_hash;
        __le32 raw_xsum;
        __le32 rate_n_flags;
        u8 energy_a;
        u8 energy_b;
        u8 channel;
        u8 mac_context;
        __le32 gp2_on_air_rise;
        union {
            __le64 tsf_on_air_rise;
            __le64 he_phy_data;
        } ;
        __le32 reserved[2];
    }

.. _`iwl_rx_mpdu_desc_v3.members`:

Members
-------

{unnamed_union}
    anonymous

filter_match
    filter match value

sigb_common0
    for HE sniffer, HE-SIG-B common part 0

{unnamed_union}
    anonymous

rss_hash
    RSS hash value

sigb_common1
    for HE sniffer, HE-SIG-B common part 1

partial_hash
    31:0 ip/tcp header hash     w/o some fields (such as IP SRC addr)

raw_xsum
    raw xsum value

rate_n_flags
    RX rate/flags encoding

energy_a
    energy chain A

energy_b
    energy chain B

channel
    channel number

mac_context
    MAC context mask

gp2_on_air_rise
    GP2 timer value on air rise (INA)

{unnamed_union}
    anonymous

tsf_on_air_rise
    TSF value on air rise (INA), only valid if
    \ ``IWL_RX_MPDU_PHY_TSF_OVERLOAD``\  isn't set

he_phy_data
    HE PHY data, see \ :c:type:`enum iwl_rx_he_phy <iwl_rx_he_phy>`\ , valid
    only if \ ``IWL_RX_MPDU_PHY_TSF_OVERLOAD``\  is set

reserved
    reserved

.. _`iwl_rx_mpdu_desc`:

struct iwl_rx_mpdu_desc
=======================

.. c:type:: struct iwl_rx_mpdu_desc

    RX MPDU descriptor

.. _`iwl_rx_mpdu_desc.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rx_mpdu_desc {
        __le16 mpdu_len;
        u8 mac_flags1;
        u8 mac_flags2;
        u8 amsdu_info;
        __le16 phy_info;
        u8 mac_phy_idx;
        __le16 raw_csum;
        union {
            __le16 l3l4_flags;
            __le16 sigb_common2;
        } ;
        __le16 status;
        u8 hash_filter;
        u8 sta_id_flags;
        __le32 reorder_data;
        union {
            struct iwl_rx_mpdu_desc_v1 v1;
            struct iwl_rx_mpdu_desc_v3 v3;
        } ;
    }

.. _`iwl_rx_mpdu_desc.members`:

Members
-------

mpdu_len
    MPDU length

mac_flags1
    \ :c:type:`enum iwl_rx_mpdu_mac_flags1 <iwl_rx_mpdu_mac_flags1>`\ 

mac_flags2
    \ :c:type:`enum iwl_rx_mpdu_mac_flags2 <iwl_rx_mpdu_mac_flags2>`\ 

amsdu_info
    \ :c:type:`enum iwl_rx_mpdu_amsdu_info <iwl_rx_mpdu_amsdu_info>`\ 

phy_info
    \ :c:type:`enum iwl_rx_mpdu_phy_info <iwl_rx_mpdu_phy_info>`\ 

mac_phy_idx
    MAC/PHY index

raw_csum
    raw checksum (alledgedly unreliable)

{unnamed_union}
    anonymous

l3l4_flags
    \ :c:type:`enum iwl_rx_l3l4_flags <iwl_rx_l3l4_flags>`\ 

sigb_common2
    for HE sniffer, HE-SIG-B common part 2

status
    \ :c:type:`enum iwl_rx_mpdu_status <iwl_rx_mpdu_status>`\ 

hash_filter
    hash filter value

sta_id_flags
    \ :c:type:`enum iwl_rx_mpdu_sta_id_flags <iwl_rx_mpdu_sta_id_flags>`\ 

reorder_data
    \ :c:type:`enum iwl_rx_mpdu_reorder_data <iwl_rx_mpdu_reorder_data>`\ 

{unnamed_union}
    anonymous

v1
    *undescribed*

v3
    *undescribed*

.. _`iwl_completion_desc_transfer_status`:

enum iwl_completion_desc_transfer_status
========================================

.. c:type:: enum iwl_completion_desc_transfer_status

    transfer status (bits 1-3)

.. _`iwl_completion_desc_transfer_status.definition`:

Definition
----------

.. code-block:: c

    enum iwl_completion_desc_transfer_status {
        IWL_CD_STTS_UNUSED,
        IWL_CD_STTS_UNUSED_2,
        IWL_CD_STTS_END_TRANSFER,
        IWL_CD_STTS_OVERFLOW,
        IWL_CD_STTS_ABORTED,
        IWL_CD_STTS_ERROR
    };

.. _`iwl_completion_desc_transfer_status.constants`:

Constants
---------

IWL_CD_STTS_UNUSED
    unused

IWL_CD_STTS_UNUSED_2
    unused

IWL_CD_STTS_END_TRANSFER
    successful transfer complete.
    In sniffer mode, when split is used, set in last CD completion. (RX)

IWL_CD_STTS_OVERFLOW
    In sniffer mode, when using split - used for
    all CD completion. (RX)

IWL_CD_STTS_ABORTED
    CR abort / close flow. (RX)

IWL_CD_STTS_ERROR
    general error (RX)

.. _`iwl_completion_desc_wifi_status`:

enum iwl_completion_desc_wifi_status
====================================

.. c:type:: enum iwl_completion_desc_wifi_status

    wifi status (bits 4-7)

.. _`iwl_completion_desc_wifi_status.definition`:

Definition
----------

.. code-block:: c

    enum iwl_completion_desc_wifi_status {
        IWL_CD_STTS_VALID,
        IWL_CD_STTS_FCS_ERR,
        IWL_CD_STTS_SEC_KEY_ERR,
        IWL_CD_STTS_DECRYPTION_ERR,
        IWL_CD_STTS_DUP,
        IWL_CD_STTS_ICV_MIC_ERR,
        IWL_CD_STTS_INTERNAL_SNAP_ERR,
        IWL_CD_STTS_SEC_PORT_FAIL,
        IWL_CD_STTS_BA_OLD_SN,
        IWL_CD_STTS_QOS_NULL,
        IWL_CD_STTS_MAC_HDR_ERR,
        IWL_CD_STTS_MAX_RETRANS,
        IWL_CD_STTS_EX_LIFETIME,
        IWL_CD_STTS_NOT_USED,
        IWL_CD_STTS_REPLAY_ERR
    };

.. _`iwl_completion_desc_wifi_status.constants`:

Constants
---------

IWL_CD_STTS_VALID
    the packet is valid (RX)

IWL_CD_STTS_FCS_ERR
    frame check sequence error (RX)

IWL_CD_STTS_SEC_KEY_ERR
    error handling the security key of rx (RX)

IWL_CD_STTS_DECRYPTION_ERR
    error decrypting the frame (RX)

IWL_CD_STTS_DUP
    duplicate packet (RX)

IWL_CD_STTS_ICV_MIC_ERR
    MIC error (RX)

IWL_CD_STTS_INTERNAL_SNAP_ERR
    problems removing the snap (RX)

IWL_CD_STTS_SEC_PORT_FAIL
    security port fail (RX)

IWL_CD_STTS_BA_OLD_SN
    block ack received old SN (RX)

IWL_CD_STTS_QOS_NULL
    QoS null packet (RX)

IWL_CD_STTS_MAC_HDR_ERR
    MAC header conversion error (RX)

IWL_CD_STTS_MAX_RETRANS
    reached max number of retransmissions (TX)

IWL_CD_STTS_EX_LIFETIME
    exceeded lifetime (TX)

IWL_CD_STTS_NOT_USED
    completed but not used (RX)

IWL_CD_STTS_REPLAY_ERR
    pn check failed, replay error (RX)

.. _`iwl_rss_config_cmd`:

struct iwl_rss_config_cmd
=========================

.. c:type:: struct iwl_rss_config_cmd

    RSS (Receive Side Scaling) configuration

.. _`iwl_rss_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rss_config_cmd {
        __le32 flags;
        u8 hash_mask;
        u8 reserved[3];
        __le32 secret_key[IWL_RSS_HASH_KEY_CNT];
        u8 indirection_table[IWL_RSS_INDIRECTION_TABLE_SIZE];
    }

.. _`iwl_rss_config_cmd.members`:

Members
-------

flags
    1 - enable, 0 - disable

hash_mask
    Type of RSS to use. Values are from \ ``iwl_rss_hash_func_en``\ 

reserved
    reserved

secret_key
    320 bit input of random key configuration from driver

indirection_table
    indirection table

.. _`iwl_rxq_sync_cmd`:

struct iwl_rxq_sync_cmd
=======================

.. c:type:: struct iwl_rxq_sync_cmd

    RXQ notification trigger

.. _`iwl_rxq_sync_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rxq_sync_cmd {
        __le32 flags;
        __le32 rxq_mask;
        __le32 count;
        u8 payload[];
    }

.. _`iwl_rxq_sync_cmd.members`:

Members
-------

flags
    flags of the notification. bit 0:3 are the sender queue

rxq_mask
    rx queues to send the notification on

count
    number of bytes in payload, should be DWORD aligned

payload
    data to send to rx queues

.. _`iwl_rxq_sync_notification`:

struct iwl_rxq_sync_notification
================================

.. c:type:: struct iwl_rxq_sync_notification

    Notification triggered by RXQ sync command

.. _`iwl_rxq_sync_notification.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rxq_sync_notification {
        __le32 count;
        u8 payload[];
    }

.. _`iwl_rxq_sync_notification.members`:

Members
-------

count
    number of bytes in payload

payload
    data to send to rx queues

.. _`iwl_mvm_rxq_notif_type`:

enum iwl_mvm_rxq_notif_type
===========================

.. c:type:: enum iwl_mvm_rxq_notif_type

    Internal message identifier

.. _`iwl_mvm_rxq_notif_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_rxq_notif_type {
        IWL_MVM_RXQ_EMPTY,
        IWL_MVM_RXQ_NOTIF_DEL_BA
    };

.. _`iwl_mvm_rxq_notif_type.constants`:

Constants
---------

IWL_MVM_RXQ_EMPTY
    empty sync notification

IWL_MVM_RXQ_NOTIF_DEL_BA
    notify RSS queues of delBA

.. _`iwl_mvm_internal_rxq_notif`:

struct iwl_mvm_internal_rxq_notif
=================================

.. c:type:: struct iwl_mvm_internal_rxq_notif

    Internal representation of the data sent in \ :c:type:`struct iwl_rxq_sync_cmd <iwl_rxq_sync_cmd>`\ . Should be DWORD aligned. FW is agnostic to the payload, so there are no endianity requirements.

.. _`iwl_mvm_internal_rxq_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_internal_rxq_notif {
        u16 type;
        u16 sync;
        u32 cookie;
        u8 data[];
    }

.. _`iwl_mvm_internal_rxq_notif.members`:

Members
-------

type
    value from \ :c:type:`struct iwl_mvm_rxq_notif_type <iwl_mvm_rxq_notif_type>`\ 

sync
    ctrl path is waiting for all notifications to be received

cookie
    internal cookie to identify old notifications

data
    payload

.. _`iwl_mvm_pm_event`:

enum iwl_mvm_pm_event
=====================

.. c:type:: enum iwl_mvm_pm_event

    type of station PM event

.. _`iwl_mvm_pm_event.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_pm_event {
        IWL_MVM_PM_EVENT_AWAKE,
        IWL_MVM_PM_EVENT_ASLEEP,
        IWL_MVM_PM_EVENT_UAPSD,
        IWL_MVM_PM_EVENT_PS_POLL
    };

.. _`iwl_mvm_pm_event.constants`:

Constants
---------

IWL_MVM_PM_EVENT_AWAKE
    station woke up

IWL_MVM_PM_EVENT_ASLEEP
    station went to sleep

IWL_MVM_PM_EVENT_UAPSD
    station sent uAPSD trigger

IWL_MVM_PM_EVENT_PS_POLL
    station sent PS-Poll

.. _`iwl_mvm_pm_state_notification`:

struct iwl_mvm_pm_state_notification
====================================

.. c:type:: struct iwl_mvm_pm_state_notification

    station PM state notification

.. _`iwl_mvm_pm_state_notification.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_pm_state_notification {
        u8 sta_id;
        u8 type;
    }

.. _`iwl_mvm_pm_state_notification.members`:

Members
-------

sta_id
    station ID of the station changing state

type
    the new powersave state, see \ :c:type:`enum iwl_mvm_pm_event <iwl_mvm_pm_event>`\ 

.. _`iwl_ba_window_status_notif`:

struct iwl_ba_window_status_notif
=================================

.. c:type:: struct iwl_ba_window_status_notif

    reordering window's status notification

.. _`iwl_ba_window_status_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ba_window_status_notif {
        __le64 bitmap[BA_WINDOW_STREAMS_MAX];
        __le16 ra_tid[BA_WINDOW_STREAMS_MAX];
        __le32 start_seq_num[BA_WINDOW_STREAMS_MAX];
        __le16 mpdu_rx_count[BA_WINDOW_STREAMS_MAX];
    }

.. _`iwl_ba_window_status_notif.members`:

Members
-------

bitmap
    bitmap of received frames [start_seq_num + 0]..[start_seq_num + 63]

ra_tid
    bit 3:0 - TID, bit 8:4 - STA_ID, bit 9 - valid

start_seq_num
    the start sequence number of the bitmap

mpdu_rx_count
    the number of received MPDUs since entering D0i3

.. _`iwl_rfh_queue_data`:

struct iwl_rfh_queue_data
=========================

.. c:type:: struct iwl_rfh_queue_data

    RX queue configuration

.. _`iwl_rfh_queue_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rfh_queue_data {
        u8 q_num;
        u8 enable;
        __le16 reserved;
        __le64 urbd_stts_wrptr;
        __le64 fr_bd_cb;
        __le64 ur_bd_cb;
        __le32 fr_bd_wid;
    }

.. _`iwl_rfh_queue_data.members`:

Members
-------

q_num
    Q num

enable
    enable queue

reserved
    alignment

urbd_stts_wrptr
    DMA address of urbd_stts_wrptr

fr_bd_cb
    DMA address of freeRB table

ur_bd_cb
    DMA address of used RB table

fr_bd_wid
    Initial index of the free table

.. _`iwl_rfh_queue_config`:

struct iwl_rfh_queue_config
===========================

.. c:type:: struct iwl_rfh_queue_config

    RX queue configuration

.. _`iwl_rfh_queue_config.definition`:

Definition
----------

.. code-block:: c

    struct iwl_rfh_queue_config {
        u8 num_queues;
        u8 reserved[3];
        struct iwl_rfh_queue_data data[];
    }

.. _`iwl_rfh_queue_config.members`:

Members
-------

num_queues
    number of queues configured

reserved
    alignment

data
    DMA addresses per-queue

.. This file was automatic generated / don't edit.

