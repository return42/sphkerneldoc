.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/sta_info.h

.. _`ieee80211_sta_info_flags`:

enum ieee80211_sta_info_flags
=============================

.. c:type:: enum ieee80211_sta_info_flags

    Stations flags

.. _`ieee80211_sta_info_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_sta_info_flags {
        WLAN_STA_AUTH,
        WLAN_STA_ASSOC,
        WLAN_STA_PS_STA,
        WLAN_STA_AUTHORIZED,
        WLAN_STA_SHORT_PREAMBLE,
        WLAN_STA_WDS,
        WLAN_STA_CLEAR_PS_FILT,
        WLAN_STA_MFP,
        WLAN_STA_BLOCK_BA,
        WLAN_STA_PS_DRIVER,
        WLAN_STA_PSPOLL,
        WLAN_STA_TDLS_PEER,
        WLAN_STA_TDLS_PEER_AUTH,
        WLAN_STA_TDLS_INITIATOR,
        WLAN_STA_TDLS_CHAN_SWITCH,
        WLAN_STA_TDLS_OFF_CHANNEL,
        WLAN_STA_TDLS_WIDER_BW,
        WLAN_STA_UAPSD,
        WLAN_STA_SP,
        WLAN_STA_4ADDR_EVENT,
        WLAN_STA_INSERTED,
        WLAN_STA_RATE_CONTROL,
        WLAN_STA_TOFFSET_KNOWN,
        WLAN_STA_MPSP_OWNER,
        WLAN_STA_MPSP_RECIPIENT,
        WLAN_STA_PS_DELIVER,
        NUM_WLAN_STA_FLAGS
    };

.. _`ieee80211_sta_info_flags.constants`:

Constants
---------

WLAN_STA_AUTH
    Station is authenticated.

WLAN_STA_ASSOC
    Station is associated.

WLAN_STA_PS_STA
    Station is in power-save mode

WLAN_STA_AUTHORIZED
    Station is authorized to send/receive traffic.
    This bit is always checked so needs to be enabled for all stations
    when virtual port control is not in use.

WLAN_STA_SHORT_PREAMBLE
    Station is capable of receiving short-preamble
    frames.

WLAN_STA_WDS
    Station is one of our WDS peers.

WLAN_STA_CLEAR_PS_FILT
    Clear PS filter in hardware (using the
    IEEE80211_TX_CTL_CLEAR_PS_FILT control flag) when the next
    frame to this station is transmitted.

WLAN_STA_MFP
    Management frame protection is used with this STA.

WLAN_STA_BLOCK_BA
    Used to deny ADDBA requests (both TX and RX)
    during suspend/resume and station removal.

WLAN_STA_PS_DRIVER
    driver requires keeping this station in
    power-save mode logically to flush frames that might still
    be in the queues

WLAN_STA_PSPOLL
    Station sent PS-poll while driver was keeping
    station in power-save mode, reply when the driver unblocks.

WLAN_STA_TDLS_PEER
    Station is a TDLS peer.

WLAN_STA_TDLS_PEER_AUTH
    This TDLS peer is authorized to send direct
    packets. This means the link is enabled.

WLAN_STA_TDLS_INITIATOR
    We are the initiator of the TDLS link with this
    station.

WLAN_STA_TDLS_CHAN_SWITCH
    This TDLS peer supports TDLS channel-switching

WLAN_STA_TDLS_OFF_CHANNEL
    The local STA is currently off-channel with this
    TDLS peer

WLAN_STA_TDLS_WIDER_BW
    This TDLS peer supports working on a wider bw on
    the BSS base channel.

WLAN_STA_UAPSD
    Station requested unscheduled SP while driver was
    keeping station in power-save mode, reply when the driver
    unblocks the station.

WLAN_STA_SP
    Station is in a service period, so don't try to
    reply to other uAPSD trigger frames or PS-Poll.

WLAN_STA_4ADDR_EVENT
    4-addr event was already sent for this frame.

WLAN_STA_INSERTED
    This station is inserted into the hash table.

WLAN_STA_RATE_CONTROL
    rate control was initialized for this station.

WLAN_STA_TOFFSET_KNOWN
    toffset calculated for this station is valid.

WLAN_STA_MPSP_OWNER
    local STA is owner of a mesh Peer Service Period.

WLAN_STA_MPSP_RECIPIENT
    local STA is recipient of a MPSP.

WLAN_STA_PS_DELIVER
    station woke up, but we're still blocking TX
    until pending frames are delivered

NUM_WLAN_STA_FLAGS
    number of defined flags

.. _`ieee80211_sta_info_flags.description`:

Description
-----------

These flags are used with \ :c:type:`struct sta_info <sta_info>`\ 's \ ``flags``\  member, but
only indirectly with \ :c:func:`set_sta_flag`\  and friends.

.. _`tid_ampdu_tx`:

struct tid_ampdu_tx
===================

.. c:type:: struct tid_ampdu_tx

    TID aggregation information (Tx).

.. _`tid_ampdu_tx.definition`:

Definition
----------

.. code-block:: c

    struct tid_ampdu_tx {
        struct rcu_head rcu_head;
        struct timer_list session_timer;
        struct timer_list addba_resp_timer;
        struct sk_buff_head pending;
        unsigned long state;
        unsigned long last_tx;
        u16 timeout;
        u8 dialog_token;
        u8 stop_initiator;
        bool tx_stop;
        u8 buf_size;
        u16 failed_bar_ssn;
        bool bar_pending;
        bool amsdu;
    }

.. _`tid_ampdu_tx.members`:

Members
-------

rcu_head
    rcu head for freeing structure

session_timer
    check if we keep Tx-ing on the TID (by timeout value)

addba_resp_timer
    timer for peer's response to addba request

pending
    pending frames queue -- use sta's spinlock to protect

state
    session state (see above)

last_tx
    jiffies of last tx activity

timeout
    session timeout value to be filled in ADDBA requests

dialog_token
    dialog token for aggregation session

stop_initiator
    initiator of a session stop

tx_stop
    TX DelBA frame when stopping

buf_size
    reorder buffer size at receiver

failed_bar_ssn
    ssn of the last failed BAR tx attempt

bar_pending
    BAR needs to be re-sent

amsdu
    support A-MSDU withing A-MDPU

.. _`tid_ampdu_tx.description`:

Description
-----------

This structure's lifetime is managed by RCU, assignments to
the array holding it must hold the aggregation mutex.

The TX path can access it under RCU lock-free if, and
only if, the state has the flag \ ``HT_AGG_STATE_OPERATIONAL``\ 
set. Otherwise, the TX path must also acquire the spinlock
and re-check the state, see comments in the tx code
touching it.

.. _`tid_ampdu_rx`:

struct tid_ampdu_rx
===================

.. c:type:: struct tid_ampdu_rx

    TID aggregation information (Rx).

.. _`tid_ampdu_rx.definition`:

Definition
----------

.. code-block:: c

    struct tid_ampdu_rx {
        struct rcu_head rcu_head;
        spinlock_t reorder_lock;
        u64 reorder_buf_filtered;
        struct sk_buff_head *reorder_buf;
        unsigned long *reorder_time;
        struct timer_list session_timer;
        struct timer_list reorder_timer;
        unsigned long last_rx;
        u16 head_seq_num;
        u16 stored_mpdu_num;
        u16 ssn;
        u16 buf_size;
        u16 timeout;
        u8 dialog_token;
        bool auto_seq;
        bool removed;
    }

.. _`tid_ampdu_rx.members`:

Members
-------

rcu_head
    RCU head used for freeing this struct

reorder_lock
    serializes access to reorder buffer, see below.

reorder_buf_filtered
    bitmap indicating where there are filtered frames in
    the reorder buffer that should be ignored when releasing frames

reorder_buf
    buffer to reorder incoming aggregated MPDUs. An MPDU may be an
    A-MSDU with individually reported subframes.

reorder_time
    jiffies when skb was added

session_timer
    check if peer keeps Tx-ing on the TID (by timeout value)

reorder_timer
    releases expired frames from the reorder buffer.

last_rx
    jiffies of last rx activity

head_seq_num
    head sequence number in reordering buffer.

stored_mpdu_num
    number of MPDUs in reordering buffer

ssn
    Starting Sequence Number expected to be aggregated.

buf_size
    buffer size for incoming A-MPDUs

timeout
    reset timer value (in TUs).

dialog_token
    dialog token for aggregation session

auto_seq
    used for offloaded BA sessions to automatically pick head_seq_and
    and ssn.

removed
    this session is removed (but might have been found due to RCU)

.. _`tid_ampdu_rx.description`:

Description
-----------

This structure's lifetime is managed by RCU, assignments to
the array holding it must hold the aggregation mutex.

The \ ``reorder_lock``\  is used to protect the members of this
struct, except for \ ``timeout``\ , \ ``buf_size``\  and \ ``dialog_token``\ ,
which are constant across the lifetime of the struct (the
dialog token being used only for debugging).

.. _`sta_ampdu_mlme`:

struct sta_ampdu_mlme
=====================

.. c:type:: struct sta_ampdu_mlme

    STA aggregation information.

.. _`sta_ampdu_mlme.definition`:

Definition
----------

.. code-block:: c

    struct sta_ampdu_mlme {
        struct mutex mtx;
        struct tid_ampdu_rx __rcu  *tid_rx[IEEE80211_NUM_TIDS];
        unsigned long tid_rx_timer_expired[BITS_TO_LONGS(IEEE80211_NUM_TIDS)];
        unsigned long tid_rx_stop_requested[BITS_TO_LONGS(IEEE80211_NUM_TIDS)];
        unsigned long agg_session_valid[BITS_TO_LONGS(IEEE80211_NUM_TIDS)];
        struct work_struct work;
        struct tid_ampdu_tx __rcu  *tid_tx[IEEE80211_NUM_TIDS];
        struct tid_ampdu_tx  *tid_start_tx[IEEE80211_NUM_TIDS];
        unsigned long last_addba_req_time[IEEE80211_NUM_TIDS];
        u8 addba_req_num[IEEE80211_NUM_TIDS];
        u8 dialog_token_allocator;
    }

.. _`sta_ampdu_mlme.members`:

Members
-------

mtx
    mutex to protect all TX data (except non-NULL assignments
    to tid_tx[idx], which are protected by the sta spinlock)
    tid_start_tx is also protected by sta->lock.

tid_rx
    aggregation info for Rx per TID -- RCU protected

tid_rx_timer_expired
    bitmap indicating on which TIDs the
    RX timer expired until the work for it runs

tid_rx_stop_requested
    bitmap indicating which BA sessions per TID the
    driver requested to close until the work for it runs

agg_session_valid
    bitmap indicating which TID has a rx BA session open on

work
    work struct for starting/stopping aggregation

tid_tx
    aggregation info for Tx per TID

tid_start_tx
    sessions where start was requested

last_addba_req_time
    timestamp of the last addBA request.

addba_req_num
    number of times addBA request has been sent.

dialog_token_allocator
    dialog token enumerator for each new session;

.. _`ieee80211_fast_tx`:

struct ieee80211_fast_tx
========================

.. c:type:: struct ieee80211_fast_tx

    TX fastpath information

.. _`ieee80211_fast_tx.definition`:

Definition
----------

.. code-block:: c

    struct ieee80211_fast_tx {
        struct ieee80211_key *key;
        u8 hdr_len;
        u8 sa_offs;
        u8 da_offs;
        u8 pn_offs;
        u8 band;
        u8 hdr[30 + 2 + IEEE80211_FAST_XMIT_MAX_IV +sizeof(rfc1042_header)];
        struct rcu_head rcu_head;
    }

.. _`ieee80211_fast_tx.members`:

Members
-------

key
    key to use for hw crypto

hdr_len
    actual 802.11 header length

sa_offs
    offset of the SA

da_offs
    offset of the DA

pn_offs
    offset where to put PN for crypto (or 0 if not needed)

band
    band this will be transmitted on, for tx_info

hdr
    the 802.11 header to put with the frame

rcu_head
    RCU head to free this struct

.. _`ieee80211_fast_tx.description`:

Description
-----------

This struct is small enough so that the common case (maximum crypto
header length of 8 like for CCMP/GCMP) fits into a single 64-byte
cache line.

.. _`ieee80211_fast_rx`:

struct ieee80211_fast_rx
========================

.. c:type:: struct ieee80211_fast_rx

    RX fastpath information

.. _`ieee80211_fast_rx.definition`:

Definition
----------

.. code-block:: c

    struct ieee80211_fast_rx {
        struct net_device *dev;
        enum nl80211_iftype vif_type;
        u8 vif_addr[ETH_ALEN];
        u8 rfc1042_hdr[6];
        __be16 control_port_protocol;
        __le16 expected_ds_bits;
        u8 icv_len;
        u8 key:1;
        u8 sta_notify:1:1;
        u8 internal_forward:1:1:1;
        u8 uses_rss:1:1:1:1;
        u8 da_offs;
        u8 sa_offs;
        struct rcu_head rcu_head;
    }

.. _`ieee80211_fast_rx.members`:

Members
-------

dev
    netdevice for reporting the SKB

vif_type
    (P2P-less) interface type of the original sdata (sdata->vif.type)

vif_addr
    interface address

rfc1042_hdr
    copy of the RFC 1042 SNAP header (to have in cache)

control_port_protocol
    control port protocol copied from sdata

expected_ds_bits
    from/to DS bits expected

icv_len
    length of the MIC if present

key
    bool indicating encryption is expected (key is set)

sta_notify
    notify the MLME code (once)

internal_forward
    forward froms internally on AP/VLAN type interfaces

uses_rss
    copy of USES_RSS hw flag

da_offs
    offset of the DA in the header (for header conversion)

sa_offs
    offset of the SA in the header (for header conversion)

rcu_head
    RCU head for freeing this structure

.. _`mesh_sta`:

struct mesh_sta
===============

.. c:type:: struct mesh_sta

    mesh STA information

.. _`mesh_sta.definition`:

Definition
----------

.. code-block:: c

    struct mesh_sta {
        struct timer_list plink_timer;
        s64 t_offset;
        s64 t_offset_setpoint;
        spinlock_t plink_lock;
        u16 llid;
        u16 plid;
        u16 aid;
        u16 reason;
        u8 plink_retries;
        bool processed_beacon;
        enum nl80211_plink_state plink_state;
        u32 plink_timeout;
        enum nl80211_mesh_power_mode local_pm;
        enum nl80211_mesh_power_mode peer_pm;
        enum nl80211_mesh_power_mode nonpeer_pm;
        unsigned int fail_avg;
    }

.. _`mesh_sta.members`:

Members
-------

plink_timer
    peer link watch timer

t_offset
    timing offset relative to this host

t_offset_setpoint
    reference timing offset of this sta to be used when
    calculating clockdrift

plink_lock
    serialize access to plink fields

llid
    Local link ID

plid
    Peer link ID

aid
    local aid supplied by peer

reason
    Cancel reason on PLINK_HOLDING state

plink_retries
    Retries in establishment

processed_beacon
    set to true after peer rates and capabilities are
    processed

plink_state
    peer link state

plink_timeout
    timeout of peer link

local_pm
    local link-specific power save mode

peer_pm
    peer-specific power save mode towards local STA

nonpeer_pm
    STA power save mode towards non-peer neighbors

fail_avg
    moving percentage of failed MSDUs

.. _`sta_info`:

struct sta_info
===============

.. c:type:: struct sta_info

    STA information

.. _`sta_info.definition`:

Definition
----------

.. code-block:: c

    struct sta_info {
        struct list_head list;
        struct list_head free_list;
        struct rcu_head rcu_head;
        struct rhash_head hash_node;
        u8 addr[ETH_ALEN];
        struct ieee80211_local *local;
        struct ieee80211_sub_if_data *sdata;
        struct ieee80211_key __rcu  *gtk[NUM_DEFAULT_KEYS + NUM_DEFAULT_MGMT_KEYS];
        struct ieee80211_key __rcu  *ptk[NUM_DEFAULT_KEYS];
        u8 ptk_idx;
        struct rate_control_ref *rate_ctrl;
        void *rate_ctrl_priv;
        spinlock_t rate_ctrl_lock;
        spinlock_t lock;
        struct ieee80211_fast_tx __rcu *fast_tx;
        struct ieee80211_fast_rx __rcu *fast_rx;
        struct ieee80211_sta_rx_stats __percpu *pcpu_rx_stats;
        #ifdef CONFIG_MAC80211_MESH
        struct mesh_sta *mesh;
        #endif
        struct work_struct drv_deliver_wk;
        u16 listen_interval;
        bool dead;
        bool removed;
        bool uploaded;
        enum ieee80211_sta_state sta_state;
        unsigned long _flags;
        spinlock_t ps_lock;
        struct sk_buff_head ps_tx_buf[IEEE80211_NUM_ACS];
        struct sk_buff_head tx_filtered[IEEE80211_NUM_ACS];
        unsigned long driver_buffered_tids;
        unsigned long txq_buffered_tids;
        long last_connected;
        struct ieee80211_sta_rx_stats rx_stats;
        struct tx_stats;
        u16 tid_seq[IEEE80211_QOS_CTL_TID_MASK + 1];
        struct sta_ampdu_mlme ampdu_mlme;
        u8 timer_to_tid[IEEE80211_NUM_TIDS];
        #ifdef CONFIG_MAC80211_DEBUGFS
        struct dentry *debugfs_dir;
        #endif
        enum ieee80211_sta_rx_bandwidth cur_max_bandwidth;
        enum ieee80211_smps_mode known_smps_mode;
        const struct ieee80211_cipher_scheme *cipher_scheme;
        u8 reserved_tid;
        struct cfg80211_chan_def tdls_chandef;
        struct ieee80211_sta sta;
    }

.. _`sta_info.members`:

Members
-------

list
    global linked list entry

free_list
    list entry for keeping track of stations to free

rcu_head
    RCU head used for freeing this station struct

hash_node
    hash node for rhashtable

addr
    station's MAC address - duplicated from public part to
    let the hash table work with just a single cacheline

local
    pointer to the global information

sdata
    virtual interface this station belongs to

gtk
    group keys negotiated with this station, if any

ptk
    peer keys negotiated with this station, if any

ptk_idx
    last installed peer key index

rate_ctrl
    rate control algorithm reference

rate_ctrl_priv
    rate control private per-STA pointer

rate_ctrl_lock
    spinlock used to protect rate control data
    (data inside the algorithm, so serializes calls there)

lock
    used for locking all fields that require locking, see comments
    in the header file.

fast_tx
    TX fastpath information

fast_rx
    RX fastpath information

pcpu_rx_stats
    per-CPU RX statistics, assigned only if the driver needs
    this (by advertising the USES_RSS hw flag)

mesh
    mesh STA information

drv_deliver_wk
    used for delivering frames after driver PS unblocking

listen_interval
    listen interval of this station, when we're acting as AP

dead
    set to true when sta is unlinked

removed
    set to true when sta is being removed from sta_list

uploaded
    set to true when sta is uploaded to the driver

sta_state
    duplicates information about station state (for debug)

_flags
    STA flags, see \ :c:type:`enum ieee80211_sta_info_flags <ieee80211_sta_info_flags>`\ , do not use directly

ps_lock
    used for powersave (when mac80211 is the AP) related locking

ps_tx_buf
    buffers (per AC) of frames to transmit to this station
    when it leaves power saving state or polls

tx_filtered
    buffers (per AC) of frames we already tried to
    transmit but were filtered by hardware due to STA having
    entered power saving state, these are also delivered to
    the station when it leaves powersave or polls for frames

driver_buffered_tids
    bitmap of TIDs the driver has data buffered on

txq_buffered_tids
    bitmap of TIDs that mac80211 has txq data buffered on

last_connected
    time (in seconds) when a station got connected

rx_stats
    RX statistics

tx_stats
    TX statistics

tid_seq
    per-TID sequence numbers for sending to this STA

ampdu_mlme
    A-MPDU state machine state

timer_to_tid
    identity mapping to ID timers

debugfs_dir
    debug filesystem directory dentry

cur_max_bandwidth
    maximum bandwidth to use for TX to the station,
    taken from HT/VHT capabilities or VHT operating mode notification

known_smps_mode
    the smps_mode the client thinks we are in. Relevant for
    AP only.

cipher_scheme
    optional cipher scheme for this station

reserved_tid
    reserved TID (if any, otherwise IEEE80211_TID_UNRESERVED)

tdls_chandef
    a TDLS peer can have a wider chandef that is compatible to
    the BSS one.

sta
    station information we share with the driver

.. _`sta_info.description`:

Description
-----------

This structure collects information about a station that
mac80211 is communicating with.

.. _`__sta_info_flush`:

__sta_info_flush
================

.. c:function:: int __sta_info_flush(struct ieee80211_sub_if_data *sdata, bool vlans)

    flush matching STA entries from the STA table

    :param struct ieee80211_sub_if_data \*sdata:
        sdata to remove all stations from

    :param bool vlans:
        if the given interface is an AP interface, also flush VLANs

.. _`__sta_info_flush.description`:

Description
-----------

Returns the number of removed STA entries.

.. This file was automatic generated / don't edit.

