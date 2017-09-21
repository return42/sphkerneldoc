.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/openvswitch/datapath.h

.. _`dp_stats_percpu`:

struct dp_stats_percpu
======================

.. c:type:: struct dp_stats_percpu

    per-cpu packet processing statistics for a given datapath.

.. _`dp_stats_percpu.definition`:

Definition
----------

.. code-block:: c

    struct dp_stats_percpu {
        u64 n_hit;
        u64 n_missed;
        u64 n_lost;
        u64 n_mask_hit;
        struct u64_stats_sync syncp;
    }

.. _`dp_stats_percpu.members`:

Members
-------

n_hit
    Number of received packets for which a matching flow was found in
    the flow table.

n_missed
    *undescribed*

n_lost
    Number of received packets that had no matching flow in the flow
    table that could not be sent to userspace (normally due to an overflow in
    one of the datapath's queues).

n_mask_hit
    Number of masks looked up for flow match.
    \ ``n_mask_hit``\  / (@n_hit + \ ``n_missed``\ )  will be the average masks looked
    up per packet.

syncp
    *undescribed*

.. _`datapath`:

struct datapath
===============

.. c:type:: struct datapath

    datapath for flow-based packet switching

.. _`datapath.definition`:

Definition
----------

.. code-block:: c

    struct datapath {
        struct rcu_head rcu;
        struct list_head list_node;
        struct flow_table table;
        struct hlist_head *ports;
        struct dp_stats_percpu __percpu *stats_percpu;
        possible_net_t net;
        u32 user_features;
        u32 max_headroom;
    }

.. _`datapath.members`:

Members
-------

rcu
    RCU callback head for deferred destruction.

list_node
    Element in global 'dps' list.

table
    flow table.

ports
    Hash table for ports.  \ ``OVSP_LOCAL``\  port always exists.  Protected by
    ovs_mutex and RCU.

stats_percpu
    Per-CPU datapath statistics.

net
    Reference to net namespace.

user_features
    *undescribed*

max_headroom
    the maximum headroom of all vports in this datapath; it will
    be used by all the internal vports in this dp.

.. _`datapath.context`:

Context
-------

See the comment on locking at the top of datapath.c for additional
locking information.

.. _`ovs_skb_cb`:

struct ovs_skb_cb
=================

.. c:type:: struct ovs_skb_cb

    OVS data in skb CB

.. _`ovs_skb_cb.definition`:

Definition
----------

.. code-block:: c

    struct ovs_skb_cb {
        struct vport *input_vport;
        u16 mru;
        u16 acts_origlen;
        u32 cutlen;
    }

.. _`ovs_skb_cb.members`:

Members
-------

input_vport
    The original vport packet came in on. This value is cached
    when a packet is received by OVS.

mru
    The maximum received fragement size; 0 if the packet is not
    fragmented.

acts_origlen
    The netlink size of the flow actions applied to this skb.

cutlen
    The number of bytes from the packet end to be removed.

.. _`dp_upcall_info`:

struct dp_upcall_info
=====================

.. c:type:: struct dp_upcall_info

    metadata to include with a packet to send to userspace

.. _`dp_upcall_info.definition`:

Definition
----------

.. code-block:: c

    struct dp_upcall_info {
        struct ip_tunnel_info *egress_tun_info;
        const struct nlattr *userdata;
        const struct nlattr *actions;
        int actions_len;
        u32 portid;
        u8 cmd;
        u16 mru;
    }

.. _`dp_upcall_info.members`:

Members
-------

egress_tun_info
    If nonnull, becomes \ ``OVS_PACKET_ATTR_EGRESS_TUN_KEY``\ .

userdata
    If nonnull, its variable-length value is passed to userspace as
    \ ``OVS_PACKET_ATTR_USERDATA``\ .

actions
    *undescribed*

actions_len
    *undescribed*

portid
    Netlink portid to which packet should be sent.  If \ ``portid``\  is 0
    then no packet is sent and the packet is accounted in the datapath's \ ``n_lost``\ 
    counter.

cmd
    One of \ ``OVS_PACKET_CMD``\ \_\*.

mru
    If not zero, Maximum received IP fragment size.

.. _`ovs_net`:

struct ovs_net
==============

.. c:type:: struct ovs_net

    Per net-namespace data for ovs.

.. _`ovs_net.definition`:

Definition
----------

.. code-block:: c

    struct ovs_net {
        struct list_head dps;
        struct work_struct dp_notify_work;
        bool xt_label;
    }

.. _`ovs_net.members`:

Members
-------

dps
    List of datapaths to enable dumping them all out.
    Protected by genl_mutex.

dp_notify_work
    *undescribed*

xt_label
    *undescribed*

.. This file was automatic generated / don't edit.

