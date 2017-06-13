.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/bridge/br_private.h

.. _`net_bridge_vlan`:

struct net_bridge_vlan
======================

.. c:type:: struct net_bridge_vlan

    per-vlan entry

.. _`net_bridge_vlan.definition`:

Definition
----------

.. code-block:: c

    struct net_bridge_vlan {
        struct rhash_head vnode;
        struct rhash_head tnode;
        u16 vid;
        u16 flags;
        struct br_vlan_stats __percpu *stats;
        union {unnamed_union};
        struct br_tunnel_info tinfo;
        struct list_head vlist;
        struct rcu_head rcu;
    }

.. _`net_bridge_vlan.members`:

Members
-------

vnode
    rhashtable member

tnode
    *undescribed*

vid
    VLAN id

flags
    bridge vlan flags

stats
    per-cpu VLAN statistics

{unnamed_union}
    anonymous


tinfo
    *undescribed*

vlist
    sorted list of VLAN entries

rcu
    used for entry destruction

.. _`net_bridge_vlan.description`:

Description
-----------

This structure is shared between the global per-VLAN entries contained in
the bridge rhashtable and the local per-port per-VLAN entries contained in
the port's rhashtable. The union entries should be interpreted depending on
the entry flags that are set.

.. _`net_bridge_vlan_group`:

struct net_bridge_vlan_group
============================

.. c:type:: struct net_bridge_vlan_group


.. _`net_bridge_vlan_group.definition`:

Definition
----------

.. code-block:: c

    struct net_bridge_vlan_group {
        struct rhashtable vlan_hash;
        struct rhashtable tunnel_hash;
        struct list_head vlan_list;
        u16 num_vlans;
        u16 pvid;
    }

.. _`net_bridge_vlan_group.members`:

Members
-------

vlan_hash
    VLAN entry rhashtable

tunnel_hash
    *undescribed*

vlan_list
    sorted VLAN entry list

num_vlans
    number of total VLAN entries

pvid
    PVID VLAN id

.. _`net_bridge_vlan_group.important`:

IMPORTANT
---------

Be careful when checking if there're VLAN entries using list
primitives because the bridge can have entries in its list which
are just for global context but not for filtering, i.e. they have
the master flag set but not the brentry flag. If you have to check
if there're "real" entries in the bridge please test \ ``num_vlans``\ 

.. This file was automatic generated / don't edit.

