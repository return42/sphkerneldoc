.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/fragmentation.c

.. _`batadv_frag_clear_chain`:

batadv_frag_clear_chain
=======================

.. c:function:: void batadv_frag_clear_chain(struct hlist_head *head, bool dropped)

    delete entries in the fragment buffer chain

    :param head:
        head of chain with entries.
    :type head: struct hlist_head \*

    :param dropped:
        whether the chain is cleared because all fragments are dropped
    :type dropped: bool

.. _`batadv_frag_clear_chain.description`:

Description
-----------

Free fragments in the passed hlist. Should be called with appropriate lock.

.. _`batadv_frag_purge_orig`:

batadv_frag_purge_orig
======================

.. c:function:: void batadv_frag_purge_orig(struct batadv_orig_node *orig_node, bool (*check_cb)(struct batadv_frag_table_entry *))

    free fragments associated to an orig

    :param orig_node:
        originator to free fragments from
    :type orig_node: struct batadv_orig_node \*

    :param bool (\*check_cb)(struct batadv_frag_table_entry \*):
        optional function to tell if an entry should be purged

.. _`batadv_frag_size_limit`:

batadv_frag_size_limit
======================

.. c:function:: int batadv_frag_size_limit( void)

    maximum possible size of packet to be fragmented

    :param void:
        no arguments
    :type void: 

.. _`batadv_frag_size_limit.return`:

Return
------

the maximum size of payload that can be fragmented.

.. _`batadv_frag_init_chain`:

batadv_frag_init_chain
======================

.. c:function:: bool batadv_frag_init_chain(struct batadv_frag_table_entry *chain, u16 seqno)

    check and prepare fragment chain for new fragment

    :param chain:
        chain in fragments table to init
    :type chain: struct batadv_frag_table_entry \*

    :param seqno:
        sequence number of the received fragment
    :type seqno: u16

.. _`batadv_frag_init_chain.description`:

Description
-----------

Make chain ready for a fragment with sequence number "seqno". Delete existing
entries if they have an "old" sequence number.

Caller must hold chain->lock.

.. _`batadv_frag_init_chain.return`:

Return
------

true if chain is empty and caller can just insert the new fragment
without searching for the right position.

.. _`batadv_frag_insert_packet`:

batadv_frag_insert_packet
=========================

.. c:function:: bool batadv_frag_insert_packet(struct batadv_orig_node *orig_node, struct sk_buff *skb, struct hlist_head *chain_out)

    insert a fragment into a fragment chain

    :param orig_node:
        originator that the fragment was received from
    :type orig_node: struct batadv_orig_node \*

    :param skb:
        skb to insert
    :type skb: struct sk_buff \*

    :param chain_out:
        list head to attach complete chains of fragments to
    :type chain_out: struct hlist_head \*

.. _`batadv_frag_insert_packet.description`:

Description
-----------

Insert a new fragment into the reverse ordered chain in the right table
entry. The hash table entry is cleared if "old" fragments exist in it.

.. _`batadv_frag_insert_packet.return`:

Return
------

true if skb is buffered, false on error. If the chain has all the
fragments needed to merge the packet, the chain is moved to the passed head
to avoid locking the chain in the table.

.. _`batadv_frag_merge_packets`:

batadv_frag_merge_packets
=========================

.. c:function:: struct sk_buff *batadv_frag_merge_packets(struct hlist_head *chain)

    merge a chain of fragments

    :param chain:
        head of chain with fragments
    :type chain: struct hlist_head \*

.. _`batadv_frag_merge_packets.description`:

Description
-----------

Expand the first skb in the chain and copy the content of the remaining
skb's into the expanded one. After doing so, clear the chain.

.. _`batadv_frag_merge_packets.return`:

Return
------

the merged skb or NULL on error.

.. _`batadv_frag_skb_buffer`:

batadv_frag_skb_buffer
======================

.. c:function:: bool batadv_frag_skb_buffer(struct sk_buff **skb, struct batadv_orig_node *orig_node_src)

    buffer fragment for later merge

    :param skb:
        skb to buffer
    :type skb: struct sk_buff \*\*

    :param orig_node_src:
        originator that the skb is received from
    :type orig_node_src: struct batadv_orig_node \*

.. _`batadv_frag_skb_buffer.description`:

Description
-----------

Add fragment to buffer and merge fragments if possible.

.. _`batadv_frag_skb_buffer.there-are-three-possible-outcomes`:

There are three possible outcomes
---------------------------------

1) Packet is merged: Return true and
set \*skb to merged packet; 2) Packet is buffered: Return true and set \*skb
to NULL; 3) Error: Return false and free skb.

.. _`batadv_frag_skb_buffer.return`:

Return
------

true when packet is merged or buffered, false when skb is not not
used.

.. _`batadv_frag_skb_fwd`:

batadv_frag_skb_fwd
===================

.. c:function:: bool batadv_frag_skb_fwd(struct sk_buff *skb, struct batadv_hard_iface *recv_if, struct batadv_orig_node *orig_node_src)

    forward fragments that would exceed MTU when merged

    :param skb:
        skb to forward
    :type skb: struct sk_buff \*

    :param recv_if:
        interface that the skb is received on
    :type recv_if: struct batadv_hard_iface \*

    :param orig_node_src:
        originator that the skb is received from
    :type orig_node_src: struct batadv_orig_node \*

.. _`batadv_frag_skb_fwd.description`:

Description
-----------

Look up the next-hop of the fragments payload and check if the merged packet
will exceed the MTU towards the next-hop. If so, the fragment is forwarded
without merging it.

.. _`batadv_frag_skb_fwd.return`:

Return
------

true if the fragment is consumed/forwarded, false otherwise.

.. _`batadv_frag_create`:

batadv_frag_create
==================

.. c:function:: struct sk_buff *batadv_frag_create(struct sk_buff *skb, struct batadv_frag_packet *frag_head, unsigned int fragment_size)

    create a fragment from skb

    :param skb:
        skb to create fragment from
    :type skb: struct sk_buff \*

    :param frag_head:
        header to use in new fragment
    :type frag_head: struct batadv_frag_packet \*

    :param fragment_size:
        size of new fragment
    :type fragment_size: unsigned int

.. _`batadv_frag_create.split-the-passed-skb-into-two-fragments`:

Split the passed skb into two fragments
---------------------------------------

A new one with size matching the
passed mtu and the old one with the rest. The new skb contains data from the
tail of the old skb.

.. _`batadv_frag_create.return`:

Return
------

the new fragment, NULL on error.

.. _`batadv_frag_send_packet`:

batadv_frag_send_packet
=======================

.. c:function:: int batadv_frag_send_packet(struct sk_buff *skb, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node)

    create up to 16 fragments from the passed skb

    :param skb:
        skb to create fragments from
    :type skb: struct sk_buff \*

    :param orig_node:
        final destination of the created fragments
    :type orig_node: struct batadv_orig_node \*

    :param neigh_node:
        next-hop of the created fragments
    :type neigh_node: struct batadv_neigh_node \*

.. _`batadv_frag_send_packet.return`:

Return
------

the netdev tx status or a negative errno code on a failure

.. This file was automatic generated / don't edit.

