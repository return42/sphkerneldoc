.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/quantenna/qtnfmac/qlink.h

.. _`qlink_msg_type`:

enum qlink_msg_type
===================

.. c:type:: enum qlink_msg_type

    QLINK message types

.. _`qlink_msg_type.definition`:

Definition
----------

.. code-block:: c

    enum qlink_msg_type {
        QLINK_MSG_TYPE_CMD,
        QLINK_MSG_TYPE_CMDRSP,
        QLINK_MSG_TYPE_EVENT
    };

.. _`qlink_msg_type.constants`:

Constants
---------

QLINK_MSG_TYPE_CMD
    Message is carrying data of a command sent from
    driver to wireless hardware.

QLINK_MSG_TYPE_CMDRSP
    Message is carrying data of a response to a command.
    Sent from wireless HW to driver in reply to previously issued command.

QLINK_MSG_TYPE_EVENT
    Data for an event originated in wireless hardware and
    sent asynchronously to driver.

.. _`qlink_msg_type.description`:

Description
-----------

Used to distinguish between message types of QLINK protocol.

.. _`qlink_msg_header`:

struct qlink_msg_header
=======================

.. c:type:: struct qlink_msg_header

    common QLINK protocol message header

.. _`qlink_msg_header.definition`:

Definition
----------

.. code-block:: c

    struct qlink_msg_header {
        __le16 type;
        __le16 len;
    }

.. _`qlink_msg_header.members`:

Members
-------

type
    Message type, one of \ :c:type:`enum qlink_msg_type <qlink_msg_type>`\ .

len
    Total length of message including all headers.

.. _`qlink_msg_header.description`:

Description
-----------

Portion of QLINK protocol header common for all message types.

.. _`qlink_hw_capab`:

enum qlink_hw_capab
===================

.. c:type:: enum qlink_hw_capab

    device capabilities.

.. _`qlink_hw_capab.definition`:

Definition
----------

.. code-block:: c

    enum qlink_hw_capab {
        QLINK_HW_CAPAB_REG_UPDATE,
        QLINK_HW_CAPAB_STA_INACT_TIMEOUT,
        QLINK_HW_CAPAB_DFS_OFFLOAD
    };

.. _`qlink_hw_capab.constants`:

Constants
---------

QLINK_HW_CAPAB_REG_UPDATE
    device can update it's regulatory region.

QLINK_HW_CAPAB_STA_INACT_TIMEOUT
    device implements a logic to kick-out
    associated STAs due to inactivity. Inactivity timeout period is taken
    from QLINK_CMD_START_AP parameters.

QLINK_HW_CAPAB_DFS_OFFLOAD
    device implements DFS offload functionality

.. _`qlink_intf_info`:

struct qlink_intf_info
======================

.. c:type:: struct qlink_intf_info

    information on virtual interface.

.. _`qlink_intf_info.definition`:

Definition
----------

.. code-block:: c

    struct qlink_intf_info {
        __le16 if_type;
        __le16 vlanid;
        u8 mac_addr[ETH_ALEN];
        u8 rsvd[2];
    }

.. _`qlink_intf_info.members`:

Members
-------

if_type
    Mode of interface operation, one of \ :c:type:`enum qlink_iface_type <qlink_iface_type>`\ 

vlanid
    VLAN ID for AP_VLAN interface type

mac_addr
    MAC address of virtual interface.

rsvd
    *undescribed*

.. _`qlink_intf_info.description`:

Description
-----------

Data describing a single virtual interface.

.. _`qlink_channel`:

struct qlink_channel
====================

.. c:type:: struct qlink_channel

    qlink control channel definition

.. _`qlink_channel.definition`:

Definition
----------

.. code-block:: c

    struct qlink_channel {
        __le16 hw_value;
        __le16 center_freq;
        __le32 flags;
        u8 band;
        u8 max_antenna_gain;
        u8 max_power;
        u8 max_reg_power;
        __le32 dfs_cac_ms;
        u8 dfs_state;
        u8 beacon_found;
        u8 rsvd[2];
    }

.. _`qlink_channel.members`:

Members
-------

hw_value
    hardware-specific value for the channel

center_freq
    center frequency in MHz

flags
    channel flags from \ :c:type:`enum qlink_channel_flags <qlink_channel_flags>`\ 

band
    band this channel belongs to

max_antenna_gain
    maximum antenna gain in dBi

max_power
    maximum transmission power (in dBm)

max_reg_power
    maximum regulatory transmission power (in dBm)

dfs_cac_ms
    *undescribed*

dfs_state
    current state of this channel.
    Only relevant if radar is required on this channel.

beacon_found
    helper to regulatory code to indicate when a beacon
    has been found on this channel. Use \ :c:func:`regulatory_hint_found_beacon`\ 
    to enable this, this is useful only on 5 GHz band.

rsvd
    *undescribed*

.. _`qlink_chandef`:

struct qlink_chandef
====================

.. c:type:: struct qlink_chandef

    qlink channel definition

.. _`qlink_chandef.definition`:

Definition
----------

.. code-block:: c

    struct qlink_chandef {
        struct qlink_channel chan;
        __le16 center_freq1;
        __le16 center_freq2;
        u8 width;
        u8 rsvd;
    }

.. _`qlink_chandef.members`:

Members
-------

chan
    primary channel definition

center_freq1
    center frequency of first segment

center_freq2
    center frequency of second segment (80+80 only)

width
    channel width, one of \ ``enum``\  qlink_channel_width

rsvd
    *undescribed*

.. _`qlink_sta_info_state`:

struct qlink_sta_info_state
===========================

.. c:type:: struct qlink_sta_info_state

    station flags mask/value

.. _`qlink_sta_info_state.definition`:

Definition
----------

.. code-block:: c

    struct qlink_sta_info_state {
        __le32 mask;
        __le32 value;
    }

.. _`qlink_sta_info_state.members`:

Members
-------

mask
    STA flags mask, bitmap of \ :c:type:`enum qlink_sta_flags <qlink_sta_flags>`\ 

value
    STA flags values, bitmap of \ :c:type:`enum qlink_sta_flags <qlink_sta_flags>`\ 

.. _`qlink_cmd_type`:

enum qlink_cmd_type
===================

.. c:type:: enum qlink_cmd_type

    list of supported commands

.. _`qlink_cmd_type.definition`:

Definition
----------

.. code-block:: c

    enum qlink_cmd_type {
        QLINK_CMD_FW_INIT,
        QLINK_CMD_FW_DEINIT,
        QLINK_CMD_REGISTER_MGMT,
        QLINK_CMD_SEND_MGMT_FRAME,
        QLINK_CMD_MGMT_SET_APPIE,
        QLINK_CMD_PHY_PARAMS_GET,
        QLINK_CMD_PHY_PARAMS_SET,
        QLINK_CMD_GET_HW_INFO,
        QLINK_CMD_MAC_INFO,
        QLINK_CMD_ADD_INTF,
        QLINK_CMD_DEL_INTF,
        QLINK_CMD_CHANGE_INTF,
        QLINK_CMD_UPDOWN_INTF,
        QLINK_CMD_REG_NOTIFY,
        QLINK_CMD_BAND_INFO_GET,
        QLINK_CMD_CHAN_SWITCH,
        QLINK_CMD_CHAN_GET,
        QLINK_CMD_START_CAC,
        QLINK_CMD_START_AP,
        QLINK_CMD_STOP_AP,
        QLINK_CMD_SET_MAC_ACL,
        QLINK_CMD_GET_STA_INFO,
        QLINK_CMD_ADD_KEY,
        QLINK_CMD_DEL_KEY,
        QLINK_CMD_SET_DEFAULT_KEY,
        QLINK_CMD_SET_DEFAULT_MGMT_KEY,
        QLINK_CMD_CHANGE_STA,
        QLINK_CMD_DEL_STA,
        QLINK_CMD_SCAN,
        QLINK_CMD_CHAN_STATS,
        QLINK_CMD_CONNECT,
        QLINK_CMD_DISCONNECT
    };

.. _`qlink_cmd_type.constants`:

Constants
---------

QLINK_CMD_FW_INIT
    *undescribed*

QLINK_CMD_FW_DEINIT
    *undescribed*

QLINK_CMD_REGISTER_MGMT
    *undescribed*

QLINK_CMD_SEND_MGMT_FRAME
    *undescribed*

QLINK_CMD_MGMT_SET_APPIE
    *undescribed*

QLINK_CMD_PHY_PARAMS_GET
    *undescribed*

QLINK_CMD_PHY_PARAMS_SET
    *undescribed*

QLINK_CMD_GET_HW_INFO
    *undescribed*

QLINK_CMD_MAC_INFO
    *undescribed*

QLINK_CMD_ADD_INTF
    *undescribed*

QLINK_CMD_DEL_INTF
    *undescribed*

QLINK_CMD_CHANGE_INTF
    *undescribed*

QLINK_CMD_UPDOWN_INTF
    *undescribed*

QLINK_CMD_REG_NOTIFY
    notify device about regulatory domain change. This
    command is supported only if device reports QLINK_HW_SUPPORTS_REG_UPDATE
    capability.

QLINK_CMD_BAND_INFO_GET
    for the specified MAC and specified band, get
    the band's description including number of operational channels and
    info on each channel, HT/VHT capabilities, supported rates etc.
    This command is generic to a specified MAC, interface index must be set
    to QLINK_VIFID_RSVD in command header.

QLINK_CMD_CHAN_SWITCH
    *undescribed*

QLINK_CMD_CHAN_GET
    *undescribed*

QLINK_CMD_START_CAC
    start radar detection procedure on a specified channel.

QLINK_CMD_START_AP
    *undescribed*

QLINK_CMD_STOP_AP
    *undescribed*

QLINK_CMD_SET_MAC_ACL
    *undescribed*

QLINK_CMD_GET_STA_INFO
    *undescribed*

QLINK_CMD_ADD_KEY
    *undescribed*

QLINK_CMD_DEL_KEY
    *undescribed*

QLINK_CMD_SET_DEFAULT_KEY
    *undescribed*

QLINK_CMD_SET_DEFAULT_MGMT_KEY
    *undescribed*

QLINK_CMD_CHANGE_STA
    *undescribed*

QLINK_CMD_DEL_STA
    *undescribed*

QLINK_CMD_SCAN
    *undescribed*

QLINK_CMD_CHAN_STATS
    *undescribed*

QLINK_CMD_CONNECT
    *undescribed*

QLINK_CMD_DISCONNECT
    *undescribed*

.. _`qlink_cmd_type.description`:

Description
-----------

Commands are QLINK messages of type \ ``QLINK_MSG_TYPE_CMD``\ , sent by driver to
wireless network device for processing. Device is expected to send back a
reply message of type \ :c:type:`struct QLINK_MSG_TYPE_CMDRSP <QLINK_MSG_TYPE_CMDRSP>`\ , containing at least command
execution status (one of \ :c:type:`enum qlink_cmd_result <qlink_cmd_result>`\ ). Reply message
may also contain data payload specific to the command type.

.. _`qlink_cmd`:

struct qlink_cmd
================

.. c:type:: struct qlink_cmd

    QLINK command message header

.. _`qlink_cmd.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd {
        struct qlink_msg_header mhdr;
        __le16 cmd_id;
        __le16 seq_num;
        u8 rsvd[2];
        u8 macid;
        u8 vifid;
    }

.. _`qlink_cmd.members`:

Members
-------

mhdr
    Common QLINK message header.

cmd_id
    command id, one of \ :c:type:`enum qlink_cmd_type <qlink_cmd_type>`\ .

seq_num
    sequence number of command message, used for matching with
    response message.

rsvd
    *undescribed*

macid
    index of physical radio device the command is destined to or
    QLINK_MACID_RSVD if not applicable.

vifid
    index of virtual wireless interface on specified \ ``macid``\  the command
    is destined to or QLINK_VIFID_RSVD if not applicable.

.. _`qlink_cmd.description`:

Description
-----------

Header used for QLINK messages of QLINK_MSG_TYPE_CMD type.

.. _`qlink_cmd_manage_intf`:

struct qlink_cmd_manage_intf
============================

.. c:type:: struct qlink_cmd_manage_intf

    interface management command

.. _`qlink_cmd_manage_intf.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_manage_intf {
        struct qlink_cmd chdr;
        struct qlink_intf_info intf_info;
    }

.. _`qlink_cmd_manage_intf.members`:

Members
-------

chdr
    *undescribed*

intf_info
    interface description.

.. _`qlink_cmd_manage_intf.description`:

Description
-----------

Data for interface management commands QLINK_CMD_ADD_INTF, QLINK_CMD_DEL_INTF
and QLINK_CMD_CHANGE_INTF.

.. _`qlink_cmd_mgmt_frame_register`:

struct qlink_cmd_mgmt_frame_register
====================================

.. c:type:: struct qlink_cmd_mgmt_frame_register

    data for QLINK_CMD_REGISTER_MGMT

.. _`qlink_cmd_mgmt_frame_register.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_mgmt_frame_register {
        struct qlink_cmd chdr;
        __le16 frame_type;
        u8 do_register;
    }

.. _`qlink_cmd_mgmt_frame_register.members`:

Members
-------

chdr
    *undescribed*

frame_type
    MGMT frame type the registration request describes, one of
    \ :c:type:`enum qlink_mgmt_frame_type <qlink_mgmt_frame_type>`\ .

do_register
    0 - unregister, otherwise register for reception of specified
    MGMT frame type.

.. _`qlink_cmd_mgmt_frame_tx`:

struct qlink_cmd_mgmt_frame_tx
==============================

.. c:type:: struct qlink_cmd_mgmt_frame_tx

    data for QLINK_CMD_SEND_MGMT_FRAME command

.. _`qlink_cmd_mgmt_frame_tx.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_mgmt_frame_tx {
        struct qlink_cmd chdr;
        __le32 cookie;
        __le16 freq;
        __le16 flags;
        u8 frame_data[0];
    }

.. _`qlink_cmd_mgmt_frame_tx.members`:

Members
-------

chdr
    *undescribed*

cookie
    opaque request identifier.

freq
    Frequency to use for frame transmission.

flags
    Transmission flags, one of \ :c:type:`enum qlink_mgmt_frame_tx_flags <qlink_mgmt_frame_tx_flags>`\ .

frame_data
    frame to transmit.

.. _`qlink_cmd_get_sta_info`:

struct qlink_cmd_get_sta_info
=============================

.. c:type:: struct qlink_cmd_get_sta_info

    data for QLINK_CMD_GET_STA_INFO command

.. _`qlink_cmd_get_sta_info.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_get_sta_info {
        struct qlink_cmd chdr;
        u8 sta_addr[ETH_ALEN];
    }

.. _`qlink_cmd_get_sta_info.members`:

Members
-------

chdr
    *undescribed*

sta_addr
    MAC address of the STA statistics is requested for.

.. _`qlink_cmd_add_key`:

struct qlink_cmd_add_key
========================

.. c:type:: struct qlink_cmd_add_key

    data for QLINK_CMD_ADD_KEY command.

.. _`qlink_cmd_add_key.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_add_key {
        struct qlink_cmd chdr;
        u8 key_index;
        u8 pairwise;
        u8 addr[ETH_ALEN];
        __le32 cipher;
        __le16 vlanid;
        u8 key_data[0];
    }

.. _`qlink_cmd_add_key.members`:

Members
-------

chdr
    *undescribed*

key_index
    index of the key being installed.

pairwise
    whether to use pairwise key.

addr
    MAC address of a STA key is being installed to.

cipher
    cipher suite.

vlanid
    VLAN ID for AP_VLAN interface type

key_data
    key data itself.

.. _`qlink_cmd_del_key`:

struct qlink_cmd_del_key
========================

.. c:type:: struct qlink_cmd_del_key

    data for QLINK_CMD_DEL_KEY command

.. _`qlink_cmd_del_key.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_del_key {
        struct qlink_cmd chdr;
        u8 key_index;
        u8 pairwise;
        u8 addr[ETH_ALEN];
    }

.. _`qlink_cmd_del_key.members`:

Members
-------

chdr
    *undescribed*

key_index
    index of the key being removed.

pairwise
    whether to use pairwise key.

addr
    MAC address of a STA for which a key is removed.

.. _`qlink_cmd_set_def_key`:

struct qlink_cmd_set_def_key
============================

.. c:type:: struct qlink_cmd_set_def_key

    data for QLINK_CMD_SET_DEFAULT_KEY command

.. _`qlink_cmd_set_def_key.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_set_def_key {
        struct qlink_cmd chdr;
        u8 key_index;
        u8 unicast;
        u8 multicast;
    }

.. _`qlink_cmd_set_def_key.members`:

Members
-------

chdr
    *undescribed*

key_index
    index of the key to be set as default one.

unicast
    key is unicast.

multicast
    key is multicast.

.. _`qlink_cmd_set_def_mgmt_key`:

struct qlink_cmd_set_def_mgmt_key
=================================

.. c:type:: struct qlink_cmd_set_def_mgmt_key

    data for QLINK_CMD_SET_DEFAULT_MGMT_KEY

.. _`qlink_cmd_set_def_mgmt_key.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_set_def_mgmt_key {
        struct qlink_cmd chdr;
        u8 key_index;
    }

.. _`qlink_cmd_set_def_mgmt_key.members`:

Members
-------

chdr
    *undescribed*

key_index
    index of the key to be set as default MGMT key.

.. _`qlink_cmd_change_sta`:

struct qlink_cmd_change_sta
===========================

.. c:type:: struct qlink_cmd_change_sta

    data for QLINK_CMD_CHANGE_STA command

.. _`qlink_cmd_change_sta.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_change_sta {
        struct qlink_cmd chdr;
        struct qlink_sta_info_state flag_update;
        __le16 if_type;
        __le16 vlanid;
        u8 sta_addr[ETH_ALEN];
    }

.. _`qlink_cmd_change_sta.members`:

Members
-------

chdr
    *undescribed*

flag_update
    STA flags to update

if_type
    Mode of interface operation, one of \ :c:type:`enum qlink_iface_type <qlink_iface_type>`\ 

vlanid
    VLAN ID to assign to specific STA

sta_addr
    address of the STA for which parameters are set.

.. _`qlink_cmd_del_sta`:

struct qlink_cmd_del_sta
========================

.. c:type:: struct qlink_cmd_del_sta

    data for QLINK_CMD_DEL_STA command.

.. _`qlink_cmd_del_sta.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_del_sta {
        struct qlink_cmd chdr;
        __le16 reason_code;
        u8 subtype;
        u8 sta_addr[ETH_ALEN];
    }

.. _`qlink_cmd_del_sta.members`:

Members
-------

chdr
    *undescribed*

reason_code
    *undescribed*

subtype
    *undescribed*

sta_addr
    *undescribed*

.. _`qlink_cmd_del_sta.description`:

Description
-----------

See \ :c:type:`struct station_del_parameters <station_del_parameters>`\ 

.. _`qlink_cmd_connect`:

struct qlink_cmd_connect
========================

.. c:type:: struct qlink_cmd_connect

    data for QLINK_CMD_CONNECT command

.. _`qlink_cmd_connect.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_connect {
        struct qlink_cmd chdr;
        u8 bssid[ETH_ALEN];
        u8 bssid_hint[ETH_ALEN];
        u8 prev_bssid[ETH_ALEN];
        __le16 bg_scan_period;
        __le32 flags;
        struct ieee80211_ht_cap ht_capa;
        struct ieee80211_ht_cap ht_capa_mask;
        struct ieee80211_vht_cap vht_capa;
        struct ieee80211_vht_cap vht_capa_mask;
        struct qlink_auth_encr aen;
        u8 mfp;
        u8 pbss;
        u8 rsvd[2];
        u8 payload[0];
    }

.. _`qlink_cmd_connect.members`:

Members
-------

chdr
    *undescribed*

bssid
    BSSID of the BSS to connect to.

bssid_hint
    recommended AP BSSID for initial connection to the BSS or
    00:00:00:00:00:00 if not specified.

prev_bssid
    previous BSSID, if specified (not 00:00:00:00:00:00) indicates
    a request to reassociate.

bg_scan_period
    period of background scan.

flags
    one of \ :c:type:`enum qlink_sta_connect_flags <qlink_sta_connect_flags>`\ .

ht_capa
    HT Capabilities overrides.

ht_capa_mask
    The bits of ht_capa which are to be used.

vht_capa
    VHT Capability overrides

vht_capa_mask
    The bits of vht_capa which are to be used.

aen
    authentication information.

mfp
    whether to use management frame protection.

pbss
    *undescribed*

rsvd
    *undescribed*

payload
    variable portion of connection request.

.. _`qlink_cmd_disconnect`:

struct qlink_cmd_disconnect
===========================

.. c:type:: struct qlink_cmd_disconnect

    data for QLINK_CMD_DISCONNECT command

.. _`qlink_cmd_disconnect.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_disconnect {
        struct qlink_cmd chdr;
        __le16 reason;
    }

.. _`qlink_cmd_disconnect.members`:

Members
-------

chdr
    *undescribed*

reason
    code of the reason of disconnect, see \ :c:type:`enum ieee80211_reasoncode <ieee80211_reasoncode>`\ .

.. _`qlink_cmd_updown`:

struct qlink_cmd_updown
=======================

.. c:type:: struct qlink_cmd_updown

    data for QLINK_CMD_UPDOWN_INTF command

.. _`qlink_cmd_updown.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_updown {
        struct qlink_cmd chdr;
        u8 if_up;
    }

.. _`qlink_cmd_updown.members`:

Members
-------

chdr
    *undescribed*

if_up
    bring specified interface DOWN (if_up==0) or UP (otherwise).
    Interface is specified in common command header \ ``chdr``\ .

.. _`qlink_band`:

enum qlink_band
===============

.. c:type:: enum qlink_band

    a list of frequency bands

.. _`qlink_band.definition`:

Definition
----------

.. code-block:: c

    enum qlink_band {
        QLINK_BAND_2GHZ,
        QLINK_BAND_5GHZ,
        QLINK_BAND_60GHZ
    };

.. _`qlink_band.constants`:

Constants
---------

QLINK_BAND_2GHZ
    2.4GHz band

QLINK_BAND_5GHZ
    5GHz band

QLINK_BAND_60GHZ
    60GHz band

.. _`qlink_cmd_band_info_get`:

struct qlink_cmd_band_info_get
==============================

.. c:type:: struct qlink_cmd_band_info_get

    data for QLINK_CMD_BAND_INFO_GET command

.. _`qlink_cmd_band_info_get.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_band_info_get {
        struct qlink_cmd chdr;
        u8 band;
    }

.. _`qlink_cmd_band_info_get.members`:

Members
-------

chdr
    *undescribed*

band
    a PHY band for which information is queried, one of \ ``enum``\  qlink_band

.. _`qlink_cmd_get_chan_stats`:

struct qlink_cmd_get_chan_stats
===============================

.. c:type:: struct qlink_cmd_get_chan_stats

    data for QLINK_CMD_CHAN_STATS command

.. _`qlink_cmd_get_chan_stats.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_get_chan_stats {
        struct qlink_cmd chdr;
        __le16 channel;
    }

.. _`qlink_cmd_get_chan_stats.members`:

Members
-------

chdr
    *undescribed*

channel
    channel number according to 802.11 17.3.8.3.2 and Annex J

.. _`qlink_reg_initiator`:

enum qlink_reg_initiator
========================

.. c:type:: enum qlink_reg_initiator

    Indicates the initiator of a reg domain request

.. _`qlink_reg_initiator.definition`:

Definition
----------

.. code-block:: c

    enum qlink_reg_initiator {
        QLINK_REGDOM_SET_BY_CORE,
        QLINK_REGDOM_SET_BY_USER,
        QLINK_REGDOM_SET_BY_DRIVER,
        QLINK_REGDOM_SET_BY_COUNTRY_IE
    };

.. _`qlink_reg_initiator.constants`:

Constants
---------

QLINK_REGDOM_SET_BY_CORE
    *undescribed*

QLINK_REGDOM_SET_BY_USER
    *undescribed*

QLINK_REGDOM_SET_BY_DRIVER
    *undescribed*

QLINK_REGDOM_SET_BY_COUNTRY_IE
    *undescribed*

.. _`qlink_reg_initiator.description`:

Description
-----------

See \ :c:type:`enum nl80211_reg_initiator <nl80211_reg_initiator>`\  for more info.

.. _`qlink_user_reg_hint_type`:

enum qlink_user_reg_hint_type
=============================

.. c:type:: enum qlink_user_reg_hint_type

    type of user regulatory hint

.. _`qlink_user_reg_hint_type.definition`:

Definition
----------

.. code-block:: c

    enum qlink_user_reg_hint_type {
        QLINK_USER_REG_HINT_USER,
        QLINK_USER_REG_HINT_CELL_BASE,
        QLINK_USER_REG_HINT_INDOOR
    };

.. _`qlink_user_reg_hint_type.constants`:

Constants
---------

QLINK_USER_REG_HINT_USER
    *undescribed*

QLINK_USER_REG_HINT_CELL_BASE
    *undescribed*

QLINK_USER_REG_HINT_INDOOR
    *undescribed*

.. _`qlink_user_reg_hint_type.description`:

Description
-----------

See \ :c:type:`enum nl80211_user_reg_hint_type <nl80211_user_reg_hint_type>`\  for more info.

.. _`qlink_cmd_reg_notify`:

struct qlink_cmd_reg_notify
===========================

.. c:type:: struct qlink_cmd_reg_notify

    data for QLINK_CMD_REG_NOTIFY command

.. _`qlink_cmd_reg_notify.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_reg_notify {
        struct qlink_cmd chdr;
        u8 alpha2[2];
        u8 initiator;
        u8 user_reg_hint_type;
    }

.. _`qlink_cmd_reg_notify.members`:

Members
-------

chdr
    *undescribed*

alpha2
    the ISO / IEC 3166 alpha2 country code.

initiator
    which entity sent the request, one of \ :c:type:`enum qlink_reg_initiator <qlink_reg_initiator>`\ .

user_reg_hint_type
    type of hint for QLINK_REGDOM_SET_BY_USER request, one
    of \ :c:type:`enum qlink_user_reg_hint_type <qlink_user_reg_hint_type>`\ .

.. _`qlink_cmd_chan_switch`:

struct qlink_cmd_chan_switch
============================

.. c:type:: struct qlink_cmd_chan_switch

    data for QLINK_CMD_CHAN_SWITCH command

.. _`qlink_cmd_chan_switch.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_chan_switch {
        struct qlink_cmd chdr;
        __le16 channel;
        u8 radar_required;
        u8 block_tx;
        u8 beacon_count;
    }

.. _`qlink_cmd_chan_switch.members`:

Members
-------

chdr
    *undescribed*

channel
    channel number according to 802.11 17.3.8.3.2 and Annex J

radar_required
    whether radar detection is required on the new channel

block_tx
    whether transmissions should be blocked while changing

beacon_count
    number of beacons until switch

.. _`qlink_hidden_ssid`:

enum qlink_hidden_ssid
======================

.. c:type:: enum qlink_hidden_ssid

    values for \ ``NL80211_ATTR_HIDDEN_SSID``\ 

.. _`qlink_hidden_ssid.definition`:

Definition
----------

.. code-block:: c

    enum qlink_hidden_ssid {
        QLINK_HIDDEN_SSID_NOT_IN_USE,
        QLINK_HIDDEN_SSID_ZERO_LEN,
        QLINK_HIDDEN_SSID_ZERO_CONTENTS
    };

.. _`qlink_hidden_ssid.constants`:

Constants
---------

QLINK_HIDDEN_SSID_NOT_IN_USE
    *undescribed*

QLINK_HIDDEN_SSID_ZERO_LEN
    *undescribed*

QLINK_HIDDEN_SSID_ZERO_CONTENTS
    *undescribed*

.. _`qlink_hidden_ssid.description`:

Description
-----------

Refer to \ :c:type:`enum nl80211_hidden_ssid <nl80211_hidden_ssid>`\ 

.. _`qlink_cmd_start_ap`:

struct qlink_cmd_start_ap
=========================

.. c:type:: struct qlink_cmd_start_ap

    data for QLINK_CMD_START_AP command

.. _`qlink_cmd_start_ap.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_start_ap {
        struct qlink_cmd chdr;
        __le16 beacon_interval;
        __le16 inactivity_timeout;
        u8 dtim_period;
        u8 hidden_ssid;
        u8 smps_mode;
        u8 p2p_ctwindow;
        u8 p2p_opp_ps;
        u8 pbss;
        u8 ht_required;
        u8 vht_required;
        struct qlink_auth_encr aen;
        u8 info[0];
    }

.. _`qlink_cmd_start_ap.members`:

Members
-------

chdr
    *undescribed*

beacon_interval
    beacon interval

inactivity_timeout
    station's inactivity period in seconds

dtim_period
    DTIM period

hidden_ssid
    whether to hide the SSID, one of \ :c:type:`enum qlink_hidden_ssid <qlink_hidden_ssid>`\ 

smps_mode
    SMPS mode

p2p_ctwindow
    *undescribed*

p2p_opp_ps
    *undescribed*

pbss
    *undescribed*

ht_required
    stations must support HT

vht_required
    stations must support VHT

aen
    encryption info

info
    variable configurations

.. _`qlink_cmd_start_cac`:

struct qlink_cmd_start_cac
==========================

.. c:type:: struct qlink_cmd_start_cac

    data for QLINK_CMD_START_CAC command

.. _`qlink_cmd_start_cac.definition`:

Definition
----------

.. code-block:: c

    struct qlink_cmd_start_cac {
        struct qlink_cmd chdr;
        struct qlink_chandef chan;
        __le32 cac_time_ms;
    }

.. _`qlink_cmd_start_cac.members`:

Members
-------

chdr
    *undescribed*

chan
    a channel to start a radar detection procedure on.

cac_time_ms
    CAC time.

.. _`qlink_acl_data`:

struct qlink_acl_data
=====================

.. c:type:: struct qlink_acl_data

    ACL data

.. _`qlink_acl_data.definition`:

Definition
----------

.. code-block:: c

    struct qlink_acl_data {
        __le32 policy;
        __le32 num_entries;
        struct qlink_mac_address mac_addrs[0];
    }

.. _`qlink_acl_data.members`:

Members
-------

policy
    filter policy, one of \ :c:type:`enum qlink_acl_policy <qlink_acl_policy>`\ .

num_entries
    number of MAC addresses in array.

mac_addrs
    *undescribed*

.. _`qlink_resp`:

struct qlink_resp
=================

.. c:type:: struct qlink_resp

    QLINK command response message header

.. _`qlink_resp.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp {
        struct qlink_msg_header mhdr;
        __le16 cmd_id;
        __le16 seq_num;
        __le16 result;
        u8 macid;
        u8 vifid;
    }

.. _`qlink_resp.members`:

Members
-------

mhdr
    see \ :c:type:`struct qlink_msg_header <qlink_msg_header>`\ .

cmd_id
    command ID the response corresponds to, one of \ :c:type:`enum qlink_cmd_type <qlink_cmd_type>`\ .

seq_num
    sequence number of command message, used for matching with
    response message.

result
    result of the command execution, one of \ :c:type:`enum qlink_cmd_result <qlink_cmd_result>`\ .

macid
    index of physical radio device the response is sent from or
    QLINK_MACID_RSVD if not applicable.

vifid
    index of virtual wireless interface on specified \ ``macid``\  the response
    is sent from or QLINK_VIFID_RSVD if not applicable.

.. _`qlink_resp.description`:

Description
-----------

Header used for QLINK messages of QLINK_MSG_TYPE_CMDRSP type.

.. _`qlink_resp_get_mac_info`:

struct qlink_resp_get_mac_info
==============================

.. c:type:: struct qlink_resp_get_mac_info

    response for QLINK_CMD_MAC_INFO command

.. _`qlink_resp_get_mac_info.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_get_mac_info {
        struct qlink_resp rhdr;
        u8 dev_mac[ETH_ALEN];
        u8 num_tx_chain;
        u8 num_rx_chain;
        struct ieee80211_vht_cap vht_cap_mod_mask;
        struct ieee80211_ht_cap ht_cap_mod_mask;
        __le16 max_ap_assoc_sta;
        __le16 radar_detect_widths;
        __le32 max_acl_mac_addrs;
        u8 bands_cap;
        u8 rsvd[1];
        u8 var_info[0];
    }

.. _`qlink_resp_get_mac_info.members`:

Members
-------

rhdr
    *undescribed*

dev_mac
    MAC address of physical WMAC device (used for first BSS on
    specified WMAC).

num_tx_chain
    Number of transmit chains used by WMAC.

num_rx_chain
    Number of receive chains used by WMAC.

vht_cap_mod_mask
    mask specifying which VHT capabilities can be altered.

ht_cap_mod_mask
    mask specifying which HT capabilities can be altered.

max_ap_assoc_sta
    Maximum number of associations supported by WMAC.

radar_detect_widths
    bitmask of channels BW for which WMAC can detect radar.

max_acl_mac_addrs
    *undescribed*

bands_cap
    wireless bands WMAC can operate in, bitmap of \ :c:type:`enum qlink_band <qlink_band>`\ .

rsvd
    *undescribed*

var_info
    variable-length WMAC info data.

.. _`qlink_resp_get_mac_info.description`:

Description
-----------

Data describing specific physical device providing wireless MAC
functionality.

.. _`qlink_dfs_regions`:

enum qlink_dfs_regions
======================

.. c:type:: enum qlink_dfs_regions

    regulatory DFS regions

.. _`qlink_dfs_regions.definition`:

Definition
----------

.. code-block:: c

    enum qlink_dfs_regions {
        QLINK_DFS_UNSET,
        QLINK_DFS_FCC,
        QLINK_DFS_ETSI,
        QLINK_DFS_JP
    };

.. _`qlink_dfs_regions.constants`:

Constants
---------

QLINK_DFS_UNSET
    *undescribed*

QLINK_DFS_FCC
    *undescribed*

QLINK_DFS_ETSI
    *undescribed*

QLINK_DFS_JP
    *undescribed*

.. _`qlink_dfs_regions.description`:

Description
-----------

Corresponds to \ :c:type:`enum nl80211_dfs_regions <nl80211_dfs_regions>`\ .

.. _`qlink_resp_get_hw_info`:

struct qlink_resp_get_hw_info
=============================

.. c:type:: struct qlink_resp_get_hw_info

    response for QLINK_CMD_GET_HW_INFO command

.. _`qlink_resp_get_hw_info.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_get_hw_info {
        struct qlink_resp rhdr;
        __le32 fw_ver;
        __le32 hw_capab;
        __le32 bld_tmstamp;
        __le32 plat_id;
        __le32 hw_ver;
        __le16 ql_proto_ver;
        u8 num_mac;
        u8 mac_bitmap;
        u8 total_tx_chain;
        u8 total_rx_chain;
        u8 alpha2[2];
        u8 n_reg_rules;
        u8 dfs_region;
        u8 info[0];
    }

.. _`qlink_resp_get_hw_info.members`:

Members
-------

rhdr
    *undescribed*

fw_ver
    wireless hardware firmware version.

hw_capab
    Bitmap of capabilities supported by firmware.

bld_tmstamp
    *undescribed*

plat_id
    *undescribed*

hw_ver
    *undescribed*

ql_proto_ver
    Version of QLINK protocol used by firmware.

num_mac
    Number of separate physical radio devices provided by hardware.

mac_bitmap
    Bitmap of MAC IDs that are active and can be used in firmware.

total_tx_chain
    *undescribed*

total_rx_chain
    *undescribed*

alpha2
    country code ID firmware is configured to.

n_reg_rules
    number of regulatory rules TLVs in variable portion of the
    message.

dfs_region
    regulatory DFS region, one of \ ``enum``\  qlink_dfs_region.

info
    variable-length HW info, can contain QTN_TLV_ID_REG_RULE.

.. _`qlink_resp_get_hw_info.description`:

Description
-----------

Description of wireless hardware capabilities and features.

.. _`qlink_resp_manage_intf`:

struct qlink_resp_manage_intf
=============================

.. c:type:: struct qlink_resp_manage_intf

    response for interface management commands

.. _`qlink_resp_manage_intf.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_manage_intf {
        struct qlink_resp rhdr;
        struct qlink_intf_info intf_info;
    }

.. _`qlink_resp_manage_intf.members`:

Members
-------

rhdr
    Common Command Response message header.

intf_info
    interface description.

.. _`qlink_resp_manage_intf.description`:

Description
-----------

Response data for QLINK_CMD_ADD_INTF and QLINK_CMD_CHANGE_INTF commands.

.. _`qlink_resp_get_sta_info`:

struct qlink_resp_get_sta_info
==============================

.. c:type:: struct qlink_resp_get_sta_info

    response for QLINK_CMD_GET_STA_INFO command

.. _`qlink_resp_get_sta_info.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_get_sta_info {
        struct qlink_resp rhdr;
        u8 sta_addr[ETH_ALEN];
        u8 rsvd[2];
        u8 info[0];
    }

.. _`qlink_resp_get_sta_info.members`:

Members
-------

rhdr
    *undescribed*

sta_addr
    MAC address of STA the response carries statistic for.

rsvd
    *undescribed*

info
    variable statistics for specified STA.

.. _`qlink_resp_get_sta_info.description`:

Description
-----------

Response data containing statistics for specified STA.

.. _`qlink_resp_band_info_get`:

struct qlink_resp_band_info_get
===============================

.. c:type:: struct qlink_resp_band_info_get

    response for QLINK_CMD_BAND_INFO_GET cmd

.. _`qlink_resp_band_info_get.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_band_info_get {
        struct qlink_resp rhdr;
        u8 band;
        u8 num_chans;
        u8 num_bitrates;
        u8 rsvd[1];
        u8 info[0];
    }

.. _`qlink_resp_band_info_get.members`:

Members
-------

rhdr
    *undescribed*

band
    frequency band that the response describes, one of \ ``enum``\  qlink_band.

num_chans
    total number of channels info TLVs contained in reply.

num_bitrates
    total number of bitrate TLVs contained in reply.

rsvd
    *undescribed*

info
    variable-length info portion.

.. _`qlink_resp_phy_params`:

struct qlink_resp_phy_params
============================

.. c:type:: struct qlink_resp_phy_params

    response for QLINK_CMD_PHY_PARAMS_GET command

.. _`qlink_resp_phy_params.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_phy_params {
        struct qlink_resp rhdr;
        u8 info[0];
    }

.. _`qlink_resp_phy_params.members`:

Members
-------

rhdr
    *undescribed*

info
    variable-length array of PHY params.

.. _`qlink_resp_get_chan_stats`:

struct qlink_resp_get_chan_stats
================================

.. c:type:: struct qlink_resp_get_chan_stats

    response for QLINK_CMD_CHAN_STATS cmd

.. _`qlink_resp_get_chan_stats.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_get_chan_stats {
        struct qlink_cmd rhdr;
        u8 info[0];
    }

.. _`qlink_resp_get_chan_stats.members`:

Members
-------

rhdr
    *undescribed*

info
    variable-length channel info.

.. _`qlink_resp_channel_get`:

struct qlink_resp_channel_get
=============================

.. c:type:: struct qlink_resp_channel_get

    response for QLINK_CMD_CHAN_GET command

.. _`qlink_resp_channel_get.definition`:

Definition
----------

.. code-block:: c

    struct qlink_resp_channel_get {
        struct qlink_resp rhdr;
        struct qlink_chandef chan;
    }

.. _`qlink_resp_channel_get.members`:

Members
-------

rhdr
    *undescribed*

chan
    definition of current operating channel.

.. _`qlink_event`:

struct qlink_event
==================

.. c:type:: struct qlink_event

    QLINK event message header

.. _`qlink_event.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event {
        struct qlink_msg_header mhdr;
        __le16 event_id;
        u8 macid;
        u8 vifid;
    }

.. _`qlink_event.members`:

Members
-------

mhdr
    Common QLINK message header.

event_id
    Specifies specific event ID, one of \ :c:type:`enum qlink_event_type <qlink_event_type>`\ .

macid
    index of physical radio device the event was generated on or
    QLINK_MACID_RSVD if not applicable.

vifid
    index of virtual wireless interface on specified \ ``macid``\  the event
    was generated on or QLINK_VIFID_RSVD if not applicable.

.. _`qlink_event.description`:

Description
-----------

Header used for QLINK messages of QLINK_MSG_TYPE_EVENT type.

.. _`qlink_event_sta_assoc`:

struct qlink_event_sta_assoc
============================

.. c:type:: struct qlink_event_sta_assoc

    data for QLINK_EVENT_STA_ASSOCIATED event

.. _`qlink_event_sta_assoc.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_sta_assoc {
        struct qlink_event ehdr;
        u8 sta_addr[ETH_ALEN];
        __le16 frame_control;
        u8 ies[0];
    }

.. _`qlink_event_sta_assoc.members`:

Members
-------

ehdr
    *undescribed*

sta_addr
    Address of a STA for which new association event was generated

frame_control
    control bits from 802.11 ASSOC_REQUEST header.

ies
    *undescribed*

.. _`qlink_event_sta_deauth`:

struct qlink_event_sta_deauth
=============================

.. c:type:: struct qlink_event_sta_deauth

    data for QLINK_EVENT_STA_DEAUTH event

.. _`qlink_event_sta_deauth.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_sta_deauth {
        struct qlink_event ehdr;
        u8 sta_addr[ETH_ALEN];
        __le16 reason;
    }

.. _`qlink_event_sta_deauth.members`:

Members
-------

ehdr
    *undescribed*

sta_addr
    Address of a deauthenticated STA.

reason
    reason for deauthentication.

.. _`qlink_event_bss_join`:

struct qlink_event_bss_join
===========================

.. c:type:: struct qlink_event_bss_join

    data for QLINK_EVENT_BSS_JOIN event

.. _`qlink_event_bss_join.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_bss_join {
        struct qlink_event ehdr;
        u8 bssid[ETH_ALEN];
        __le16 status;
    }

.. _`qlink_event_bss_join.members`:

Members
-------

ehdr
    *undescribed*

bssid
    BSSID of a BSS which interface tried to joined.

status
    status of joining attempt, see \ :c:type:`enum ieee80211_statuscode <ieee80211_statuscode>`\ .

.. _`qlink_event_bss_leave`:

struct qlink_event_bss_leave
============================

.. c:type:: struct qlink_event_bss_leave

    data for QLINK_EVENT_BSS_LEAVE event

.. _`qlink_event_bss_leave.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_bss_leave {
        struct qlink_event ehdr;
        __le16 reason;
    }

.. _`qlink_event_bss_leave.members`:

Members
-------

ehdr
    *undescribed*

reason
    reason of disconnecting from BSS.

.. _`qlink_event_freq_change`:

struct qlink_event_freq_change
==============================

.. c:type:: struct qlink_event_freq_change

    data for QLINK_EVENT_FREQ_CHANGE event

.. _`qlink_event_freq_change.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_freq_change {
        struct qlink_event ehdr;
        struct qlink_chandef chan;
    }

.. _`qlink_event_freq_change.members`:

Members
-------

ehdr
    *undescribed*

chan
    new operating channel definition

.. _`qlink_event_rxmgmt`:

struct qlink_event_rxmgmt
=========================

.. c:type:: struct qlink_event_rxmgmt

    data for QLINK_EVENT_MGMT_RECEIVED event

.. _`qlink_event_rxmgmt.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_rxmgmt {
        struct qlink_event ehdr;
        __le32 freq;
        __le32 flags;
        s8 sig_dbm;
        u8 rsvd[3];
        u8 frame_data[0];
    }

.. _`qlink_event_rxmgmt.members`:

Members
-------

ehdr
    *undescribed*

freq
    Frequency on which the frame was received in MHz.

flags
    bitmap of \ :c:type:`enum qlink_rxmgmt_flags <qlink_rxmgmt_flags>`\ .

sig_dbm
    signal strength in dBm.

rsvd
    *undescribed*

frame_data
    data of Rx'd frame itself.

.. _`qlink_event_scan_result`:

struct qlink_event_scan_result
==============================

.. c:type:: struct qlink_event_scan_result

    data for QLINK_EVENT_SCAN_RESULTS event

.. _`qlink_event_scan_result.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_scan_result {
        struct qlink_event ehdr;
        __le64 tsf;
        __le16 freq;
        __le16 capab;
        __le16 bintval;
        s8 sig_dbm;
        u8 ssid_len;
        u8 ssid[IEEE80211_MAX_SSID_LEN];
        u8 bssid[ETH_ALEN];
        u8 rsvd[2];
        u8 payload[0];
    }

.. _`qlink_event_scan_result.members`:

Members
-------

ehdr
    *undescribed*

tsf
    TSF timestamp indicating when scan results were generated.

freq
    Center frequency of the channel where BSS for which the scan result
    event was generated was discovered.

capab
    capabilities field.

bintval
    beacon interval announced by discovered BSS.

sig_dbm
    signal strength in dBm.

ssid_len
    length of SSID announced by BSS.

ssid
    SSID announced by discovered BSS.

bssid
    BSSID announced by discovered BSS.

rsvd
    *undescribed*

payload
    IEs that are announced by discovered BSS in its MGMt frames.

.. _`qlink_scan_complete_flags`:

enum qlink_scan_complete_flags
==============================

.. c:type:: enum qlink_scan_complete_flags

    indicates result of scan request.

.. _`qlink_scan_complete_flags.definition`:

Definition
----------

.. code-block:: c

    enum qlink_scan_complete_flags {
        QLINK_SCAN_NONE,
        QLINK_SCAN_ABORTED
    };

.. _`qlink_scan_complete_flags.constants`:

Constants
---------

QLINK_SCAN_NONE
    Scan request was processed.

QLINK_SCAN_ABORTED
    Scan was aborted.

.. _`qlink_event_scan_complete`:

struct qlink_event_scan_complete
================================

.. c:type:: struct qlink_event_scan_complete

    data for QLINK_EVENT_SCAN_COMPLETE event

.. _`qlink_event_scan_complete.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_scan_complete {
        struct qlink_event ehdr;
        __le32 flags;
    }

.. _`qlink_event_scan_complete.members`:

Members
-------

ehdr
    *undescribed*

flags
    flags indicating the status of pending scan request,
    see \ :c:type:`enum qlink_scan_complete_flags <qlink_scan_complete_flags>`\ .

.. _`qlink_event_radar`:

struct qlink_event_radar
========================

.. c:type:: struct qlink_event_radar

    data for QLINK_EVENT_RADAR event

.. _`qlink_event_radar.definition`:

Definition
----------

.. code-block:: c

    struct qlink_event_radar {
        struct qlink_event ehdr;
        struct qlink_chandef chan;
        u8 event;
        u8 rsvd[3];
    }

.. _`qlink_event_radar.members`:

Members
-------

ehdr
    *undescribed*

chan
    channel on which radar event happened.

event
    radar event type, one of \ :c:type:`enum qlink_radar_event <qlink_radar_event>`\ .

rsvd
    *undescribed*

.. _`qlink_tlv_id`:

enum qlink_tlv_id
=================

.. c:type:: enum qlink_tlv_id

    list of TLVs that Qlink messages can carry

.. _`qlink_tlv_id.definition`:

Definition
----------

.. code-block:: c

    enum qlink_tlv_id {
        QTN_TLV_ID_FRAG_THRESH,
        QTN_TLV_ID_RTS_THRESH,
        QTN_TLV_ID_SRETRY_LIMIT,
        QTN_TLV_ID_LRETRY_LIMIT,
        QTN_TLV_ID_REG_RULE,
        QTN_TLV_ID_CHANNEL,
        QTN_TLV_ID_CHANDEF,
        QTN_TLV_ID_STA_STATS_MAP,
        QTN_TLV_ID_STA_STATS,
        QTN_TLV_ID_COVERAGE_CLASS,
        QTN_TLV_ID_IFACE_LIMIT,
        QTN_TLV_ID_NUM_IFACE_COMB,
        QTN_TLV_ID_CHANNEL_STATS,
        QTN_TLV_ID_KEY,
        QTN_TLV_ID_SEQ,
        QTN_TLV_ID_IE_SET,
        QTN_TLV_ID_EXT_CAPABILITY_MASK,
        QTN_TLV_ID_ACL_DATA,
        QTN_TLV_ID_BUILD_NAME,
        QTN_TLV_ID_BUILD_REV,
        QTN_TLV_ID_BUILD_TYPE,
        QTN_TLV_ID_BUILD_LABEL,
        QTN_TLV_ID_HW_ID,
        QTN_TLV_ID_CALIBRATION_VER,
        QTN_TLV_ID_UBOOT_VER
    };

.. _`qlink_tlv_id.constants`:

Constants
---------

QTN_TLV_ID_FRAG_THRESH
    *undescribed*

QTN_TLV_ID_RTS_THRESH
    *undescribed*

QTN_TLV_ID_SRETRY_LIMIT
    *undescribed*

QTN_TLV_ID_LRETRY_LIMIT
    *undescribed*

QTN_TLV_ID_REG_RULE
    *undescribed*

QTN_TLV_ID_CHANNEL
    *undescribed*

QTN_TLV_ID_CHANDEF
    *undescribed*

QTN_TLV_ID_STA_STATS_MAP
    a bitmap of \ :c:type:`enum qlink_sta_info <qlink_sta_info>`\ , used to
    indicate which statistic carried in QTN_TLV_ID_STA_STATS is valid.

QTN_TLV_ID_STA_STATS
    per-STA statistics as defined by
    \ :c:type:`struct qlink_sta_stats <qlink_sta_stats>`\ . Valid values are marked as such in a bitmap
    carried by QTN_TLV_ID_STA_STATS_MAP.

QTN_TLV_ID_COVERAGE_CLASS
    *undescribed*

QTN_TLV_ID_IFACE_LIMIT
    *undescribed*

QTN_TLV_ID_NUM_IFACE_COMB
    *undescribed*

QTN_TLV_ID_CHANNEL_STATS
    *undescribed*

QTN_TLV_ID_KEY
    *undescribed*

QTN_TLV_ID_SEQ
    *undescribed*

QTN_TLV_ID_IE_SET
    *undescribed*

QTN_TLV_ID_EXT_CAPABILITY_MASK
    *undescribed*

QTN_TLV_ID_ACL_DATA
    *undescribed*

QTN_TLV_ID_BUILD_NAME
    *undescribed*

QTN_TLV_ID_BUILD_REV
    *undescribed*

QTN_TLV_ID_BUILD_TYPE
    *undescribed*

QTN_TLV_ID_BUILD_LABEL
    *undescribed*

QTN_TLV_ID_HW_ID
    *undescribed*

QTN_TLV_ID_CALIBRATION_VER
    *undescribed*

QTN_TLV_ID_UBOOT_VER
    *undescribed*

.. _`qlink_reg_rule_flags`:

enum qlink_reg_rule_flags
=========================

.. c:type:: enum qlink_reg_rule_flags

    regulatory rule flags

.. _`qlink_reg_rule_flags.definition`:

Definition
----------

.. code-block:: c

    enum qlink_reg_rule_flags {
        QLINK_RRF_NO_OFDM,
        QLINK_RRF_NO_CCK,
        QLINK_RRF_NO_INDOOR,
        QLINK_RRF_NO_OUTDOOR,
        QLINK_RRF_DFS,
        QLINK_RRF_PTP_ONLY,
        QLINK_RRF_PTMP_ONLY,
        QLINK_RRF_NO_IR,
        QLINK_RRF_AUTO_BW,
        QLINK_RRF_IR_CONCURRENT,
        QLINK_RRF_NO_HT40MINUS,
        QLINK_RRF_NO_HT40PLUS,
        QLINK_RRF_NO_80MHZ,
        QLINK_RRF_NO_160MHZ
    };

.. _`qlink_reg_rule_flags.constants`:

Constants
---------

QLINK_RRF_NO_OFDM
    *undescribed*

QLINK_RRF_NO_CCK
    *undescribed*

QLINK_RRF_NO_INDOOR
    *undescribed*

QLINK_RRF_NO_OUTDOOR
    *undescribed*

QLINK_RRF_DFS
    *undescribed*

QLINK_RRF_PTP_ONLY
    *undescribed*

QLINK_RRF_PTMP_ONLY
    *undescribed*

QLINK_RRF_NO_IR
    *undescribed*

QLINK_RRF_AUTO_BW
    *undescribed*

QLINK_RRF_IR_CONCURRENT
    *undescribed*

QLINK_RRF_NO_HT40MINUS
    *undescribed*

QLINK_RRF_NO_HT40PLUS
    *undescribed*

QLINK_RRF_NO_80MHZ
    *undescribed*

QLINK_RRF_NO_160MHZ
    *undescribed*

.. _`qlink_reg_rule_flags.description`:

Description
-----------

See description of \ :c:type:`enum nl80211_reg_rule_flags <nl80211_reg_rule_flags>`\ 

.. _`qlink_tlv_reg_rule`:

struct qlink_tlv_reg_rule
=========================

.. c:type:: struct qlink_tlv_reg_rule

    data for QTN_TLV_ID_REG_RULE TLV

.. _`qlink_tlv_reg_rule.definition`:

Definition
----------

.. code-block:: c

    struct qlink_tlv_reg_rule {
        struct qlink_tlv_hdr hdr;
        __le32 start_freq_khz;
        __le32 end_freq_khz;
        __le32 max_bandwidth_khz;
        __le32 max_antenna_gain;
        __le32 max_eirp;
        __le32 flags;
        __le32 dfs_cac_ms;
    }

.. _`qlink_tlv_reg_rule.members`:

Members
-------

hdr
    *undescribed*

start_freq_khz
    start frequency of the range the rule is attributed to.

end_freq_khz
    end frequency of the range the rule is attributed to.

max_bandwidth_khz
    max bandwidth that channels in specified range can be
    configured to.

max_antenna_gain
    max antenna gain that can be used in the specified
    frequency range, dBi.

max_eirp
    maximum EIRP.

flags
    regulatory rule flags in \ :c:type:`enum qlink_reg_rule_flags <qlink_reg_rule_flags>`\ .

dfs_cac_ms
    DFS CAC period.

.. _`qlink_tlv_reg_rule.description`:

Description
-----------

Regulatory rule description.

.. _`qlink_tlv_channel`:

struct qlink_tlv_channel
========================

.. c:type:: struct qlink_tlv_channel

    data for QTN_TLV_ID_CHANNEL TLV

.. _`qlink_tlv_channel.definition`:

Definition
----------

.. code-block:: c

    struct qlink_tlv_channel {
        struct qlink_tlv_hdr hdr;
        struct qlink_channel chan;
    }

.. _`qlink_tlv_channel.members`:

Members
-------

hdr
    *undescribed*

chan
    *undescribed*

.. _`qlink_tlv_channel.description`:

Description
-----------

Channel settings.

.. _`qlink_tlv_chandef`:

struct qlink_tlv_chandef
========================

.. c:type:: struct qlink_tlv_chandef

    data for QTN_TLV_ID_CHANDEF TLV

.. _`qlink_tlv_chandef.definition`:

Definition
----------

.. code-block:: c

    struct qlink_tlv_chandef {
        struct qlink_tlv_hdr hdr;
        struct qlink_chandef chdef;
    }

.. _`qlink_tlv_chandef.members`:

Members
-------

hdr
    *undescribed*

chdef
    *undescribed*

.. _`qlink_tlv_chandef.description`:

Description
-----------

Channel definition.

.. _`qlink_tlv_ie_set`:

struct qlink_tlv_ie_set
=======================

.. c:type:: struct qlink_tlv_ie_set

    data for QTN_TLV_ID_IE_SET

.. _`qlink_tlv_ie_set.definition`:

Definition
----------

.. code-block:: c

    struct qlink_tlv_ie_set {
        struct qlink_tlv_hdr hdr;
        u8 type;
        u8 flags;
        u8 ie_data[0];
    }

.. _`qlink_tlv_ie_set.members`:

Members
-------

hdr
    *undescribed*

type
    type of MGMT frame IEs belong to, one of \ :c:type:`enum qlink_ie_set_type <qlink_ie_set_type>`\ .

flags
    for future use.

ie_data
    IEs data.

.. _`qlink_sta_info`:

enum qlink_sta_info
===================

.. c:type:: enum qlink_sta_info

    station information bitmap

.. _`qlink_sta_info.definition`:

Definition
----------

.. code-block:: c

    enum qlink_sta_info {
        QLINK_STA_INFO_CONNECTED_TIME,
        QLINK_STA_INFO_INACTIVE_TIME,
        QLINK_STA_INFO_RX_BYTES,
        QLINK_STA_INFO_TX_BYTES,
        QLINK_STA_INFO_RX_BYTES64,
        QLINK_STA_INFO_TX_BYTES64,
        QLINK_STA_INFO_RX_DROP_MISC,
        QLINK_STA_INFO_BEACON_RX,
        QLINK_STA_INFO_SIGNAL,
        QLINK_STA_INFO_SIGNAL_AVG,
        QLINK_STA_INFO_RX_BITRATE,
        QLINK_STA_INFO_TX_BITRATE,
        QLINK_STA_INFO_RX_PACKETS,
        QLINK_STA_INFO_TX_PACKETS,
        QLINK_STA_INFO_TX_RETRIES,
        QLINK_STA_INFO_TX_FAILED,
        QLINK_STA_INFO_STA_FLAGS,
        QLINK_STA_INFO_NUM
    };

.. _`qlink_sta_info.constants`:

Constants
---------

QLINK_STA_INFO_CONNECTED_TIME
    connected_time value is valid.

QLINK_STA_INFO_INACTIVE_TIME
    inactive_time value is valid.

QLINK_STA_INFO_RX_BYTES
    lower 32 bits of rx_bytes value are valid.

QLINK_STA_INFO_TX_BYTES
    lower 32 bits of tx_bytes value are valid.

QLINK_STA_INFO_RX_BYTES64
    rx_bytes value is valid.

QLINK_STA_INFO_TX_BYTES64
    tx_bytes value is valid.

QLINK_STA_INFO_RX_DROP_MISC
    rx_dropped_misc value is valid.

QLINK_STA_INFO_BEACON_RX
    rx_beacon value is valid.

QLINK_STA_INFO_SIGNAL
    signal value is valid.

QLINK_STA_INFO_SIGNAL_AVG
    signal_avg value is valid.

QLINK_STA_INFO_RX_BITRATE
    rxrate value is valid.

QLINK_STA_INFO_TX_BITRATE
    txrate value is valid.

QLINK_STA_INFO_RX_PACKETS
    rx_packets value is valid.

QLINK_STA_INFO_TX_PACKETS
    tx_packets value is valid.

QLINK_STA_INFO_TX_RETRIES
    tx_retries value is valid.

QLINK_STA_INFO_TX_FAILED
    tx_failed value is valid.

QLINK_STA_INFO_STA_FLAGS
    sta_flags value is valid.

QLINK_STA_INFO_NUM
    *undescribed*

.. _`qlink_sta_info.description`:

Description
-----------

Used to indicate which statistics values in \ :c:type:`struct qlink_sta_stats <qlink_sta_stats>`\ 
are valid. Individual values are used to fill a bitmap carried in a
payload of QTN_TLV_ID_STA_STATS_MAP.

.. _`qlink_sta_info_rate`:

struct qlink_sta_info_rate
==========================

.. c:type:: struct qlink_sta_info_rate

    STA rate statistics

.. _`qlink_sta_info_rate.definition`:

Definition
----------

.. code-block:: c

    struct qlink_sta_info_rate {
        __le16 rate;
        u8 flags;
        u8 mcs;
        u8 nss;
        u8 bw;
    }

.. _`qlink_sta_info_rate.members`:

Members
-------

rate
    data rate in Mbps.

flags
    bitmap of \ :c:type:`enum qlink_sta_info_rate_flags <qlink_sta_info_rate_flags>`\ .

mcs
    802.11-defined MCS index.

nss
    *undescribed*

bw
    bandwidth, one of \ :c:type:`enum qlink_channel_width <qlink_channel_width>`\ .

.. _`qlink_sta_info_rate.nss`:

nss
---

Number of Spatial Streams.

.. _`qlink_sta_stats`:

struct qlink_sta_stats
======================

.. c:type:: struct qlink_sta_stats

    data for QTN_TLV_ID_STA_STATS

.. _`qlink_sta_stats.definition`:

Definition
----------

.. code-block:: c

    struct qlink_sta_stats {
        __le64 rx_bytes;
        __le64 tx_bytes;
        __le64 rx_beacon;
        __le64 rx_duration;
        __le64 t_offset;
        __le32 connected_time;
        __le32 inactive_time;
        __le32 rx_packets;
        __le32 tx_packets;
        __le32 tx_retries;
        __le32 tx_failed;
        __le32 rx_dropped_misc;
        __le32 beacon_loss_count;
        __le32 expected_throughput;
        struct qlink_sta_info_state sta_flags;
        struct qlink_sta_info_rate txrate;
        struct qlink_sta_info_rate rxrate;
        __le16 llid;
        __le16 plid;
        u8 local_pm;
        u8 peer_pm;
        u8 nonpeer_pm;
        u8 rx_beacon_signal_avg;
        u8 plink_state;
        u8 signal;
        u8 signal_avg;
        u8 rsvd[1];
    }

.. _`qlink_sta_stats.members`:

Members
-------

rx_bytes
    *undescribed*

tx_bytes
    *undescribed*

rx_beacon
    *undescribed*

rx_duration
    *undescribed*

t_offset
    *undescribed*

connected_time
    *undescribed*

inactive_time
    *undescribed*

rx_packets
    *undescribed*

tx_packets
    *undescribed*

tx_retries
    *undescribed*

tx_failed
    *undescribed*

rx_dropped_misc
    *undescribed*

beacon_loss_count
    *undescribed*

expected_throughput
    *undescribed*

sta_flags
    *undescribed*

txrate
    *undescribed*

rxrate
    *undescribed*

llid
    *undescribed*

plid
    *undescribed*

local_pm
    *undescribed*

peer_pm
    *undescribed*

nonpeer_pm
    *undescribed*

rx_beacon_signal_avg
    *undescribed*

plink_state
    *undescribed*

signal
    *undescribed*

signal_avg
    *undescribed*

rsvd
    *undescribed*

.. _`qlink_sta_stats.description`:

Description
-----------

Carries statistics of a STA. Not all fields may be filled with
valid values. Valid fields should be indicated as such using a bitmap of
\ :c:type:`enum qlink_sta_info <qlink_sta_info>`\ . Bitmap is carried separately in a payload of
QTN_TLV_ID_STA_STATS_MAP.

.. This file was automatic generated / don't edit.

