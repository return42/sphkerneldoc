.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-sta-info:

===============
struct sta_info
===============

*man struct sta_info(9)*

*4.6.0-rc5*

STA information


Synopsis
========

.. code-block:: c

    struct sta_info {
      struct list_head list;
      struct list_head free_list;
      struct rcu_head rcu_head;
      struct rhash_head hash_node;
      u8 addr[ETH_ALEN];
      struct ieee80211_local * local;
      struct ieee80211_sub_if_data * sdata;
      struct ieee80211_key __rcu * gtk[NUM_DEFAULT_KEYS + NUM_DEFAULT_MGMT_KEYS];
      struct ieee80211_key __rcu * ptk[NUM_DEFAULT_KEYS];
      u8 ptk_idx;
      struct rate_control_ref * rate_ctrl;
      void * rate_ctrl_priv;
      spinlock_t rate_ctrl_lock;
      spinlock_t lock;
      struct ieee80211_fast_tx __rcu * fast_tx;
    #ifdef CONFIG_MAC80211_MESH
      struct mesh_sta * mesh;
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
      struct debugfs;
    #endif
      enum ieee80211_sta_rx_bandwidth cur_max_bandwidth;
      enum ieee80211_smps_mode known_smps_mode;
      const struct ieee80211_cipher_scheme * cipher_scheme;
      u8 reserved_tid;
      struct cfg80211_chan_def tdls_chandef;
      struct ieee80211_sta sta;
    };


Members
=======

list
    global linked list entry

free_list
    list entry for keeping track of stations to free

rcu_head
    RCU head used for freeing this station struct

hash_node
    hash node for rhashtable

addr[ETH_ALEN]
    station's MAC address - duplicated from public part to let the hash
    table work with just a single cacheline

local
    pointer to the global information

sdata
    virtual interface this station belongs to

gtk[NUM_DEFAULT_KEYS + NUM_DEFAULT_MGMT_KEYS]
    group keys negotiated with this station, if any

ptk[NUM_DEFAULT_KEYS]
    peer keys negotiated with this station, if any

ptk_idx
    last installed peer key index

rate_ctrl
    rate control algorithm reference

rate_ctrl_priv
    rate control private per-STA pointer

rate_ctrl_lock
    spinlock used to protect rate control data (data inside the
    algorithm, so serializes calls there)

lock
    used for locking all fields that require locking, see comments in
    the header file.

fast_tx
    TX fastpath information

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
    STA flags, see ``enum`` ieee80211_sta_info_flags, do not use
    directly

ps_lock
    used for powersave (when mac80211 is the AP) related locking

ps_tx_buf[IEEE80211_NUM_ACS]
    buffers (per AC) of frames to transmit to this station when it
    leaves power saving state or polls

tx_filtered[IEEE80211_NUM_ACS]
    buffers (per AC) of frames we already tried to transmit but were
    filtered by hardware due to STA having entered power saving state,
    these are also delivered to the station when it leaves powersave or
    polls for frames

driver_buffered_tids
    bitmap of TIDs the driver has data buffered on

txq_buffered_tids
    bitmap of TIDs that mac80211 has txq data buffered on

last_connected
    time (in seconds) when a station got connected

debugfs
    debug filesystem info

cur_max_bandwidth
    maximum bandwidth to use for TX to the station, taken from HT/VHT
    capabilities or VHT operating mode notification

known_smps_mode
    the smps_mode the client thinks we are in. Relevant for AP only.

cipher_scheme
    optional cipher scheme for this station

reserved_tid
    reserved TID (if any, otherwise IEEE80211_TID_UNRESERVED)

tdls_chandef
    a TDLS peer can have a wider chandef that is compatible to the BSS
    one.

sta
    station information we share with the driver


Description
===========

This structure collects information about a station that mac80211 is
communicating with.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
