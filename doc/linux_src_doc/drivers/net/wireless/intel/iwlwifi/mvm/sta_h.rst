.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/sta.h

.. _`iwl_mvm_agg_state`:

enum iwl_mvm_agg_state
======================

.. c:type:: enum iwl_mvm_agg_state


.. _`iwl_mvm_agg_state.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_agg_state {
        IWL_AGG_OFF,
        IWL_AGG_STARTING,
        IWL_AGG_ON,
        IWL_EMPTYING_HW_QUEUE_ADDBA,
        IWL_EMPTYING_HW_QUEUE_DELBA
    };

.. _`iwl_mvm_agg_state.constants`:

Constants
---------

IWL_AGG_OFF
    aggregation is not used

IWL_AGG_STARTING
    aggregation are starting (between start and oper)

IWL_AGG_ON
    aggregation session is up

IWL_EMPTYING_HW_QUEUE_ADDBA
    establishing a BA session - waiting for the
    HW queue to be empty from packets for this RA /TID.

IWL_EMPTYING_HW_QUEUE_DELBA
    tearing down a BA session - waiting for the
    HW queue to be empty from packets for this RA /TID.

.. _`iwl_mvm_agg_state.description`:

Description
-----------

The state machine of the BA agreement establishment / tear down.
These states relate to a specific RA / TID.

.. _`iwl_mvm_tid_data`:

struct iwl_mvm_tid_data
=======================

.. c:type:: struct iwl_mvm_tid_data

    holds the states for each RA / TID

.. _`iwl_mvm_tid_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_tid_data {
        struct sk_buff_head deferred_tx_frames;
        u16 seq_number;
        u16 next_reclaimed;
        u32 rate_n_flags;
        bool amsdu_in_ampdu_allowed;
        enum iwl_mvm_agg_state state;
        u16 txq_id;
        u16 ssn;
        u16 tx_time;
    }

.. _`iwl_mvm_tid_data.members`:

Members
-------

deferred_tx_frames
    deferred TX frames for this RA/TID

seq_number
    the next WiFi sequence number to use

next_reclaimed
    the WiFi sequence number of the next packet to be acked.
    This is basically (last acked packet++).

rate_n_flags
    Rate at which Tx was attempted. Holds the data between the
    Tx response (TX_CMD), and the block ack notification (COMPRESSED_BA).

amsdu_in_ampdu_allowed
    true if A-MSDU in A-MPDU is allowed.

state
    state of the BA agreement establishment / tear down.

txq_id
    Tx queue used by the BA session / DQA

ssn
    the first packet to be sent in AGG HW queue in Tx AGG start flow, or
    the first packet to be sent in legacy HW queue in Tx AGG stop flow.
    Basically when next_reclaimed reaches ssn, we can tell mac80211 that
    we are ready to finish the Tx AGG stop / start flow.

tx_time
    medium time consumed by this A-MPDU

.. _`iwl_mvm_rxq_dup_data`:

struct iwl_mvm_rxq_dup_data
===========================

.. c:type:: struct iwl_mvm_rxq_dup_data

    per station per rx queue data

.. _`iwl_mvm_rxq_dup_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_rxq_dup_data {
        __le16 last_seq[IWL_MAX_TID_COUNT + 1];
        u8 last_sub_frame[IWL_MAX_TID_COUNT + 1];
    }

.. _`iwl_mvm_rxq_dup_data.members`:

Members
-------

last_seq
    last sequence per tid for duplicate packet detection

last_sub_frame
    last subframe packet

.. _`iwl_mvm_sta`:

struct iwl_mvm_sta
==================

.. c:type:: struct iwl_mvm_sta

    representation of a station in the driver

.. _`iwl_mvm_sta.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_sta {
        u32 sta_id;
        u32 tfd_queue_msk;
        u8 hw_queue[IEEE80211_NUM_ACS];
        u32 mac_id_n_color;
        u16 tid_disable_agg;
        u8 max_agg_bufsize;
        bool bt_reduced_txpower;
        bool next_status_eosp;
        spinlock_t lock;
        struct iwl_mvm_tid_data tid_data[IWL_MAX_TID_COUNT + 1];
        u8 tid_to_baid[IWL_MAX_TID_COUNT];
        struct iwl_lq_sta lq_sta;
        struct ieee80211_vif *vif;
        struct iwl_mvm_key_pn __rcu  *ptk_pn[4];
        struct iwl_mvm_rxq_dup_data *dup_data;
        u16 deferred_traffic_tid_map;
        u8 reserved_queue;
        s8 tx_protection;
        bool tt_tx_protection;
        bool disable_tx;
        bool tlc_amsdu;
        u8 agg_tids;
        u8 sleep_tx_count;
    }

.. _`iwl_mvm_sta.members`:

Members
-------

sta_id
    the index of the station in the fw (will be replaced by id_n_color)

tfd_queue_msk
    the tfd queues used by the station

hw_queue
    per-AC mapping of the TFD queues used by station

mac_id_n_color
    the MAC context this station is linked to

tid_disable_agg
    bitmap: if bit(tid) is set, the fw won't send ampdus for
    tid.

max_agg_bufsize
    the maximal size of the AGG buffer for this station

bt_reduced_txpower
    is reduced tx power enabled for this station

next_status_eosp
    the next reclaimed packet is a PS-Poll response and
    we need to signal the EOSP

lock
    lock to protect the whole struct. Since \ ``tid_data``\  is access from Tx
    and from Tx response flow, it needs a spinlock.

tid_data
    per tid data + mgmt. Look at \ ``iwl_mvm_tid_data``\ .

tid_to_baid
    a simple map of TID to baid

lq_sta
    *undescribed*

vif
    *undescribed*

ptk_pn
    per-queue PTK PN data structures

dup_data
    per queue duplicate packet detection data

deferred_traffic_tid_map
    indication bitmap of deferred traffic per-TID

reserved_queue
    the queue reserved for this STA for DQA purposes
    Every STA has is given one reserved queue to allow it to operate. If no
    such queue can be guaranteed, the STA addition will fail.

tx_protection
    reference counter for controlling the Tx protection.

tt_tx_protection
    is thermal throttling enable Tx protection?

disable_tx
    is tx to this STA disabled?

tlc_amsdu
    true if A-MSDU is allowed

agg_tids
    bitmap of tids whose status is operational aggregated (IWL_AGG_ON)

sleep_tx_count
    the number of frames that we told the firmware to let out
    even when that station is asleep. This is useful in case the queue
    gets empty before all the frames were sent, which can happen when
    we are sending frames from an AMPDU queue and there was a hole in
    the BA window. To be used for UAPSD only.

.. _`iwl_mvm_sta.description`:

Description
-----------

When mac80211 creates a station it reserves some space (hw->sta_data_size)
in the structure for use by driver. This structure is placed in that
space.

.. _`iwl_mvm_int_sta`:

struct iwl_mvm_int_sta
======================

.. c:type:: struct iwl_mvm_int_sta

    representation of an internal station (auxiliary or broadcast)

.. _`iwl_mvm_int_sta.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_int_sta {
        u32 sta_id;
        u32 tfd_queue_msk;
    }

.. _`iwl_mvm_int_sta.members`:

Members
-------

sta_id
    the index of the station in the fw (will be replaced by id_n_color)

tfd_queue_msk
    the tfd queues used by the station

.. _`iwl_mvm_sta_send_to_fw`:

iwl_mvm_sta_send_to_fw
======================

.. c:function:: int iwl_mvm_sta_send_to_fw(struct iwl_mvm *mvm, struct ieee80211_sta *sta, bool update, unsigned int flags)

    :param struct iwl_mvm \*mvm:
        the iwl_mvm\* to use

    :param struct ieee80211_sta \*sta:
        the STA

    :param bool update:
        this is true if the FW is being updated about a STA it already knows
        about. Otherwise (if this is a new STA), this should be false.

    :param unsigned int flags:
        if update==true, this marks what is being changed via ORs of values
        from enum iwl_sta_modify_flag. Otherwise, this is ignored.

.. This file was automatic generated / don't edit.

