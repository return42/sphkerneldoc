.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/flower/lag_conf.c

.. _`nfp_flower_cmsg_lag_config`:

struct nfp_flower_cmsg_lag_config
=================================

.. c:type:: struct nfp_flower_cmsg_lag_config

    control message payload for LAG config

.. _`nfp_flower_cmsg_lag_config.definition`:

Definition
----------

.. code-block:: c

    struct nfp_flower_cmsg_lag_config {
        u8 ctrl_flags;
        u8 reserved[2];
        u8 ttl;
        __be32 pkt_number;
        __be32 batch_ver;
        __be32 group_id;
        __be32 group_inst;
        __be32 members[];
    }

.. _`nfp_flower_cmsg_lag_config.members`:

Members
-------

ctrl_flags
    Configuration flags

reserved
    Reserved for future use

ttl
    Time to live of packet - host always sets to 0xff

pkt_number
    Config message packet number - increment for each message

batch_ver
    Batch version of messages - increment for each batch of messages

group_id
    Group ID applicable

group_inst
    Group instance number - increment when group is reused

members
    Array of 32-bit words listing all active group members

.. _`nfp_fl_lag_group`:

struct nfp_fl_lag_group
=======================

.. c:type:: struct nfp_fl_lag_group

    list entry for each LAG group

.. _`nfp_fl_lag_group.definition`:

Definition
----------

.. code-block:: c

    struct nfp_fl_lag_group {
        unsigned int group_id;
        u8 group_inst;
        struct list_head list;
        struct net_device *master_ndev;
        bool dirty;
        bool offloaded;
        bool to_remove;
        bool to_destroy;
        unsigned int slave_cnt;
    }

.. _`nfp_fl_lag_group.members`:

Members
-------

group_id
    Assigned group ID for host/kernel sync

group_inst
    Group instance in case of ID reuse

list
    List entry

master_ndev
    Group master Netdev

dirty
    Marked if the group needs synced to HW

offloaded
    Marked if the group is currently offloaded to NIC

to_remove
    Marked if the group should be removed from NIC

to_destroy
    Marked if the group should be removed from driver

slave_cnt
    Number of slaves in group

.. This file was automatic generated / don't edit.

