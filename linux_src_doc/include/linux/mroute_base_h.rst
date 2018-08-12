.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mroute_base.h

.. _`vif_device`:

struct vif_device
=================

.. c:type:: struct vif_device

    interface representor for multicast routing

.. _`vif_device.definition`:

Definition
----------

.. code-block:: c

    struct vif_device {
        struct net_device *dev;
        unsigned long bytes_in, bytes_out;
        unsigned long pkt_in, pkt_out;
        unsigned long rate_limit;
        unsigned char threshold;
        unsigned short flags;
        int link;
        struct netdev_phys_item_id dev_parent_id;
        __be32 local, remote;
    }

.. _`vif_device.members`:

Members
-------

dev
    network device being used

bytes_in
    statistic; bytes ingressing

bytes_out
    statistic; bytes egresing

pkt_in
    statistic; packets ingressing

pkt_out
    statistic; packets egressing

rate_limit
    Traffic shaping (NI)

threshold
    TTL threshold

flags
    Control flags

link
    Physical interface index

dev_parent_id
    device parent id

local
    Local address

remote
    Remote address for tunnels

.. _`mr_mfc`:

struct mr_mfc
=============

.. c:type:: struct mr_mfc

    common multicast routing entries

.. _`mr_mfc.definition`:

Definition
----------

.. code-block:: c

    struct mr_mfc {
        struct rhlist_head mnode;
        unsigned short mfc_parent;
        int mfc_flags;
        union {
            struct {
                unsigned long expires;
                struct sk_buff_head unresolved;
            } unres;
            struct {
                unsigned long last_assert;
                int minvif;
                int maxvif;
                unsigned long bytes;
                unsigned long pkt;
                unsigned long wrong_if;
                unsigned long lastuse;
                unsigned char ttls[MAXVIFS];
                refcount_t refcount;
            } res;
        } mfc_un;
        struct list_head list;
        struct rcu_head rcu;
        void (*free)(struct rcu_head *head);
    }

.. _`mr_mfc.members`:

Members
-------

mnode
    rhashtable list

mfc_parent
    source interface (iif)

mfc_flags
    entry flags

mfc_un
    *undescribed*

list
    global entry list

rcu
    used for entry destruction

free
    Operation used for freeing an entry under RCU

.. _`mr_table_ops`:

struct mr_table_ops
===================

.. c:type:: struct mr_table_ops

    callbacks and info for protocol-specific ops

.. _`mr_table_ops.definition`:

Definition
----------

.. code-block:: c

    struct mr_table_ops {
        const struct rhashtable_params *rht_params;
        void *cmparg_any;
    }

.. _`mr_table_ops.members`:

Members
-------

rht_params
    parameters for accessing the MFC hash

cmparg_any
    a hash key to be used for matching on (\*,\*) routes

.. _`mr_table`:

struct mr_table
===============

.. c:type:: struct mr_table

    a multicast routing table

.. _`mr_table.definition`:

Definition
----------

.. code-block:: c

    struct mr_table {
        struct list_head list;
        possible_net_t net;
        struct mr_table_ops ops;
        u32 id;
        struct sock __rcu *mroute_sk;
        struct timer_list ipmr_expire_timer;
        struct list_head mfc_unres_queue;
        struct vif_device vif_table[MAXVIFS];
        struct rhltable mfc_hash;
        struct list_head mfc_cache_list;
        int maxvif;
        atomic_t cache_resolve_queue_len;
        bool mroute_do_assert;
        bool mroute_do_pim;
        int mroute_reg_vif_num;
    }

.. _`mr_table.members`:

Members
-------

list
    entry within a list of multicast routing tables

net
    net where this table belongs

ops
    protocol specific operations

id
    identifier of the table

mroute_sk
    socket associated with the table

ipmr_expire_timer
    timer for handling unresolved routes

mfc_unres_queue
    list of unresolved MFC entries

vif_table
    array containing all possible vifs

mfc_hash
    Hash table of all resolved routes for easy lookup

mfc_cache_list
    list of resovled routes for possible traversal

maxvif
    Identifier of highest value vif currently in use

cache_resolve_queue_len
    current size of unresolved queue

mroute_do_assert
    Whether to inform userspace on wrong ingress

mroute_do_pim
    Whether to receive IGMP PIMv1

mroute_reg_vif_num
    PIM-device vif index

.. This file was automatic generated / don't edit.

