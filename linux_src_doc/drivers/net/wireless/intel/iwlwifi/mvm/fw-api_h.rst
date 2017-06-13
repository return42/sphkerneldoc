.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api.h

.. _`iwl_cmd_response`:

struct iwl_cmd_response
=======================

.. c:type:: struct iwl_cmd_response

    generic response struct for most commands

.. _`iwl_cmd_response.definition`:

Definition
----------

.. code-block:: c

    struct iwl_cmd_response {
        __le32 status;
    }

.. _`iwl_cmd_response.members`:

Members
-------

status
    status of the command asked, changes for each one

.. _`iwl_nvm_access_cmd`:

struct iwl_nvm_access_cmd
=========================

.. c:type:: struct iwl_nvm_access_cmd

    Request the device to send an NVM section

.. _`iwl_nvm_access_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_access_cmd {
        u8 op_code;
        u8 target;
        __le16 type;
        __le16 offset;
        __le16 length;
        u8 data;
    }

.. _`iwl_nvm_access_cmd.members`:

Members
-------

op_code
    0 - read, 1 - write

target
    NVM_ACCESS_TARGET\_\*

type
    NVM_SECTION_TYPE\_\*

offset
    offset in bytes into the section

length
    in bytes, to read/write

data
    if write operation, the data to write. On read its empty

.. _`iwl_nvm_access_resp`:

struct iwl_nvm_access_resp
==========================

.. c:type:: struct iwl_nvm_access_resp

    response to NVM_ACCESS_CMD

.. _`iwl_nvm_access_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_access_resp {
        __le16 offset;
        __le16 length;
        __le16 type;
        __le16 status;
        u8 data;
    }

.. _`iwl_nvm_access_resp.members`:

Members
-------

offset
    offset in bytes into the section

length
    in bytes, either how much was written or read

type
    NVM_SECTION_TYPE\_\*

status
    0 for success, fail otherwise

data
    if read operation, the data returned. Empty on write.

.. _`iwl_error_resp`:

struct iwl_error_resp
=====================

.. c:type:: struct iwl_error_resp

    FW error indication ( REPLY_ERROR = 0x2 )

.. _`iwl_error_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_error_resp {
        __le32 error_type;
        u8 cmd_id;
        u8 reserved1;
        __le16 bad_cmd_seq_num;
        __le32 error_service;
        __le64 timestamp;
    }

.. _`iwl_error_resp.members`:

Members
-------

error_type
    one of FW_ERR\_\*

cmd_id
    the command ID for which the error occured

reserved1
    *undescribed*

bad_cmd_seq_num
    sequence number of the erroneous command

error_service
    which service created the error, applicable only if
    error_type = 2, otherwise 0

timestamp
    TSF in usecs.

.. _`iwl_time_event_cmd`:

struct iwl_time_event_cmd
=========================

.. c:type:: struct iwl_time_event_cmd

    configuring Time Events with struct MAC_TIME_EVENT_DATA_API_S_VER_2 (see also with version 1. determined by IWL_UCODE_TLV_FLAGS) ( TIME_EVENT_CMD = 0x29 )

.. _`iwl_time_event_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_event_cmd {
        __le32 id_and_color;
        __le32 action;
        __le32 id;
        __le32 apply_time;
        __le32 max_delay;
        __le32 depends_on;
        __le32 interval;
        __le32 duration;
        u8 repeat;
        u8 max_frags;
        __le16 policy;
    }

.. _`iwl_time_event_cmd.members`:

Members
-------

id_and_color
    ID and color of the relevant MAC

action
    action to perform, one of FW_CTXT_ACTION\_\*

id
    this field has two meanings, depending on the action:
    If the action is ADD, then it means the type of event to add.
    For all other actions it is the unique event ID assigned when the
    event was added by the FW.

apply_time
    When to start the Time Event (in GP2)

max_delay
    maximum delay to event's start (apply time), in TU

depends_on
    the unique ID of the event we depend on (if any)

interval
    interval between repetitions, in TU

duration
    duration of event in TU

repeat
    how many repetitions to do, can be TE_REPEAT_ENDLESS

max_frags
    maximal number of fragments the Time Event can be divided to

policy
    defines whether uCode shall notify the host or other uCode modules
    on event and/or fragment start and/or end
    using one of TE_INDEPENDENT, TE_DEP_OTHER, TE_DEP_TSF
    TE_EVENT_SOCIOPATHIC
    using TE_ABSENCE and using TE_NOTIF\_\*

.. _`iwl_time_event_resp`:

struct iwl_time_event_resp
==========================

.. c:type:: struct iwl_time_event_resp

    response structure to iwl_time_event_cmd

.. _`iwl_time_event_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_event_resp {
        __le32 status;
        __le32 id;
        __le32 unique_id;
        __le32 id_and_color;
    }

.. _`iwl_time_event_resp.members`:

Members
-------

status
    bit 0 indicates success, all others specify errors

id
    the Time Event type

unique_id
    the unique ID assigned (in ADD) or given (others) to the TE

id_and_color
    ID and color of the relevant MAC

.. _`iwl_time_event_notif`:

struct iwl_time_event_notif
===========================

.. c:type:: struct iwl_time_event_notif

    notifications of time event start/stop ( TIME_EVENT_NOTIFICATION = 0x2a )

.. _`iwl_time_event_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_event_notif {
        __le32 timestamp;
        __le32 session_id;
        __le32 unique_id;
        __le32 id_and_color;
        __le32 action;
        __le32 status;
    }

.. _`iwl_time_event_notif.members`:

Members
-------

timestamp
    action timestamp in GP2

session_id
    session's unique id

unique_id
    unique id of the Time Event itself

id_and_color
    ID and color of the relevant MAC

action
    one of TE_NOTIF_START or TE_NOTIF_END

status
    true if scheduled, false otherwise (not executed)

.. _`iwl_binding_cmd`:

struct iwl_binding_cmd
======================

.. c:type:: struct iwl_binding_cmd

    configuring bindings ( BINDING_CONTEXT_CMD = 0x2b )

.. _`iwl_binding_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_binding_cmd {
        __le32 id_and_color;
        __le32 action;
        __le32 macs;
        __le32 phy;
        __le32 lmac_id;
    }

.. _`iwl_binding_cmd.members`:

Members
-------

id_and_color
    ID and color of the relevant Binding

action
    action to perform, one of FW_CTXT_ACTION\_\*

macs
    array of MAC id and colors which belong to the binding

phy
    PHY id and color which belongs to the binding

lmac_id
    the lmac id the binding belongs to

.. _`iwl_time_quota_data`:

struct iwl_time_quota_data
==========================

.. c:type:: struct iwl_time_quota_data

    configuration of time quota per binding

.. _`iwl_time_quota_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_quota_data {
        __le32 id_and_color;
        __le32 quota;
        __le32 max_duration;
    }

.. _`iwl_time_quota_data.members`:

Members
-------

id_and_color
    ID and color of the relevant Binding

quota
    absolute time quota in TU. The scheduler will try to divide the
    remainig quota (after Time Events) according to this quota.

max_duration
    max uninterrupted context duration in TU

.. _`iwl_time_quota_cmd`:

struct iwl_time_quota_cmd
=========================

.. c:type:: struct iwl_time_quota_cmd

    configuration of time quota between bindings ( TIME_QUOTA_CMD = 0x2c )

.. _`iwl_time_quota_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_quota_cmd {
        struct iwl_time_quota_data quotas;
    }

.. _`iwl_time_quota_cmd.members`:

Members
-------

quotas
    allocations per binding

.. _`iwl_time_quota_cmd.note`:

Note
----

on non-CDB the fourth one is the auxilary mac and is
essentially zero.
On CDB the fourth one is a regular binding.

.. _`iwl_phy_context_cmd`:

struct iwl_phy_context_cmd
==========================

.. c:type:: struct iwl_phy_context_cmd

    config of the PHY context ( PHY_CONTEXT_CMD = 0x8 )

.. _`iwl_phy_context_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_phy_context_cmd {
        __le32 id_and_color;
        __le32 action;
        __le32 apply_time;
        __le32 tx_param_color;
        struct iwl_fw_channel_info ci;
        __le32 txchain_info;
        __le32 rxchain_info;
        __le32 acquisition_data;
        __le32 dsp_cfg_flags;
    }

.. _`iwl_phy_context_cmd.members`:

Members
-------

id_and_color
    ID and color of the relevant Binding

action
    action to perform, one of FW_CTXT_ACTION\_\*

apply_time
    0 means immediate apply and context switch.
    other value means apply new params after X usecs

tx_param_color
    ???

ci
    *undescribed*

txchain_info
    ???

rxchain_info
    ???

acquisition_data
    ???

dsp_cfg_flags
    set to 0

.. _`iwl_radio_version_notif`:

struct iwl_radio_version_notif
==============================

.. c:type:: struct iwl_radio_version_notif

    information on the radio version ( RADIO_VERSION_NOTIFICATION = 0x68 )

.. _`iwl_radio_version_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_radio_version_notif {
        __le32 radio_flavor;
        __le32 radio_step;
        __le32 radio_dash;
    }

.. _`iwl_radio_version_notif.members`:

Members
-------

radio_flavor
    *undescribed*

radio_step
    *undescribed*

radio_dash
    *undescribed*

.. _`iwl_card_state_notif`:

struct iwl_card_state_notif
===========================

.. c:type:: struct iwl_card_state_notif

    information on the radio version ( CARD_STATE_NOTIFICATION = 0xa1 )

.. _`iwl_card_state_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_card_state_notif {
        __le32 flags;
    }

.. _`iwl_card_state_notif.members`:

Members
-------

flags
    %iwl_card_state_flags

.. _`iwl_missed_beacons_notif`:

struct iwl_missed_beacons_notif
===============================

.. c:type:: struct iwl_missed_beacons_notif

    information on missed beacons ( MISSED_BEACONS_NOTIFICATION = 0xa2 )

.. _`iwl_missed_beacons_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_missed_beacons_notif {
        __le32 mac_id;
        __le32 consec_missed_beacons_since_last_rx;
        __le32 consec_missed_beacons;
        __le32 num_expected_beacons;
        __le32 num_recvd_beacons;
    }

.. _`iwl_missed_beacons_notif.members`:

Members
-------

mac_id
    interface ID

consec_missed_beacons_since_last_rx
    number of consecutive missed
    beacons since last RX.

consec_missed_beacons
    number of consecutive missed beacons

num_expected_beacons
    *undescribed*

num_recvd_beacons
    *undescribed*

.. _`iwl_mfuart_load_notif`:

struct iwl_mfuart_load_notif
============================

.. c:type:: struct iwl_mfuart_load_notif

    mfuart image version & status ( MFUART_LOAD_NOTIFICATION = 0xb1 )

.. _`iwl_mfuart_load_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mfuart_load_notif {
        __le32 installed_ver;
        __le32 external_ver;
        __le32 status;
        __le32 duration;
        __le32 image_size;
    }

.. _`iwl_mfuart_load_notif.members`:

Members
-------

installed_ver
    installed image version

external_ver
    external image version

status
    MFUART loading status

duration
    MFUART loading time

image_size
    MFUART image size in bytes

.. _`iwl_mfu_assert_dump_notif`:

struct iwl_mfu_assert_dump_notif
================================

.. c:type:: struct iwl_mfu_assert_dump_notif

    mfuart dump logs ( MFU_ASSERT_DUMP_NTF = 0xfe )

.. _`iwl_mfu_assert_dump_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mfu_assert_dump_notif {
        __le32 assert_id;
        __le32 curr_reset_num;
        __le16 index_num;
        __le16 parts_num;
        __le32 data_size;
        __le32 data;
    }

.. _`iwl_mfu_assert_dump_notif.members`:

Members
-------

assert_id
    mfuart assert id that cause the notif

curr_reset_num
    number of asserts since uptime

index_num
    current chunk id

parts_num
    total number of chunks

data_size
    number of data bytes sent

data
    data buffer

.. _`iwl_set_calib_default_cmd`:

struct iwl_set_calib_default_cmd
================================

.. c:type:: struct iwl_set_calib_default_cmd

    set default value for calibration. ( SET_CALIB_DEFAULT_CMD = 0x8e )

.. _`iwl_set_calib_default_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_set_calib_default_cmd {
        __le16 calib_index;
        __le16 length;
        u8 data;
    }

.. _`iwl_set_calib_default_cmd.members`:

Members
-------

calib_index
    the calibration to set value for

length
    of data

data
    the value to set for the calibration result

.. _`iwl_mcast_filter_cmd`:

struct iwl_mcast_filter_cmd
===========================

.. c:type:: struct iwl_mcast_filter_cmd

    configure multicast filter.

.. _`iwl_mcast_filter_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcast_filter_cmd {
        u8 filter_own;
        u8 port_id;
        u8 count;
        u8 pass_all;
        u8 bssid;
        u8 reserved;
        u8 addr_list;
    }

.. _`iwl_mcast_filter_cmd.members`:

Members
-------

filter_own
    Set 1 to filter out multicast packets sent by station itself

port_id
    Multicast MAC addresses array specifier. This is a strange way
    to identify network interface adopted in host-device IF.
    It is used by FW as index in array of addresses. This array has
    MAX_PORT_ID_NUM members.

count
    Number of MAC addresses in the array

pass_all
    Set 1 to pass all multicast packets.

bssid
    current association BSSID.

reserved
    *undescribed*

addr_list
    Place holder for array of MAC addresses.
    IMPORTANT: add padding if necessary to ensure DWORD alignment.

.. _`iwl_mvm_bcast_filter_attr_offset`:

enum iwl_mvm_bcast_filter_attr_offset
=====================================

.. c:type:: enum iwl_mvm_bcast_filter_attr_offset

    written by fw for each Rx packet

.. _`iwl_mvm_bcast_filter_attr_offset.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_bcast_filter_attr_offset {
        BCAST_FILTER_OFFSET_PAYLOAD_START,
        BCAST_FILTER_OFFSET_IP_END
    };

.. _`iwl_mvm_bcast_filter_attr_offset.constants`:

Constants
---------

BCAST_FILTER_OFFSET_PAYLOAD_START
    offset is from payload start.

BCAST_FILTER_OFFSET_IP_END
    offset is from ip header end (i.e.
    start of ip payload).

.. _`iwl_fw_bcast_filter_attr`:

struct iwl_fw_bcast_filter_attr
===============================

.. c:type:: struct iwl_fw_bcast_filter_attr

    broadcast filter attribute

.. _`iwl_fw_bcast_filter_attr.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_bcast_filter_attr {
        u8 offset_type;
        u8 offset;
        __le16 reserved1;
        __be32 val;
        __be32 mask;
    }

.. _`iwl_fw_bcast_filter_attr.members`:

Members
-------

offset_type
    &enum iwl_mvm_bcast_filter_attr_offset.

offset
    starting offset of this pattern.

reserved1
    *undescribed*

val
    value to match - big endian (MSB is the first
    byte to match from offset pos).

mask
    mask to match (big endian).

.. _`iwl_mvm_bcast_filter_frame_type`:

enum iwl_mvm_bcast_filter_frame_type
====================================

.. c:type:: enum iwl_mvm_bcast_filter_frame_type

    filter frame type

.. _`iwl_mvm_bcast_filter_frame_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_bcast_filter_frame_type {
        BCAST_FILTER_FRAME_TYPE_ALL,
        BCAST_FILTER_FRAME_TYPE_IPV4
    };

.. _`iwl_mvm_bcast_filter_frame_type.constants`:

Constants
---------

BCAST_FILTER_FRAME_TYPE_ALL
    consider all frames.

BCAST_FILTER_FRAME_TYPE_IPV4
    consider only ipv4 frames

.. _`iwl_fw_bcast_filter`:

struct iwl_fw_bcast_filter
==========================

.. c:type:: struct iwl_fw_bcast_filter

    broadcast filter

.. _`iwl_fw_bcast_filter.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_bcast_filter {
        u8 discard;
        u8 frame_type;
        u8 num_attrs;
        u8 reserved1;
        struct iwl_fw_bcast_filter_attr attrs;
    }

.. _`iwl_fw_bcast_filter.members`:

Members
-------

discard
    discard frame (1) or let it pass (0).

frame_type
    &enum iwl_mvm_bcast_filter_frame_type.

num_attrs
    number of valid attributes in this filter.

reserved1
    *undescribed*

attrs
    attributes of this filter. a filter is considered matched
    only when all its attributes are matched (i.e. AND relationship)

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
        __le64 bitmap;
        __le16 ra_tid;
        __le32 start_seq_num;
        __le16 mpdu_rx_count;
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

.. _`iwl_fw_bcast_mac`:

struct iwl_fw_bcast_mac
=======================

.. c:type:: struct iwl_fw_bcast_mac

    per-mac broadcast filtering configuration.

.. _`iwl_fw_bcast_mac.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_bcast_mac {
        u8 default_discard;
        u8 reserved1;
        __le16 attached_filters;
    }

.. _`iwl_fw_bcast_mac.members`:

Members
-------

default_discard
    default action for this mac (discard (1) / pass (0)).

reserved1
    *undescribed*

attached_filters
    bitmap of relevant filters for this mac.

.. _`iwl_bcast_filter_cmd`:

struct iwl_bcast_filter_cmd
===========================

.. c:type:: struct iwl_bcast_filter_cmd

    broadcast filtering configuration

.. _`iwl_bcast_filter_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bcast_filter_cmd {
        u8 disable;
        u8 max_bcast_filters;
        u8 max_macs;
        u8 reserved1;
        struct iwl_fw_bcast_filter filters;
        struct iwl_fw_bcast_mac macs;
    }

.. _`iwl_bcast_filter_cmd.members`:

Members
-------

disable
    enable (0) / disable (1)

max_bcast_filters
    max number of filters (MAX_BCAST_FILTERS)

max_macs
    max number of macs (NUM_MAC_INDEX_DRIVER)

reserved1
    *undescribed*

filters
    broadcast filters

macs
    broadcast filtering configuration per-mac

.. _`iwl_mvm_marker`:

struct iwl_mvm_marker
=====================

.. c:type:: struct iwl_mvm_marker

    mark info into the usniffer logs

.. _`iwl_mvm_marker.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_marker {
        u8 dwLen;
        u8 markerId;
        __le16 reserved;
        __le64 timestamp;
        __le32 metadata;
    }

.. _`iwl_mvm_marker.members`:

Members
-------

dwLen
    *undescribed*

markerId
    *undescribed*

reserved
    reserved.

timestamp
    in milliseconds since 1970-01-01 00:00:00 UTC

metadata
    additional meta data that will be written to the unsiffer log

.. _`iwl_mvm_marker.description`:

Description
-----------

(MARKER_CMD = 0xcb)

Mark the UTC time stamp into the usniffer logs together with additional
metadata, so the usniffer output can be parsed.
In the command response the ucode will return the GP2 time.

.. _`iwl_dc2dc_config_cmd`:

struct iwl_dc2dc_config_cmd
===========================

.. c:type:: struct iwl_dc2dc_config_cmd

    configure dc2dc values

.. _`iwl_dc2dc_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dc2dc_config_cmd {
        __le32 flags;
        __le32 enable_low_power_mode;
        __le32 dc2dc_freq_tune0;
        __le32 dc2dc_freq_tune1;
    }

.. _`iwl_dc2dc_config_cmd.members`:

Members
-------

flags
    set/get dc2dc

enable_low_power_mode
    not used.

dc2dc_freq_tune0
    frequency divider - digital domain

dc2dc_freq_tune1
    frequency divider - analog domain

.. _`iwl_dc2dc_config_cmd.description`:

Description
-----------

(DC2DC_CONFIG_CMD = 0x83)

Set/Get & configure dc2dc values.
The command always returns the current dc2dc values.

.. _`iwl_dc2dc_config_resp`:

struct iwl_dc2dc_config_resp
============================

.. c:type:: struct iwl_dc2dc_config_resp

    response for iwl_dc2dc_config_cmd

.. _`iwl_dc2dc_config_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dc2dc_config_resp {
        __le32 dc2dc_freq_tune0;
        __le32 dc2dc_freq_tune1;
    }

.. _`iwl_dc2dc_config_resp.members`:

Members
-------

dc2dc_freq_tune0
    frequency divider - digital domain

dc2dc_freq_tune1
    frequency divider - analog domain

.. _`iwl_dc2dc_config_resp.description`:

Description
-----------

Current dc2dc values returned by the FW.

.. _`iwl_mcc_update_cmd_v1`:

struct iwl_mcc_update_cmd_v1
============================

.. c:type:: struct iwl_mcc_update_cmd_v1

    Request the device to update geographic regulatory profile according to the given MCC (Mobile Country Code). The MCC is two letter-code, ascii upper case[A-Z] or '00' for world domain. 'ZZ' MCC will be used to switch to NVM default profile; in this case, the MCC in the cmd response will be the relevant MCC in the NVM.

.. _`iwl_mcc_update_cmd_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcc_update_cmd_v1 {
        __le16 mcc;
        u8 source_id;
        u8 reserved;
    }

.. _`iwl_mcc_update_cmd_v1.members`:

Members
-------

mcc
    given mobile country code

source_id
    the source from where we got the MCC, see iwl_mcc_source

reserved
    reserved for alignment

.. _`iwl_mcc_update_cmd`:

struct iwl_mcc_update_cmd
=========================

.. c:type:: struct iwl_mcc_update_cmd

    Request the device to update geographic regulatory profile according to the given MCC (Mobile Country Code). The MCC is two letter-code, ascii upper case[A-Z] or '00' for world domain. 'ZZ' MCC will be used to switch to NVM default profile; in this case, the MCC in the cmd response will be the relevant MCC in the NVM.

.. _`iwl_mcc_update_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcc_update_cmd {
        __le16 mcc;
        u8 source_id;
        u8 reserved;
        __le32 key;
        __le32 reserved2;
    }

.. _`iwl_mcc_update_cmd.members`:

Members
-------

mcc
    given mobile country code

source_id
    the source from where we got the MCC, see iwl_mcc_source

reserved
    reserved for alignment

key
    integrity key for MCC API OEM testing

reserved2
    reserved

.. _`iwl_mcc_chub_notif`:

struct iwl_mcc_chub_notif
=========================

.. c:type:: struct iwl_mcc_chub_notif

    chub notifies of mcc change (MCC_CHUB_UPDATE_CMD = 0xc9) The Chub (Communication Hub, CommsHUB) is a HW component that connects to the cellular and connectivity cores that gets updates of the mcc, and notifies the ucode directly of any mcc change. The ucode requests the driver to request the device to update geographic regulatory  profile according to the given MCC (Mobile Country Code). The MCC is two letter-code, ascii upper case[A-Z] or '00' for world domain. 'ZZ' MCC will be used to switch to NVM default profile; in this case, the MCC in the cmd response will be the relevant MCC in the NVM.

.. _`iwl_mcc_chub_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcc_chub_notif {
        u16 mcc;
        u8 source_id;
        u8 reserved1;
    }

.. _`iwl_mcc_chub_notif.members`:

Members
-------

mcc
    given mobile country code

source_id
    identity of the change originator, see iwl_mcc_source

reserved1
    reserved for alignment

.. _`iwl_dts_control_measurement_mode`:

enum iwl_dts_control_measurement_mode
=====================================

.. c:type:: enum iwl_dts_control_measurement_mode

    DTS measurement type

.. _`iwl_dts_control_measurement_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_dts_control_measurement_mode {
        DTS_AUTOMATIC,
        DTS_REQUEST_READ,
        DTS_OVER_WRITE,
        DTS_DIRECT_WITHOUT_MEASURE
    };

.. _`iwl_dts_control_measurement_mode.constants`:

Constants
---------

DTS_AUTOMATIC
    Automatic mode (full SW control). Provide temperature read
    back (latest value. Not waiting for new value). Use automatic
    SW DTS configuration.

DTS_REQUEST_READ
    Request DTS read. Configure DTS with manual settings,
    trigger DTS reading and provide read back temperature read
    when available.

DTS_OVER_WRITE
    over-write the DTS temperatures in the SW until next read

DTS_DIRECT_WITHOUT_MEASURE
    DTS returns its latest temperature result,
    without measurement trigger.

.. _`iwl_dts_used`:

enum iwl_dts_used
=================

.. c:type:: enum iwl_dts_used

    DTS to use or used for measurement in the DTS request

.. _`iwl_dts_used.definition`:

Definition
----------

.. code-block:: c

    enum iwl_dts_used {
        DTS_USE_TOP,
        DTS_USE_CHAIN_A,
        DTS_USE_CHAIN_B,
        DTS_USE_CHAIN_C,
        XTAL_TEMPERATURE
    };

.. _`iwl_dts_used.constants`:

Constants
---------

DTS_USE_TOP
    Top

DTS_USE_CHAIN_A
    chain A

DTS_USE_CHAIN_B
    chain B

DTS_USE_CHAIN_C
    chain C
    \ ``XTAL_TEMPERATURE``\  - read temperature from xtal

XTAL_TEMPERATURE
    *undescribed*

.. _`iwl_dts_bit_mode`:

enum iwl_dts_bit_mode
=====================

.. c:type:: enum iwl_dts_bit_mode

    bit-mode to use in DTS request read mode

.. _`iwl_dts_bit_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_dts_bit_mode {
        DTS_BIT6_MODE,
        DTS_BIT8_MODE
    };

.. _`iwl_dts_bit_mode.constants`:

Constants
---------

DTS_BIT6_MODE
    bit 6 mode

DTS_BIT8_MODE
    bit 8 mode

.. _`iwl_dts_measurement_notif_v1`:

struct iwl_dts_measurement_notif_v1
===================================

.. c:type:: struct iwl_dts_measurement_notif_v1

    measurements notification

.. _`iwl_dts_measurement_notif_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dts_measurement_notif_v1 {
        __le32 temp;
        __le32 voltage;
    }

.. _`iwl_dts_measurement_notif_v1.members`:

Members
-------

temp
    the measured temperature

voltage
    the measured voltage

.. _`iwl_dts_measurement_notif_v2`:

struct iwl_dts_measurement_notif_v2
===================================

.. c:type:: struct iwl_dts_measurement_notif_v2

    measurements notification

.. _`iwl_dts_measurement_notif_v2.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dts_measurement_notif_v2 {
        __le32 temp;
        __le32 voltage;
        __le32 threshold_idx;
    }

.. _`iwl_dts_measurement_notif_v2.members`:

Members
-------

temp
    the measured temperature

voltage
    the measured voltage

threshold_idx
    the trip index that was crossed

.. _`ct_kill_notif`:

struct ct_kill_notif
====================

.. c:type:: struct ct_kill_notif

    CT-kill entry notification

.. _`ct_kill_notif.definition`:

Definition
----------

.. code-block:: c

    struct ct_kill_notif {
        __le16 temperature;
        __le16 reserved;
    }

.. _`ct_kill_notif.members`:

Members
-------

temperature
    the current temperature in celsius

reserved
    reserved

.. _`iwl_mvm_ctdp_cmd_operation`:

enum iwl_mvm_ctdp_cmd_operation
===============================

.. c:type:: enum iwl_mvm_ctdp_cmd_operation

    CTDP command operations

.. _`iwl_mvm_ctdp_cmd_operation.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_ctdp_cmd_operation {
        CTDP_CMD_OPERATION_START,
        CTDP_CMD_OPERATION_STOP,
        CTDP_CMD_OPERATION_REPORT
    };

.. _`iwl_mvm_ctdp_cmd_operation.constants`:

Constants
---------

CTDP_CMD_OPERATION_START
    update the current budget

CTDP_CMD_OPERATION_STOP
    stop ctdp

CTDP_CMD_OPERATION_REPORT
    get the avgerage budget

.. _`iwl_mvm_ctdp_cmd`:

struct iwl_mvm_ctdp_cmd
=======================

.. c:type:: struct iwl_mvm_ctdp_cmd

    track and manage the FW power consumption budget

.. _`iwl_mvm_ctdp_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_ctdp_cmd {
        __le32 operation;
        __le32 budget;
        __le32 window_size;
    }

.. _`iwl_mvm_ctdp_cmd.members`:

Members
-------

operation
    see \ :c:type:`enum iwl_mvm_ctdp_cmd_operation <iwl_mvm_ctdp_cmd_operation>`\ 

budget
    the budget in milliwatt

window_size
    defined in API but not used

.. _`temp_report_ths_cmd`:

struct temp_report_ths_cmd
==========================

.. c:type:: struct temp_report_ths_cmd

    set temperature thresholds

.. _`temp_report_ths_cmd.definition`:

Definition
----------

.. code-block:: c

    struct temp_report_ths_cmd {
        __le32 num_temps;
        __le16 thresholds;
    }

.. _`temp_report_ths_cmd.members`:

Members
-------

num_temps
    number of temperature thresholds passed

thresholds
    array with the thresholds to be configured

.. _`iwl_shared_mem_lmac_cfg`:

struct iwl_shared_mem_lmac_cfg
==============================

.. c:type:: struct iwl_shared_mem_lmac_cfg

    LMAC shared memory configuration

.. _`iwl_shared_mem_lmac_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_shared_mem_lmac_cfg {
        __le32 txfifo_addr;
        __le32 txfifo_size;
        __le32 rxfifo1_addr;
        __le32 rxfifo1_size;
    }

.. _`iwl_shared_mem_lmac_cfg.members`:

Members
-------

txfifo_addr
    start addr of TXF0 (excluding the context table 0.5KB)

txfifo_size
    size of TX FIFOs

rxfifo1_addr
    RXF1 addr

rxfifo1_size
    RXF1 size

.. _`iwl_mu_group_mgmt_notif`:

struct iwl_mu_group_mgmt_notif
==============================

.. c:type:: struct iwl_mu_group_mgmt_notif

    VHT MU-MIMO group id notification

.. _`iwl_mu_group_mgmt_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mu_group_mgmt_notif {
        __le32 membership_status;
        __le32 user_position;
    }

.. _`iwl_mu_group_mgmt_notif.members`:

Members
-------

membership_status
    a bitmap of MU groups

user_position
    the position of station in a group. If the station is in the
    group then bits (group \* 2) is the position -1

.. _`iwl_dbg_mem_access_cmd`:

struct iwl_dbg_mem_access_cmd
=============================

.. c:type:: struct iwl_dbg_mem_access_cmd

    Request the device to read/write memory

.. _`iwl_dbg_mem_access_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dbg_mem_access_cmd {
        __le32 op;
        __le32 addr;
        __le32 len;
        __le32 data;
    }

.. _`iwl_dbg_mem_access_cmd.members`:

Members
-------

op
    DEBUG_MEM_OP\_\*

addr
    address to read/write from/to

len
    in dwords, to read/write

data
    for write opeations, contains the source buffer

.. _`iwl_dbg_mem_access_rsp`:

struct iwl_dbg_mem_access_rsp
=============================

.. c:type:: struct iwl_dbg_mem_access_rsp

    Response to debug mem commands

.. _`iwl_dbg_mem_access_rsp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_dbg_mem_access_rsp {
        __le32 status;
        __le32 len;
        __le32 data;
    }

.. _`iwl_dbg_mem_access_rsp.members`:

Members
-------

status
    DEBUG_MEM_STATUS\_\*

len
    read dwords (0 for write operations)

data
    contains the read DWs

.. _`iwl_nvm_access_complete_cmd`:

struct iwl_nvm_access_complete_cmd
==================================

.. c:type:: struct iwl_nvm_access_complete_cmd

    NVM_ACCESS commands are completed

.. _`iwl_nvm_access_complete_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_access_complete_cmd {
        __le32 reserved;
    }

.. _`iwl_nvm_access_complete_cmd.members`:

Members
-------

reserved
    *undescribed*

.. _`iwl_extended_cfg_flags`:

enum iwl_extended_cfg_flags
===========================

.. c:type:: enum iwl_extended_cfg_flags

    commands driver may send before finishing init flow

.. _`iwl_extended_cfg_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_extended_cfg_flags {
        IWL_INIT_DEBUG_CFG,
        IWL_INIT_NVM,
        IWL_INIT_PHY
    };

.. _`iwl_extended_cfg_flags.constants`:

Constants
---------

IWL_INIT_DEBUG_CFG
    driver is going to send debug config command

IWL_INIT_NVM
    driver is going to send NVM_ACCESS commands

IWL_INIT_PHY
    driver is going to send PHY_DB commands

.. _`iwl_init_extended_cfg_cmd`:

struct iwl_init_extended_cfg_cmd
================================

.. c:type:: struct iwl_init_extended_cfg_cmd

    mark what commands ucode should wait for before finishing init flows

.. _`iwl_init_extended_cfg_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_init_extended_cfg_cmd {
        __le32 init_flags;
    }

.. _`iwl_init_extended_cfg_cmd.members`:

Members
-------

init_flags
    values from iwl_extended_cfg_flags

.. This file was automatic generated / don't edit.

