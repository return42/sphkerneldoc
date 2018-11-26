.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/d3.h

.. _`iwl_d3_wakeup_flags`:

enum iwl_d3_wakeup_flags
========================

.. c:type:: enum iwl_d3_wakeup_flags

    D3 manager wakeup flags

.. _`iwl_d3_wakeup_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_d3_wakeup_flags {
        IWL_WAKEUP_D3_CONFIG_FW_ERROR
    };

.. _`iwl_d3_wakeup_flags.constants`:

Constants
---------

IWL_WAKEUP_D3_CONFIG_FW_ERROR
    wake up on firmware sysassert

.. _`iwl_d3_manager_config`:

struct iwl_d3_manager_config
============================

.. c:type:: struct iwl_d3_manager_config

    D3 manager configuration command

.. _`iwl_d3_manager_config.definition`:

Definition
----------

.. code-block:: c

    struct iwl_d3_manager_config {
        __le32 min_sleep_time;
        __le32 wakeup_flags;
        __le32 wakeup_host_timer;
    }

.. _`iwl_d3_manager_config.members`:

Members
-------

min_sleep_time
    minimum sleep time (in usec)

wakeup_flags
    wakeup flags, see \ :c:type:`enum iwl_d3_wakeup_flags <iwl_d3_wakeup_flags>`\ 

wakeup_host_timer
    force wakeup after this many seconds

.. _`iwl_d3_manager_config.description`:

Description
-----------

The structure is used for the D3_CONFIG_CMD command.

.. _`iwl_proto_offloads`:

enum iwl_proto_offloads
=======================

.. c:type:: enum iwl_proto_offloads

    enabled protocol offloads

.. _`iwl_proto_offloads.definition`:

Definition
----------

.. code-block:: c

    enum iwl_proto_offloads {
        IWL_D3_PROTO_OFFLOAD_ARP,
        IWL_D3_PROTO_OFFLOAD_NS,
        IWL_D3_PROTO_IPV4_VALID,
        IWL_D3_PROTO_IPV6_VALID
    };

.. _`iwl_proto_offloads.constants`:

Constants
---------

IWL_D3_PROTO_OFFLOAD_ARP
    ARP data is enabled

IWL_D3_PROTO_OFFLOAD_NS
    NS (Neighbor Solicitation) is enabled

IWL_D3_PROTO_IPV4_VALID
    IPv4 data is valid

IWL_D3_PROTO_IPV6_VALID
    IPv6 data is valid

.. _`iwl_proto_offload_cmd_common`:

struct iwl_proto_offload_cmd_common
===================================

.. c:type:: struct iwl_proto_offload_cmd_common

    ARP/NS offload common part

.. _`iwl_proto_offload_cmd_common.definition`:

Definition
----------

.. code-block:: c

    struct iwl_proto_offload_cmd_common {
        __le32 enabled;
        __be32 remote_ipv4_addr;
        __be32 host_ipv4_addr;
        u8 arp_mac_addr[ETH_ALEN];
        __le16 reserved;
    }

.. _`iwl_proto_offload_cmd_common.members`:

Members
-------

enabled
    enable flags

remote_ipv4_addr
    remote address to answer to (or zero if all)

host_ipv4_addr
    our IPv4 address to respond to queries for

arp_mac_addr
    our MAC address for ARP responses

reserved
    unused

.. _`iwl_proto_offload_cmd_v1`:

struct iwl_proto_offload_cmd_v1
===============================

.. c:type:: struct iwl_proto_offload_cmd_v1

    ARP/NS offload configuration

.. _`iwl_proto_offload_cmd_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_proto_offload_cmd_v1 {
        struct iwl_proto_offload_cmd_common common;
        u8 remote_ipv6_addr[16];
        u8 solicited_node_ipv6_addr[16];
        u8 target_ipv6_addr[IWL_PROTO_OFFLOAD_NUM_IPV6_ADDRS_V1][16];
        u8 ndp_mac_addr[ETH_ALEN];
        __le16 reserved2;
    }

.. _`iwl_proto_offload_cmd_v1.members`:

Members
-------

common
    common/IPv4 configuration

remote_ipv6_addr
    remote address to answer to (or zero if all)

solicited_node_ipv6_addr
    broken -- solicited node address exists
    for each target address

target_ipv6_addr
    our target addresses

ndp_mac_addr
    neighbor solicitation response MAC address

reserved2
    reserved

.. _`iwl_proto_offload_cmd_v2`:

struct iwl_proto_offload_cmd_v2
===============================

.. c:type:: struct iwl_proto_offload_cmd_v2

    ARP/NS offload configuration

.. _`iwl_proto_offload_cmd_v2.definition`:

Definition
----------

.. code-block:: c

    struct iwl_proto_offload_cmd_v2 {
        struct iwl_proto_offload_cmd_common common;
        u8 remote_ipv6_addr[16];
        u8 solicited_node_ipv6_addr[16];
        u8 target_ipv6_addr[IWL_PROTO_OFFLOAD_NUM_IPV6_ADDRS_V2][16];
        u8 ndp_mac_addr[ETH_ALEN];
        u8 num_valid_ipv6_addrs;
        u8 reserved2[3];
    }

.. _`iwl_proto_offload_cmd_v2.members`:

Members
-------

common
    common/IPv4 configuration

remote_ipv6_addr
    remote address to answer to (or zero if all)

solicited_node_ipv6_addr
    broken -- solicited node address exists
    for each target address

target_ipv6_addr
    our target addresses

ndp_mac_addr
    neighbor solicitation response MAC address

num_valid_ipv6_addrs
    number of valid IPv6 addresses

reserved2
    reserved

.. _`iwl_proto_offload_cmd_v3_small`:

struct iwl_proto_offload_cmd_v3_small
=====================================

.. c:type:: struct iwl_proto_offload_cmd_v3_small

    ARP/NS offload configuration

.. _`iwl_proto_offload_cmd_v3_small.definition`:

Definition
----------

.. code-block:: c

    struct iwl_proto_offload_cmd_v3_small {
        struct iwl_proto_offload_cmd_common common;
        __le32 num_valid_ipv6_addrs;
        struct iwl_targ_addr targ_addrs[IWL_PROTO_OFFLOAD_NUM_IPV6_ADDRS_V3S];
        struct iwl_ns_config ns_config[IWL_PROTO_OFFLOAD_NUM_NS_CONFIG_V3S];
    }

.. _`iwl_proto_offload_cmd_v3_small.members`:

Members
-------

common
    common/IPv4 configuration

num_valid_ipv6_addrs
    number of valid IPv6 addresses

targ_addrs
    target IPv6 addresses

ns_config
    NS offload configurations

.. _`iwl_proto_offload_cmd_v3_large`:

struct iwl_proto_offload_cmd_v3_large
=====================================

.. c:type:: struct iwl_proto_offload_cmd_v3_large

    ARP/NS offload configuration

.. _`iwl_proto_offload_cmd_v3_large.definition`:

Definition
----------

.. code-block:: c

    struct iwl_proto_offload_cmd_v3_large {
        struct iwl_proto_offload_cmd_common common;
        __le32 num_valid_ipv6_addrs;
        struct iwl_targ_addr targ_addrs[IWL_PROTO_OFFLOAD_NUM_IPV6_ADDRS_V3L];
        struct iwl_ns_config ns_config[IWL_PROTO_OFFLOAD_NUM_NS_CONFIG_V3L];
    }

.. _`iwl_proto_offload_cmd_v3_large.members`:

Members
-------

common
    common/IPv4 configuration

num_valid_ipv6_addrs
    number of valid IPv6 addresses

targ_addrs
    target IPv6 addresses

ns_config
    NS offload configurations

.. _`iwl_wowlan_config_cmd`:

struct iwl_wowlan_config_cmd
============================

.. c:type:: struct iwl_wowlan_config_cmd

    WoWLAN configuration

.. _`iwl_wowlan_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_wowlan_config_cmd {
        __le32 wakeup_filter;
        __le16 non_qos_seq;
        __le16 qos_seq[8];
        u8 wowlan_ba_teardown_tids;
        u8 is_11n_connection;
        u8 offloading_tid;
        u8 flags;
        u8 reserved[2];
    }

.. _`iwl_wowlan_config_cmd.members`:

Members
-------

wakeup_filter
    filter from \ :c:type:`enum iwl_wowlan_wakeup_filters <iwl_wowlan_wakeup_filters>`\ 

non_qos_seq
    non-QoS sequence counter to use next

qos_seq
    QoS sequence counters to use next

wowlan_ba_teardown_tids
    bitmap of BA sessions to tear down

is_11n_connection
    indicates HT connection

offloading_tid
    TID reserved for firmware use

flags
    extra flags, see \ :c:type:`enum iwl_wowlan_flags <iwl_wowlan_flags>`\ 

reserved
    reserved

.. _`iwl_wowlan_gtk_status`:

struct iwl_wowlan_gtk_status
============================

.. c:type:: struct iwl_wowlan_gtk_status

    GTK status

.. _`iwl_wowlan_gtk_status.definition`:

Definition
----------

.. code-block:: c

    struct iwl_wowlan_gtk_status {
        u8 key[WOWLAN_KEY_MAX_SIZE];
        u8 key_len;
        u8 key_flags;
        u8 reserved[2];
        u8 tkip_mic_key[8];
        struct iwl_wowlan_rsc_tsc_params_cmd rsc;
    }

.. _`iwl_wowlan_gtk_status.members`:

Members
-------

key
    GTK material

key_len
    GTK legth, if set to 0, the key is not available

key_flags
    information about the key:
    bits[0:1]:  key index assigned by the AP
    bits[2:6]:  GTK index of the key in the internal DB
    bit[7]:     Set iff this is the currently used GTK

reserved
    padding

tkip_mic_key
    TKIP RX MIC key

rsc
    TSC RSC counters

.. _`iwl_wowlan_igtk_status`:

struct iwl_wowlan_igtk_status
=============================

.. c:type:: struct iwl_wowlan_igtk_status

    IGTK status

.. _`iwl_wowlan_igtk_status.definition`:

Definition
----------

.. code-block:: c

    struct iwl_wowlan_igtk_status {
        u8 key[WOWLAN_KEY_MAX_SIZE];
        u8 ipn[6];
        u8 key_len;
        u8 key_flags;
    }

.. _`iwl_wowlan_igtk_status.members`:

Members
-------

key
    IGTK material

ipn
    the IGTK packet number (replay counter)

key_len
    IGTK length, if set to 0, the key is not available

key_flags
    information about the key:
    bits[0]:    key index assigned by the AP (0: index 4, 1: index 5)
    bits[1:5]:  IGTK index of the key in the internal DB
    bit[6]:     Set iff this is the currently used IGTK

.. _`iwl_wowlan_status_v6`:

struct iwl_wowlan_status_v6
===========================

.. c:type:: struct iwl_wowlan_status_v6

    WoWLAN status

.. _`iwl_wowlan_status_v6.definition`:

Definition
----------

.. code-block:: c

    struct iwl_wowlan_status_v6 {
        struct iwl_wowlan_gtk_status_v1 gtk;
        __le64 replay_ctr;
        __le16 pattern_number;
        __le16 non_qos_seq_ctr;
        __le16 qos_seq_ctr[8];
        __le32 wakeup_reasons;
        __le32 num_of_gtk_rekeys;
        __le32 transmitted_ndps;
        __le32 received_beacons;
        __le32 wake_packet_length;
        __le32 wake_packet_bufsize;
        u8 wake_packet[];
    }

.. _`iwl_wowlan_status_v6.members`:

Members
-------

gtk
    GTK data

replay_ctr
    GTK rekey replay counter

pattern_number
    number of the matched pattern

non_qos_seq_ctr
    non-QoS sequence counter to use next

qos_seq_ctr
    QoS sequence counters to use next

wakeup_reasons
    wakeup reasons, see \ :c:type:`enum iwl_wowlan_wakeup_reason <iwl_wowlan_wakeup_reason>`\ 

num_of_gtk_rekeys
    number of GTK rekeys

transmitted_ndps
    number of transmitted neighbor discovery packets

received_beacons
    number of received beacons

wake_packet_length
    wakeup packet length

wake_packet_bufsize
    wakeup packet buffer size

wake_packet
    wakeup packet

.. _`iwl_wowlan_status`:

struct iwl_wowlan_status
========================

.. c:type:: struct iwl_wowlan_status

    WoWLAN status

.. _`iwl_wowlan_status.definition`:

Definition
----------

.. code-block:: c

    struct iwl_wowlan_status {
        struct iwl_wowlan_gtk_status gtk[WOWLAN_GTK_KEYS_NUM];
        struct iwl_wowlan_igtk_status igtk[WOWLAN_IGTK_KEYS_NUM];
        __le64 replay_ctr;
        __le16 pattern_number;
        __le16 non_qos_seq_ctr;
        __le16 qos_seq_ctr[8];
        __le32 wakeup_reasons;
        __le32 num_of_gtk_rekeys;
        __le32 transmitted_ndps;
        __le32 received_beacons;
        __le32 wake_packet_length;
        __le32 wake_packet_bufsize;
        u8 wake_packet[];
    }

.. _`iwl_wowlan_status.members`:

Members
-------

gtk
    GTK data

igtk
    IGTK data

replay_ctr
    GTK rekey replay counter

pattern_number
    number of the matched pattern

non_qos_seq_ctr
    non-QoS sequence counter to use next

qos_seq_ctr
    QoS sequence counters to use next

wakeup_reasons
    wakeup reasons, see \ :c:type:`enum iwl_wowlan_wakeup_reason <iwl_wowlan_wakeup_reason>`\ 

num_of_gtk_rekeys
    number of GTK rekeys

transmitted_ndps
    number of transmitted neighbor discovery packets

received_beacons
    number of received beacons

wake_packet_length
    wakeup packet length

wake_packet_bufsize
    wakeup packet buffer size

wake_packet
    wakeup packet

.. This file was automatic generated / don't edit.

