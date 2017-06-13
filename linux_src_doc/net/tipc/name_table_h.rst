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
        u32 ref;
        u32 key;
        struct list_head nodesub_list;
        struct list_head local_list;
        struct list_head pport_list;
        struct list_head node_list;
        struct list_head cluster_list;
        struct list_head zone_list;
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
    scope of publication

node
    network address of publishing port's node

ref
    publishing port

key
    publication key

nodesub_list
    subscription to "node down" event (off-node publication only)

local_list
    adjacent entries in list of publications made by this node

pport_list
    adjacent entries in list of publications made by this port

node_list
    adjacent matching name seq publications with >= node scope

cluster_list
    adjacent matching name seq publications with >= cluster scope

zone_list
    adjacent matching name seq publications with >= zone scope

rcu
    RCU callback head used for deferred freeing

.. _`publication.description`:

Description
-----------

Note that the node list, cluster list, and zone list are circular lists.

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
        struct hlist_head seq_hlist;
        struct list_head publ_list;
        u32 local_publ_count;
    }

.. _`name_table.members`:

Members
-------

seq_hlist
    name sequence hash lists

publ_list
    pulication lists

local_publ_count
    number of publications issued by this node

.. This file was automatic generated / don't edit.

