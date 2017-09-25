.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h

.. _`brcmf_ampdu_rx_reorder`:

struct brcmf_ampdu_rx_reorder
=============================

.. c:type:: struct brcmf_ampdu_rx_reorder

    AMPDU receive reorder info

.. _`brcmf_ampdu_rx_reorder.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_ampdu_rx_reorder {
        struct sk_buff **pktslots;
        u8 flow_id;
        u8 cur_idx;
        u8 exp_idx;
        u8 max_idx;
        u8 pend_pkts;
    }

.. _`brcmf_ampdu_rx_reorder.members`:

Members
-------

pktslots
    dynamic allocated array for ordering AMPDU packets.

flow_id
    AMPDU flow identifier.

cur_idx
    last AMPDU index from firmware.

exp_idx
    expected next AMPDU index.

max_idx
    maximum amount of packets per AMPDU.

pend_pkts
    number of packets currently in \ ``pktslots``\ .

.. _`brcmf_netif_stop_reason`:

enum brcmf_netif_stop_reason
============================

.. c:type:: enum brcmf_netif_stop_reason

    reason for stopping netif queue.

.. _`brcmf_netif_stop_reason.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_netif_stop_reason {
        BRCMF_NETIF_STOP_REASON_FWS_FC,
        BRCMF_NETIF_STOP_REASON_FLOW,
        BRCMF_NETIF_STOP_REASON_DISCONNECTED
    };

.. _`brcmf_netif_stop_reason.constants`:

Constants
---------

BRCMF_NETIF_STOP_REASON_FWS_FC
    netif stopped due to firmware signalling flow control.

BRCMF_NETIF_STOP_REASON_FLOW
    netif stopped due to flowring full.

BRCMF_NETIF_STOP_REASON_DISCONNECTED
    netif stopped due to not being connected (STA mode).

.. _`brcmf_if`:

struct brcmf_if
===============

.. c:type:: struct brcmf_if

    interface control information.

.. _`brcmf_if.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_if {
        struct brcmf_pub *drvr;
        struct brcmf_cfg80211_vif *vif;
        struct net_device *ndev;
        struct work_struct multicast_work;
        struct work_struct ndoffload_work;
        struct brcmf_fws_mac_descriptor *fws_desc;
        int ifidx;
        s32 bsscfgidx;
        u8 mac_addr[ETH_ALEN];
        u8 netif_stop;
        spinlock_t netif_stop_lock;
        atomic_t pend_8021x_cnt;
        wait_queue_head_t pend_8021x_wait;
        struct in6_addr ipv6_addr_tbl[NDOL_MAX_ENTRIES];
        u8 ipv6addr_idx;
    }

.. _`brcmf_if.members`:

Members
-------

drvr
    points to device related information.

vif
    points to cfg80211 specific interface information.

ndev
    associated network device.

multicast_work
    worker object for multicast provisioning.

ndoffload_work
    worker object for neighbor discovery offload configuration.

fws_desc
    interface specific firmware-signalling descriptor.

ifidx
    interface index in device firmware.

bsscfgidx
    index of bss associated with this interface.

mac_addr
    assigned mac address.

netif_stop
    bitmap indicates reason why netif queues are stopped.

netif_stop_lock
    spinlock for update netif_stop from multiple sources.

pend_8021x_cnt
    tracks outstanding number of 802.1x frames.

pend_8021x_wait
    used for signalling change in count.

ipv6_addr_tbl
    *undescribed*

ipv6addr_idx
    *undescribed*

.. This file was automatic generated / don't edit.

