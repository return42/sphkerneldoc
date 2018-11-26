.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/mac.h

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
    TSF of first beacon after association

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
        MAC_FILTER_IN_PROBE_REQUEST,
        MAC_FILTER_IN_11AX
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

MAC_FILTER_IN_11AX
    mark BSS as supporting 802.11ax

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
        union {
            struct iwl_mac_data_ap ap;
            struct iwl_mac_data_go go;
            struct iwl_mac_data_sta sta;
            struct iwl_mac_data_p2p_sta p2p_sta;
            struct iwl_mac_data_p2p_dev p2p_dev;
            struct iwl_mac_data_pibss pibss;
            struct iwl_mac_data_ibss ibss;
        } ;
    }

.. _`iwl_mac_ctx_cmd.members`:

Members
-------

id_and_color
    ID and color of the MAC

action
    action to perform, one of FW_CTXT_ACTION\_\*

mac_type
    one of \ :c:type:`enum iwl_mac_types <iwl_mac_types>`\ 

tsf_id
    TSF HW timer, one of \ :c:type:`enum iwl_tsf_id <iwl_tsf_id>`\ 

node_addr
    MAC address

reserved_for_node_addr
    reserved

bssid_addr
    BSSID

reserved_for_bssid_addr
    reserved

cck_rates
    basic rates available for CCK

ofdm_rates
    basic rates available for OFDM

protection_flags
    combination of \ :c:type:`enum iwl_mac_protection_flags <iwl_mac_protection_flags>`\ 

cck_short_preamble
    0x20 for enabling short preamble, 0 otherwise

short_slot
    0x10 for enabling short slots, 0 otherwise

filter_flags
    combination of \ :c:type:`enum iwl_mac_filter_flags <iwl_mac_filter_flags>`\ 

qos_flags
    from \ :c:type:`enum iwl_mac_qos_flags <iwl_mac_qos_flags>`\ 

ac
    one iwl_mac_qos configuration for each AC

{unnamed_union}
    anonymous

ap
    *undescribed*

go
    *undescribed*

sta
    *undescribed*

p2p_sta
    *undescribed*

p2p_dev
    *undescribed*

pibss
    *undescribed*

ibss
    *undescribed*

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
    number of expected beacons

num_recvd_beacons
    number of received beacons

.. _`iwl_he_backoff_conf`:

struct iwl_he_backoff_conf
==========================

.. c:type:: struct iwl_he_backoff_conf

    used for backoff configuration Per each trigger-based AC, (set by MU EDCA Parameter set info-element) used for backoff configuration of TXF5..TXF8 trigger based. The MU-TIMER is reloaded w/ MU_TIME each time a frame from the AC is sent via trigger-based TX.

.. _`iwl_he_backoff_conf.definition`:

Definition
----------

.. code-block:: c

    struct iwl_he_backoff_conf {
        __le16 cwmin;
        __le16 cwmax;
        __le16 aifsn;
        __le16 mu_time;
    }

.. _`iwl_he_backoff_conf.members`:

Members
-------

cwmin
    CW min

cwmax
    CW max

aifsn
    AIFSN
    AIFSN=0, means that no backoff from the specified TRIG-BASED AC is
    allowed till the MU-TIMER is 0

mu_time
    MU time in 8TU units

.. _`iwl_he_pkt_ext`:

struct iwl_he_pkt_ext
=====================

.. c:type:: struct iwl_he_pkt_ext

    QAM thresholds The required PPE is set via HE Capabilities IE, per Nss x BW x MCS

.. _`iwl_he_pkt_ext.definition`:

Definition
----------

.. code-block:: c

    struct iwl_he_pkt_ext {
        u8 pkt_ext_qam_th[MAX_HE_SUPP_NSS][MAX_HE_CHANNEL_BW_INDX][2];
    }

.. _`iwl_he_pkt_ext.members`:

Members
-------

pkt_ext_qam_th
    QAM thresholds
    For each Nss/Bw define 2 QAM thrsholds (0..5)
    For rates below the low_th, no need for PPE
    For rates between low_th and high_th, need 8us PPE
    For rates equal or higher then the high_th, need 16us PPE
    Nss (0-siso, 1-mimo2) x BW (0-20MHz, 1-40MHz, 2-80MHz, 3-160MHz) x
    (0-low_th, 1-high_th)

.. _`iwl_he_pkt_ext.the-ie-is-organized-in-the-following-way`:

The IE is organized in the following way
----------------------------------------

Support for Nss x BW (or RU) matrix:
(0=SISO, 1=MIMO2) x (0-20MHz, 1-40MHz, 2-80MHz, 3-160MHz)

.. _`iwl_he_pkt_ext.each-entry-contains-2-qam-thresholds-for-8us-and-16us`:

Each entry contains 2 QAM thresholds for 8us and 16us
-----------------------------------------------------

0=BPSK, 1=QPSK, 2=16QAM, 3=64QAM, 4=256QAM, 5=1024QAM, 6/7=RES
i.e. QAM_th1 < QAM_th2 such if TX uses QAM_tx:
QAM_tx < QAM_th1            --> PPE=0us
QAM_th1 <= QAM_tx < QAM_th2 --> PPE=8us
QAM_th2 <= QAM_tx           --> PPE=16us

.. _`iwl_he_sta_ctxt_flags`:

enum iwl_he_sta_ctxt_flags
==========================

.. c:type:: enum iwl_he_sta_ctxt_flags

    HE STA context flags

.. _`iwl_he_sta_ctxt_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_he_sta_ctxt_flags {
        STA_CTXT_HE_REF_BSSID_VALID,
        STA_CTXT_HE_BSS_COLOR_DIS,
        STA_CTXT_HE_PARTIAL_BSS_COLOR,
        STA_CTXT_HE_32BIT_BA_BITMAP,
        STA_CTXT_HE_PACKET_EXT,
        STA_CTXT_HE_TRIG_RND_ALLOC,
        STA_CTXT_HE_CONST_TRIG_RND_ALLOC,
        STA_CTXT_HE_ACK_ENABLED,
        STA_CTXT_HE_MU_EDCA_CW
    };

.. _`iwl_he_sta_ctxt_flags.constants`:

Constants
---------

STA_CTXT_HE_REF_BSSID_VALID
    ref bssid addr valid (for receiving specific
    control frames such as TRIG, NDPA, BACK)

STA_CTXT_HE_BSS_COLOR_DIS
    BSS color disable, don't use the BSS
    color for RX filter but use MAC header

STA_CTXT_HE_PARTIAL_BSS_COLOR
    partial BSS color allocation

STA_CTXT_HE_32BIT_BA_BITMAP
    indicates the receiver supports BA bitmap
    of 32-bits

STA_CTXT_HE_PACKET_EXT
    indicates that the packet-extension info is valid
    and should be used

STA_CTXT_HE_TRIG_RND_ALLOC
    indicates that trigger based random allocation
    is enabled according to UORA element existence

STA_CTXT_HE_CONST_TRIG_RND_ALLOC
    used for AV testing

STA_CTXT_HE_ACK_ENABLED
    indicates that the AP supports receiving ACK-
    enabled AGG, i.e. both BACK and non-BACK frames in a single AGG

STA_CTXT_HE_MU_EDCA_CW
    indicates that there is an element of MU EDCA
    parameter set, i.e. the backoff counters for trig-based ACs

.. _`iwl_he_htc_flags`:

enum iwl_he_htc_flags
=====================

.. c:type:: enum iwl_he_htc_flags

    HE HTC support flags

.. _`iwl_he_htc_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_he_htc_flags {
        IWL_HE_HTC_SUPPORT,
        IWL_HE_HTC_UL_MU_RESP_SCHED,
        IWL_HE_HTC_BSR_SUPP,
        IWL_HE_HTC_OMI_SUPP,
        IWL_HE_HTC_BQR_SUPP
    };

.. _`iwl_he_htc_flags.constants`:

Constants
---------

IWL_HE_HTC_SUPPORT
    HE-HTC support

IWL_HE_HTC_UL_MU_RESP_SCHED
    HE UL MU response schedule
    support via A-control field

IWL_HE_HTC_BSR_SUPP
    BSR support in A-control field

IWL_HE_HTC_OMI_SUPP
    A-OMI support in A-control field

IWL_HE_HTC_BQR_SUPP
    A-BQR support in A-control field

.. _`iwl_he_sta_context_cmd`:

struct iwl_he_sta_context_cmd
=============================

.. c:type:: struct iwl_he_sta_context_cmd

    configure FW to work with HE AP

.. _`iwl_he_sta_context_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_he_sta_context_cmd {
        u8 sta_id;
        u8 tid_limit;
        u8 reserved1;
        u8 reserved2;
        __le32 flags;
        u8 ref_bssid_addr[6];
        __le16 reserved0;
        __le32 htc_flags;
        u8 frag_flags;
        u8 frag_level;
        u8 frag_max_num;
        u8 frag_min_size;
        struct iwl_he_pkt_ext pkt_ext;
        u8 bss_color;
        u8 htc_trig_based_pkt_ext;
        __le16 frame_time_rts_th;
        u8 rand_alloc_ecwmin;
        u8 rand_alloc_ecwmax;
        __le16 reserved3;
        struct iwl_he_backoff_conf trig_based_txf[AC_NUM];
    }

.. _`iwl_he_sta_context_cmd.members`:

Members
-------

sta_id
    STA id

tid_limit
    max num of TIDs in TX HE-SU multi-TID agg
    0 - bad value, 1 - multi-tid not supported, 2..8 - tid limit

reserved1
    reserved byte for future use

reserved2
    reserved byte for future use

flags
    see \ ``iwl_11ax_sta_ctxt_flags``\ 

ref_bssid_addr
    reference BSSID used by the AP

reserved0
    reserved 2 bytes for aligning the ref_bssid_addr field to 8 bytes

htc_flags
    which features are supported in HTC

frag_flags
    frag support in A-MSDU

frag_level
    frag support level

frag_max_num
    max num of "open" MSDUs in the receiver (in power of 2)

frag_min_size
    min frag size (except last frag)

pkt_ext
    optional, exists according to PPE-present bit in the HE-PHY capa

bss_color
    11ax AP ID that is used in the HE SIG-A to mark inter BSS frame

htc_trig_based_pkt_ext
    default PE in 4us units

frame_time_rts_th
    HE duration RTS threshold, in units of 32us

rand_alloc_ecwmin
    random CWmin = 2\*\*ECWmin-1

rand_alloc_ecwmax
    random CWmax = 2\*\*ECWmax-1

reserved3
    reserved byte for future use

trig_based_txf
    MU EDCA Parameter set for the trigger based traffic queues

.. _`iwl_he_monitor_cmd`:

struct iwl_he_monitor_cmd
=========================

.. c:type:: struct iwl_he_monitor_cmd

    configure air sniffer for HE

.. _`iwl_he_monitor_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_he_monitor_cmd {
        u8 bssid[6];
        __le16 reserved1;
        __le16 aid;
        u8 reserved2[6];
    }

.. _`iwl_he_monitor_cmd.members`:

Members
-------

bssid
    the BSSID to sniff for

reserved1
    reserved for dword alignment

aid
    the AID to track on for HE MU

reserved2
    reserved for future use

.. This file was automatic generated / don't edit.

