.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bat_v.c

.. _`batadv_v_iface_update_mac`:

batadv_v_iface_update_mac
=========================

.. c:function:: void batadv_v_iface_update_mac(struct batadv_hard_iface *hard_iface)

    react to hard-interface MAC address change

    :param hard_iface:
        the modified interface
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_v_iface_update_mac.description`:

Description
-----------

If the modified interface is the primary one, update the originator
address in the ELP and OGM messages to reflect the new MAC address.

.. _`batadv_v_orig_print_neigh`:

batadv_v_orig_print_neigh
=========================

.. c:function:: void batadv_v_orig_print_neigh(struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing, struct seq_file *seq)

    print neighbors for the originator table

    :param orig_node:
        the orig_node for which the neighbors are printed
    :type orig_node: struct batadv_orig_node \*

    :param if_outgoing:
        outgoing interface for these entries
    :type if_outgoing: struct batadv_hard_iface \*

    :param seq:
        debugfs table seq_file struct
    :type seq: struct seq_file \*

.. _`batadv_v_orig_print_neigh.description`:

Description
-----------

Must be called while holding an rcu lock.

.. _`batadv_v_hardif_neigh_print`:

batadv_v_hardif_neigh_print
===========================

.. c:function:: void batadv_v_hardif_neigh_print(struct seq_file *seq, struct batadv_hardif_neigh_node *hardif_neigh)

    print a single ELP neighbour node

    :param seq:
        neighbour table seq_file struct
    :type seq: struct seq_file \*

    :param hardif_neigh:
        hardif neighbour information
    :type hardif_neigh: struct batadv_hardif_neigh_node \*

.. _`batadv_v_neigh_print`:

batadv_v_neigh_print
====================

.. c:function:: void batadv_v_neigh_print(struct batadv_priv *bat_priv, struct seq_file *seq)

    print the single hop neighbour list

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param seq:
        neighbour table seq_file struct
    :type seq: struct seq_file \*

.. _`batadv_v_neigh_dump_neigh`:

batadv_v_neigh_dump_neigh
=========================

.. c:function:: int batadv_v_neigh_dump_neigh(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hardif_neigh_node *hardif_neigh)

    Dump a neighbour into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param hardif_neigh:
        Neighbour to dump
    :type hardif_neigh: struct batadv_hardif_neigh_node \*

.. _`batadv_v_neigh_dump_neigh.return`:

Return
------

Error code, or 0 on success

.. _`batadv_v_neigh_dump_hardif`:

batadv_v_neigh_dump_hardif
==========================

.. c:function:: int batadv_v_neigh_dump_hardif(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *hard_iface, int *idx_s)

    Dump the  neighbours of a hard interface into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param hard_iface:
        The hard interface to be dumped
    :type hard_iface: struct batadv_hard_iface \*

    :param idx_s:
        Entries to be skipped
    :type idx_s: int \*

.. _`batadv_v_neigh_dump_hardif.description`:

Description
-----------

This function assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`batadv_v_neigh_dump_hardif.return`:

Return
------

Error code, or 0 on success

.. _`batadv_v_neigh_dump`:

batadv_v_neigh_dump
===================

.. c:function:: void batadv_v_neigh_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv, struct batadv_hard_iface *single_hardif)

    Dump the neighbours of a hard interface  into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        Control block containing additional options
    :type cb: struct netlink_callback \*

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param single_hardif:
        Limit dumping to this hard interface
    :type single_hardif: struct batadv_hard_iface \*

.. _`batadv_v_orig_print`:

batadv_v_orig_print
===================

.. c:function:: void batadv_v_orig_print(struct batadv_priv *bat_priv, struct seq_file *seq, struct batadv_hard_iface *if_outgoing)

    print the originator table

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param seq:
        debugfs table seq_file struct
    :type seq: struct seq_file \*

    :param if_outgoing:
        the outgoing interface for which this should be printed
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_v_orig_dump_subentry`:

batadv_v_orig_dump_subentry
===========================

.. c:function:: int batadv_v_orig_dump_subentry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node, bool best)

    Dump an originator subentry into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param if_outgoing:
        Limit dump to entries with this outgoing interface
    :type if_outgoing: struct batadv_hard_iface \*

    :param orig_node:
        Originator to dump
    :type orig_node: struct batadv_orig_node \*

    :param neigh_node:
        Single hops neighbour
    :type neigh_node: struct batadv_neigh_node \*

    :param best:
        Is the best originator
    :type best: bool

.. _`batadv_v_orig_dump_subentry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_v_orig_dump_entry`:

batadv_v_orig_dump_entry
========================

.. c:function:: int batadv_v_orig_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct batadv_orig_node *orig_node, int *sub_s)

    Dump an originator entry into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param if_outgoing:
        Limit dump to entries with this outgoing interface
    :type if_outgoing: struct batadv_hard_iface \*

    :param orig_node:
        Originator to dump
    :type orig_node: struct batadv_orig_node \*

    :param sub_s:
        Number of sub entries to skip
    :type sub_s: int \*

.. _`batadv_v_orig_dump_entry.description`:

Description
-----------

This function assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`batadv_v_orig_dump_entry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_v_orig_dump_bucket`:

batadv_v_orig_dump_bucket
=========================

.. c:function:: int batadv_v_orig_dump_bucket(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct hlist_head *head, int *idx_s, int *sub)

    Dump an originator bucket into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param if_outgoing:
        Limit dump to entries with this outgoing interface
    :type if_outgoing: struct batadv_hard_iface \*

    :param head:
        Bucket to be dumped
    :type head: struct hlist_head \*

    :param idx_s:
        Number of entries to be skipped
    :type idx_s: int \*

    :param sub:
        Number of sub entries to be skipped
    :type sub: int \*

.. _`batadv_v_orig_dump_bucket.return`:

Return
------

Error code, or 0 on success

.. _`batadv_v_orig_dump`:

batadv_v_orig_dump
==================

.. c:function:: void batadv_v_orig_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing)

    Dump the originators into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        Control block containing additional options
    :type cb: struct netlink_callback \*

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param if_outgoing:
        Limit dump to entries with this outgoing interface
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_v_init_sel_class`:

batadv_v_init_sel_class
=======================

.. c:function:: void batadv_v_init_sel_class(struct batadv_priv *bat_priv)

    initialize GW selection class

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_v_gw_throughput_get`:

batadv_v_gw_throughput_get
==========================

.. c:function:: int batadv_v_gw_throughput_get(struct batadv_gw_node *gw_node, u32 *bw)

    retrieve the GW-bandwidth for a given GW

    :param gw_node:
        the GW to retrieve the metric for
    :type gw_node: struct batadv_gw_node \*

    :param bw:
        the pointer where the metric will be stored. The metric is computed as
        the minimum between the GW advertised throughput and the path throughput to
        it in the mesh
    :type bw: u32 \*

.. _`batadv_v_gw_throughput_get.return`:

Return
------

0 on success, -1 on failure

.. _`batadv_v_gw_get_best_gw_node`:

batadv_v_gw_get_best_gw_node
============================

.. c:function:: struct batadv_gw_node *batadv_v_gw_get_best_gw_node(struct batadv_priv *bat_priv)

    retrieve the best GW node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_v_gw_get_best_gw_node.return`:

Return
------

the GW node having the best GW-metric, NULL if no GW is known

.. _`batadv_v_gw_is_eligible`:

batadv_v_gw_is_eligible
=======================

.. c:function:: bool batadv_v_gw_is_eligible(struct batadv_priv *bat_priv, struct batadv_orig_node *curr_gw_orig, struct batadv_orig_node *orig_node)

    check if a originator would be selected as GW

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param curr_gw_orig:
        originator representing the currently selected GW
    :type curr_gw_orig: struct batadv_orig_node \*

    :param orig_node:
        the originator representing the new candidate
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_v_gw_is_eligible.return`:

Return
------

true if orig_node can be selected as current GW, false otherwise

.. _`batadv_v_gw_print`:

batadv_v_gw_print
=================

.. c:function:: void batadv_v_gw_print(struct batadv_priv *bat_priv, struct seq_file *seq)

    print the gateway list

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param seq:
        gateway table seq_file struct
    :type seq: struct seq_file \*

.. _`batadv_v_gw_dump_entry`:

batadv_v_gw_dump_entry
======================

.. c:function:: int batadv_v_gw_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_gw_node *gw_node)

    Dump a gateway into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param gw_node:
        Gateway to be dumped
    :type gw_node: struct batadv_gw_node \*

.. _`batadv_v_gw_dump_entry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_v_gw_dump`:

batadv_v_gw_dump
================

.. c:function:: void batadv_v_gw_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv)

    Dump gateways into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        Control block containing additional options
    :type cb: struct netlink_callback \*

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_v_hardif_init`:

batadv_v_hardif_init
====================

.. c:function:: void batadv_v_hardif_init(struct batadv_hard_iface *hard_iface)

    initialize the algorithm specific fields in the hard-interface object

    :param hard_iface:
        the hard-interface to initialize
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_v_mesh_init`:

batadv_v_mesh_init
==================

.. c:function:: int batadv_v_mesh_init(struct batadv_priv *bat_priv)

    initialize the B.A.T.M.A.N. V private resources for a mesh

    :param bat_priv:
        the object representing the mesh interface to initialise
    :type bat_priv: struct batadv_priv \*

.. _`batadv_v_mesh_init.return`:

Return
------

0 on success or a negative error code otherwise

.. _`batadv_v_mesh_free`:

batadv_v_mesh_free
==================

.. c:function:: void batadv_v_mesh_free(struct batadv_priv *bat_priv)

    free the B.A.T.M.A.N. V private resources for a mesh

    :param bat_priv:
        the object representing the mesh interface to free
    :type bat_priv: struct batadv_priv \*

.. _`batadv_v_init`:

batadv_v_init
=============

.. c:function:: int batadv_v_init( void)

    B.A.T.M.A.N. V initialization function

    :param void:
        no arguments
    :type void: 

.. _`batadv_v_init.description`:

Description
-----------

Takes care of initializing all the subcomponents.
It is invoked upon module load only.

.. _`batadv_v_init.return`:

Return
------

0 on success or a negative error code otherwise

.. This file was automatic generated / don't edit.

