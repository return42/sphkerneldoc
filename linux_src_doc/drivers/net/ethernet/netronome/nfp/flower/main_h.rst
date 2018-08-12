.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/flower/main.h

.. _`nfp_mtu_conf`:

struct nfp_mtu_conf
===================

.. c:type:: struct nfp_mtu_conf

    manage MTU setting

.. _`nfp_mtu_conf.definition`:

Definition
----------

.. code-block:: c

    struct nfp_mtu_conf {
        u32 portnum;
        unsigned int requested_val;
        bool ack;
        wait_queue_head_t wait_q;
        spinlock_t lock;
    }

.. _`nfp_mtu_conf.members`:

Members
-------

portnum
    NFP port number of repr with requested MTU change

requested_val
    MTU value requested for repr

ack
    Received ack that MTU has been correctly set

wait_q
    Wait queue for MTU acknowledgements

lock
    Lock for setting/reading MTU variables

.. _`nfp_fl_lag`:

struct nfp_fl_lag
=================

.. c:type:: struct nfp_fl_lag

    Flower APP priv data for link aggregation

.. _`nfp_fl_lag.definition`:

Definition
----------

.. code-block:: c

    struct nfp_fl_lag {
        struct notifier_block lag_nb;
        struct delayed_work work;
        struct mutex lock;
        struct list_head group_list;
        struct ida ida_handle;
        unsigned int pkt_num;
        unsigned int batch_ver;
        u8 global_inst;
        bool rst_cfg;
        struct sk_buff_head retrans_skbs;
    }

.. _`nfp_fl_lag.members`:

Members
-------

lag_nb
    Notifier to track master/slave events

work
    Work queue for writing configs to the HW

lock
    Lock to protect lag_group_list

group_list
    List of all master/slave groups offloaded

ida_handle
    IDA to handle group ids

pkt_num
    Incremented for each config packet sent

batch_ver
    Incremented for each batch of config packets

global_inst
    Instance allocator for groups

rst_cfg
    Marker to reset HW LAG config

retrans_skbs
    Cmsgs that could not be processed by HW and require
    retransmission

.. _`nfp_flower_priv`:

struct nfp_flower_priv
======================

.. c:type:: struct nfp_flower_priv

    Flower APP per-vNIC priv data

.. _`nfp_flower_priv.definition`:

Definition
----------

.. code-block:: c

    struct nfp_flower_priv {
        struct nfp_app *app;
        struct nfp_net *nn;
        u32 mask_id_seed;
        u64 flower_version;
        u64 flower_ext_feats;
        struct nfp_fl_stats_id stats_ids;
        struct nfp_fl_mask_id mask_ids;
        DECLARE_HASHTABLE(mask_table, NFP_FLOWER_MASK_HASH_BITS);
        DECLARE_HASHTABLE(flow_table, NFP_FLOWER_HASH_BITS);
        struct work_struct cmsg_work;
        struct sk_buff_head cmsg_skbs_high;
        struct sk_buff_head cmsg_skbs_low;
        struct list_head nfp_mac_off_list;
        struct list_head nfp_mac_index_list;
        struct list_head nfp_ipv4_off_list;
        struct list_head nfp_neigh_off_list;
        struct mutex nfp_mac_off_lock;
        struct mutex nfp_mac_index_lock;
        struct mutex nfp_ipv4_off_lock;
        spinlock_t nfp_neigh_off_lock;
        struct ida nfp_mac_off_ids;
        int nfp_mac_off_count;
        struct notifier_block nfp_tun_mac_nb;
        struct notifier_block nfp_tun_neigh_nb;
        atomic_t reify_replies;
        wait_queue_head_t reify_wait_queue;
        struct nfp_mtu_conf mtu_conf;
        struct nfp_fl_lag nfp_lag;
    }

.. _`nfp_flower_priv.members`:

Members
-------

app
    Back pointer to app

nn
    Pointer to vNIC

mask_id_seed
    Seed used for mask hash table

flower_version
    HW version of flower

flower_ext_feats
    Bitmap of extra features the HW supports

stats_ids
    List of free stats ids

mask_ids
    List of free mask ids

mask_table
    Hash table used to store masks

flow_table
    Hash table used to store flower rules

cmsg_work
    Workqueue for control messages processing

cmsg_skbs_high
    List of higher priority skbs for control message
    processing

cmsg_skbs_low
    List of lower priority skbs for control message
    processing

nfp_mac_off_list
    List of MAC addresses to offload

nfp_mac_index_list
    List of unique 8-bit indexes for non NFP netdevs

nfp_ipv4_off_list
    List of IPv4 addresses to offload

nfp_neigh_off_list
    List of neighbour offloads

nfp_mac_off_lock
    Lock for the MAC address list

nfp_mac_index_lock
    Lock for the MAC index list

nfp_ipv4_off_lock
    Lock for the IPv4 address list

nfp_neigh_off_lock
    Lock for the neighbour address list

nfp_mac_off_ids
    IDA to manage id assignment for offloaded macs

nfp_mac_off_count
    Number of MACs in address list

nfp_tun_mac_nb
    Notifier to monitor link state

nfp_tun_neigh_nb
    Notifier to monitor neighbour state

reify_replies
    atomically stores the number of replies received
    from firmware for repr reify

reify_wait_queue
    wait queue for repr reify response counting

mtu_conf
    Configuration of repr MTU value

nfp_lag
    Link aggregation data block

.. _`nfp_flower_repr_priv`:

struct nfp_flower_repr_priv
===========================

.. c:type:: struct nfp_flower_repr_priv

    Flower APP per-repr priv data

.. _`nfp_flower_repr_priv.definition`:

Definition
----------

.. code-block:: c

    struct nfp_flower_repr_priv {
        unsigned long lag_port_flags;
    }

.. _`nfp_flower_repr_priv.members`:

Members
-------

lag_port_flags
    Extended port flags to record lag state of repr

.. This file was automatic generated / don't edit.

