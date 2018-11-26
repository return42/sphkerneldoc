.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/p2p.h

.. _`p2p_bss_type`:

enum p2p_bss_type
=================

.. c:type:: enum p2p_bss_type

    different type of BSS configurations.

.. _`p2p_bss_type.definition`:

Definition
----------

.. code-block:: c

    enum p2p_bss_type {
        P2PAPI_BSSCFG_PRIMARY,
        P2PAPI_BSSCFG_DEVICE,
        P2PAPI_BSSCFG_CONNECTION,
        P2PAPI_BSSCFG_MAX
    };

.. _`p2p_bss_type.constants`:

Constants
---------

P2PAPI_BSSCFG_PRIMARY
    maps to driver's primary bsscfg.

P2PAPI_BSSCFG_DEVICE
    maps to driver's P2P device discovery bsscfg.

P2PAPI_BSSCFG_CONNECTION
    maps to driver's P2P connection bsscfg.

P2PAPI_BSSCFG_MAX
    used for range checking.

.. _`p2p_bss`:

struct p2p_bss
==============

.. c:type:: struct p2p_bss

    peer-to-peer bss related information.

.. _`p2p_bss.definition`:

Definition
----------

.. code-block:: c

    struct p2p_bss {
        struct brcmf_cfg80211_vif *vif;
        void *private_data;
    }

.. _`p2p_bss.members`:

Members
-------

vif
    virtual interface of this P2P bss.

private_data
    TBD

.. _`brcmf_p2p_status`:

enum brcmf_p2p_status
=====================

.. c:type:: enum brcmf_p2p_status

    P2P specific dongle status.

.. _`brcmf_p2p_status.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_p2p_status {
        BRCMF_P2P_STATUS_ENABLED,
        BRCMF_P2P_STATUS_IF_ADD,
        BRCMF_P2P_STATUS_IF_DEL,
        BRCMF_P2P_STATUS_IF_DELETING,
        BRCMF_P2P_STATUS_IF_CHANGING,
        BRCMF_P2P_STATUS_IF_CHANGED,
        BRCMF_P2P_STATUS_ACTION_TX_COMPLETED,
        BRCMF_P2P_STATUS_ACTION_TX_NOACK,
        BRCMF_P2P_STATUS_GO_NEG_PHASE,
        BRCMF_P2P_STATUS_DISCOVER_LISTEN,
        BRCMF_P2P_STATUS_SENDING_ACT_FRAME,
        BRCMF_P2P_STATUS_WAITING_NEXT_AF_LISTEN,
        BRCMF_P2P_STATUS_WAITING_NEXT_ACT_FRAME,
        BRCMF_P2P_STATUS_FINDING_COMMON_CHANNEL
    };

.. _`brcmf_p2p_status.constants`:

Constants
---------

BRCMF_P2P_STATUS_ENABLED
    *undescribed*

BRCMF_P2P_STATUS_IF_ADD
    peer-to-peer vif add sent to dongle.

BRCMF_P2P_STATUS_IF_DEL
    NOT-USED?

BRCMF_P2P_STATUS_IF_DELETING
    peer-to-peer vif delete sent to dongle.

BRCMF_P2P_STATUS_IF_CHANGING
    peer-to-peer vif change sent to dongle.

BRCMF_P2P_STATUS_IF_CHANGED
    peer-to-peer vif change completed on dongle.

BRCMF_P2P_STATUS_ACTION_TX_COMPLETED
    action frame tx completed.

BRCMF_P2P_STATUS_ACTION_TX_NOACK
    action frame tx not acked.

BRCMF_P2P_STATUS_GO_NEG_PHASE
    P2P GO negotiation ongoing.

BRCMF_P2P_STATUS_DISCOVER_LISTEN
    P2P listen, remaining on channel.

BRCMF_P2P_STATUS_SENDING_ACT_FRAME
    In the process of sending action frame.

BRCMF_P2P_STATUS_WAITING_NEXT_AF_LISTEN
    extra listen time for af tx.

BRCMF_P2P_STATUS_WAITING_NEXT_ACT_FRAME
    waiting for action frame response.

BRCMF_P2P_STATUS_FINDING_COMMON_CHANNEL
    search channel for AF active.

.. _`afx_hdl`:

struct afx_hdl
==============

.. c:type:: struct afx_hdl

    action frame off channel storage.

.. _`afx_hdl.definition`:

Definition
----------

.. code-block:: c

    struct afx_hdl {
        struct work_struct afx_work;
        struct completion act_frm_scan;
        bool is_active;
        s32 peer_chan;
        bool is_listen;
        u16 my_listen_chan;
        u16 peer_listen_chan;
        u8 tx_dst_addr[ETH_ALEN];
    }

.. _`afx_hdl.members`:

Members
-------

afx_work
    worker thread for searching channel

act_frm_scan
    thread synchronizing struct.

is_active
    channel searching active.

peer_chan
    current channel.

is_listen
    sets mode for afx worker.

my_listen_chan
    this peers listen channel.

peer_listen_chan
    remote peers listen channel.

tx_dst_addr
    mac address where tx af should be sent to.

.. _`brcmf_p2p_info`:

struct brcmf_p2p_info
=====================

.. c:type:: struct brcmf_p2p_info

    p2p specific driver information.

.. _`brcmf_p2p_info.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_p2p_info {
        struct brcmf_cfg80211_info *cfg;
        unsigned long status;
        u8 dev_addr[ETH_ALEN];
        u8 int_addr[ETH_ALEN];
        struct p2p_bss bss_idx[P2PAPI_BSSCFG_MAX];
        struct timer_list listen_timer;
        u8 listen_channel;
        struct ieee80211_channel remain_on_channel;
        u32 remain_on_channel_cookie;
        u8 next_af_subtype;
        struct completion send_af_done;
        struct afx_hdl afx_hdl;
        u32 af_sent_channel;
        unsigned long af_tx_sent_jiffies;
        struct completion wait_next_af;
        bool gon_req_action;
        bool block_gon_req_tx;
        bool p2pdev_dynamically;
        bool wait_for_offchan_complete;
    }

.. _`brcmf_p2p_info.members`:

Members
-------

cfg
    driver private data for cfg80211 interface.

status
    status of P2P (see enum brcmf_p2p_status).

dev_addr
    P2P device address.

int_addr
    P2P interface address.

bss_idx
    informate for P2P bss types.

listen_timer
    timer for \ ``WL_P2P_DISC_ST_LISTEN``\  discover state.

listen_channel
    channel for \ ``WL_P2P_DISC_ST_LISTEN``\  discover state.

remain_on_channel
    contains copy of struct used by cfg80211.

remain_on_channel_cookie
    cookie counter for remain on channel cmd

next_af_subtype
    expected action frame subtype.

send_af_done
    indication that action frame tx is complete.

afx_hdl
    action frame search handler info.

af_sent_channel
    channel action frame is sent.

af_tx_sent_jiffies
    jiffies time when af tx was transmitted.

wait_next_af
    thread synchronizing struct.

gon_req_action
    about to send go negotiation requets frame.

block_gon_req_tx
    drop tx go negotiation requets frame.

p2pdev_dynamically
    is p2p device if created by module param or supplicant.

wait_for_offchan_complete
    wait for off-channel tx completion event.

.. This file was automatic generated / don't edit.

