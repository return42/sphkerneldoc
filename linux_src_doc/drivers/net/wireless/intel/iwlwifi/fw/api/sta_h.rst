.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/sta.h

.. _`iwl_sta_flags`:

enum iwl_sta_flags
==================

.. c:type:: enum iwl_sta_flags

    flags for the ADD_STA host command

.. _`iwl_sta_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_sta_flags {
        STA_FLG_REDUCED_TX_PWR_CTRL,
        STA_FLG_REDUCED_TX_PWR_DATA,
        STA_FLG_DISABLE_TX,
        STA_FLG_PS,
        STA_FLG_DRAIN_FLOW,
        STA_FLG_PAN,
        STA_FLG_CLASS_AUTH,
        STA_FLG_CLASS_ASSOC,
        STA_FLG_RTS_MIMO_PROT,
        STA_FLG_MAX_AGG_SIZE_SHIFT,
        STA_FLG_MAX_AGG_SIZE_8K,
        STA_FLG_MAX_AGG_SIZE_16K,
        STA_FLG_MAX_AGG_SIZE_32K,
        STA_FLG_MAX_AGG_SIZE_64K,
        STA_FLG_MAX_AGG_SIZE_128K,
        STA_FLG_MAX_AGG_SIZE_256K,
        STA_FLG_MAX_AGG_SIZE_512K,
        STA_FLG_MAX_AGG_SIZE_1024K,
        STA_FLG_MAX_AGG_SIZE_MSK,
        STA_FLG_AGG_MPDU_DENS_SHIFT,
        STA_FLG_AGG_MPDU_DENS_2US,
        STA_FLG_AGG_MPDU_DENS_4US,
        STA_FLG_AGG_MPDU_DENS_8US,
        STA_FLG_AGG_MPDU_DENS_16US,
        STA_FLG_AGG_MPDU_DENS_MSK,
        STA_FLG_FAT_EN_20MHZ,
        STA_FLG_FAT_EN_40MHZ,
        STA_FLG_FAT_EN_80MHZ,
        STA_FLG_FAT_EN_160MHZ,
        STA_FLG_FAT_EN_MSK,
        STA_FLG_MIMO_EN_SISO,
        STA_FLG_MIMO_EN_MIMO2,
        STA_FLG_MIMO_EN_MIMO3,
        STA_FLG_MIMO_EN_MSK
    };

.. _`iwl_sta_flags.constants`:

Constants
---------

STA_FLG_REDUCED_TX_PWR_CTRL
    reduced TX power (control frames)

STA_FLG_REDUCED_TX_PWR_DATA
    reduced TX power (data frames)

STA_FLG_DISABLE_TX
    set if TX should be disabled

STA_FLG_PS
    set if STA is in Power Save

STA_FLG_DRAIN_FLOW
    drain flow

STA_FLG_PAN
    STA is for PAN interface

STA_FLG_CLASS_AUTH
    station is authenticated

STA_FLG_CLASS_ASSOC
    station is associated

STA_FLG_RTS_MIMO_PROT
    station requires RTS MIMO protection (dynamic SMPS)

STA_FLG_MAX_AGG_SIZE_SHIFT
    maximal size for A-MPDU (bit shift)

STA_FLG_MAX_AGG_SIZE_8K
    maximal size for A-MPDU (8k supported)

STA_FLG_MAX_AGG_SIZE_16K
    maximal size for A-MPDU (16k supported)

STA_FLG_MAX_AGG_SIZE_32K
    maximal size for A-MPDU (32k supported)

STA_FLG_MAX_AGG_SIZE_64K
    maximal size for A-MPDU (64k supported)

STA_FLG_MAX_AGG_SIZE_128K
    maximal size for A-MPDU (128k supported)

STA_FLG_MAX_AGG_SIZE_256K
    maximal size for A-MPDU (256k supported)

STA_FLG_MAX_AGG_SIZE_512K
    maximal size for A-MPDU (512k supported)

STA_FLG_MAX_AGG_SIZE_1024K
    maximal size for A-MPDU (1024k supported)

STA_FLG_MAX_AGG_SIZE_MSK
    maximal size for A-MPDU (mask)

STA_FLG_AGG_MPDU_DENS_SHIFT
    A-MPDU density (bit shift)

STA_FLG_AGG_MPDU_DENS_2US
    A-MPDU density (2 usec gap)

STA_FLG_AGG_MPDU_DENS_4US
    A-MPDU density (4 usec gap)

STA_FLG_AGG_MPDU_DENS_8US
    A-MPDU density (8 usec gap)

STA_FLG_AGG_MPDU_DENS_16US
    A-MPDU density (16 usec gap)

STA_FLG_AGG_MPDU_DENS_MSK
    A-MPDU density (mask)

STA_FLG_FAT_EN_20MHZ
    no wide channels are supported, only 20 MHz

STA_FLG_FAT_EN_40MHZ
    wide channels up to 40 MHz supported

STA_FLG_FAT_EN_80MHZ
    wide channels up to 80 MHz supported

STA_FLG_FAT_EN_160MHZ
    wide channels up to 160 MHz supported

STA_FLG_FAT_EN_MSK
    support for channel width (for Tx). This flag is
    initialised by driver and can be updated by fw upon reception of
    action frames that can change the channel width. When cleared the fw
    will send all the frames in 20MHz even when FAT channel is requested.

STA_FLG_MIMO_EN_SISO
    no support for MIMO

STA_FLG_MIMO_EN_MIMO2
    2 streams supported

STA_FLG_MIMO_EN_MIMO3
    3 streams supported

STA_FLG_MIMO_EN_MSK
    support for MIMO. This flag is initialised by the
    driver and can be updated by fw upon reception of action frames.

.. _`iwl_sta_key_flag`:

enum iwl_sta_key_flag
=====================

.. c:type:: enum iwl_sta_key_flag

    key flags for the ADD_STA host command

.. _`iwl_sta_key_flag.definition`:

Definition
----------

.. code-block:: c

    enum iwl_sta_key_flag {
        STA_KEY_FLG_NO_ENC,
        STA_KEY_FLG_WEP,
        STA_KEY_FLG_CCM,
        STA_KEY_FLG_TKIP,
        STA_KEY_FLG_EXT,
        STA_KEY_FLG_GCMP,
        STA_KEY_FLG_CMAC,
        STA_KEY_FLG_ENC_UNKNOWN,
        STA_KEY_FLG_EN_MSK,
        STA_KEY_FLG_WEP_KEY_MAP,
        STA_KEY_FLG_KEYID_POS,
        STA_KEY_FLG_KEYID_MSK,
        STA_KEY_NOT_VALID,
        STA_KEY_FLG_WEP_13BYTES,
        STA_KEY_FLG_KEY_32BYTES,
        STA_KEY_MULTICAST,
        STA_KEY_MFP
    };

.. _`iwl_sta_key_flag.constants`:

Constants
---------

STA_KEY_FLG_NO_ENC
    no encryption

STA_KEY_FLG_WEP
    WEP encryption algorithm

STA_KEY_FLG_CCM
    CCMP encryption algorithm

STA_KEY_FLG_TKIP
    TKIP encryption algorithm

STA_KEY_FLG_EXT
    extended cipher algorithm (depends on the FW support)

STA_KEY_FLG_GCMP
    GCMP encryption algorithm

STA_KEY_FLG_CMAC
    CMAC encryption algorithm

STA_KEY_FLG_ENC_UNKNOWN
    unknown encryption algorithm

STA_KEY_FLG_EN_MSK
    mask for encryption algorithmi value

STA_KEY_FLG_WEP_KEY_MAP
    wep is either a group key (0 - legacy WEP) or from
    station info array (1 - n 1X mode)

STA_KEY_FLG_KEYID_POS
    key index bit position

STA_KEY_FLG_KEYID_MSK
    the index of the key

STA_KEY_NOT_VALID
    key is invalid

STA_KEY_FLG_WEP_13BYTES
    set for 13 bytes WEP key

STA_KEY_FLG_KEY_32BYTES
    for non-wep key set for 32 bytes key

STA_KEY_MULTICAST
    set for multical key

STA_KEY_MFP
    key is used for Management Frame Protection

.. _`iwl_sta_modify_flag`:

enum iwl_sta_modify_flag
========================

.. c:type:: enum iwl_sta_modify_flag

    indicate to the fw what flag are being changed

.. _`iwl_sta_modify_flag.definition`:

Definition
----------

.. code-block:: c

    enum iwl_sta_modify_flag {
        STA_MODIFY_QUEUE_REMOVAL,
        STA_MODIFY_TID_DISABLE_TX,
        STA_MODIFY_UAPSD_ACS,
        STA_MODIFY_ADD_BA_TID,
        STA_MODIFY_REMOVE_BA_TID,
        STA_MODIFY_SLEEPING_STA_TX_COUNT,
        STA_MODIFY_PROT_TH,
        STA_MODIFY_QUEUES
    };

.. _`iwl_sta_modify_flag.constants`:

Constants
---------

STA_MODIFY_QUEUE_REMOVAL
    this command removes a queue

STA_MODIFY_TID_DISABLE_TX
    this command modifies \ ``tid_disable_tx``\ 

STA_MODIFY_UAPSD_ACS
    this command modifies \ ``uapsd_acs``\ 

STA_MODIFY_ADD_BA_TID
    this command modifies \ ``add_immediate_ba_tid``\ 

STA_MODIFY_REMOVE_BA_TID
    this command modifies \ ``remove_immediate_ba_tid``\ 

STA_MODIFY_SLEEPING_STA_TX_COUNT
    this command modifies \ ``sleep_tx_count``\ 

STA_MODIFY_PROT_TH
    modify RTS threshold

STA_MODIFY_QUEUES
    modify the queues used by this station

.. _`iwl_sta_mode`:

enum iwl_sta_mode
=================

.. c:type:: enum iwl_sta_mode

    station command mode

.. _`iwl_sta_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_sta_mode {
        STA_MODE_ADD,
        STA_MODE_MODIFY
    };

.. _`iwl_sta_mode.constants`:

Constants
---------

STA_MODE_ADD
    add new station

STA_MODE_MODIFY
    modify the station

.. _`iwl_sta_sleep_flag`:

enum iwl_sta_sleep_flag
=======================

.. c:type:: enum iwl_sta_sleep_flag

    type of sleep of the station

.. _`iwl_sta_sleep_flag.definition`:

Definition
----------

.. code-block:: c

    enum iwl_sta_sleep_flag {
        STA_SLEEP_STATE_AWAKE,
        STA_SLEEP_STATE_PS_POLL,
        STA_SLEEP_STATE_UAPSD,
        STA_SLEEP_STATE_MOREDATA
    };

.. _`iwl_sta_sleep_flag.constants`:

Constants
---------

STA_SLEEP_STATE_AWAKE
    station is awake

STA_SLEEP_STATE_PS_POLL
    station is PS-polling

STA_SLEEP_STATE_UAPSD
    station uses U-APSD

STA_SLEEP_STATE_MOREDATA
    set more-data bit on
    (last) released frame

.. _`iwl_mvm_keyinfo`:

struct iwl_mvm_keyinfo
======================

.. c:type:: struct iwl_mvm_keyinfo

    key information

.. _`iwl_mvm_keyinfo.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_keyinfo {
        __le16 key_flags;
        u8 tkip_rx_tsc_byte2;
        u8 reserved1;
        __le16 tkip_rx_ttak[5];
        u8 key_offset;
        u8 reserved2;
        u8 key[16];
        __le64 tx_secur_seq_cnt;
        __le64 hw_tkip_mic_rx_key;
        __le64 hw_tkip_mic_tx_key;
    }

.. _`iwl_mvm_keyinfo.members`:

Members
-------

key_flags
    type \ :c:type:`enum iwl_sta_key_flag <iwl_sta_key_flag>`\ 

tkip_rx_tsc_byte2
    TSC[2] for key mix ph1 detection

reserved1
    reserved

tkip_rx_ttak
    10-byte unicast TKIP TTAK for Rx

key_offset
    key offset in the fw's key table

reserved2
    reserved

key
    16-byte unicast decryption key

tx_secur_seq_cnt
    initial RSC / PN needed for replay check

hw_tkip_mic_rx_key
    byte: MIC Rx Key - used for TKIP only

hw_tkip_mic_tx_key
    byte: MIC Tx Key - used for TKIP only

.. _`iwl_mvm_add_sta_cmd_v7`:

struct iwl_mvm_add_sta_cmd_v7
=============================

.. c:type:: struct iwl_mvm_add_sta_cmd_v7

    Add/modify a station in the fw's sta table. ( REPLY_ADD_STA = 0x18 )

.. _`iwl_mvm_add_sta_cmd_v7.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_add_sta_cmd_v7 {
        u8 add_modify;
        u8 awake_acs;
        __le16 tid_disable_tx;
        __le32 mac_id_n_color;
        u8 addr[ETH_ALEN];
        __le16 reserved2;
        u8 sta_id;
        u8 modify_mask;
        __le16 reserved3;
        __le32 station_flags;
        __le32 station_flags_msk;
        u8 add_immediate_ba_tid;
        u8 remove_immediate_ba_tid;
        __le16 add_immediate_ba_ssn;
        __le16 sleep_tx_count;
        __le16 sleep_state_flags;
        __le16 assoc_id;
        __le16 beamform_flags;
        __le32 tfd_queue_msk;
    }

.. _`iwl_mvm_add_sta_cmd_v7.members`:

Members
-------

add_modify
    see \ :c:type:`enum iwl_sta_mode <iwl_sta_mode>`\ 

awake_acs
    ACs to transmit data on while station is sleeping (for U-APSD)

tid_disable_tx
    is tid BIT(tid) enabled for Tx. Clear BIT(x) to enable
    AMPDU for tid x. Set \ ``STA_MODIFY_TID_DISABLE_TX``\  to change this field.

mac_id_n_color
    the Mac context this station belongs to,
    see \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

addr
    station's MAC address

reserved2
    reserved

sta_id
    index of station in uCode's station table

modify_mask
    STA_MODIFY\_\*, selects which parameters to modify vs. leave
    alone. 1 - modify, 0 - don't change.

reserved3
    reserved

station_flags
    look at \ :c:type:`enum iwl_sta_flags <iwl_sta_flags>`\ 

station_flags_msk
    what of \ ``station_flags``\  have changed,
    also \ :c:type:`enum iwl_sta_flags <iwl_sta_flags>`\ 

add_immediate_ba_tid
    tid for which to add block-ack support (Rx)
    Set \ ``STA_MODIFY_ADD_BA_TID``\  to use this field, and also set
    add_immediate_ba_ssn.

remove_immediate_ba_tid
    tid for which to remove block-ack support (Rx)
    Set \ ``STA_MODIFY_REMOVE_BA_TID``\  to use this field

add_immediate_ba_ssn
    ssn for the Rx block-ack session. Used together with
    add_immediate_ba_tid.

sleep_tx_count
    number of packets to transmit to station even though it is
    asleep. Used to synchronise PS-poll and u-APSD responses while ucode
    keeps track of STA sleep state.

sleep_state_flags
    Look at \ :c:type:`enum iwl_sta_sleep_flag <iwl_sta_sleep_flag>`\ .

assoc_id
    assoc_id to be sent in VHT PLCP (9-bit), for grp use 0, for AP
    mac-addr.

beamform_flags
    beam forming controls

tfd_queue_msk
    tfd queues used by this station

.. _`iwl_mvm_add_sta_cmd_v7.description`:

Description
-----------

The device contains an internal table of per-station information, with info
on security keys, aggregation parameters, and Tx rates for initial Tx
attempt and any retries (set by REPLY_TX_LINK_QUALITY_CMD).

ADD_STA sets up the table entry for one station, either creating a new
entry, or modifying a pre-existing one.

.. _`iwl_sta_type`:

enum iwl_sta_type
=================

.. c:type:: enum iwl_sta_type

    FW station types ( REPLY_ADD_STA = 0x18 )

.. _`iwl_sta_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_sta_type {
        IWL_STA_LINK,
        IWL_STA_GENERAL_PURPOSE,
        IWL_STA_MULTICAST,
        IWL_STA_TDLS_LINK,
        IWL_STA_AUX_ACTIVITY
    };

.. _`iwl_sta_type.constants`:

Constants
---------

IWL_STA_LINK
    Link station - normal RX and TX traffic.

IWL_STA_GENERAL_PURPOSE
    General purpose. In AP mode used for beacons
    and probe responses.

IWL_STA_MULTICAST
    multicast traffic,

IWL_STA_TDLS_LINK
    TDLS link station

IWL_STA_AUX_ACTIVITY
    auxilary station (scan, ROC and so on).

.. _`iwl_mvm_add_sta_cmd`:

struct iwl_mvm_add_sta_cmd
==========================

.. c:type:: struct iwl_mvm_add_sta_cmd

    Add/modify a station in the fw's sta table. ( REPLY_ADD_STA = 0x18 )

.. _`iwl_mvm_add_sta_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_add_sta_cmd {
        u8 add_modify;
        u8 awake_acs;
        __le16 tid_disable_tx;
        __le32 mac_id_n_color;
        u8 addr[ETH_ALEN];
        __le16 reserved2;
        u8 sta_id;
        u8 modify_mask;
        __le16 reserved3;
        __le32 station_flags;
        __le32 station_flags_msk;
        u8 add_immediate_ba_tid;
        u8 remove_immediate_ba_tid;
        __le16 add_immediate_ba_ssn;
        __le16 sleep_tx_count;
        u8 sleep_state_flags;
        u8 station_type;
        __le16 assoc_id;
        __le16 beamform_flags;
        __le32 tfd_queue_msk;
        __le16 rx_ba_window;
        u8 sp_length;
        u8 uapsd_acs;
    }

.. _`iwl_mvm_add_sta_cmd.members`:

Members
-------

add_modify
    see \ :c:type:`enum iwl_sta_mode <iwl_sta_mode>`\ 

awake_acs
    ACs to transmit data on while station is sleeping (for U-APSD)

tid_disable_tx
    is tid BIT(tid) enabled for Tx. Clear BIT(x) to enable
    AMPDU for tid x. Set \ ``STA_MODIFY_TID_DISABLE_TX``\  to change this field.

mac_id_n_color
    the Mac context this station belongs to,
    see \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

addr
    station's MAC address

reserved2
    reserved

sta_id
    index of station in uCode's station table

modify_mask
    STA_MODIFY\_\*, selects which parameters to modify vs. leave
    alone. 1 - modify, 0 - don't change.

reserved3
    reserved

station_flags
    look at \ :c:type:`enum iwl_sta_flags <iwl_sta_flags>`\ 

station_flags_msk
    what of \ ``station_flags``\  have changed,
    also \ :c:type:`enum iwl_sta_flags <iwl_sta_flags>`\ 

add_immediate_ba_tid
    tid for which to add block-ack support (Rx)
    Set \ ``STA_MODIFY_ADD_BA_TID``\  to use this field, and also set
    add_immediate_ba_ssn.

remove_immediate_ba_tid
    tid for which to remove block-ack support (Rx)
    Set \ ``STA_MODIFY_REMOVE_BA_TID``\  to use this field

add_immediate_ba_ssn
    ssn for the Rx block-ack session. Used together with
    add_immediate_ba_tid.

sleep_tx_count
    number of packets to transmit to station even though it is
    asleep. Used to synchronise PS-poll and u-APSD responses while ucode
    keeps track of STA sleep state.

sleep_state_flags
    Look at \ :c:type:`enum iwl_sta_sleep_flag <iwl_sta_sleep_flag>`\ .

station_type
    type of this station. See \ :c:type:`enum iwl_sta_type <iwl_sta_type>`\ .

assoc_id
    assoc_id to be sent in VHT PLCP (9-bit), for grp use 0, for AP
    mac-addr.

beamform_flags
    beam forming controls

tfd_queue_msk
    tfd queues used by this station.
    Obselete for new TX API (9 and above).

rx_ba_window
    aggregation window size

sp_length
    the size of the SP in actual number of frames

uapsd_acs
    4 LS bits are trigger enabled ACs, 4 MS bits are the deliver
    enabled ACs.

.. _`iwl_mvm_add_sta_cmd.description`:

Description
-----------

The device contains an internal table of per-station information, with info
on security keys, aggregation parameters, and Tx rates for initial Tx
attempt and any retries (set by REPLY_TX_LINK_QUALITY_CMD).

ADD_STA sets up the table entry for one station, either creating a new
entry, or modifying a pre-existing one.

.. _`iwl_mvm_add_sta_key_common`:

struct iwl_mvm_add_sta_key_common
=================================

.. c:type:: struct iwl_mvm_add_sta_key_common

    add/modify sta key common part ( REPLY_ADD_STA_KEY = 0x17 )

.. _`iwl_mvm_add_sta_key_common.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_add_sta_key_common {
        u8 sta_id;
        u8 key_offset;
        __le16 key_flags;
        u8 key[32];
        u8 rx_secur_seq_cnt[16];
    }

.. _`iwl_mvm_add_sta_key_common.members`:

Members
-------

sta_id
    index of station in uCode's station table

key_offset
    key offset in key storage

key_flags
    type \ :c:type:`enum iwl_sta_key_flag <iwl_sta_key_flag>`\ 

key
    key material data

rx_secur_seq_cnt
    RX security sequence counter for the key

.. _`iwl_mvm_add_sta_key_cmd_v1`:

struct iwl_mvm_add_sta_key_cmd_v1
=================================

.. c:type:: struct iwl_mvm_add_sta_key_cmd_v1

    add/modify sta key

.. _`iwl_mvm_add_sta_key_cmd_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_add_sta_key_cmd_v1 {
        struct iwl_mvm_add_sta_key_common common;
        u8 tkip_rx_tsc_byte2;
        u8 reserved;
        __le16 tkip_rx_ttak[5];
    }

.. _`iwl_mvm_add_sta_key_cmd_v1.members`:

Members
-------

common
    see \ :c:type:`struct iwl_mvm_add_sta_key_common <iwl_mvm_add_sta_key_common>`\ 

tkip_rx_tsc_byte2
    TSC[2] for key mix ph1 detection

reserved
    reserved

tkip_rx_ttak
    10-byte unicast TKIP TTAK for Rx

.. _`iwl_mvm_add_sta_key_cmd`:

struct iwl_mvm_add_sta_key_cmd
==============================

.. c:type:: struct iwl_mvm_add_sta_key_cmd

    add/modify sta key

.. _`iwl_mvm_add_sta_key_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_add_sta_key_cmd {
        struct iwl_mvm_add_sta_key_common common;
        __le64 rx_mic_key;
        __le64 tx_mic_key;
        __le64 transmit_seq_cnt;
    }

.. _`iwl_mvm_add_sta_key_cmd.members`:

Members
-------

common
    see \ :c:type:`struct iwl_mvm_add_sta_key_common <iwl_mvm_add_sta_key_common>`\ 

rx_mic_key
    TKIP RX unicast or multicast key

tx_mic_key
    TKIP TX key

transmit_seq_cnt
    TSC, transmit packet number

.. _`iwl_mvm_add_sta_rsp_status`:

enum iwl_mvm_add_sta_rsp_status
===============================

.. c:type:: enum iwl_mvm_add_sta_rsp_status

    status in the response to ADD_STA command

.. _`iwl_mvm_add_sta_rsp_status.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_add_sta_rsp_status {
        ADD_STA_SUCCESS,
        ADD_STA_STATIONS_OVERLOAD,
        ADD_STA_IMMEDIATE_BA_FAILURE,
        ADD_STA_MODIFY_NON_EXISTING_STA
    };

.. _`iwl_mvm_add_sta_rsp_status.constants`:

Constants
---------

ADD_STA_SUCCESS
    operation was executed successfully

ADD_STA_STATIONS_OVERLOAD
    no room left in the fw's station table

ADD_STA_IMMEDIATE_BA_FAILURE
    can't add Rx block ack session

ADD_STA_MODIFY_NON_EXISTING_STA
    driver requested to modify a station that
    doesn't exist.

.. _`iwl_mvm_rm_sta_cmd`:

struct iwl_mvm_rm_sta_cmd
=========================

.. c:type:: struct iwl_mvm_rm_sta_cmd

    Add / modify a station in the fw's station table ( REMOVE_STA = 0x19 )

.. _`iwl_mvm_rm_sta_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_rm_sta_cmd {
        u8 sta_id;
        u8 reserved[3];
    }

.. _`iwl_mvm_rm_sta_cmd.members`:

Members
-------

sta_id
    the station id of the station to be removed

reserved
    reserved

.. _`iwl_mvm_mgmt_mcast_key_cmd_v1`:

struct iwl_mvm_mgmt_mcast_key_cmd_v1
====================================

.. c:type:: struct iwl_mvm_mgmt_mcast_key_cmd_v1

    ( MGMT_MCAST_KEY = 0x1f )

.. _`iwl_mvm_mgmt_mcast_key_cmd_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_mgmt_mcast_key_cmd_v1 {
        __le32 ctrl_flags;
        u8 igtk[16];
        u8 k1[16];
        u8 k2[16];
        __le32 key_id;
        __le32 sta_id;
        __le64 receive_seq_cnt;
    }

.. _`iwl_mvm_mgmt_mcast_key_cmd_v1.members`:

Members
-------

ctrl_flags
    \ :c:type:`enum iwl_sta_key_flag <iwl_sta_key_flag>`\ 

igtk
    IGTK key material

k1
    unused

k2
    unused

key_id
    key ID

sta_id
    station ID that support IGTK

receive_seq_cnt
    initial RSC/PN needed for replay check

.. _`iwl_mvm_mgmt_mcast_key_cmd`:

struct iwl_mvm_mgmt_mcast_key_cmd
=================================

.. c:type:: struct iwl_mvm_mgmt_mcast_key_cmd

    ( MGMT_MCAST_KEY = 0x1f )

.. _`iwl_mvm_mgmt_mcast_key_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_mgmt_mcast_key_cmd {
        __le32 ctrl_flags;
        u8 igtk[32];
        __le32 key_id;
        __le32 sta_id;
        __le64 receive_seq_cnt;
    }

.. _`iwl_mvm_mgmt_mcast_key_cmd.members`:

Members
-------

ctrl_flags
    \ :c:type:`enum iwl_sta_key_flag <iwl_sta_key_flag>`\ 

igtk
    IGTK master key

key_id
    key ID

sta_id
    station ID that support IGTK

receive_seq_cnt
    initial RSC/PN needed for replay check

.. _`iwl_mvm_eosp_notification`:

struct iwl_mvm_eosp_notification
================================

.. c:type:: struct iwl_mvm_eosp_notification

    EOSP notification from firmware

.. _`iwl_mvm_eosp_notification.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_eosp_notification {
        __le32 remain_frame_count;
        __le32 sta_id;
    }

.. _`iwl_mvm_eosp_notification.members`:

Members
-------

remain_frame_count
    # of frames remaining, non-zero if SP was cut
    short by GO absence

sta_id
    station ID

.. This file was automatic generated / don't edit.

