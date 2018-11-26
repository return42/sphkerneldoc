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

    :param lq_recv:
        pointer to the ring buffer
    :type lq_recv: u8

    :param lq_index:
        index to store the value at
    :type lq_index: u8 \*

    :param value:
        value to store in the ring buffer
    :type value: u8

.. _`batadv_ring_buffer_avg`:

batadv_ring_buffer_avg
======================

.. c:function:: u8 batadv_ring_buffer_avg(const u8 lq_recv)

    compute the average of all non-zero values stored in the given ring buffer

    :param lq_recv:
        pointer to the ring buffer
    :type lq_recv: const u8

.. _`batadv_ring_buffer_avg.return`:

Return
------

computed average value.

.. _`batadv_iv_ogm_orig_get`:

batadv_iv_ogm_orig_get
======================

.. c:function:: struct batadv_orig_node *batadv_iv_ogm_orig_get(struct batadv_priv *bat_priv, const u8 *addr)

    retrieve or create (if does not exist) an originator

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        mac address of the originator
    :type addr: const u8 \*

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

    :param buff_pos:
        current position in the skb
    :type buff_pos: int

    :param packet_len:
        total length of the skb
    :type packet_len: int

    :param tvlv_len:
        tvlv length of the previously considered OGM
    :type tvlv_len: __be16

.. _`batadv_iv_ogm_aggr_packet.return`:

Return
------

true if there is enough space for another OGM, false otherwise.

.. _`batadv_iv_ogm_can_aggregate`:

batadv_iv_ogm_can_aggregate
===========================

.. c:function:: bool batadv_iv_ogm_can_aggregate(const struct batadv_ogm_packet *new_bat_ogm_packet, struct batadv_priv *bat_priv, int packet_len, unsigned long send_time, bool directlink, const struct batadv_hard_iface *if_incoming, const struct batadv_hard_iface *if_outgoing, const struct batadv_forw_packet *forw_packet)

    find out if an OGM can be aggregated on an existing forward packet

    :param new_bat_ogm_packet:
        OGM packet to be aggregated
    :type new_bat_ogm_packet: const struct batadv_ogm_packet \*

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param packet_len:
        (total) length of the OGM
    :type packet_len: int

    :param send_time:
        timestamp (jiffies) when the packet is to be sent
    :type send_time: unsigned long

    :param directlink:
        true if this is a direct link packet
    :type directlink: bool

    :param if_incoming:
        interface where the packet was received
    :type if_incoming: const struct batadv_hard_iface \*

    :param if_outgoing:
        interface for which the retransmission should be considered
    :type if_outgoing: const struct batadv_hard_iface \*

    :param forw_packet:
        the forwarded packet which should be checked
    :type forw_packet: const struct batadv_forw_packet \*

.. _`batadv_iv_ogm_can_aggregate.return`:

Return
------

true if new_packet can be aggregated with forw_packet

.. _`batadv_iv_ogm_aggregate_new`:

batadv_iv_ogm_aggregate_new
===========================

.. c:function:: void batadv_iv_ogm_aggregate_new(const unsigned char *packet_buff, int packet_len, unsigned long send_time, bool direct_link, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, int own_packet)

    create a new aggregated packet and add this packet to it.

    :param packet_buff:
        pointer to the OGM
    :type packet_buff: const unsigned char \*

    :param packet_len:
        (total) length of the OGM
    :type packet_len: int

    :param send_time:
        timestamp (jiffies) when the packet is to be sent
    :type send_time: unsigned long

    :param direct_link:
        whether this OGM has direct link status
    :type direct_link: bool

    :param if_incoming:
        interface where the packet was received
    :type if_incoming: struct batadv_hard_iface \*

    :param if_outgoing:
        interface for which the retransmission should be considered
    :type if_outgoing: struct batadv_hard_iface \*

    :param own_packet:
        true if it is a self-generated ogm
    :type own_packet: int

.. _`batadv_iv_ogm_queue_add`:

batadv_iv_ogm_queue_add
=======================

.. c:function:: void batadv_iv_ogm_queue_add(struct batadv_priv *bat_priv, unsigned char *packet_buff, int packet_len, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, int own_packet, unsigned long send_time)

    queue up an OGM for transmission

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param packet_buff:
        pointer to the OGM
    :type packet_buff: unsigned char \*

    :param packet_len:
        (total) length of the OGM
    :type packet_len: int

    :param if_incoming:
        interface where the packet was received
    :type if_incoming: struct batadv_hard_iface \*

    :param if_outgoing:
        interface for which the retransmission should be considered
    :type if_outgoing: struct batadv_hard_iface \*

    :param own_packet:
        true if it is a self-generated ogm
    :type own_packet: int

    :param send_time:
        timestamp (jiffies) when the packet is to be sent
    :type send_time: unsigned long

.. _`batadv_iv_ogm_slide_own_bcast_window`:

batadv_iv_ogm_slide_own_bcast_window
====================================

.. c:function:: void batadv_iv_ogm_slide_own_bcast_window(struct batadv_hard_iface *hard_iface)

    bitshift own OGM broadcast windows for the given interface

    :param hard_iface:
        the interface for which the windows have to be shifted
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_iv_orig_ifinfo_sum`:

batadv_iv_orig_ifinfo_sum
=========================

.. c:function:: u8 batadv_iv_orig_ifinfo_sum(struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing)

    Get bcast_own sum for originator over iterface

    :param orig_node:
        originator which reproadcasted the OGMs directly
    :type orig_node: struct batadv_orig_node \*

    :param if_outgoing:
        interface which transmitted the original OGM and received the
        direct rebroadcast
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_iv_orig_ifinfo_sum.return`:

Return
------

Number of replied (rebroadcasted) OGMs which were transmitted by
an originator and directly (without intermediate hop) received by a specific
interface

.. _`batadv_iv_ogm_orig_update`:

batadv_iv_ogm_orig_update
=========================

.. c:function:: void batadv_iv_ogm_orig_update(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_orig_ifinfo *orig_ifinfo, const struct ethhdr *ethhdr, const struct batadv_ogm_packet *batadv_ogm_packet, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, enum batadv_dup_status dup_status)

    use OGM to update corresponding data in an originator

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        the orig node who originally emitted the ogm packet
    :type orig_node: struct batadv_orig_node \*

    :param orig_ifinfo:
        ifinfo for the outgoing interface of the orig_node
    :type orig_ifinfo: struct batadv_orig_ifinfo \*

    :param ethhdr:
        Ethernet header of the OGM
    :type ethhdr: const struct ethhdr \*

    :param batadv_ogm_packet:
        the ogm packet
    :type batadv_ogm_packet: const struct batadv_ogm_packet \*

    :param if_incoming:
        interface where the packet was received
    :type if_incoming: struct batadv_hard_iface \*

    :param if_outgoing:
        interface for which the retransmission should be considered
    :type if_outgoing: struct batadv_hard_iface \*

    :param dup_status:
        the duplicate status of this ogm packet.
    :type dup_status: enum batadv_dup_status

.. _`batadv_iv_ogm_calc_tq`:

batadv_iv_ogm_calc_tq
=====================

.. c:function:: bool batadv_iv_ogm_calc_tq(struct batadv_orig_node *orig_node, struct batadv_orig_node *orig_neigh_node, struct batadv_ogm_packet *batadv_ogm_packet, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    calculate tq for current received ogm packet

    :param orig_node:
        the orig node who originally emitted the ogm packet
    :type orig_node: struct batadv_orig_node \*

    :param orig_neigh_node:
        the orig node struct of the neighbor who sent the packet
    :type orig_neigh_node: struct batadv_orig_node \*

    :param batadv_ogm_packet:
        the ogm packet
    :type batadv_ogm_packet: struct batadv_ogm_packet \*

    :param if_incoming:
        interface where the packet was received
    :type if_incoming: struct batadv_hard_iface \*

    :param if_outgoing:
        interface for which the retransmission should be considered
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_iv_ogm_calc_tq.return`:

Return
------

true if the link can be considered bidirectional, false otherwise

.. _`batadv_iv_ogm_update_seqnos`:

batadv_iv_ogm_update_seqnos
===========================

.. c:function:: enum batadv_dup_status batadv_iv_ogm_update_seqnos(const struct ethhdr *ethhdr, const struct batadv_ogm_packet *batadv_ogm_packet, const struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    process a batman packet for all interfaces, adjust the sequence number and find out whether it is a duplicate

    :param ethhdr:
        ethernet header of the packet
    :type ethhdr: const struct ethhdr \*

    :param batadv_ogm_packet:
        OGM packet to be considered
    :type batadv_ogm_packet: const struct batadv_ogm_packet \*

    :param if_incoming:
        interface on which the OGM packet was received
    :type if_incoming: const struct batadv_hard_iface \*

    :param if_outgoing:
        interface for which the retransmission should be considered
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_iv_ogm_update_seqnos.return`:

Return
------

duplicate status as enum batadv_dup_status

.. _`batadv_iv_ogm_process_per_outif`:

batadv_iv_ogm_process_per_outif
===============================

.. c:function:: void batadv_iv_ogm_process_per_outif(const struct sk_buff *skb, int ogm_offset, struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    process a batman iv OGM for an outgoing interface

    :param skb:
        the skb containing the OGM
    :type skb: const struct sk_buff \*

    :param ogm_offset:
        offset from skb->data to start of ogm header
    :type ogm_offset: int

    :param orig_node:
        the (cached) orig node for the originator of this OGM
    :type orig_node: struct batadv_orig_node \*

    :param if_incoming:
        the interface where this packet was received
    :type if_incoming: struct batadv_hard_iface \*

    :param if_outgoing:
        the interface for which the packet should be considered
    :type if_outgoing: struct batadv_hard_iface \*

.. _`batadv_iv_ogm_process_reply`:

batadv_iv_ogm_process_reply
===========================

.. c:function:: void batadv_iv_ogm_process_reply(struct batadv_ogm_packet *ogm_packet, struct batadv_hard_iface *if_incoming, struct batadv_orig_node *orig_node, u32 if_incoming_seqno)

    Check OGM for direct reply and process it

    :param ogm_packet:
        rebroadcast OGM packet to process
    :type ogm_packet: struct batadv_ogm_packet \*

    :param if_incoming:
        the interface where this packet was received
    :type if_incoming: struct batadv_hard_iface \*

    :param orig_node:
        originator which reproadcasted the OGMs
    :type orig_node: struct batadv_orig_node \*

    :param if_incoming_seqno:
        OGM sequence number when rebroadcast was received
    :type if_incoming_seqno: u32

.. _`batadv_iv_ogm_process`:

batadv_iv_ogm_process
=====================

.. c:function:: void batadv_iv_ogm_process(const struct sk_buff *skb, int ogm_offset, struct batadv_hard_iface *if_incoming)

    process an incoming batman iv OGM

    :param skb:
        the skb containing the OGM
    :type skb: const struct sk_buff \*

    :param ogm_offset:
        offset to the OGM which should be processed (for aggregates)
    :type ogm_offset: int

    :param if_incoming:
        the interface where this packet was receved
    :type if_incoming: struct batadv_hard_iface \*

.. _`batadv_iv_ogm_orig_print_neigh`:

batadv_iv_ogm_orig_print_neigh
==============================

.. c:function:: void batadv_iv_ogm_orig_print_neigh(struct batadv_orig_node *orig_node, struct batadv_hard_iface *if_outgoing, struct seq_file *seq)

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

.. _`batadv_iv_ogm_orig_print_neigh.description`:

Description
-----------

Must be called while holding an rcu lock.

.. _`batadv_iv_ogm_orig_print`:

batadv_iv_ogm_orig_print
========================

.. c:function:: void batadv_iv_ogm_orig_print(struct batadv_priv *bat_priv, struct seq_file *seq, struct batadv_hard_iface *if_outgoing)

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

.. _`batadv_iv_ogm_neigh_get_tq_avg`:

batadv_iv_ogm_neigh_get_tq_avg
==============================

.. c:function:: bool batadv_iv_ogm_neigh_get_tq_avg(struct batadv_neigh_node *neigh_node, struct batadv_hard_iface *if_outgoing, u8 *tq_avg)

    Get the TQ average for a neighbour on a given outgoing interface.

    :param neigh_node:
        Neighbour of interest
    :type neigh_node: struct batadv_neigh_node \*

    :param if_outgoing:
        Outgoing interface of interest
    :type if_outgoing: struct batadv_hard_iface \*

    :param tq_avg:
        Pointer of where to store the TQ average
    :type tq_avg: u8 \*

.. _`batadv_iv_ogm_neigh_get_tq_avg.return`:

Return
------

False if no average TQ available, otherwise true.

.. _`batadv_iv_ogm_orig_dump_subentry`:

batadv_iv_ogm_orig_dump_subentry
================================

.. c:function:: int batadv_iv_ogm_orig_dump_subentry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node, bool best)

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

.. _`batadv_iv_ogm_orig_dump_subentry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_orig_dump_entry`:

batadv_iv_ogm_orig_dump_entry
=============================

.. c:function:: int batadv_iv_ogm_orig_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing, struct batadv_orig_node *orig_node, int *sub_s)

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

.. _`batadv_iv_ogm_orig_dump_bucket.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_orig_dump`:

batadv_iv_ogm_orig_dump
=======================

.. c:function:: void batadv_iv_ogm_orig_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv, struct batadv_hard_iface *if_outgoing)

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

.. _`batadv_iv_hardif_neigh_print`:

batadv_iv_hardif_neigh_print
============================

.. c:function:: void batadv_iv_hardif_neigh_print(struct seq_file *seq, struct batadv_hardif_neigh_node *hardif_neigh)

    print a single hop neighbour node

    :param seq:
        neighbour table seq_file struct
    :type seq: struct seq_file \*

    :param hardif_neigh:
        hardif neighbour information
    :type hardif_neigh: struct batadv_hardif_neigh_node \*

.. _`batadv_iv_neigh_print`:

batadv_iv_neigh_print
=====================

.. c:function:: void batadv_iv_neigh_print(struct batadv_priv *bat_priv, struct seq_file *seq)

    print the single hop neighbour list

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param seq:
        neighbour table seq_file struct
    :type seq: struct seq_file \*

.. _`batadv_iv_ogm_neigh_diff`:

batadv_iv_ogm_neigh_diff
========================

.. c:function:: bool batadv_iv_ogm_neigh_diff(struct batadv_neigh_node *neigh1, struct batadv_hard_iface *if_outgoing1, struct batadv_neigh_node *neigh2, struct batadv_hard_iface *if_outgoing2, int *diff)

    calculate tq difference of two neighbors

    :param neigh1:
        the first neighbor object of the comparison
    :type neigh1: struct batadv_neigh_node \*

    :param if_outgoing1:
        outgoing interface for the first neighbor
    :type if_outgoing1: struct batadv_hard_iface \*

    :param neigh2:
        the second neighbor object of the comparison
    :type neigh2: struct batadv_neigh_node \*

    :param if_outgoing2:
        outgoing interface for the second neighbor
    :type if_outgoing2: struct batadv_hard_iface \*

    :param diff:
        pointer to integer receiving the calculated difference
    :type diff: int \*

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
        Neighbour to be dumped
    :type hardif_neigh: struct batadv_hardif_neigh_node \*

.. _`batadv_iv_ogm_neigh_dump_neigh.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_ogm_neigh_dump_hardif`:

batadv_iv_ogm_neigh_dump_hardif
===============================

.. c:function:: int batadv_iv_ogm_neigh_dump_hardif(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_hard_iface *hard_iface, int *idx_s)

    Dump the neighbours of a hard interface into a message

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
        Hard interface to dump the neighbours for
    :type hard_iface: struct batadv_hard_iface \*

    :param idx_s:
        Number of entries to skip
    :type idx_s: int \*

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
        Limit dump to this hard interfaace
    :type single_hardif: struct batadv_hard_iface \*

.. _`batadv_iv_ogm_neigh_cmp`:

batadv_iv_ogm_neigh_cmp
=======================

.. c:function:: int batadv_iv_ogm_neigh_cmp(struct batadv_neigh_node *neigh1, struct batadv_hard_iface *if_outgoing1, struct batadv_neigh_node *neigh2, struct batadv_hard_iface *if_outgoing2)

    compare the metrics of two neighbors

    :param neigh1:
        the first neighbor object of the comparison
    :type neigh1: struct batadv_neigh_node \*

    :param if_outgoing1:
        outgoing interface for the first neighbor
    :type if_outgoing1: struct batadv_hard_iface \*

    :param neigh2:
        the second neighbor object of the comparison
    :type neigh2: struct batadv_neigh_node \*

    :param if_outgoing2:
        outgoing interface for the second neighbor
    :type if_outgoing2: struct batadv_hard_iface \*

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

    :param neigh1:
        the first neighbor object of the comparison
    :type neigh1: struct batadv_neigh_node \*

    :param if_outgoing1:
        outgoing interface for the first neighbor
    :type if_outgoing1: struct batadv_hard_iface \*

    :param neigh2:
        the second neighbor object of the comparison
    :type neigh2: struct batadv_neigh_node \*

    :param if_outgoing2:
        outgoing interface for the second neighbor
    :type if_outgoing2: struct batadv_hard_iface \*

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

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_iv_gw_dump_entry`:

batadv_iv_gw_dump_entry
=======================

.. c:function:: int batadv_iv_gw_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_gw_node *gw_node)

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

.. _`batadv_iv_gw_dump_entry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_iv_gw_dump`:

batadv_iv_gw_dump
=================

.. c:function:: void batadv_iv_gw_dump(struct sk_buff *msg, struct netlink_callback *cb, struct batadv_priv *bat_priv)

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

.. _`batadv_iv_init`:

batadv_iv_init
==============

.. c:function:: int batadv_iv_init( void)

    B.A.T.M.A.N. IV initialization function

    :param void:
        no arguments
    :type void: 

.. _`batadv_iv_init.return`:

Return
------

0 on success or negative error number in case of failure

.. This file was automatic generated / don't edit.

