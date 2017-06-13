.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-mac.h

.. _`iwl_mac_protection_flags`:

enum iwl_mac_protection_flags
=============================

.. c:type:: enum iwl_mac_protection_flags

    MAC context flags

.. _`iwl_mac_protection_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mac_protection_flags {
        MAC_PROT_FLG_TGG_PROTECT,
        MAC_PROT_FLG_HT_PROT,
        MAC_PROT_FLG_FAT_PROT,
        MAC_PROT_FLG_SELF_CTS_EN
    };

.. _`iwl_mac_protection_flags.constants`:

Constants
---------

MAC_PROT_FLG_TGG_PROTECT
    11g protection when transmitting OFDM frames,
    this will require CCK RTS/CTS2self.
    RTS/CTS will protect full burst time.

MAC_PROT_FLG_HT_PROT
    enable HT protection

MAC_PROT_FLG_FAT_PROT
    protect 40 MHz transmissions

MAC_PROT_FLG_SELF_CTS_EN
    allow CTS2self

.. _`iwl_mac_types`:

enum iwl_mac_types
==================

.. c:type:: enum iwl_mac_types

    Supported MAC types

.. _`iwl_mac_types.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mac_types {
        FW_MAC_TYPE_FIRST,
        FW_MAC_TYPE_AUX,
        FW_MAC_TYPE_LISTENER,
        FW_MAC_TYPE_PIBSS,
        FW_MAC_TYPE_IBSS,
        FW_MAC_TYPE_BSS_STA,
        FW_MAC_TYPE_P2P_DEVICE,
        FW_MAC_TYPE_P2P_STA,
        FW_MAC_TYPE_GO,
        FW_MAC_TYPE_TEST,
        FW_MAC_TYPE_MAX
    };

.. _`iwl_mac_types.constants`:

Constants
---------

FW_MAC_TYPE_FIRST
    lowest supported MAC type

FW_MAC_TYPE_AUX
    Auxiliary MAC (internal)

FW_MAC_TYPE_LISTENER
    monitor MAC type (?)

FW_MAC_TYPE_PIBSS
    Pseudo-IBSS

FW_MAC_TYPE_IBSS
    IBSS

FW_MAC_TYPE_BSS_STA
    BSS (managed) station

FW_MAC_TYPE_P2P_DEVICE
    P2P Device

FW_MAC_TYPE_P2P_STA
    P2P client

FW_MAC_TYPE_GO
    P2P GO

FW_MAC_TYPE_TEST
    ?

FW_MAC_TYPE_MAX
    highest support MAC type

.. _`iwl_tsf_id`:

enum iwl_tsf_id
===============

.. c:type:: enum iwl_tsf_id

    TSF hw timer ID

.. _`iwl_tsf_id.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tsf_id {
        TSF_ID_A,
        TSF_ID_B,
        TSF_ID_C,
        TSF_ID_D,
        NUM_TSF_IDS
    };

.. _`iwl_tsf_id.constants`:

Constants
---------

TSF_ID_A
    use TSF A

TSF_ID_B
    use TSF B

TSF_ID_C
    use TSF C

TSF_ID_D
    use TSF D

NUM_TSF_IDS
    number of TSF timers available

.. _`iwl_mac_data_ap`:

struct iwl_mac_data_ap
======================

.. c:type:: struct iwl_mac_data_ap

    configuration data for AP MAC context

.. _`iwl_mac_data_ap.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_data_ap {
        __le32 beacon_time;
        __le64 beacon_tsf;
        __le32 bi;
        __le32 bi_reciprocal;
        __le32 dtim_interval;
        __le32 dtim_reciprocal;
        __le32 mcast_qid;
        __le32 beacon_template;
    }

.. _`iwl_mac_data_ap.members`:

Members
-------

beacon_time
    beacon transmit time in system time

beacon_tsf
    beacon transmit time in TSF

bi
    beacon interval in TU

bi_reciprocal
    2^32 / bi

dtim_interval
    dtim transmit time in TU

dtim_reciprocal
    2^32 / dtim_interval

mcast_qid
    queue ID for multicast traffic.

beacon_template
    beacon template ID

.. _`iwl_mac_data_ap.note`:

NOTE
----

obsolete from VER2 and on

.. _`iwl_mac_data_ibss`:

struct iwl_mac_data_ibss
========================

.. c:type:: struct iwl_mac_data_ibss

    configuration data for IBSS MAC context

.. _`iwl_mac_data_ibss.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_data_ibss {
        __le32 beacon_time;
        __le64 beacon_tsf;
        __le32 bi;
        __le32 bi_reciprocal;
        __le32 beacon_template;
    }

.. _`iwl_mac_data_ibss.members`:

Members
-------

beacon_time
    beacon transmit time in system time

beacon_tsf
    beacon transmit time in TSF

bi
    beacon interval in TU

bi_reciprocal
    2^32 / bi

beacon_template
    beacon template ID

.. _`iwl_mac_data_sta`:

struct iwl_mac_data_sta
=======================

.. c:type:: struct iwl_mac_data_sta

    configuration data for station MAC context

.. _`iwl_mac_data_sta.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_data_sta {
        __le32 is_assoc;
        __le32 dtim_time;
        __le64 dtim_tsf;
        __le32 bi;
        __le32 bi_reciprocal;
        __le32 dtim_interval;
        __le32 dtim_reciprocal;
        __le32 listen_interval;
        __le32 assoc_id;
        __le32 assoc_beacon_arrive_time;
    }

.. _`iwl_mac_data_sta.members`:

Members
-------

is_assoc
    1 for associated state, 0 otherwise

dtim_time
    DTIM arrival time in system time

dtim_tsf
    DTIM arrival time in TSF

bi
    beacon interval in TU, applicable only when associated

bi_reciprocal
    2^32 / bi , applicable only when associated

dtim_interval
    DTIM interval in TU, applicable only when associated

dtim_reciprocal
    2^32 / dtim_interval , applicable only when associated

listen_interval
    in beacon intervals, applicable only when associated

assoc_id
    unique ID assigned by the AP during association

assoc_beacon_arrive_time
    *undescribed*

.. _`iwl_mac_data_go`:

struct iwl_mac_data_go
======================

.. c:type:: struct iwl_mac_data_go

    configuration data for P2P GO MAC context

.. _`iwl_mac_data_go.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_data_go {
        struct iwl_mac_data_ap ap;
        __le32 ctwin;
        __le32 opp_ps_enabled;
    }

.. _`iwl_mac_data_go.members`:

Members
-------

ap
    iwl_mac_data_ap struct with most config data

ctwin
    client traffic window in TU (period after TBTT when GO is present).
    0 indicates that there is no CT window.

opp_ps_enabled
    indicate that opportunistic PS allowed

.. _`iwl_mac_data_p2p_sta`:

struct iwl_mac_data_p2p_sta
===========================

.. c:type:: struct iwl_mac_data_p2p_sta

    configuration data for P2P client MAC context

.. _`iwl_mac_data_p2p_sta.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_data_p2p_sta {
        struct iwl_mac_data_sta sta;
        __le32 ctwin;
    }

.. _`iwl_mac_data_p2p_sta.members`:

Members
-------

sta
    iwl_mac_data_sta struct with most config data

ctwin
    client traffic window in TU (period after TBTT when GO is present).
    0 indicates that there is no CT window.

.. _`iwl_mac_data_pibss`:

struct iwl_mac_data_pibss
=========================

.. c:type:: struct iwl_mac_data_pibss

    Pseudo IBSS config data

.. _`iwl_mac_data_pibss.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_data_pibss {
        __le32 stats_interval;
    }

.. _`iwl_mac_data_pibss.members`:

Members
-------

stats_interval
    interval in TU between statistics notifications to host.

.. _`iwl_mac_filter_flags`:

enum iwl_mac_filter_flags
=========================

.. c:type:: enum iwl_mac_filter_flags

    MAC context filter flags

.. _`iwl_mac_filter_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mac_filter_flags {
        MAC_FILTER_IN_PROMISC,
        MAC_FILTER_IN_CONTROL_AND_MGMT,
        MAC_FILTER_ACCEPT_GRP,
        MAC_FILTER_DIS_DECRYPT,
        MAC_FILTER_DIS_GRP_DECRYPT,
        MAC_FILTER_IN_BEACON,
        MAC_FILTER_OUT_BCAST,
        MAC_FILTER_IN_CRC32,
        MAC_FILTER_IN_PROBE_REQUEST
    };

.. _`iwl_mac_filter_flags.constants`:

Constants
---------

MAC_FILTER_IN_PROMISC
    accept all data frames

MAC_FILTER_IN_CONTROL_AND_MGMT
    pass all management and
    control frames to the host

MAC_FILTER_ACCEPT_GRP
    accept multicast frames

MAC_FILTER_DIS_DECRYPT
    don't decrypt unicast frames

MAC_FILTER_DIS_GRP_DECRYPT
    don't decrypt multicast frames

MAC_FILTER_IN_BEACON
    transfer foreign BSS's beacons to host
    (in station mode when associated)

MAC_FILTER_OUT_BCAST
    filter out all broadcast frames

MAC_FILTER_IN_CRC32
    extract FCS and append it to frames

MAC_FILTER_IN_PROBE_REQUEST
    pass probe requests to host

.. _`iwl_mac_qos_flags`:

enum iwl_mac_qos_flags
======================

.. c:type:: enum iwl_mac_qos_flags

    QoS flags

.. _`iwl_mac_qos_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mac_qos_flags {
        MAC_QOS_FLG_UPDATE_EDCA,
        MAC_QOS_FLG_TGN,
        MAC_QOS_FLG_TXOP_TYPE
    };

.. _`iwl_mac_qos_flags.constants`:

Constants
---------

MAC_QOS_FLG_UPDATE_EDCA
    ?

MAC_QOS_FLG_TGN
    HT is enabled

MAC_QOS_FLG_TXOP_TYPE
    ?

.. _`iwl_ac_qos`:

struct iwl_ac_qos
=================

.. c:type:: struct iwl_ac_qos

    QOS timing params for MAC_CONTEXT_CMD

.. _`iwl_ac_qos.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ac_qos {
        __le16 cw_min;
        __le16 cw_max;
        u8 aifsn;
        u8 fifos_mask;
        __le16 edca_txop;
    }

.. _`iwl_ac_qos.members`:

Members
-------

cw_min
    Contention window, start value in numbers of slots.
    Should be a power-of-2, minus 1.  Device's default is 0x0f.

cw_max
    Contention window, max value in numbers of slots.
    Should be a power-of-2, minus 1.  Device's default is 0x3f.

aifsn
    Number of slots in Arbitration Interframe Space (before
    performing random backoff timing prior to Tx).  Device default 1.

fifos_mask
    FIFOs used by this MAC for this AC

edca_txop
    Length of Tx opportunity, in uSecs.  Device default is 0.

.. _`iwl_ac_qos.description`:

Description
-----------

One instance of this config struct for each of 4 EDCA access categories
in struct iwl_qosparam_cmd.

Device will automatically increase contention window by (2\*CW) + 1 for each
transmission retry.  Device uses cw_max as a bit mask, ANDed with new CW
value, to cap the CW value.

.. _`iwl_mac_ctx_cmd`:

struct iwl_mac_ctx_cmd
======================

.. c:type:: struct iwl_mac_ctx_cmd

    command structure to configure MAC contexts ( MAC_CONTEXT_CMD = 0x28 )

.. _`iwl_mac_ctx_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_ctx_cmd {
        __le32 id_and_color;
        __le32 action;
        __le32 mac_type;
        __le32 tsf_id;
        u8 node_addr[6];
        __le16 reserved_for_node_addr;
        u8 bssid_addr[6];
        __le16 reserved_for_bssid_addr;
        __le32 cck_rates;
        __le32 ofdm_rates;
        __le32 protection_flags;
        __le32 cck_short_preamble;
        __le32 short_slot;
        __le32 filter_flags;
        __le32 qos_flags;
        struct iwl_ac_qos ac[AC_NUM+1];
        union {unnamed_union};
    }

.. _`iwl_mac_ctx_cmd.members`:

Members
-------

id_and_color
    ID and color of the MAC

action
    action to perform, one of FW_CTXT_ACTION\_\*

mac_type
    one of FW_MAC_TYPE\_\*

tsf_id
    *undescribed*

node_addr
    MAC address

reserved_for_node_addr
    *undescribed*

bssid_addr
    BSSID

reserved_for_bssid_addr
    *undescribed*

cck_rates
    basic rates available for CCK

ofdm_rates
    basic rates available for OFDM

protection_flags
    combination of MAC_PROT_FLG_FLAG\_\*

cck_short_preamble
    0x20 for enabling short preamble, 0 otherwise

short_slot
    0x10 for enabling short slots, 0 otherwise

filter_flags
    combination of MAC_FILTER\_\*

qos_flags
    from MAC_QOS_FLG\_\*

ac
    one iwl_mac_qos configuration for each AC

{unnamed_union}
    anonymous


.. This file was automatic generated / don't edit.

