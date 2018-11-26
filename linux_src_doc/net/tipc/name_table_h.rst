.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/name_table.h

.. _`publication`:

struct publication
==================

.. c:type:: struct publication

    info about a published (name or) name sequence

.. _`publication.definition`:

Definition
----------

.. code-block:: c

    struct publication {
        u32 type;
        u32 lower;
        u32 upper;
        u32 scope;
        u32 node;
        u32 port;
        u32 key;
        struct list_head binding_node;
        struct list_head binding_sock;
        struct list_head local_publ;
        struct list_head all_publ;
        struct rcu_head rcu;
    }

.. _`publication.members`:

Members
-------

type
    name sequence type

lower
    name sequence lower bound

upper
    name sequence upper bound

scope
    scope of publication, TIPC_NODE_SCOPE or TIPC_CLUSTER_SCOPE

node
    network address of publishing socket's node

port
    publishing port

key
    publication key, unique across the cluster

binding_node
    all publications from the same node which bound this one
    - Remote publications: in node->publ_list
    Used by node/name distr to withdraw publications when node is lost
    - Local/node scope publications: in name_table->node_scope list
    - Local/cluster scope publications: in name_table->cluster_scope list

binding_sock
    all publications from the same socket which bound this one
    Used by socket to withdraw publications when socket is unbound/released

local_publ
    list of identical publications made from this node
    Used by closest_first and multicast receive lookup algorithms

all_publ
    all publications identical to this one, whatever node and scope
    Used by round-robin lookup algorithm

rcu
    RCU callback head used for deferred freeing

.. _`name_table`:

struct name_table
=================

.. c:type:: struct name_table

    table containing all existing port name publications

.. _`name_table.definition`:

Definition
----------

.. code-block:: c

    struct name_table {
        struct hlist_head services[TIPC_NAMETBL_SIZE];
        struct list_head node_scope;
        struct list_head cluster_scope;
        rwlock_t cluster_scope_lock;
        u32 local_publ_count;
    }

.. _`name_table.members`:

Members
-------

services
    *undescribed*

node_scope
    all local publications with node scope
    - used by name_distr during re-init of name table

cluster_scope
    all local publications with cluster scope
    - used by name_distr to send bulk updates to new nodes
    - used by name_distr during re-init of name table

cluster_scope_lock
    *undescribed*

local_publ_count
    number of publications issued by this node

.. This file was automatic generated / don't edit.

