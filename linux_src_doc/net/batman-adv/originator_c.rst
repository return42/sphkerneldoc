.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/originator.c

.. _`batadv_orig_hash_find`:

batadv_orig_hash_find
=====================

.. c:function:: struct batadv_orig_node *batadv_orig_hash_find(struct batadv_priv *bat_priv, const void *data)

    Find and return originator from orig_hash

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param data:
        mac address of the originator
    :type data: const void \*

.. _`batadv_orig_hash_find.return`:

Return
------

orig_node (with increased refcnt), NULL on errors

.. _`batadv_compare_orig`:

batadv_compare_orig
===================

.. c:function:: bool batadv_compare_orig(const struct hlist_node *node, const void *data2)

    comparing function used in the originator hash table

    :param node:
        node in the local table
    :type node: const struct hlist_node \*

    :param data2:
        second object to compare the node to
    :type data2: const void \*

.. _`batadv_compare_orig.return`:

Return
------

true if they are the same originator

.. _`batadv_orig_node_vlan_get`:

batadv_orig_node_vlan_get
=========================

.. c:function:: struct batadv_orig_node_vlan *batadv_orig_node_vlan_get(struct batadv_orig_node *orig_node, unsigned short vid)

    get an orig_node_vlan object

    :param orig_node:
        the originator serving the VLAN
    :type orig_node: struct batadv_orig_node \*

    :param vid:
        the VLAN identifier
    :type vid: unsigned short

.. _`batadv_orig_node_vlan_get.return`:

Return
------

the vlan object identified by vid and belonging to orig_node or NULL
if it does not exist.

.. _`batadv_orig_node_vlan_new`:

batadv_orig_node_vlan_new
=========================

.. c:function:: struct batadv_orig_node_vlan *batadv_orig_node_vlan_new(struct batadv_orig_node *orig_node, unsigned short vid)

    search and possibly create an orig_node_vlan object

    :param orig_node:
        the originator serving the VLAN
    :type orig_node: struct batadv_orig_node \*

    :param vid:
        the VLAN identifier
    :type vid: unsigned short

.. _`batadv_orig_node_vlan_new.return`:

Return
------

NULL in case of failure or the vlan object identified by vid and
belonging to orig_node otherwise. The object is created and added to the list
if it does not exist.

The object is returned with refcounter increased by 1.

.. _`batadv_orig_node_vlan_release`:

batadv_orig_node_vlan_release
=============================

.. c:function:: void batadv_orig_node_vlan_release(struct kref *ref)

    release originator-vlan object from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the originator-vlan object
    :type ref: struct kref \*

.. _`batadv_orig_node_vlan_put`:

batadv_orig_node_vlan_put
=========================

.. c:function:: void batadv_orig_node_vlan_put(struct batadv_orig_node_vlan *orig_vlan)

    decrement the refcounter and possibly release the originator-vlan object

    :param orig_vlan:
        the originator-vlan object to release
    :type orig_vlan: struct batadv_orig_node_vlan \*

.. _`batadv_originator_init`:

batadv_originator_init
======================

.. c:function:: int batadv_originator_init(struct batadv_priv *bat_priv)

    Initialize all originator structures

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_originator_init.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_neigh_ifinfo_release`:

batadv_neigh_ifinfo_release
===========================

.. c:function:: void batadv_neigh_ifinfo_release(struct kref *ref)

    release neigh_ifinfo from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the neigh_ifinfo
    :type ref: struct kref \*

.. _`batadv_neigh_ifinfo_put`:

batadv_neigh_ifinfo_put
=======================

.. c:function:: void batadv_neigh_ifinfo_put(struct batadv_neigh_ifinfo *neigh_ifinfo)

    decrement the refcounter and possibly release the neigh_ifinfo

    :param neigh_ifinfo:
        the neigh_ifinfo object to release
    :type neigh_ifinfo: struct batadv_neigh_ifinfo \*

.. _`batadv_hardif_neigh_release`:

batadv_hardif_neigh_release
===========================

.. c:function:: void batadv_hardif_neigh_release(struct kref *ref)

    release hardif neigh node from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the neigh_node
    :type ref: struct kref \*

.. _`batadv_hardif_neigh_put`:

batadv_hardif_neigh_put
=======================

.. c:function:: void batadv_hardif_neigh_put(struct batadv_hardif_neigh_node *hardif_neigh)

    decrement the hardif neighbors refcounter and possibly release it

    :param hardif_neigh:
        hardif neigh neighbor to free
    :type hardif_neigh: struct batadv_hardif_neigh_node \*

.. _`batadv_neigh_node_release`:

batadv_neigh_node_release
=========================

.. c:function:: void batadv_neigh_node_release(struct kref *ref)

    release neigh_node from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the neigh_node
    :type ref: struct kref \*

.. _`batadv_neigh_node_put`:

batadv_neigh_node_put
=====================

.. c:function:: void batadv_neigh_node_put(struct batadv_neigh_node *neigh_node)

    decrement the neighbors refcounter and possibly release it

    :param neigh_node:
        neigh neighbor to free
    :type neigh_node: struct batadv_neigh_node \*

.. _`batadv_orig_router_get`:

batadv_orig_router_get
======================

.. c:function:: struct batadv_neigh_node *batadv_orig_router_get(struct batadv_orig_node *orig_node, const struct batadv_hard_iface *if_outgoing)

    router to the originator depending on iface

    :param orig_node:
        the orig node for the router
    :type orig_node: struct batadv_orig_node \*

    :param if_outgoing:
        the interface where the payload packet has been received or
        the OGM should be sent to
    :type if_outgoing: const struct batadv_hard_iface \*

.. _`batadv_orig_router_get.return`:

Return
------

the neighbor which should be router for this orig_node/iface.

The object is returned with refcounter increased by 1.

.. _`batadv_orig_ifinfo_get`:

batadv_orig_ifinfo_get
======================

.. c:function:: struct batadv_orig_ifinfo *batadv_orig_ifinfo_get(struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing)

    find the ifinfo from an orig_node

    :param orig_node:
        the orig node to be queried
    :type orig_node: struct batadv_orig_node \*

    :param if_outgoing:
        the interface for which the ifinfo should be acquired
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_orig_ifinfo_get.return`:

Return
------

the requested orig_ifinfo or NULL if not found.

The object is returned with refcounter increased by 1.

.. _`batadv_orig_ifinfo_new`:

batadv_orig_ifinfo_new
======================

.. c:function:: struct batadv_orig_ifinfo *batadv_orig_ifinfo_new(struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing)

    search and possibly create an orig_ifinfo object

    :param orig_node:
        the orig node to be queried
    :type orig_node: struct batadv_orig_node \*

    :param if_outgoing:
        the interface for which the ifinfo should be acquired
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_orig_ifinfo_new.return`:

Return
------

NULL in case of failure or the orig_ifinfo object for the if_outgoing
interface otherwise. The object is created and added to the list
if it does not exist.

The object is returned with refcounter increased by 1.

.. _`batadv_neigh_ifinfo_get`:

batadv_neigh_ifinfo_get
=======================

.. c:function:: struct batadv_neigh_ifinfo *batadv_neigh_ifinfo_get(struct batadv_neigh_node *neigh, struct batadv_hard_iface *if_outgoing)

    find the ifinfo from an neigh_node

    :param neigh:
        the neigh node to be queried
    :type neigh: struct batadv_neigh_node \*

    :param if_outgoing:
        the interface for which the ifinfo should be acquired
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_neigh_ifinfo_get.description`:

Description
-----------

The object is returned with refcounter increased by 1.

.. _`batadv_neigh_ifinfo_get.return`:

Return
------

the requested neigh_ifinfo or NULL if not found

.. _`batadv_neigh_ifinfo_new`:

batadv_neigh_ifinfo_new
=======================

.. c:function:: struct batadv_neigh_ifinfo *batadv_neigh_ifinfo_new(struct batadv_neigh_node *neigh, struct batadv_hard_iface *if_outgoing)

    search and possibly create an neigh_ifinfo object

    :param neigh:
        the neigh node to be queried
    :type neigh: struct batadv_neigh_node \*

    :param if_outgoing:
        the interface for which the ifinfo should be acquired
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_neigh_ifinfo_new.return`:

Return
------

NULL in case of failure or the neigh_ifinfo object for the
if_outgoing interface otherwise. The object is created and added to the list
if it does not exist.

The object is returned with refcounter increased by 1.

.. _`batadv_neigh_node_get`:

batadv_neigh_node_get
=====================

.. c:function:: struct batadv_neigh_node *batadv_neigh_node_get(const struct batadv_orig_node *orig_node, const struct batadv_hard_iface *hard_iface, const u8 *addr)

    retrieve a neighbour from the list

    :param orig_node:
        originator which the neighbour belongs to
    :type orig_node: const struct batadv_orig_node \*

    :param hard_iface:
        the interface where this neighbour is connected to
    :type hard_iface: const struct batadv_hard_iface \*

    :param addr:
        the address of the neighbour
    :type addr: const u8 \*

.. _`batadv_neigh_node_get.description`:

Description
-----------

Looks for and possibly returns a neighbour belonging to this originator list
which is connected through the provided hard interface.

.. _`batadv_neigh_node_get.return`:

Return
------

neighbor when found. Othwerwise NULL

.. _`batadv_hardif_neigh_create`:

batadv_hardif_neigh_create
==========================

.. c:function:: struct batadv_hardif_neigh_node *batadv_hardif_neigh_create(struct batadv_hard_iface *hard_iface, const u8 *neigh_addr, struct batadv_orig_node *orig_node)

    create a hardif neighbour node

    :param hard_iface:
        the interface this neighbour is connected to
    :type hard_iface: struct batadv_hard_iface \*

    :param neigh_addr:
        the interface address of the neighbour to retrieve
    :type neigh_addr: const u8 \*

    :param orig_node:
        originator object representing the neighbour
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_hardif_neigh_create.return`:

Return
------

the hardif neighbour node if found or created or NULL otherwise.

.. _`batadv_hardif_neigh_get_or_create`:

batadv_hardif_neigh_get_or_create
=================================

.. c:function:: struct batadv_hardif_neigh_node *batadv_hardif_neigh_get_or_create(struct batadv_hard_iface *hard_iface, const u8 *neigh_addr, struct batadv_orig_node *orig_node)

    retrieve or create a hardif neighbour node

    :param hard_iface:
        the interface this neighbour is connected to
    :type hard_iface: struct batadv_hard_iface \*

    :param neigh_addr:
        the interface address of the neighbour to retrieve
    :type neigh_addr: const u8 \*

    :param orig_node:
        originator object representing the neighbour
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_hardif_neigh_get_or_create.return`:

Return
------

the hardif neighbour node if found or created or NULL otherwise.

.. _`batadv_hardif_neigh_get`:

batadv_hardif_neigh_get
=======================

.. c:function:: struct batadv_hardif_neigh_node *batadv_hardif_neigh_get(const struct batadv_hard_iface *hard_iface, const u8 *neigh_addr)

    retrieve a hardif neighbour from the list

    :param hard_iface:
        the interface where this neighbour is connected to
    :type hard_iface: const struct batadv_hard_iface \*

    :param neigh_addr:
        the address of the neighbour
    :type neigh_addr: const u8 \*

.. _`batadv_hardif_neigh_get.description`:

Description
-----------

Looks for and possibly returns a neighbour belonging to this hard interface.

.. _`batadv_hardif_neigh_get.return`:

Return
------

neighbor when found. Othwerwise NULL

.. _`batadv_neigh_node_create`:

batadv_neigh_node_create
========================

.. c:function:: struct batadv_neigh_node *batadv_neigh_node_create(struct batadv_orig_node *orig_node, struct batadv_hard_iface *hard_iface, const u8 *neigh_addr)

    create a neigh node object

    :param orig_node:
        originator object representing the neighbour
    :type orig_node: struct batadv_orig_node \*

    :param hard_iface:
        the interface where the neighbour is connected to
    :type hard_iface: struct batadv_hard_iface \*

    :param neigh_addr:
        the mac address of the neighbour interface
    :type neigh_addr: const u8 \*

.. _`batadv_neigh_node_create.description`:

Description
-----------

Allocates a new neigh_node object and initialises all the generic fields.

.. _`batadv_neigh_node_create.return`:

Return
------

the neighbour node if found or created or NULL otherwise.

.. _`batadv_neigh_node_get_or_create`:

batadv_neigh_node_get_or_create
===============================

.. c:function:: struct batadv_neigh_node *batadv_neigh_node_get_or_create(struct batadv_orig_node *orig_node, struct batadv_hard_iface *hard_iface, const u8 *neigh_addr)

    retrieve or create a neigh node object

    :param orig_node:
        originator object representing the neighbour
    :type orig_node: struct batadv_orig_node \*

    :param hard_iface:
        the interface where the neighbour is connected to
    :type hard_iface: struct batadv_hard_iface \*

    :param neigh_addr:
        the mac address of the neighbour interface
    :type neigh_addr: const u8 \*

.. _`batadv_neigh_node_get_or_create.return`:

Return
------

the neighbour node if found or created or NULL otherwise.

.. _`batadv_hardif_neigh_seq_print_text`:

batadv_hardif_neigh_seq_print_text
==================================

.. c:function:: int batadv_hardif_neigh_seq_print_text(struct seq_file *seq, void *offset)

    print the single hop neighbour list

    :param seq:
        neighbour table seq_file struct
    :type seq: struct seq_file \*

    :param offset:
        not used
    :type offset: void \*

.. _`batadv_hardif_neigh_seq_print_text.return`:

Return
------

always 0

.. _`batadv_hardif_neigh_dump`:

batadv_hardif_neigh_dump
========================

.. c:function:: int batadv_hardif_neigh_dump(struct sk_buff *msg, struct netlink_callback *cb)

    Dump to netlink the neighbor infos for a specific outgoing interface

    :param msg:
        message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        parameters for the dump
    :type cb: struct netlink_callback \*

.. _`batadv_hardif_neigh_dump.return`:

Return
------

0 or error value

.. _`batadv_orig_ifinfo_release`:

batadv_orig_ifinfo_release
==========================

.. c:function:: void batadv_orig_ifinfo_release(struct kref *ref)

    release orig_ifinfo from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the orig_ifinfo
    :type ref: struct kref \*

.. _`batadv_orig_ifinfo_put`:

batadv_orig_ifinfo_put
======================

.. c:function:: void batadv_orig_ifinfo_put(struct batadv_orig_ifinfo *orig_ifinfo)

    decrement the refcounter and possibly release the orig_ifinfo

    :param orig_ifinfo:
        the orig_ifinfo object to release
    :type orig_ifinfo: struct batadv_orig_ifinfo \*

.. _`batadv_orig_node_free_rcu`:

batadv_orig_node_free_rcu
=========================

.. c:function:: void batadv_orig_node_free_rcu(struct rcu_head *rcu)

    free the orig_node

    :param rcu:
        rcu pointer of the orig_node
    :type rcu: struct rcu_head \*

.. _`batadv_orig_node_release`:

batadv_orig_node_release
========================

.. c:function:: void batadv_orig_node_release(struct kref *ref)

    release orig_node from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the orig_node
    :type ref: struct kref \*

.. _`batadv_orig_node_put`:

batadv_orig_node_put
====================

.. c:function:: void batadv_orig_node_put(struct batadv_orig_node *orig_node)

    decrement the orig node refcounter and possibly release it

    :param orig_node:
        the orig node to free
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_originator_free`:

batadv_originator_free
======================

.. c:function:: void batadv_originator_free(struct batadv_priv *bat_priv)

    Free all originator structures

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_orig_node_new`:

batadv_orig_node_new
====================

.. c:function:: struct batadv_orig_node *batadv_orig_node_new(struct batadv_priv *bat_priv, const u8 *addr)

    creates a new orig_node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the originator
    :type addr: const u8 \*

.. _`batadv_orig_node_new.description`:

Description
-----------

Creates a new originator object and initialise all the generic fields.
The new object is not added to the originator list.

.. _`batadv_orig_node_new.return`:

Return
------

the newly created object or NULL on failure.

.. _`batadv_purge_neigh_ifinfo`:

batadv_purge_neigh_ifinfo
=========================

.. c:function:: void batadv_purge_neigh_ifinfo(struct batadv_priv *bat_priv, struct batadv_neigh_node *neigh)

    purge obsolete ifinfo entries from neighbor

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param neigh:
        orig node which is to be checked
    :type neigh: struct batadv_neigh_node \*

.. _`batadv_purge_orig_ifinfo`:

batadv_purge_orig_ifinfo
========================

.. c:function:: bool batadv_purge_orig_ifinfo(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    purge obsolete ifinfo entries from originator

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        orig node which is to be checked
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_purge_orig_ifinfo.return`:

Return
------

true if any ifinfo entry was purged, false otherwise.

.. _`batadv_purge_orig_neighbors`:

batadv_purge_orig_neighbors
===========================

.. c:function:: bool batadv_purge_orig_neighbors(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    purges neighbors from originator

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        orig node which is to be checked
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_purge_orig_neighbors.return`:

Return
------

true if any neighbor was purged, false otherwise

.. _`batadv_find_best_neighbor`:

batadv_find_best_neighbor
=========================

.. c:function:: struct batadv_neigh_node *batadv_find_best_neighbor(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing)

    finds the best neighbor after purging

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        orig node which is to be checked
    :type orig_node: struct batadv_orig_node \*

    :param if_outgoing:
        the interface for which the metric should be compared
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_find_best_neighbor.return`:

Return
------

the current best neighbor, with refcount increased.

.. _`batadv_purge_orig_node`:

batadv_purge_orig_node
======================

.. c:function:: bool batadv_purge_orig_node(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    purges obsolete information from an orig_node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        orig node which is to be checked
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_purge_orig_node.description`:

Description
-----------

This function checks if the orig_node or substructures of it have become
obsolete, and purges this information if that's the case.

.. _`batadv_purge_orig_node.return`:

Return
------

true if the orig_node is to be removed, false otherwise.

.. _`batadv_purge_orig_ref`:

batadv_purge_orig_ref
=====================

.. c:function:: void batadv_purge_orig_ref(struct batadv_priv *bat_priv)

    Purge all outdated originators

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_orig_seq_print_text`:

batadv_orig_seq_print_text
==========================

.. c:function:: int batadv_orig_seq_print_text(struct seq_file *seq, void *offset)

    Print the originator table in a seq file

    :param seq:
        seq file to print on
    :type seq: struct seq_file \*

    :param offset:
        not used
    :type offset: void \*

.. _`batadv_orig_seq_print_text.return`:

Return
------

always 0

.. _`batadv_orig_hardif_seq_print_text`:

batadv_orig_hardif_seq_print_text
=================================

.. c:function:: int batadv_orig_hardif_seq_print_text(struct seq_file *seq, void *offset)

    writes originator infos for a specific outgoing interface

    :param seq:
        debugfs table seq_file struct
    :type seq: struct seq_file \*

    :param offset:
        not used
    :type offset: void \*

.. _`batadv_orig_hardif_seq_print_text.return`:

Return
------

0

.. _`batadv_orig_dump`:

batadv_orig_dump
================

.. c:function:: int batadv_orig_dump(struct sk_buff *msg, struct netlink_callback *cb)

    Dump to netlink the originator infos for a specific outgoing interface

    :param msg:
        message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        parameters for the dump
    :type cb: struct netlink_callback \*

.. _`batadv_orig_dump.return`:

Return
------

0 or error value

.. This file was automatic generated / don't edit.

