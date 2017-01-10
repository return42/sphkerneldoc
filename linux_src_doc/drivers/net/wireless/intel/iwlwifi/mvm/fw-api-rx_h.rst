.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-rx.h

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
    *undescribed*

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
    *undescribed*

assist
    see CSUM_RX_ASSIST\_ above

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
    *undescribed*

RX_RES_PHY_FLAGS_SHORT_PREAMBLE
    true if packet's preamble was short

RX_RES_PHY_FLAGS_NARROW_BAND
    *undescribed*

RX_RES_PHY_FLAGS_ANTENNA
    antenna on which the packet was received

RX_RES_PHY_FLAGS_ANTENNA_POS
    *undescribed*

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
        RX_MPDU_RES_STATUS_PROTECT_FRAME_BIT_CMP,
        RX_MPDU_RES_STATUS_EXT_IV_BIT_CMP,
        RX_MPDU_RES_STATUS_KEY_ID_CMP_BIT,
        RX_MPDU_RES_STATUS_ROBUST_MNG_FRAME,
        RX_MPDU_RES_STATUS_CSUM_DONE,
        RX_MPDU_RES_STATUS_CSUM_OK,
        RX_MPDU_RES_STATUS_HASH_INDEX_MSK,
        RX_MDPU_RES_STATUS_STA_ID_SHIFT,
        RX_MPDU_RES_STATUS_STA_ID_MSK,
        RX_MPDU_RES_STATUS_RRF_KILL,
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
    *undescribed*

RX_MPDU_RES_STATUS_KEY_VALID
    *undescribed*

RX_MPDU_RES_STATUS_KEY_PARAM_OK
    *undescribed*

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
    *undescribed*

RX_MPDU_RES_STATUS_SEC_CCM_CMAC_ENC
    this frame is encrypted using CCM_CMAC

RX_MPDU_RES_STATUS_SEC_ENC_ERR
    this frame couldn't be decrypted

RX_MPDU_RES_STATUS_SEC_ENC_MSK
    bitmask of the encryption algorithm

RX_MPDU_RES_STATUS_DEC_DONE
    this frame has been successfully decrypted

RX_MPDU_RES_STATUS_PROTECT_FRAME_BIT_CMP
    *undescribed*

RX_MPDU_RES_STATUS_EXT_IV_BIT_CMP
    *undescribed*

RX_MPDU_RES_STATUS_KEY_ID_CMP_BIT
    *undescribed*

RX_MPDU_RES_STATUS_ROBUST_MNG_FRAME
    this frame is an 11w management frame

RX_MPDU_RES_STATUS_CSUM_DONE
    checksum was done by the hw

RX_MPDU_RES_STATUS_CSUM_OK
    checksum found no errors

RX_MPDU_RES_STATUS_HASH_INDEX_MSK
    *undescribed*

RX_MDPU_RES_STATUS_STA_ID_SHIFT
    *undescribed*

RX_MPDU_RES_STATUS_STA_ID_MSK
    *undescribed*

RX_MPDU_RES_STATUS_RRF_KILL
    *undescribed*

RX_MPDU_RES_STATUS_FILTERING_MSK
    *undescribed*

RX_MPDU_RES_STATUS2_FILTERING_MSK
    *undescribed*

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
    the new powersave state, see IWL_MVM_PM_EVENT\_ above

.. This file was automatic generated / don't edit.

