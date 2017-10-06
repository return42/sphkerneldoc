.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/file.h

.. _`iwl_ucode_tlv_flag`:

enum iwl_ucode_tlv_flag
=======================

.. c:type:: enum iwl_ucode_tlv_flag

    ucode API flags

.. _`iwl_ucode_tlv_flag.definition`:

Definition
----------

.. code-block:: c

    enum iwl_ucode_tlv_flag {
        IWL_UCODE_TLV_FLAGS_PAN,
        IWL_UCODE_TLV_FLAGS_NEWSCAN,
        IWL_UCODE_TLV_FLAGS_MFP,
        IWL_UCODE_TLV_FLAGS_SHORT_BL,
        IWL_UCODE_TLV_FLAGS_D3_6_IPV6_ADDRS,
        IWL_UCODE_TLV_FLAGS_NO_BASIC_SSID,
        IWL_UCODE_TLV_FLAGS_NEW_NSOFFL_SMALL,
        IWL_UCODE_TLV_FLAGS_NEW_NSOFFL_LARGE,
        IWL_UCODE_TLV_FLAGS_UAPSD_SUPPORT,
        IWL_UCODE_TLV_FLAGS_EBS_SUPPORT,
        IWL_UCODE_TLV_FLAGS_P2P_PS_UAPSD,
        IWL_UCODE_TLV_FLAGS_BCAST_FILTERING
    };

.. _`iwl_ucode_tlv_flag.constants`:

Constants
---------

IWL_UCODE_TLV_FLAGS_PAN
    This is PAN capable microcode; this previously
    was a separate TLV but moved here to save space.

IWL_UCODE_TLV_FLAGS_NEWSCAN
    new uCode scan behavior on hidden SSID,
    treats good CRC threshold as a boolean

IWL_UCODE_TLV_FLAGS_MFP
    This uCode image supports MFP (802.11w).

IWL_UCODE_TLV_FLAGS_SHORT_BL
    16 entries of black list instead of 64 in scan
    offload profile config command.

IWL_UCODE_TLV_FLAGS_D3_6_IPV6_ADDRS
    D3 image supports up to six
    (rather than two) IPv6 addresses

IWL_UCODE_TLV_FLAGS_NO_BASIC_SSID
    not sending a probe with the SSID element
    from the probe request template.

IWL_UCODE_TLV_FLAGS_NEW_NSOFFL_SMALL
    new NS offload (small version)

IWL_UCODE_TLV_FLAGS_NEW_NSOFFL_LARGE
    new NS offload (large version)

IWL_UCODE_TLV_FLAGS_UAPSD_SUPPORT
    General support for uAPSD

IWL_UCODE_TLV_FLAGS_EBS_SUPPORT
    this uCode image supports EBS.

IWL_UCODE_TLV_FLAGS_P2P_PS_UAPSD
    P2P client supports uAPSD power save

IWL_UCODE_TLV_FLAGS_BCAST_FILTERING
    uCode supports broadcast filtering.

.. _`iwl_ucode_tlv_api`:

enum iwl_ucode_tlv_api
======================

.. c:type:: enum iwl_ucode_tlv_api

    ucode api

.. _`iwl_ucode_tlv_api.definition`:

Definition
----------

.. code-block:: c

    enum iwl_ucode_tlv_api {
        IWL_UCODE_TLV_API_FRAGMENTED_SCAN,
        IWL_UCODE_TLV_API_WIFI_MCC_UPDATE,
        IWL_UCODE_TLV_API_LQ_SS_PARAMS,
        IWL_UCODE_TLV_API_NEW_VERSION,
        IWL_UCODE_TLV_API_SCAN_TSF_REPORT,
        IWL_UCODE_TLV_API_TKIP_MIC_KEYS,
        IWL_UCODE_TLV_API_STA_TYPE,
        IWL_UCODE_TLV_API_NAN2_VER2,
        IWL_UCODE_TLV_API_NEW_BEACON_TEMPLATE,
        IWL_UCODE_TLV_API_NEW_RX_STATS,
        IWL_UCODE_TLV_API_COEX_ATS_EXTERNAL,
        NUM_IWL_UCODE_TLV_API
    };

.. _`iwl_ucode_tlv_api.constants`:

Constants
---------

IWL_UCODE_TLV_API_FRAGMENTED_SCAN
    This ucode supports active dwell time
    longer than the passive one, which is essential for fragmented scan.

IWL_UCODE_TLV_API_WIFI_MCC_UPDATE
    ucode supports MCC updates with source.

IWL_UCODE_TLV_API_LQ_SS_PARAMS
    Configure STBC/BFER via LQ CMD ss_params

IWL_UCODE_TLV_API_NEW_VERSION
    new versioning format

IWL_UCODE_TLV_API_SCAN_TSF_REPORT
    Scan start time reported in scan
    iteration complete notification, and the timestamp reported for RX
    received during scan, are reported in TSF of the mac specified in the
    scan request.

IWL_UCODE_TLV_API_TKIP_MIC_KEYS
    This ucode supports version 2 of
    ADD_MODIFY_STA_KEY_API_S_VER_2.

IWL_UCODE_TLV_API_STA_TYPE
    This ucode supports station type assignement.

IWL_UCODE_TLV_API_NAN2_VER2
    This ucode supports NAN API version 2

IWL_UCODE_TLV_API_NEW_BEACON_TEMPLATE
    *undescribed*

IWL_UCODE_TLV_API_NEW_RX_STATS
    should new RX STATISTICS API be used

IWL_UCODE_TLV_API_COEX_ATS_EXTERNAL
    *undescribed*

NUM_IWL_UCODE_TLV_API
    number of bits used

.. _`iwl_ucode_tlv_capa`:

enum iwl_ucode_tlv_capa
=======================

.. c:type:: enum iwl_ucode_tlv_capa

    ucode capabilities

.. _`iwl_ucode_tlv_capa.definition`:

Definition
----------

.. code-block:: c

    enum iwl_ucode_tlv_capa {
        IWL_UCODE_TLV_CAPA_D0I3_SUPPORT,
        IWL_UCODE_TLV_CAPA_LAR_SUPPORT,
        IWL_UCODE_TLV_CAPA_UMAC_SCAN,
        IWL_UCODE_TLV_CAPA_BEAMFORMER,
        IWL_UCODE_TLV_CAPA_TOF_SUPPORT,
        IWL_UCODE_TLV_CAPA_TDLS_SUPPORT,
        IWL_UCODE_TLV_CAPA_TXPOWER_INSERTION_SUPPORT,
        IWL_UCODE_TLV_CAPA_DS_PARAM_SET_IE_SUPPORT,
        IWL_UCODE_TLV_CAPA_WFA_TPC_REP_IE_SUPPORT,
        IWL_UCODE_TLV_CAPA_QUIET_PERIOD_SUPPORT,
        IWL_UCODE_TLV_CAPA_DQA_SUPPORT,
        IWL_UCODE_TLV_CAPA_TDLS_CHANNEL_SWITCH,
        IWL_UCODE_TLV_CAPA_CNSLDTD_D3_D0_IMG,
        IWL_UCODE_TLV_CAPA_HOTSPOT_SUPPORT,
        IWL_UCODE_TLV_CAPA_DC2DC_CONFIG_SUPPORT,
        IWL_UCODE_TLV_CAPA_CSUM_SUPPORT,
        IWL_UCODE_TLV_CAPA_RADIO_BEACON_STATS,
        IWL_UCODE_TLV_CAPA_P2P_SCM_UAPSD,
        IWL_UCODE_TLV_CAPA_BT_COEX_PLCR,
        IWL_UCODE_TLV_CAPA_LAR_MULTI_MCC,
        IWL_UCODE_TLV_CAPA_BT_COEX_RRC,
        IWL_UCODE_TLV_CAPA_GSCAN_SUPPORT,
        IWL_UCODE_TLV_CAPA_STA_PM_NOTIF,
        IWL_UCODE_TLV_CAPA_BINDING_CDB_SUPPORT,
        IWL_UCODE_TLV_CAPA_CDB_SUPPORT,
        IWL_UCODE_TLV_CAPA_D0I3_END_FIRST,
        IWL_UCODE_TLV_CAPA_EXTENDED_DTS_MEASURE,
        IWL_UCODE_TLV_CAPA_SHORT_PM_TIMEOUTS,
        IWL_UCODE_TLV_CAPA_BT_MPLUT_SUPPORT,
        IWL_UCODE_TLV_CAPA_MULTI_QUEUE_RX_SUPPORT,
        IWL_UCODE_TLV_CAPA_CSA_AND_TBTT_OFFLOAD,
        IWL_UCODE_TLV_CAPA_BEACON_ANT_SELECTION,
        IWL_UCODE_TLV_CAPA_BEACON_STORING,
        IWL_UCODE_TLV_CAPA_LAR_SUPPORT_V2,
        IWL_UCODE_TLV_CAPA_CT_KILL_BY_FW,
        IWL_UCODE_TLV_CAPA_TEMP_THS_REPORT_SUPPORT,
        IWL_UCODE_TLV_CAPA_CTDP_SUPPORT,
        IWL_UCODE_TLV_CAPA_USNIFFER_UNIFIED,
        IWL_UCODE_TLV_CAPA_EXTEND_SHARED_MEM_CFG,
        IWL_UCODE_TLV_CAPA_LQM_SUPPORT,
        IWL_UCODE_TLV_CAPA_TX_POWER_ACK,
        IWL_UCODE_TLV_CAPA_LED_CMD_SUPPORT,
        IWL_UCODE_TLV_CAPA_MLME_OFFLOAD,
        NUM_IWL_UCODE_TLV_CAPA
    };

.. _`iwl_ucode_tlv_capa.constants`:

Constants
---------

IWL_UCODE_TLV_CAPA_D0I3_SUPPORT
    supports D0i3

IWL_UCODE_TLV_CAPA_LAR_SUPPORT
    supports Location Aware Regulatory

IWL_UCODE_TLV_CAPA_UMAC_SCAN
    supports UMAC scan.

IWL_UCODE_TLV_CAPA_BEAMFORMER
    supports Beamformer

IWL_UCODE_TLV_CAPA_TOF_SUPPORT
    supports Time of Flight (802.11mc FTM)

IWL_UCODE_TLV_CAPA_TDLS_SUPPORT
    support basic TDLS functionality

IWL_UCODE_TLV_CAPA_TXPOWER_INSERTION_SUPPORT
    supports insertion of current
    tx power value into TPC Report action frame and Link Measurement Report
    action frame

IWL_UCODE_TLV_CAPA_DS_PARAM_SET_IE_SUPPORT
    supports updating current
    channel in DS parameter set element in probe requests.

IWL_UCODE_TLV_CAPA_WFA_TPC_REP_IE_SUPPORT
    supports adding TPC Report IE in
    probe requests.

IWL_UCODE_TLV_CAPA_QUIET_PERIOD_SUPPORT
    supports Quiet Period requests

IWL_UCODE_TLV_CAPA_DQA_SUPPORT
    supports dynamic queue allocation (DQA),
    which also implies support for the scheduler configuration command

IWL_UCODE_TLV_CAPA_TDLS_CHANNEL_SWITCH
    supports TDLS channel switching

IWL_UCODE_TLV_CAPA_CNSLDTD_D3_D0_IMG
    Consolidated D3-D0 image

IWL_UCODE_TLV_CAPA_HOTSPOT_SUPPORT
    supports Hot Spot Command

IWL_UCODE_TLV_CAPA_DC2DC_CONFIG_SUPPORT
    *undescribed*

IWL_UCODE_TLV_CAPA_CSUM_SUPPORT
    supports TCP Checksum Offload

IWL_UCODE_TLV_CAPA_RADIO_BEACON_STATS
    support radio and beacon statistics

IWL_UCODE_TLV_CAPA_P2P_SCM_UAPSD
    supports U-APSD on p2p interface when it
    is standalone or with a BSS station interface in the same binding.

IWL_UCODE_TLV_CAPA_BT_COEX_PLCR
    enabled BT Coex packet level co-running

IWL_UCODE_TLV_CAPA_LAR_MULTI_MCC
    ucode supports LAR updates with different
    sources for the MCC. This TLV bit is a future replacement to
    IWL_UCODE_TLV_API_WIFI_MCC_UPDATE. When either is set, multi-source LAR
    is supported.

IWL_UCODE_TLV_CAPA_BT_COEX_RRC
    supports BT Coex RRC

IWL_UCODE_TLV_CAPA_GSCAN_SUPPORT
    supports gscan

IWL_UCODE_TLV_CAPA_STA_PM_NOTIF
    firmware will send STA PM notification

IWL_UCODE_TLV_CAPA_BINDING_CDB_SUPPORT
    *undescribed*

IWL_UCODE_TLV_CAPA_CDB_SUPPORT
    *undescribed*

IWL_UCODE_TLV_CAPA_D0I3_END_FIRST
    *undescribed*

IWL_UCODE_TLV_CAPA_EXTENDED_DTS_MEASURE
    extended DTS measurement

IWL_UCODE_TLV_CAPA_SHORT_PM_TIMEOUTS
    supports short PM timeouts

IWL_UCODE_TLV_CAPA_BT_MPLUT_SUPPORT
    supports bt-coex Multi-priority LUT

IWL_UCODE_TLV_CAPA_MULTI_QUEUE_RX_SUPPORT
    *undescribed*

IWL_UCODE_TLV_CAPA_CSA_AND_TBTT_OFFLOAD
    the firmware supports CSA
    countdown offloading. Beacon notifications are not sent to the host.
    The fw also offloads TBTT alignment.

IWL_UCODE_TLV_CAPA_BEACON_ANT_SELECTION
    firmware will decide on what
    antenna the beacon should be transmitted

IWL_UCODE_TLV_CAPA_BEACON_STORING
    firmware will store the latest beacon
    from AP and will send it upon d0i3 exit.

IWL_UCODE_TLV_CAPA_LAR_SUPPORT_V2
    support LAR API V2

IWL_UCODE_TLV_CAPA_CT_KILL_BY_FW
    firmware responsible for CT-kill

IWL_UCODE_TLV_CAPA_TEMP_THS_REPORT_SUPPORT
    supports temperature
    thresholds reporting

IWL_UCODE_TLV_CAPA_CTDP_SUPPORT
    supports cTDP command

IWL_UCODE_TLV_CAPA_USNIFFER_UNIFIED
    supports usniffer enabled in
    regular image.

IWL_UCODE_TLV_CAPA_EXTEND_SHARED_MEM_CFG
    support getting more shared
    memory addresses from the firmware.

IWL_UCODE_TLV_CAPA_LQM_SUPPORT
    supports Link Quality Measurement

IWL_UCODE_TLV_CAPA_TX_POWER_ACK
    reduced TX power API has larger
    command size (command version 4) that supports toggling ACK TX
    power reduction.

IWL_UCODE_TLV_CAPA_LED_CMD_SUPPORT
    *undescribed*

IWL_UCODE_TLV_CAPA_MLME_OFFLOAD
    supports MLME offload

NUM_IWL_UCODE_TLV_CAPA
    number of bits used

.. _`iwl_tlv_calib_ctrl`:

struct iwl_tlv_calib_ctrl
=========================

.. c:type:: struct iwl_tlv_calib_ctrl

    Calibration control struct. Sent as part of the phy configuration command.

.. _`iwl_tlv_calib_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tlv_calib_ctrl {
        __le32 flow_trigger;
        __le32 event_trigger;
    }

.. _`iwl_tlv_calib_ctrl.members`:

Members
-------

flow_trigger
    bitmap for which calibrations to perform according to
    flow triggers.

event_trigger
    bitmap for which calibrations to perform according to
    event triggers.

.. _`iwl_fw_cipher_scheme`:

struct iwl_fw_cipher_scheme
===========================

.. c:type:: struct iwl_fw_cipher_scheme

    a cipher scheme supported by FW.

.. _`iwl_fw_cipher_scheme.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_cipher_scheme {
        __le32 cipher;
        u8 flags;
        u8 hdr_len;
        u8 pn_len;
        u8 pn_off;
        u8 key_idx_off;
        u8 key_idx_mask;
        u8 key_idx_shift;
        u8 mic_len;
        u8 hw_cipher;
    }

.. _`iwl_fw_cipher_scheme.members`:

Members
-------

cipher
    a cipher suite selector

flags
    cipher scheme flags (currently reserved for a future use)

hdr_len
    a size of MPDU security header

pn_len
    a size of PN

pn_off
    an offset of pn from the beginning of the security header

key_idx_off
    an offset of key index byte in the security header

key_idx_mask
    a bit mask of key_idx bits

key_idx_shift
    bit shift needed to get key_idx

mic_len
    mic length in bytes

hw_cipher
    a HW cipher index used in host commands

.. _`iwl_fw_dbg_reg_op`:

struct iwl_fw_dbg_reg_op
========================

.. c:type:: struct iwl_fw_dbg_reg_op

    an operation on a register

.. _`iwl_fw_dbg_reg_op.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_reg_op {
        u8 op;
        u8 reserved[3];
        __le32 addr;
        __le32 val;
    }

.. _`iwl_fw_dbg_reg_op.members`:

Members
-------

op
    &enum iwl_fw_dbg_reg_operator

reserved
    *undescribed*

addr
    offset of the register

val
    value

.. _`iwl_fw_dbg_monitor_mode`:

enum iwl_fw_dbg_monitor_mode
============================

.. c:type:: enum iwl_fw_dbg_monitor_mode

    available monitor recording modes

.. _`iwl_fw_dbg_monitor_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_fw_dbg_monitor_mode {
        SMEM_MODE,
        EXTERNAL_MODE,
        MARBH_MODE,
        MIPI_MODE
    };

.. _`iwl_fw_dbg_monitor_mode.constants`:

Constants
---------

SMEM_MODE
    monitor stores the data in SMEM

EXTERNAL_MODE
    monitor stores the data in allocated DRAM

MARBH_MODE
    monitor stores the data in MARBH buffer

MIPI_MODE
    monitor outputs the data through the MIPI interface

.. _`iwl_fw_mem_seg_type`:

enum iwl_fw_mem_seg_type
========================

.. c:type:: enum iwl_fw_mem_seg_type

    memory segment type

.. _`iwl_fw_mem_seg_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_fw_mem_seg_type {
        FW_DBG_MEM_TYPE_MASK,
        FW_DBG_MEM_TYPE_REGULAR,
        FW_DBG_MEM_TYPE_PRPH
    };

.. _`iwl_fw_mem_seg_type.constants`:

Constants
---------

FW_DBG_MEM_TYPE_MASK
    mask for the type indication

FW_DBG_MEM_TYPE_REGULAR
    regular memory

FW_DBG_MEM_TYPE_PRPH
    periphery memory (requires special reading)

.. _`iwl_fw_dbg_mem_seg_tlv`:

struct iwl_fw_dbg_mem_seg_tlv
=============================

.. c:type:: struct iwl_fw_dbg_mem_seg_tlv

    configures the debug data memory segments

.. _`iwl_fw_dbg_mem_seg_tlv.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_mem_seg_tlv {
        __le32 data_type;
        __le32 ofs;
        __le32 len;
    }

.. _`iwl_fw_dbg_mem_seg_tlv.members`:

Members
-------

data_type
    the memory segment type to record, see \ :c:type:`enum iwl_fw_mem_seg_type <iwl_fw_mem_seg_type>`\ 
    for what we care about

ofs
    the memory segment offset

len
    the memory segment length, in bytes

.. _`iwl_fw_dbg_mem_seg_tlv.description`:

Description
-----------

This parses IWL_UCODE_TLV_FW_MEM_SEG

.. _`iwl_fw_dbg_dest_tlv`:

struct iwl_fw_dbg_dest_tlv
==========================

.. c:type:: struct iwl_fw_dbg_dest_tlv

    configures the destination of the debug data

.. _`iwl_fw_dbg_dest_tlv.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_dest_tlv {
        u8 version;
        u8 monitor_mode;
        u8 size_power;
        u8 reserved;
        __le32 base_reg;
        __le32 end_reg;
        __le32 write_ptr_reg;
        __le32 wrap_count;
        u8 base_shift;
        u8 end_shift;
        struct iwl_fw_dbg_reg_op reg_ops[0];
    }

.. _`iwl_fw_dbg_dest_tlv.members`:

Members
-------

version
    version of the TLV - currently 0

monitor_mode
    &enum iwl_fw_dbg_monitor_mode

size_power
    buffer size will be 2^(size_power + 11)

reserved
    *undescribed*

base_reg
    addr of the base addr register (PRPH)

end_reg
    addr of the end addr register (PRPH)

write_ptr_reg
    the addr of the reg of the write pointer

wrap_count
    the addr of the reg of the wrap_count

base_shift
    shift right of the base addr reg

end_shift
    shift right of the end addr reg

reg_ops
    array of registers operations

.. _`iwl_fw_dbg_dest_tlv.description`:

Description
-----------

This parses IWL_UCODE_TLV_FW_DBG_DEST

.. _`iwl_fw_dbg_trigger_mode`:

enum iwl_fw_dbg_trigger_mode
============================

.. c:type:: enum iwl_fw_dbg_trigger_mode

    triggers functionalities

.. _`iwl_fw_dbg_trigger_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_fw_dbg_trigger_mode {
        IWL_FW_DBG_TRIGGER_START,
        IWL_FW_DBG_TRIGGER_STOP,
        IWL_FW_DBG_TRIGGER_MONITOR_ONLY
    };

.. _`iwl_fw_dbg_trigger_mode.constants`:

Constants
---------

IWL_FW_DBG_TRIGGER_START
    when trigger occurs re-conf the dbg mechanism

IWL_FW_DBG_TRIGGER_STOP
    when trigger occurs pull the dbg data

IWL_FW_DBG_TRIGGER_MONITOR_ONLY
    when trigger occurs trigger is set to
    collect only monitor data

.. _`iwl_fw_dbg_trigger_vif_type`:

enum iwl_fw_dbg_trigger_vif_type
================================

.. c:type:: enum iwl_fw_dbg_trigger_vif_type

    define the VIF type for a trigger

.. _`iwl_fw_dbg_trigger_vif_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_fw_dbg_trigger_vif_type {
        IWL_FW_DBG_CONF_VIF_ANY,
        IWL_FW_DBG_CONF_VIF_IBSS,
        IWL_FW_DBG_CONF_VIF_STATION,
        IWL_FW_DBG_CONF_VIF_AP,
        IWL_FW_DBG_CONF_VIF_P2P_CLIENT,
        IWL_FW_DBG_CONF_VIF_P2P_GO,
        IWL_FW_DBG_CONF_VIF_P2P_DEVICE
    };

.. _`iwl_fw_dbg_trigger_vif_type.constants`:

Constants
---------

IWL_FW_DBG_CONF_VIF_ANY
    any vif type

IWL_FW_DBG_CONF_VIF_IBSS
    IBSS mode

IWL_FW_DBG_CONF_VIF_STATION
    BSS mode

IWL_FW_DBG_CONF_VIF_AP
    AP mode

IWL_FW_DBG_CONF_VIF_P2P_CLIENT
    P2P Client mode

IWL_FW_DBG_CONF_VIF_P2P_GO
    P2P GO mode

IWL_FW_DBG_CONF_VIF_P2P_DEVICE
    P2P device

.. _`iwl_fw_dbg_trigger_tlv`:

struct iwl_fw_dbg_trigger_tlv
=============================

.. c:type:: struct iwl_fw_dbg_trigger_tlv

    a TLV that describes the trigger

.. _`iwl_fw_dbg_trigger_tlv.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_tlv {
        __le32 id;
        __le32 vif_type;
        __le32 stop_conf_ids;
        __le32 stop_delay;
        u8 mode;
        u8 start_conf_id;
        __le16 occurrences;
        __le16 trig_dis_ms;
        __le16 reserved[3];
        u8 data[0];
    }

.. _`iwl_fw_dbg_trigger_tlv.members`:

Members
-------

id
    &enum iwl_fw_dbg_trigger

vif_type
    &enum iwl_fw_dbg_trigger_vif_type

stop_conf_ids
    bitmap of configurations this trigger relates to.
    if the mode is \ ``IWL_FW_DBG_TRIGGER_STOP``\ , then if the bit corresponding
    to the currently running configuration is set, the data should be
    collected.

stop_delay
    how many milliseconds to wait before collecting the data
    after the STOP trigger fires.

mode
    &enum iwl_fw_dbg_trigger_mode - can be stop / start of both

start_conf_id
    if mode is \ ``IWL_FW_DBG_TRIGGER_START``\ , this defines what
    configuration should be applied when the triggers kicks in.

occurrences
    number of occurrences. 0 means the trigger will never fire.

trig_dis_ms
    the time, in milliseconds, after an occurrence of this
    trigger in which another occurrence should be ignored.

reserved
    *undescribed*

data
    *undescribed*

.. _`iwl_fw_dbg_trigger_missed_bcon`:

struct iwl_fw_dbg_trigger_missed_bcon
=====================================

.. c:type:: struct iwl_fw_dbg_trigger_missed_bcon

    configures trigger for missed beacons

.. _`iwl_fw_dbg_trigger_missed_bcon.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_missed_bcon {
        __le32 stop_consec_missed_bcon;
        __le32 stop_consec_missed_bcon_since_rx;
        __le32 reserved2[2];
        __le32 start_consec_missed_bcon;
        __le32 start_consec_missed_bcon_since_rx;
        __le32 reserved1[2];
    }

.. _`iwl_fw_dbg_trigger_missed_bcon.members`:

Members
-------

stop_consec_missed_bcon
    stop recording if threshold is crossed.

stop_consec_missed_bcon_since_rx
    stop recording if threshold is crossed.

reserved2
    reserved

start_consec_missed_bcon
    start recording if threshold is crossed.

start_consec_missed_bcon_since_rx
    start recording if threshold is crossed.

reserved1
    reserved

.. _`iwl_fw_dbg_trigger_cmd`:

struct iwl_fw_dbg_trigger_cmd
=============================

.. c:type:: struct iwl_fw_dbg_trigger_cmd

    configures trigger for messages from FW.

.. _`iwl_fw_dbg_trigger_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_cmd {
        struct cmd {
            u8 cmd_id;
            u8 group_id;
        } __packed cmds[16];
    }

.. _`iwl_fw_dbg_trigger_cmd.members`:

Members
-------

cmds
    *undescribed*

.. _`iwl_fw_dbg_trigger_cmd.cmds`:

cmds
----

the list of commands to trigger the collection on

.. _`iwl_fw_dbg_trigger_low_rssi`:

struct iwl_fw_dbg_trigger_low_rssi
==================================

.. c:type:: struct iwl_fw_dbg_trigger_low_rssi

    trigger for low beacon RSSI

.. _`iwl_fw_dbg_trigger_low_rssi.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_low_rssi {
        __le32 rssi;
    }

.. _`iwl_fw_dbg_trigger_low_rssi.members`:

Members
-------

rssi
    RSSI value to trigger at

.. _`iwl_fw_dbg_trigger_mlme`:

struct iwl_fw_dbg_trigger_mlme
==============================

.. c:type:: struct iwl_fw_dbg_trigger_mlme

    configures trigger for mlme events

.. _`iwl_fw_dbg_trigger_mlme.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_mlme {
        u8 stop_auth_denied;
        u8 stop_auth_timeout;
        u8 stop_rx_deauth;
        u8 stop_tx_deauth;
        u8 stop_assoc_denied;
        u8 stop_assoc_timeout;
        u8 stop_connection_loss;
        u8 reserved;
        u8 start_auth_denied;
        u8 start_auth_timeout;
        u8 start_rx_deauth;
        u8 start_tx_deauth;
        u8 start_assoc_denied;
        u8 start_assoc_timeout;
        u8 start_connection_loss;
        u8 reserved2;
    }

.. _`iwl_fw_dbg_trigger_mlme.members`:

Members
-------

stop_auth_denied
    number of denied authentication to collect

stop_auth_timeout
    number of authentication timeout to collect

stop_rx_deauth
    number of Rx deauth before to collect

stop_tx_deauth
    number of Tx deauth before to collect

stop_assoc_denied
    number of denied association to collect

stop_assoc_timeout
    number of association timeout to collect

stop_connection_loss
    number of connection loss to collect

reserved
    *undescribed*

start_auth_denied
    number of denied authentication to start recording

start_auth_timeout
    number of authentication timeout to start recording

start_rx_deauth
    number of Rx deauth to start recording

start_tx_deauth
    number of Tx deauth to start recording

start_assoc_denied
    number of denied association to start recording

start_assoc_timeout
    number of association timeout to start recording

start_connection_loss
    number of connection loss to start recording

reserved2
    *undescribed*

.. _`iwl_fw_dbg_trigger_txq_timer`:

struct iwl_fw_dbg_trigger_txq_timer
===================================

.. c:type:: struct iwl_fw_dbg_trigger_txq_timer

    configures the Tx queue's timer

.. _`iwl_fw_dbg_trigger_txq_timer.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_txq_timer {
        __le32 command_queue;
        __le32 bss;
        __le32 softap;
        __le32 p2p_go;
        __le32 p2p_client;
        __le32 p2p_device;
        __le32 ibss;
        __le32 tdls;
        __le32 reserved[4];
    }

.. _`iwl_fw_dbg_trigger_txq_timer.members`:

Members
-------

command_queue
    timeout for the command queue in ms

bss
    timeout for the queues of a BSS (except for TDLS queues) in ms

softap
    timeout for the queues of a softAP in ms

p2p_go
    timeout for the queues of a P2P GO in ms

p2p_client
    timeout for the queues of a P2P client in ms

p2p_device
    timeout for the queues of a P2P device in ms

ibss
    timeout for the queues of an IBSS in ms

tdls
    timeout for the queues of a TDLS station in ms

reserved
    *undescribed*

.. _`iwl_fw_dbg_trigger_time_event`:

struct iwl_fw_dbg_trigger_time_event
====================================

.. c:type:: struct iwl_fw_dbg_trigger_time_event

    configures a time event trigger

.. _`iwl_fw_dbg_trigger_time_event.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_time_event {
        struct {
            __le32 id;
            __le32 action_bitmap;
            __le32 status_bitmap;
        } __packed time_events[16];
    }

.. _`iwl_fw_dbg_trigger_time_event.members`:

Members
-------

time_events
    *undescribed*

.. _`iwl_fw_dbg_trigger_time_event.time_events`:

time_Events
-----------

a list of tuples <id, action_bitmap>. The driver will issue a
trigger each time a time event notification that relates to time event
id with one of the actions in the bitmap is received and
BIT(notif->status) is set in status_bitmap.

.. _`iwl_fw_dbg_trigger_ba`:

struct iwl_fw_dbg_trigger_ba
============================

.. c:type:: struct iwl_fw_dbg_trigger_ba

    configures BlockAck related trigger

.. _`iwl_fw_dbg_trigger_ba.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_ba {
        __le16 rx_ba_start;
        __le16 rx_ba_stop;
        __le16 tx_ba_start;
        __le16 tx_ba_stop;
        __le16 rx_bar;
        __le16 tx_bar;
        __le16 frame_timeout;
    }

.. _`iwl_fw_dbg_trigger_ba.members`:

Members
-------

rx_ba_start
    *undescribed*

rx_ba_stop
    *undescribed*

tx_ba_start
    *undescribed*

tx_ba_stop
    *undescribed*

rx_bar
    *undescribed*

tx_bar
    *undescribed*

frame_timeout
    *undescribed*

.. _`iwl_fw_dbg_trigger_ba.rx_ba_start`:

rx_ba_start
-----------

tid bitmap to configure on what tid the trigger should occur
when an Rx BlockAck session is started.

.. _`iwl_fw_dbg_trigger_ba.rx_ba_stop`:

rx_ba_stop
----------

tid bitmap to configure on what tid the trigger should occur
when an Rx BlockAck session is stopped.

.. _`iwl_fw_dbg_trigger_ba.tx_ba_start`:

tx_ba_start
-----------

tid bitmap to configure on what tid the trigger should occur
when a Tx BlockAck session is started.

.. _`iwl_fw_dbg_trigger_ba.tx_ba_stop`:

tx_ba_stop
----------

tid bitmap to configure on what tid the trigger should occur
when a Tx BlockAck session is stopped.

.. _`iwl_fw_dbg_trigger_ba.rx_bar`:

rx_bar
------

tid bitmap to configure on what tid the trigger should occur
when a BAR is received (for a Tx BlockAck session).

.. _`iwl_fw_dbg_trigger_ba.tx_bar`:

tx_bar
------

tid bitmap to configure on what tid the trigger should occur
when a BAR is send (for an Rx BlocAck session).

.. _`iwl_fw_dbg_trigger_ba.frame_timeout`:

frame_timeout
-------------

tid bitmap to configure on what tid the trigger should occur
when a frame times out in the reodering buffer.

.. _`iwl_fw_dbg_trigger_tdls`:

struct iwl_fw_dbg_trigger_tdls
==============================

.. c:type:: struct iwl_fw_dbg_trigger_tdls

    configures trigger for TDLS events.

.. _`iwl_fw_dbg_trigger_tdls.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_tdls {
        u8 action_bitmap;
        u8 peer_mode;
        u8 peer[ETH_ALEN];
        u8 reserved[4];
    }

.. _`iwl_fw_dbg_trigger_tdls.members`:

Members
-------

action_bitmap
    the TDLS action to trigger the collection upon

peer_mode
    trigger on specific peer or all

peer
    the TDLS peer to trigger the collection on

reserved
    *undescribed*

.. _`iwl_fw_dbg_trigger_tx_status`:

struct iwl_fw_dbg_trigger_tx_status
===================================

.. c:type:: struct iwl_fw_dbg_trigger_tx_status

    configures trigger for tx response status.

.. _`iwl_fw_dbg_trigger_tx_status.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_trigger_tx_status {
        struct tx_status {
            u8 status;
            u8 reserved[3];
        } __packed statuses[16];
        __le32 reserved[2];
    }

.. _`iwl_fw_dbg_trigger_tx_status.members`:

Members
-------

statuses
    the list of statuses to trigger the collection on

reserved
    *undescribed*

.. _`iwl_fw_dbg_conf_tlv`:

struct iwl_fw_dbg_conf_tlv
==========================

.. c:type:: struct iwl_fw_dbg_conf_tlv

    a TLV that describes a debug configuration.

.. _`iwl_fw_dbg_conf_tlv.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_dbg_conf_tlv {
        u8 id;
        u8 usniffer;
        u8 reserved;
        u8 num_of_hcmds;
        struct iwl_fw_dbg_conf_hcmd hcmd;
    }

.. _`iwl_fw_dbg_conf_tlv.members`:

Members
-------

id
    conf id

usniffer
    should the uSniffer image be used

reserved
    *undescribed*

num_of_hcmds
    how many HCMDs to send are present here

hcmd
    a variable length host command to be sent to apply the configuration.
    If there is more than one HCMD to send, they will appear one after the
    other and be sent in the order that they appear in.
    This parses IWL_UCODE_TLV_FW_DBG_CONF. The user can add up-to
    \ ``FW_DBG_CONF_MAX``\  configuration per run.

.. _`iwl_fw_gscan_capabilities`:

struct iwl_fw_gscan_capabilities
================================

.. c:type:: struct iwl_fw_gscan_capabilities

    gscan capabilities supported by FW

.. _`iwl_fw_gscan_capabilities.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_gscan_capabilities {
        __le32 max_scan_cache_size;
        __le32 max_scan_buckets;
        __le32 max_ap_cache_per_scan;
        __le32 max_rssi_sample_size;
        __le32 max_scan_reporting_threshold;
        __le32 max_hotlist_aps;
        __le32 max_significant_change_aps;
        __le32 max_bssid_history_entries;
        __le32 max_hotlist_ssids;
        __le32 max_number_epno_networks;
        __le32 max_number_epno_networks_by_ssid;
        __le32 max_number_of_white_listed_ssid;
        __le32 max_number_of_black_listed_ssid;
    }

.. _`iwl_fw_gscan_capabilities.members`:

Members
-------

max_scan_cache_size
    total space allocated for scan results (in bytes).

max_scan_buckets
    maximum number of channel buckets.

max_ap_cache_per_scan
    maximum number of APs that can be stored per scan.

max_rssi_sample_size
    number of RSSI samples used for averaging RSSI.

max_scan_reporting_threshold
    max possible report threshold. in percentage.

max_hotlist_aps
    maximum number of entries for hotlist APs.

max_significant_change_aps
    maximum number of entries for significant
    change APs.

max_bssid_history_entries
    number of BSSID/RSSI entries that the device can
    hold.

max_hotlist_ssids
    maximum number of entries for hotlist SSIDs.

max_number_epno_networks
    max number of epno entries.

max_number_epno_networks_by_ssid
    max number of epno entries if ssid is
    specified.

max_number_of_white_listed_ssid
    max number of white listed SSIDs.

max_number_of_black_listed_ssid
    max number of black listed SSIDs.

.. This file was automatic generated / don't edit.

