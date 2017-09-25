.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/tdls.h

.. _`iwl_tdls_channel_switch_timing`:

struct iwl_tdls_channel_switch_timing
=====================================

.. c:type:: struct iwl_tdls_channel_switch_timing

    Switch timing in TDLS channel-switch

.. _`iwl_tdls_channel_switch_timing.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_channel_switch_timing {
        __le32 frame_timestamp;
        __le32 max_offchan_duration;
        __le32 switch_time;
        __le32 switch_timeout;
    }

.. _`iwl_tdls_channel_switch_timing.members`:

Members
-------

frame_timestamp
    GP2 timestamp of channel-switch request/response packet
    received from peer

max_offchan_duration
    What amount of microseconds out of a DTIM is given
    to the TDLS off-channel communication. For instance if the DTIM is
    200TU and the TDLS peer is to be given 25% of the time, the value
    given will be 50TU, or 50 \* 1024 if translated into microseconds.

switch_time
    switch time the peer sent in its channel switch timing IE

switch_timeout
    switch timeout the peer sent in its channel switch timing IE

.. _`iwl_tdls_channel_switch_frame`:

struct iwl_tdls_channel_switch_frame
====================================

.. c:type:: struct iwl_tdls_channel_switch_frame

    TDLS channel switch frame template

.. _`iwl_tdls_channel_switch_frame.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_channel_switch_frame {
        __le32 switch_time_offset;
        struct iwl_tx_cmd tx_cmd;
        u8 data[IWL_TDLS_CH_SW_FRAME_MAX_SIZE];
    }

.. _`iwl_tdls_channel_switch_frame.members`:

Members
-------

switch_time_offset
    offset to the channel switch timing IE in the template

tx_cmd
    Tx parameters for the frame

data
    frame data

.. _`iwl_tdls_channel_switch_frame.description`:

Description
-----------

A template representing a TDLS channel-switch request or response frame

.. _`iwl_tdls_channel_switch_cmd`:

struct iwl_tdls_channel_switch_cmd
==================================

.. c:type:: struct iwl_tdls_channel_switch_cmd

    TDLS channel switch command

.. _`iwl_tdls_channel_switch_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_channel_switch_cmd {
        u8 switch_type;
        __le32 peer_sta_id;
        struct iwl_fw_channel_info ci;
        struct iwl_tdls_channel_switch_timing timing;
        struct iwl_tdls_channel_switch_frame frame;
    }

.. _`iwl_tdls_channel_switch_cmd.members`:

Members
-------

switch_type
    see \ :c:type:`enum iwl_tdls_channel_switch_type <iwl_tdls_channel_switch_type>`\ 

peer_sta_id
    station id of TDLS peer

ci
    channel we switch to

timing
    timing related data for command

frame
    channel-switch request/response template, depending to switch_type

.. _`iwl_tdls_channel_switch_cmd.description`:

Description
-----------

The command is sent to initiate a channel switch and also in response to
incoming TDLS channel-switch request/response packets from remote peers.

.. _`iwl_tdls_channel_switch_notif`:

struct iwl_tdls_channel_switch_notif
====================================

.. c:type:: struct iwl_tdls_channel_switch_notif

    TDLS channel switch start notification

.. _`iwl_tdls_channel_switch_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_channel_switch_notif {
        __le32 status;
        __le32 offchannel_duration;
        __le32 sta_id;
    }

.. _`iwl_tdls_channel_switch_notif.members`:

Members
-------

status
    non-zero on success

offchannel_duration
    duration given in microseconds

sta_id
    peer currently performing the channel-switch with

.. _`iwl_tdls_sta_info`:

struct iwl_tdls_sta_info
========================

.. c:type:: struct iwl_tdls_sta_info

    TDLS station info

.. _`iwl_tdls_sta_info.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_sta_info {
        u8 sta_id;
        u8 tx_to_peer_tid;
        __le16 tx_to_peer_ssn;
        __le32 is_initiator;
    }

.. _`iwl_tdls_sta_info.members`:

Members
-------

sta_id
    station id of the TDLS peer

tx_to_peer_tid
    TID reserved vs. the peer for FW based Tx

tx_to_peer_ssn
    initial SSN the FW should use for Tx on its TID vs the peer

is_initiator
    1 if the peer is the TDLS link initiator, 0 otherwise

.. _`iwl_tdls_config_cmd`:

struct iwl_tdls_config_cmd
==========================

.. c:type:: struct iwl_tdls_config_cmd

    TDLS basic config command

.. _`iwl_tdls_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_config_cmd {
        __le32 id_and_color;
        u8 tdls_peer_count;
        u8 tx_to_ap_tid;
        __le16 tx_to_ap_ssn;
        struct iwl_tdls_sta_info sta_info[IWL_MVM_TDLS_STA_COUNT];
        __le32 pti_req_data_offset;
        struct iwl_tx_cmd pti_req_tx_cmd;
        u8 pti_req_template[0];
    }

.. _`iwl_tdls_config_cmd.members`:

Members
-------

id_and_color
    MAC id and color being configured

tdls_peer_count
    amount of currently connected TDLS peers

tx_to_ap_tid
    TID reverved vs. the AP for FW based Tx

tx_to_ap_ssn
    initial SSN the FW should use for Tx on its TID vs. the AP

sta_info
    per-station info. Only the first tdls_peer_count entries are set

pti_req_data_offset
    offset of network-level data for the PTI template

pti_req_tx_cmd
    Tx parameters for PTI request template

pti_req_template
    PTI request template data

.. _`iwl_tdls_config_sta_info_res`:

struct iwl_tdls_config_sta_info_res
===================================

.. c:type:: struct iwl_tdls_config_sta_info_res

    TDLS per-station config information

.. _`iwl_tdls_config_sta_info_res.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_config_sta_info_res {
        __le16 sta_id;
        __le16 tx_to_peer_last_seq;
    }

.. _`iwl_tdls_config_sta_info_res.members`:

Members
-------

sta_id
    station id of the TDLS peer

tx_to_peer_last_seq
    last sequence number used by FW during FW-based Tx to
    the peer

.. _`iwl_tdls_config_res`:

struct iwl_tdls_config_res
==========================

.. c:type:: struct iwl_tdls_config_res

    TDLS config information from FW

.. _`iwl_tdls_config_res.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tdls_config_res {
        __le32 tx_to_ap_last_seq;
        struct iwl_tdls_config_sta_info_res sta_info[IWL_MVM_TDLS_STA_COUNT];
    }

.. _`iwl_tdls_config_res.members`:

Members
-------

tx_to_ap_last_seq
    last sequence number used by FW during FW-based Tx to AP

sta_info
    per-station TDLS config information

.. This file was automatic generated / don't edit.

