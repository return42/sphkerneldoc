.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bat_iv_ogm.c

.. _`batadv_dup_status`:

enum batadv_dup_status
======================

.. c:type:: enum batadv_dup_status

    duplicate status

.. _`batadv_dup_status.definition`:

Definition
----------

.. code-block:: c

    enum batadv_dup_status {
        BATADV_NO_DUP,
        BATADV_ORIG_DUP,
        BATADV_NEIGH_DUP,
        BATADV_PROTECTED
    };

.. _`batadv_dup_status.constants`:

Constants
---------

BATADV_NO_DUP
    the packet is no duplicate

BATADV_ORIG_DUP
    OGM is a duplicate in the originator (but not for the neighbor)

BATADV_NEIGH_DUP
    OGM is a duplicate for the neighbor

BATADV_PROTECTED
    originator is currently protected (after reboot)

.. _`batadv_ring_buffer_set`:

batadv_ring_buffer_set
======================

.. c:function:: void batadv_ring_buffer_set(u8 lq_recv, u8 *lq_index, u8 value)

    update the ring buffer with the given value

    :param u8 lq_recv:
        pointer to the ring buffer

    :param u8 \*lq_index:
        index to store the value at

    :param u8 value:
        value to store in the ring buffer

.. _`batadv_ring_buffer_avg`:

batadv_ring_buffer_avg
======================

.. c:function:: u8 batadv_ring_buffer_avg(const u8 lq_recv)

    compute the average of all non-zero values stored in the given ring buffer

    :param const u8 lq_recv:
        pointer to the ring buffer

.. _`batadv_ring_buffer_avg.return`:

Return
------

computed average value.

.. _`batadv_iv_ogm_orig_free`:

batadv_iv_ogm_orig_free
=======================

.. c:function:: void batadv_iv_ogm_orig_free(struct batadv_orig_node *orig_node)

    free the private resources allocated for this orig_node

    :param struct batadv_orig_node \*orig_node:
        the orig_node for which the resources have to be free'd

.. _`batadv_iv_ogm_orig_add_if`:

batadv_iv_ogm_orig_add_if
=========================

.. c:function:: int batadv_iv_ogm_orig_add_if(struct batadv_orig_node *orig_node, int max_if_num)

    change the private structures of the orig_node to include the new hard-interface

    :param struct batadv_orig_node \*orig_node:
        the orig_node that has to be changed

    :param int max_if_num:
        the current amount of interfaces

.. _`batadv_iv_ogm_orig_add_if.return`:

Return
------

0 on success, a negative error code otherwise.

.. _`batadv_iv_ogm_drop_bcast_own_entry`:

batadv_iv_ogm_drop_bcast_own_entry
==================================

.. c:function:: void batadv_iv_ogm_drop_bcast_own_entry(struct batadv_orig_node *orig_node, int max_if_num, int del_if_num)

    drop section of bcast_own

    :param struct batadv_orig_node \*orig_node:
        the orig_node that has to be changed

    :param int max_if_num:
        the current amount of interfaces

    :param int del_if_num:
        the index of the interface being removed

.. _`batadv_iv_ogm_drop_bcast_own_sum_entry`:

batadv_iv_ogm_drop_bcast_own_sum_entry
======================================

.. c:function:: void batadv_iv_ogm_drop_bcast_own_sum_entry(struct batadv_orig_node *orig_node, int max_if_num, int del_if_num)

    drop section of bcast_own_sum

    :param struct batadv_orig_node \*orig_node:
        the orig_node that has to be changed

    :param int max_if_num:
        the current amount of interfaces

    :param int del_if_num:
        the index of the interface being removed

.. _`batadv_iv_ogm_orig_del_if`:

batadv_iv_ogm_orig_del_if
=========================

.. c:function:: int batadv_iv_ogm_orig_del_if(struct batadv_orig_node *orig_node, int max_if_num, int del_if_num)

    change the private structures of the orig_node to exclude the removed interface

    :param struct batadv_orig_node \*orig_node:
        the orig_node that has to be changed

    :param int max_if_num:
        the current amount of interfaces

    :param int del_if_num:
        the index of the interface being removed

.. _`batadv_iv_ogm_orig_del_if.return`:

Return
------

0 on success, a negative error code otherwise.

.. _`batadv_iv_ogm_orig_get`:

batadv_iv_ogm_orig_get
======================

.. c:function:: struct batadv_orig_node *batadv_iv_ogm_orig_get(struct batadv_priv *bat_priv, const u8 *addr)

    retrieve or create (if does not exist) an originator

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        mac address of the originator

.. _`batadv_iv_ogm_orig_get.return`:

Return
------

the originator object corresponding to the passed mac address or NULL
on failure.
If the object does not exists it is created an initialised.

.. _`batadv_iv_ogm_aggr_packet`:

batadv_iv_ogm_aggr_packet
=========================

.. c:function:: bool batadv_iv_ogm_aggr_packet(int buff_pos, int packet_len, __be16 tvlv_len)

    checks if there is another OGM attached

    :param int buff_pos:
        current position in the skb

    :param int packet_len:
        total length of the skb

    :param __be16 tvlv_len:
        tvlv length of the previously considered OGM

.. _`batadv_iv_ogm_aggr_packet.return`:

Return
------

true if there is enough space for another OGM, false otherwise.

.. _`batadv_iv_ogm_can_aggregate`:

batadv_iv_ogm_can_aggregate
===========================

.. c:function:: bool batadv_iv_ogm_can_aggregate(const struct batadv_ogm_packet *new_bat_ogm_packet, struct batadv_priv *bat_priv, int packet_len, unsigned long send_time, bool directlink, const struct batadv_hard_iface *if_incoming, const struct batadv_hard_iface *if_outgoing, const struct batadv_forw_packet *forw_packet)

    find out if an OGM can be aggregated on an existing forward packet

    :param const struct batadv_ogm_packet \*new_bat_ogm_packet:
        OGM packet to be aggregated

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param int packet_len:
        (total) length of the OGM

    :param unsigned long send_time:
        timestamp (jiffies) when the packet is to be sent

    :param bool directlink:
        true if this is a direct link packet

    :param const struct batadv_hard_iface \*if_incoming:
        interface where the packet was received

    :param const struct batadv_hard_iface \*if_outgoing:
        interface for which the retransmission should be considered

    :param const struct batadv_forw_packet \*forw_packet:
        the forwarded packet which should be checked

.. _`batadv_iv_ogm_can_aggregate.return`:

Return
------

true if new_packet can be aggregated with forw_packet

.. _`batadv_iv_ogm_aggregate_new`:

batadv_iv_ogm_aggregate_new
===========================

.. c:function:: void batadv_iv_ogm_aggregate_new(const unsigned char *packet_buff, int packet_len, unsigned long send_time, bool direct_link, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, int own_packet)

    create a new aggregated packet and add this packet to it.

    :param const unsigned char \*packet_buff:
        pointer to the OGM

    :param int packet_len:
        (total) length of the OGM

    :param unsigned long send_time:
        timestamp (jiffies) when the packet is to be sent

    :param bool direct_link:
        whether this OGM has direct link status

    :param struct batadv_hard_iface \*if_incoming:
        interface where the packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        interface for which the retransmission should be considered

    :param int own_packet:
        true if it is a self-generated ogm

.. _`batadv_iv_ogm_queue_add`:

batadv_iv_ogm_queue_add
=======================

.. c:function:: void batadv_iv_ogm_queue_add(struct batadv_priv *bat_priv, unsigned char *packet_buff, int packet_len, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, int own_packet, unsigned long send_time)

    queue up an OGM for transmission

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned char \*packet_buff:
        pointer to the OGM

    :param int packet_len:
        (total) length of the OGM

    :param struct batadv_hard_iface \*if_incoming:
        interface where the packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        interface for which the retransmission should be considered

    :param int own_packet:
        true if it is a self-generated ogm

    :param unsigned long send_time:
        timestamp (jiffies) when the packet is to be sent

.. _`batadv_iv_ogm_slide_own_bcast_window`:

batadv_iv_ogm_slide_own_bcast_window
====================================

.. c:function:: void batadv_iv_ogm_slide_own_bcast_window(struct batadv_hard_iface *hard_iface)

    bitshift own OGM broadcast windows for the given interface

    :param struct batadv_hard_iface \*hard_iface:
        the interface for which the windows have to be shifted

.. _`batadv_iv_ogm_orig_update`:

batadv_iv_ogm_orig_update
=========================

.. c:function:: void batadv_iv_ogm_orig_update(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_orig_ifinfo *orig_ifinfo, const struct ethhdr *ethhdr, const struct batadv_ogm_packet *batadv_ogm_packet, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, enum batadv_dup_status dup_status)

    use OGM to update corresponding data in an originator

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        the orig node who originally emitted the ogm packet

    :param struct batadv_orig_ifinfo \*orig_ifinfo:
        ifinfo for the outgoing interface of the orig_node

    :param const struct ethhdr \*ethhdr:
        Ethernet header of the OGM

    :param const struct batadv_ogm_packet \*batadv_ogm_packet:
        the ogm packet

    :param struct batadv_hard_iface \*if_incoming:
        interface where the packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        interface for which the retransmission should be considered

    :param enum batadv_dup_status dup_status:
        the duplicate status of this ogm packet.

.. _`batadv_iv_ogm_calc_tq`:

batadv_iv_ogm_calc_tq
=====================

.. c:function:: bool batadv_iv_ogm_calc_tq(struct batadv_orig_node *orig_node, struct batadv_orig_node *orig_neigh_node, struct batadv_ogm_packet *batadv_ogm_packet, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    calculate tq for current received ogm packet

    :param struct batadv_orig_node \*orig_node:
        the orig node who originally emitted the ogm packet

    :param struct batadv_orig_node \*orig_neigh_node:
        the orig node struct of the neighbor who sent the packet

    :param struct batadv_ogm_packet \*batadv_ogm_packet:
        the ogm packet

    :param struct batadv_hard_iface \*if_incoming:
        interface where the packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        interface for which the retransmission should be considered

.. _`batadv_iv_ogm_calc_tq.return`:

Return
------

true if the link can be considered bidirectional, false otherwise

.. _`batadv_iv_ogm_update_seqnos`:

batadv_iv_ogm_update_seqnos
===========================

.. c:function:: enum batadv_dup_status batadv_iv_ogm_update_seqnos(const struct ethhdr *ethhdr, const struct batadv_ogm_packet *batadv_ogm_packet, const struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    process a batman packet for all interfaces, adjust the sequence number and find out whether it is a duplicate

    :param const struct ethhdr \*ethhdr:
        ethernet header of the packet

    :param const struct batadv_ogm_packet \*batadv_ogm_packet:
        OGM packet to be considered

    :param const struct batadv_hard_iface \*if_incoming:
        interface on which the OGM packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        interface for which the retransmission should be considered

.. _`batadv_iv_ogm_update_seqnos.return`:

Return
------

duplicate status as enum batadv_dup_status

.. _`batadv_iv_ogm_process_per_outif`:

batadv_iv_ogm_process_per_outif
===============================

.. c:function:: void batadv_iv_ogm_process_per_outif(const struct sk_buff *skb, int ogm_offset, struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    process a batman iv OGM for an outgoing interface

    :param const struct sk_buff \*skb:
        the skb containing the OGM

    :param int ogm_offset:
        offset from skb->data to start of ogm header

    :param struct batadv_orig_node \*orig_node:
        the (cached) orig node for the originator of this OGM

    :param struct batadv_hard_iface \*if_incoming:
        the interface where this packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        the interface for which the packet should be considered

.. _`batadv_iv_ogm_process`:

batadv_iv_ogm_process
=====================

.. c:function:: void batadv_iv_ogm_process(const struct sk_buff *skb, int ogm_offset, struct batadv_hard_iface *if_incoming)

    process an incoming batman iv OGM

    :param const struct sk_buff \*skb:
        the skb containing the OGM

    :param int ogm_offset:
        offset to the OGM which should be processed (for aggregates)

    :param struct batadv_hard_iface \*if_incoming:
        the interface where this packet was receved

.. _`batadv_iv_ogm_orig_print_neigh`:

batadv_iv_ogm_orig_print_neigh
==============================

.. c:function:: void batadv_iv_ogm_orig_print_neigh(struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing, struct seq_file *seq)

    print neighbors for the originator table

    :param struct batadv_orig_node \*orig_node:
        the orig_node for which the neighbors are printed

    :param struct batadv_hard_iface \*if_outgoing:
        outgoing interface for these entries

    :param struct seq_file \*seq:
        debugfs table seq_file struct

.. _`batadv_iv_ogm_orig_print_neigh.description`:

Description
-----------

Must be called while holding an rcu lock.

.. _`batadv_iv_ogm_orig_print`:

batadv_iv_ogm_orig_print
========================

.. c:function:: void batadv_iv_ogm_orig_print(struct batadv_priv *bat_priv, struct seq_file *seq, struct batadv_hard_iface *if_outgoing)

    print the originator table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct seq_file \*seq:
        debugfs table seq_file struct

    :param struct batadv_hard_iface \*if_outgoing:
        the outgoing interface for which this should be printed

.. _`batadv_iv_ogm_neigh_get_tq_avg`:

batadv_iv_ogm_neigh_get_tq_avg
==============================

.. c:function:: bool batadv_iv_ogm_neigh_get_tq_avg(struct batadv_neigh_node *neigh_node, struct batadv_hard_iface *if_outgoing, u8 *tq_avg)

    Get the TQ average for a neighbour on a given outgoing interface.

    :param struct batadv_neigh_node \*neigh_node:
        Neighbour of interest

    :param struct batadv_hard_iface \*if_outgoing:
        Outgoing interface of interest

    :param u8 \*tq_avg:
        Pointer of where to store the TQ average

.. _`batadv_iv_ogm_neigh_get_tq_avg.return`:

Return
------

False if no average TQ available, otherwise true.

.. _`batadv_iv_ogm_orig_dump_subentry`:

batadv_iv_ogm_orig_dump_subentry
================================

.. c:function:: int batadv_iv_ogm_orig_dump_subentry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node, bool best)

    Dump an originator subentry into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param u32 portid:
        Port making netlink request

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

    :param struct batadv_hard_iface \*if_outgoing:
        Limit dump to entries with this outgoing interface

    :param struct batadv_orig_node \*orig_node:
        Originator to dump

    :param struct batadv_neigh_node \*neigh_node:
        Single hops neighbour

    :param bool best:
        Is the best originator

.. _`batadv_iv_ogm_orig_dump_subentry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_orig_dump_entry`:

batadv_iv_ogm_orig_dump_entry
=============================

.. c:function:: int batadv_iv_ogm_orig_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct batadv_orig_node *orig_node, int *sub_s)

    Dump an originator entry into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param u32 portid:
        Port making netlink request

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

    :param struct batadv_hard_iface \*if_outgoing:
        Limit dump to entries with this outgoing interface

    :param struct batadv_orig_node \*orig_node:
        Originator to dump

    :param int \*sub_s:
        Number of sub entries to skip

.. _`batadv_iv_ogm_orig_dump_entry.description`:

Description
-----------

This function assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`batadv_iv_ogm_orig_dump_entry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_orig_dump_bucket`:

batadv_iv_ogm_orig_dump_bucket
==============================

.. c:function:: int batadv_iv_ogm_orig_dump_bucket(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct hlist_head *head, int *idx_s, int *sub)

    Dump an originator bucket into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param u32 portid:
        Port making netlink request

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

    :param struct batadv_hard_iface \*if_outgoing:
        Limit dump to entries with this outgoing interface

    :param struct hlist_head \*head:
        Bucket to be dumped

    :param int \*idx_s:
        Number of entries to be skipped

    :param int \*sub:
        Number of sub entries to be skipped

.. _`batadv_iv_ogm_orig_dump_bucket.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_orig_dump`:

batadv_iv_ogm_orig_dump
=======================

.. c:function:: void batadv_iv_ogm_orig_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing)

    Dump the originators into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param struct netlink_callback \*cb:
        Control block containing additional options

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

    :param struct batadv_hard_iface \*if_outgoing:
        Limit dump to entries with this outgoing interface

.. _`batadv_iv_hardif_neigh_print`:

batadv_iv_hardif_neigh_print
============================

.. c:function:: void batadv_iv_hardif_neigh_print(struct seq_file *seq, struct batadv_hardif_neigh_node *hardif_neigh)

    print a single hop neighbour node

    :param struct seq_file \*seq:
        neighbour table seq_file struct

    :param struct batadv_hardif_neigh_node \*hardif_neigh:
        hardif neighbour information

.. _`batadv_iv_neigh_print`:

batadv_iv_neigh_print
=====================

.. c:function:: void batadv_iv_neigh_print(struct batadv_priv *bat_priv, struct seq_file *seq)

    print the single hop neighbour list

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct seq_file \*seq:
        neighbour table seq_file struct

.. _`batadv_iv_ogm_neigh_diff`:

batadv_iv_ogm_neigh_diff
========================

.. c:function:: bool batadv_iv_ogm_neigh_diff(struct batadv_neigh_node *neigh1, struct batadv_hard_iface *if_outgoing1, struct batadv_neigh_node *neigh2, struct batadv_hard_iface *if_outgoing2, int *diff)

    calculate tq difference of two neighbors

    :param struct batadv_neigh_node \*neigh1:
        the first neighbor object of the comparison

    :param struct batadv_hard_iface \*if_outgoing1:
        outgoing interface for the first neighbor

    :param struct batadv_neigh_node \*neigh2:
        the second neighbor object of the comparison

    :param struct batadv_hard_iface \*if_outgoing2:
        outgoing interface for the second neighbor

    :param int \*diff:
        pointer to integer receiving the calculated difference

.. _`batadv_iv_ogm_neigh_diff.description`:

Description
-----------

The content of \*@diff is only valid when this function returns true.
It is less, equal to or greater than 0 if the metric via neigh1 is lower,
the same as or higher than the metric via neigh2

.. _`batadv_iv_ogm_neigh_diff.return`:

Return
------

true when the difference could be calculated, false otherwise

.. _`batadv_iv_ogm_neigh_dump_neigh`:

batadv_iv_ogm_neigh_dump_neigh
==============================

.. c:function:: int batadv_iv_ogm_neigh_dump_neigh(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hardif_neigh_node *hardif_neigh)

    Dump a neighbour into a netlink message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param u32 portid:
        Port making netlink request

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_hardif_neigh_node \*hardif_neigh:
        Neighbour to be dumped

.. _`batadv_iv_ogm_neigh_dump_neigh.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_neigh_dump_hardif`:

batadv_iv_ogm_neigh_dump_hardif
===============================

.. c:function:: int batadv_iv_ogm_neigh_dump_hardif(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *hard_iface, int *idx_s)

    Dump the neighbours of a hard interface into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param u32 portid:
        Port making netlink request

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

    :param struct batadv_hard_iface \*hard_iface:
        Hard interface to dump the neighbours for

    :param int \*idx_s:
        Number of entries to skip

.. _`batadv_iv_ogm_neigh_dump_hardif.description`:

Description
-----------

This function assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`batadv_iv_ogm_neigh_dump_hardif.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_neigh_dump`:

batadv_iv_ogm_neigh_dump
========================

.. c:function:: void batadv_iv_ogm_neigh_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv, struct batadv_hard_iface *single_hardif)

    Dump the neighbours into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param struct netlink_callback \*cb:
        Control block containing additional options

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

    :param struct batadv_hard_iface \*single_hardif:
        Limit dump to this hard interfaace

.. _`batadv_iv_ogm_neigh_cmp`:

batadv_iv_ogm_neigh_cmp
=======================

.. c:function:: int batadv_iv_ogm_neigh_cmp(struct batadv_neigh_node *neigh1, struct batadv_hard_iface *if_outgoing1, struct batadv_neigh_node *neigh2, struct batadv_hard_iface *if_outgoing2)

    compare the metrics of two neighbors

    :param struct batadv_neigh_node \*neigh1:
        the first neighbor object of the comparison

    :param struct batadv_hard_iface \*if_outgoing1:
        outgoing interface for the first neighbor

    :param struct batadv_neigh_node \*neigh2:
        the second neighbor object of the comparison

    :param struct batadv_hard_iface \*if_outgoing2:
        outgoing interface for the second neighbor

.. _`batadv_iv_ogm_neigh_cmp.return`:

Return
------

a value less, equal to or greater than 0 if the metric via neigh1 is
lower, the same as or higher than the metric via neigh2

.. _`batadv_iv_ogm_neigh_is_sob`:

batadv_iv_ogm_neigh_is_sob
==========================

.. c:function:: bool batadv_iv_ogm_neigh_is_sob(struct batadv_neigh_node *neigh1, struct batadv_hard_iface *if_outgoing1, struct batadv_neigh_node *neigh2, struct batadv_hard_iface *if_outgoing2)

    check if neigh1 is similarly good or better than neigh2 from the metric prospective

    :param struct batadv_neigh_node \*neigh1:
        the first neighbor object of the comparison

    :param struct batadv_hard_iface \*if_outgoing1:
        outgoing interface for the first neighbor

    :param struct batadv_neigh_node \*neigh2:
        the second neighbor object of the comparison

    :param struct batadv_hard_iface \*if_outgoing2:
        outgoing interface for the second neighbor

.. _`batadv_iv_ogm_neigh_is_sob.return`:

Return
------

true if the metric via neigh1 is equally good or better than
the metric via neigh2, false otherwise.

.. _`batadv_iv_init_sel_class`:

batadv_iv_init_sel_class
========================

.. c:function:: void batadv_iv_init_sel_class(struct batadv_priv *bat_priv)

    initialize GW selection class

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_iv_gw_dump_entry`:

batadv_iv_gw_dump_entry
=======================

.. c:function:: int batadv_iv_gw_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_gw_node *gw_node)

    Dump a gateway into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param u32 portid:
        Port making netlink request

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

    :param struct batadv_gw_node \*gw_node:
        Gateway to be dumped

.. _`batadv_iv_gw_dump_entry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_gw_dump`:

batadv_iv_gw_dump
=================

.. c:function:: void batadv_iv_gw_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv)

    Dump gateways into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param struct netlink_callback \*cb:
        Control block containing additional options

    :param struct batadv_priv \*bat_priv:
        The bat priv with all the soft interface information

.. _`batadv_iv_init`:

batadv_iv_init
==============

.. c:function:: int batadv_iv_init( void)

    B.A.T.M.A.N. IV initialization function

    :param  void:
        no arguments

.. _`batadv_iv_init.return`:

Return
------

0 on success or negative error number in case of failure

.. This file was automatic generated / don't edit.

