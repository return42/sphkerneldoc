.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwsignal.c

.. _`brcmf_fws_skb_state`:

enum brcmf_fws_skb_state
========================

.. c:type:: enum brcmf_fws_skb_state

    indicates processing state of skb.

.. _`brcmf_fws_skb_state.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_fws_skb_state {
        BRCMF_FWS_SKBSTATE_NEW,
        BRCMF_FWS_SKBSTATE_DELAYED,
        BRCMF_FWS_SKBSTATE_SUPPRESSED,
        BRCMF_FWS_SKBSTATE_TIM
    };

.. _`brcmf_fws_skb_state.constants`:

Constants
---------

BRCMF_FWS_SKBSTATE_NEW
    sk_buff is newly arrived in the driver.

BRCMF_FWS_SKBSTATE_DELAYED
    sk_buff had to wait on queue.

BRCMF_FWS_SKBSTATE_SUPPRESSED
    sk_buff has been suppressed by firmware.

BRCMF_FWS_SKBSTATE_TIM
    allocated for TIM update info.

.. _`brcmf_skbuff_cb`:

struct brcmf_skbuff_cb
======================

.. c:type:: struct brcmf_skbuff_cb

    control buffer associated with skbuff.

.. _`brcmf_skbuff_cb.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_skbuff_cb {
        u16 bus_flags;
        u16 if_flags;
        u32 htod;
        u16 htod_seq;
        enum brcmf_fws_skb_state state;
        struct brcmf_fws_mac_descriptor *mac;
    }

.. _`brcmf_skbuff_cb.members`:

Members
-------

bus_flags
    2 bytes reserved for bus specific parameters

if_flags
    holds interface index and packet related flags.

htod
    host to device packet identifier (used in PKTTAG tlv).

htod_seq
    this 16-bit is original seq number for every suppress packet.

state
    transmit state of the packet.

mac
    descriptor related to destination for this packet.

.. _`brcmf_skbuff_cb.description`:

Description
-----------

This information is stored in control buffer struct sk_buff::cb, which
provides 48 bytes of storage so this structure should not exceed that.

.. _`brcmf_fws_fifo`:

enum brcmf_fws_fifo
===================

.. c:type:: enum brcmf_fws_fifo

    fifo indices used by dongle firmware.

.. _`brcmf_fws_fifo.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_fws_fifo {
        BRCMF_FWS_FIFO_FIRST,
        BRCMF_FWS_FIFO_AC_BK,
        BRCMF_FWS_FIFO_AC_BE,
        BRCMF_FWS_FIFO_AC_VI,
        BRCMF_FWS_FIFO_AC_VO,
        BRCMF_FWS_FIFO_BCMC,
        BRCMF_FWS_FIFO_ATIM,
        BRCMF_FWS_FIFO_COUNT
    };

.. _`brcmf_fws_fifo.constants`:

Constants
---------

BRCMF_FWS_FIFO_FIRST
    first fifo, ie. background.

BRCMF_FWS_FIFO_AC_BK
    fifo for background traffic.

BRCMF_FWS_FIFO_AC_BE
    fifo for best-effort traffic.

BRCMF_FWS_FIFO_AC_VI
    fifo for video traffic.

BRCMF_FWS_FIFO_AC_VO
    fifo for voice traffic.

BRCMF_FWS_FIFO_BCMC
    fifo for broadcast/multicast (AP only).

BRCMF_FWS_FIFO_ATIM
    fifo for ATIM (AP only).

BRCMF_FWS_FIFO_COUNT
    number of fifos.

.. _`brcmf_fws_txstatus`:

enum brcmf_fws_txstatus
=======================

.. c:type:: enum brcmf_fws_txstatus

    txstatus flag values.

.. _`brcmf_fws_txstatus.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_fws_txstatus {
        BRCMF_FWS_TXSTATUS_DISCARD,
        BRCMF_FWS_TXSTATUS_CORE_SUPPRESS,
        BRCMF_FWS_TXSTATUS_FW_PS_SUPPRESS,
        BRCMF_FWS_TXSTATUS_FW_TOSSED,
        BRCMF_FWS_TXSTATUS_HOST_TOSSED
    };

.. _`brcmf_fws_txstatus.constants`:

Constants
---------

BRCMF_FWS_TXSTATUS_DISCARD
    host is free to discard the packet.

BRCMF_FWS_TXSTATUS_CORE_SUPPRESS
    802.11 core suppressed the packet.

BRCMF_FWS_TXSTATUS_FW_PS_SUPPRESS
    firmware suppress the packet as device is already in PS mode.

BRCMF_FWS_TXSTATUS_FW_TOSSED
    firmware tossed the packet.

BRCMF_FWS_TXSTATUS_HOST_TOSSED
    host tossed the packet.

.. _`brcmf_fws_mac_descriptor`:

struct brcmf_fws_mac_descriptor
===============================

.. c:type:: struct brcmf_fws_mac_descriptor

    firmware signalling data per node/interface

.. _`brcmf_fws_mac_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_fws_mac_descriptor {
        char name[16];
        u8 occupied;
        u8 mac_handle;
        u8 interface_id;
        u8 state;
        bool suppressed;
        u8 generation;
        u8 ac_bitmap;
        u8 requested_credit;
        u8 requested_packet;
        u8 ea[ETH_ALEN];
        u8 seq[BRCMF_FWS_FIFO_COUNT];
        struct pktq psq;
        int transit_count;
        int suppr_transit_count;
        bool send_tim_signal;
        u8 traffic_pending_bmp;
        u8 traffic_lastreported_bmp;
    }

.. _`brcmf_fws_mac_descriptor.members`:

Members
-------

occupied
    slot is in use.

mac_handle
    handle for mac entry determined by firmware.

interface_id
    interface index.

state
    current state.

suppressed
    mac entry is suppressed.

generation
    generation bit.

ac_bitmap
    ac queue bitmap.

requested_credit
    credits requested by firmware.

requested_packet
    *undescribed*

ea
    ethernet address.

seq
    per-node free-running sequence.

psq
    power-save queue.

transit_count
    packet in transit to firmware.

suppr_transit_count
    *undescribed*

send_tim_signal
    *undescribed*

traffic_pending_bmp
    *undescribed*

traffic_lastreported_bmp
    *undescribed*

.. _`brcmf_fws_hanger_item_state`:

enum brcmf_fws_hanger_item_state
================================

.. c:type:: enum brcmf_fws_hanger_item_state

    state of hanger item.

.. _`brcmf_fws_hanger_item_state.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_fws_hanger_item_state {
        BRCMF_FWS_HANGER_ITEM_STATE_FREE,
        BRCMF_FWS_HANGER_ITEM_STATE_INUSE,
        BRCMF_FWS_HANGER_ITEM_STATE_INUSE_SUPPRESSED
    };

.. _`brcmf_fws_hanger_item_state.constants`:

Constants
---------

BRCMF_FWS_HANGER_ITEM_STATE_FREE
    item is free for use.

BRCMF_FWS_HANGER_ITEM_STATE_INUSE
    item is in use.

BRCMF_FWS_HANGER_ITEM_STATE_INUSE_SUPPRESSED
    item was suppressed.

.. _`brcmf_fws_hanger_item`:

struct brcmf_fws_hanger_item
============================

.. c:type:: struct brcmf_fws_hanger_item

    single entry for tx pending packet.

.. _`brcmf_fws_hanger_item.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_fws_hanger_item {
        enum brcmf_fws_hanger_item_state state;
        struct sk_buff *pkt;
    }

.. _`brcmf_fws_hanger_item.members`:

Members
-------

state
    entry is either free or occupied.

pkt
    packet itself.

.. _`brcmf_fws_hanger`:

struct brcmf_fws_hanger
=======================

.. c:type:: struct brcmf_fws_hanger

    holds packets awaiting firmware txstatus.

.. _`brcmf_fws_hanger.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_fws_hanger {
        u32 pushed;
        u32 popped;
        u32 failed_to_push;
        u32 failed_to_pop;
        u32 failed_slotfind;
        u32 slot_pos;
        struct brcmf_fws_hanger_item items[BRCMF_FWS_HANGER_MAXITEMS];
    }

.. _`brcmf_fws_hanger.members`:

Members
-------

pushed
    packets pushed to await txstatus.

popped
    packets popped upon handling txstatus.

failed_to_push
    packets that could not be pushed.

failed_to_pop
    packets that could not be popped.

failed_slotfind
    packets for which failed to find an entry.

slot_pos
    last returned item index for a free entry.

items
    array of hanger items.

.. _`brcmf_fws_get_tlv_len`:

brcmf_fws_get_tlv_len
=====================

.. c:function:: int brcmf_fws_get_tlv_len(struct brcmf_fws_info *fws, enum brcmf_fws_tlv_type id)

    returns defined length for given tlv id.

    :param struct brcmf_fws_info \*fws:
        firmware-signalling information.

    :param enum brcmf_fws_tlv_type id:
        identifier of the TLV.

.. _`brcmf_fws_get_tlv_len.return`:

Return
------

the specified length for the given TLV; Otherwise -EINVAL.

.. This file was automatic generated / don't edit.

