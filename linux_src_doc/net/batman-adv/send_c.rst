.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/send.c

.. _`batadv_send_skb_packet`:

batadv_send_skb_packet
======================

.. c:function:: int batadv_send_skb_packet(struct sk_buff *skb, struct batadv_hard_iface *hard_iface, const u8 *dst_addr)

    send an already prepared packet

    :param skb:
        the packet to send
    :type skb: struct sk_buff \*

    :param hard_iface:
        the interface to use to send the broadcast packet
    :type hard_iface: struct batadv_hard_iface \*

    :param dst_addr:
        the payload destination
    :type dst_addr: const u8 \*

.. _`batadv_send_skb_packet.description`:

Description
-----------

Send out an already prepared packet to the given neighbor or broadcast it
using the specified interface. Either hard_iface or neigh_node must be not
NULL.
If neigh_node is NULL, then the packet is broadcasted using hard_iface,
otherwise it is sent as unicast to the given neighbor.

Regardless of the return value, the skb is consumed.

.. _`batadv_send_skb_packet.return`:

Return
------

A negative errno code is returned on a failure. A success does not
guarantee the frame will be transmitted as it may be dropped due
to congestion or traffic shaping.

.. _`batadv_send_broadcast_skb`:

batadv_send_broadcast_skb
=========================

.. c:function:: int batadv_send_broadcast_skb(struct sk_buff *skb, struct batadv_hard_iface *hard_iface)

    Send broadcast packet via hard interface

    :param skb:
        packet to be transmitted (with batadv header and no outer eth header)
    :type skb: struct sk_buff \*

    :param hard_iface:
        outgoing interface
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_send_broadcast_skb.return`:

Return
------

A negative errno code is returned on a failure. A success does not
guarantee the frame will be transmitted as it may be dropped due
to congestion or traffic shaping.

.. _`batadv_send_unicast_skb`:

batadv_send_unicast_skb
=======================

.. c:function:: int batadv_send_unicast_skb(struct sk_buff *skb, struct batadv_neigh_node *neigh)

    Send unicast packet to neighbor

    :param skb:
        packet to be transmitted (with batadv header and no outer eth header)
    :type skb: struct sk_buff \*

    :param neigh:
        neighbor which is used as next hop to destination
    :type neigh: struct batadv_neigh_node \*

.. _`batadv_send_unicast_skb.return`:

Return
------

A negative errno code is returned on a failure. A success does not
guarantee the frame will be transmitted as it may be dropped due
to congestion or traffic shaping.

.. _`batadv_send_skb_to_orig`:

batadv_send_skb_to_orig
=======================

.. c:function:: int batadv_send_skb_to_orig(struct sk_buff *skb, struct batadv_orig_node *orig_node, struct batadv_hard_iface *recv_if)

    Lookup next-hop and transmit skb.

    :param skb:
        Packet to be transmitted.
    :type skb: struct sk_buff \*

    :param orig_node:
        Final destination of the packet.
    :type orig_node: struct batadv_orig_node \*

    :param recv_if:
        Interface used when receiving the packet (can be NULL).
    :type recv_if: struct batadv_hard_iface \*

.. _`batadv_send_skb_to_orig.description`:

Description
-----------

Looks up the best next-hop towards the passed originator and passes the
skb on for preparation of MAC header. If the packet originated from this
host, NULL can be passed as recv_if and no interface alternating is
attempted.

.. _`batadv_send_skb_to_orig.return`:

Return
------

negative errno code on a failure, -EINPROGRESS if the skb is
buffered for later transmit or the NET_XMIT status returned by the
lower routine if the packet has been passed down.

.. _`batadv_send_skb_push_fill_unicast`:

batadv_send_skb_push_fill_unicast
=================================

.. c:function:: bool batadv_send_skb_push_fill_unicast(struct sk_buff *skb, int hdr_size, struct batadv_orig_node *orig_node)

    extend the buffer and initialize the common fields for unicast packets

    :param skb:
        the skb carrying the unicast header to initialize
    :type skb: struct sk_buff \*

    :param hdr_size:
        amount of bytes to push at the beginning of the skb
    :type hdr_size: int

    :param orig_node:
        the destination node
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_send_skb_push_fill_unicast.return`:

Return
------

false if the buffer extension was not possible or true otherwise.

.. _`batadv_send_skb_prepare_unicast`:

batadv_send_skb_prepare_unicast
===============================

.. c:function:: bool batadv_send_skb_prepare_unicast(struct sk_buff *skb, struct batadv_orig_node *orig_node)

    encapsulate an skb with a unicast header

    :param skb:
        the skb containing the payload to encapsulate
    :type skb: struct sk_buff \*

    :param orig_node:
        the destination node
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_send_skb_prepare_unicast.return`:

Return
------

false if the payload could not be encapsulated or true otherwise.

.. _`batadv_send_skb_prepare_unicast_4addr`:

batadv_send_skb_prepare_unicast_4addr
=====================================

.. c:function:: bool batadv_send_skb_prepare_unicast_4addr(struct batadv_priv *bat_priv, struct sk_buff *skb, struct batadv_orig_node *orig, int packet_subtype)

    encapsulate an skb with a unicast 4addr header

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        the skb containing the payload to encapsulate
    :type skb: struct sk_buff \*

    :param orig:
        the destination node
    :type orig: struct batadv_orig_node \*

    :param packet_subtype:
        the unicast 4addr packet subtype to use
    :type packet_subtype: int

.. _`batadv_send_skb_prepare_unicast_4addr.return`:

Return
------

false if the payload could not be encapsulated or true otherwise.

.. _`batadv_send_skb_unicast`:

batadv_send_skb_unicast
=======================

.. c:function:: int batadv_send_skb_unicast(struct batadv_priv *bat_priv, struct sk_buff *skb, int packet_type, int packet_subtype, struct batadv_orig_node *orig_node, unsigned short vid)

    encapsulate and send an skb via unicast

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        payload to send
    :type skb: struct sk_buff \*

    :param packet_type:
        the batman unicast packet type to use
    :type packet_type: int

    :param packet_subtype:
        the unicast 4addr packet subtype (only relevant for unicast
        4addr packets)
    :type packet_subtype: int

    :param orig_node:
        the originator to send the packet to
    :type orig_node: struct batadv_orig_node \*

    :param vid:
        the vid to be used to search the translation table
    :type vid: unsigned short

.. _`batadv_send_skb_unicast.description`:

Description
-----------

Wrap the given skb into a batman-adv unicast or unicast-4addr header
depending on whether BATADV_UNICAST or BATADV_UNICAST_4ADDR was supplied
as packet_type. Then send this frame to the given orig_node.

.. _`batadv_send_skb_unicast.return`:

Return
------

NET_XMIT_DROP in case of error or NET_XMIT_SUCCESS otherwise.

.. _`batadv_send_skb_via_tt_generic`:

batadv_send_skb_via_tt_generic
==============================

.. c:function:: int batadv_send_skb_via_tt_generic(struct batadv_priv *bat_priv, struct sk_buff *skb, int packet_type, int packet_subtype, u8 *dst_hint, unsigned short vid)

    send an skb via TT lookup

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        payload to send
    :type skb: struct sk_buff \*

    :param packet_type:
        the batman unicast packet type to use
    :type packet_type: int

    :param packet_subtype:
        the unicast 4addr packet subtype (only relevant for unicast
        4addr packets)
    :type packet_subtype: int

    :param dst_hint:
        can be used to override the destination contained in the skb
    :type dst_hint: u8 \*

    :param vid:
        the vid to be used to search the translation table
    :type vid: unsigned short

.. _`batadv_send_skb_via_tt_generic.description`:

Description
-----------

Look up the recipient node for the destination address in the ethernet
header via the translation table. Wrap the given skb into a batman-adv
unicast or unicast-4addr header depending on whether BATADV_UNICAST or
BATADV_UNICAST_4ADDR was supplied as packet_type. Then send this frame
to the according destination node.

.. _`batadv_send_skb_via_tt_generic.return`:

Return
------

NET_XMIT_DROP in case of error or NET_XMIT_SUCCESS otherwise.

.. _`batadv_send_skb_via_gw`:

batadv_send_skb_via_gw
======================

.. c:function:: int batadv_send_skb_via_gw(struct batadv_priv *bat_priv, struct sk_buff *skb, unsigned short vid)

    send an skb via gateway lookup

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        payload to send
    :type skb: struct sk_buff \*

    :param vid:
        the vid to be used to search the translation table
    :type vid: unsigned short

.. _`batadv_send_skb_via_gw.description`:

Description
-----------

Look up the currently selected gateway. Wrap the given skb into a batman-adv
unicast header and send this frame to this gateway node.

.. _`batadv_send_skb_via_gw.return`:

Return
------

NET_XMIT_DROP in case of error or NET_XMIT_SUCCESS otherwise.

.. _`batadv_forw_packet_free`:

batadv_forw_packet_free
=======================

.. c:function:: void batadv_forw_packet_free(struct batadv_forw_packet *forw_packet, bool dropped)

    free a forwarding packet

    :param forw_packet:
        The packet to free
    :type forw_packet: struct batadv_forw_packet \*

    :param dropped:
        whether the packet is freed because is is dropped
    :type dropped: bool

.. _`batadv_forw_packet_free.description`:

Description
-----------

This frees a forwarding packet and releases any resources it might
have claimed.

.. _`batadv_forw_packet_alloc`:

batadv_forw_packet_alloc
========================

.. c:function:: struct batadv_forw_packet *batadv_forw_packet_alloc(struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, atomic_t *queue_left, struct batadv_priv *bat_priv, struct sk_buff *skb)

    allocate a forwarding packet

    :param if_incoming:
        The (optional) if_incoming to be grabbed
    :type if_incoming: struct batadv_hard_iface \*

    :param if_outgoing:
        The (optional) if_outgoing to be grabbed
    :type if_outgoing: struct batadv_hard_iface \*

    :param queue_left:
        The (optional) queue counter to decrease
    :type queue_left: atomic_t \*

    :param bat_priv:
        The bat_priv for the mesh of this forw_packet
    :type bat_priv: struct batadv_priv \*

    :param skb:
        The raw packet this forwarding packet shall contain
    :type skb: struct sk_buff \*

.. _`batadv_forw_packet_alloc.description`:

Description
-----------

Allocates a forwarding packet and tries to get a reference to the
(optional) if_incoming, if_outgoing and queue_left. If queue_left
is NULL then bat_priv is optional, too.

.. _`batadv_forw_packet_alloc.return`:

Return
------

An allocated forwarding packet on success, NULL otherwise.

.. _`batadv_forw_packet_was_stolen`:

batadv_forw_packet_was_stolen
=============================

.. c:function:: bool batadv_forw_packet_was_stolen(struct batadv_forw_packet *forw_packet)

    check whether someone stole this packet

    :param forw_packet:
        the forwarding packet to check
    :type forw_packet: struct batadv_forw_packet \*

.. _`batadv_forw_packet_was_stolen.description`:

Description
-----------

This function checks whether the given forwarding packet was claimed by
someone else for \ :c:func:`free`\ .

.. _`batadv_forw_packet_was_stolen.return`:

Return
------

True if someone stole it, false otherwise.

.. _`batadv_forw_packet_steal`:

batadv_forw_packet_steal
========================

.. c:function:: bool batadv_forw_packet_steal(struct batadv_forw_packet *forw_packet, spinlock_t *lock)

    claim a forw_packet for \ :c:func:`free`\ 

    :param forw_packet:
        the forwarding packet to steal
    :type forw_packet: struct batadv_forw_packet \*

    :param lock:
        a key to the store to steal from (e.g. forw_{bat,bcast}_list_lock)
    :type lock: spinlock_t \*

.. _`batadv_forw_packet_steal.description`:

Description
-----------

This function tries to steal a specific forw_packet from global
visibility for the purpose of getting it for \ :c:func:`free`\ . That means
the caller is \*not\* allowed to requeue it afterwards.

.. _`batadv_forw_packet_steal.return`:

Return
------

True if stealing was successful. False if someone else stole it
before us.

.. _`batadv_forw_packet_list_steal`:

batadv_forw_packet_list_steal
=============================

.. c:function:: void batadv_forw_packet_list_steal(struct hlist_head *forw_list, struct hlist_head *cleanup_list, const struct batadv_hard_iface *hard_iface)

    claim a list of forward packets for \ :c:func:`free`\ 

    :param forw_list:
        the to be stolen forward packets
    :type forw_list: struct hlist_head \*

    :param cleanup_list:
        a backup pointer, to be able to dispose the packet later
    :type cleanup_list: struct hlist_head \*

    :param hard_iface:
        the interface to steal forward packets from
    :type hard_iface: const struct batadv_hard_iface \*

.. _`batadv_forw_packet_list_steal.description`:

Description
-----------

This function claims responsibility to free any forw_packet queued on the
given hard_iface. If hard_iface is NULL forwarding packets on all hard
interfaces will be claimed.

The packets are being moved from the forw_list to the cleanup_list and
by that allows already running threads to notice the claiming.

.. _`batadv_forw_packet_list_free`:

batadv_forw_packet_list_free
============================

.. c:function:: void batadv_forw_packet_list_free(struct hlist_head *head)

    free a list of forward packets

    :param head:
        a list of to be freed forw_packets
    :type head: struct hlist_head \*

.. _`batadv_forw_packet_list_free.description`:

Description
-----------

This function cancels the scheduling of any packet in the provided list,
waits for any possibly running packet forwarding thread to finish and
finally, safely frees this forward packet.

This function might sleep.

.. _`batadv_forw_packet_queue`:

batadv_forw_packet_queue
========================

.. c:function:: void batadv_forw_packet_queue(struct batadv_forw_packet *forw_packet, spinlock_t *lock, struct hlist_head *head, unsigned long send_time)

    try to queue a forwarding packet

    :param forw_packet:
        the forwarding packet to queue
    :type forw_packet: struct batadv_forw_packet \*

    :param lock:
        a key to the store (e.g. forw_{bat,bcast}_list_lock)
    :type lock: spinlock_t \*

    :param head:
        the shelve to queue it on (e.g. forw_{bat,bcast}_list)
    :type head: struct hlist_head \*

    :param send_time:
        timestamp (jiffies) when the packet is to be sent
    :type send_time: unsigned long

.. _`batadv_forw_packet_queue.description`:

Description
-----------

This function tries to (re)queue a forwarding packet. Requeuing
is prevented if the according interface is shutting down
(e.g. if \ :c:func:`batadv_forw_packet_list_steal`\  was called for this
packet earlier).

Calling \ :c:func:`batadv_forw_packet_queue`\  after a call to
\ :c:func:`batadv_forw_packet_steal`\  is forbidden!

Caller needs to ensure that forw_packet->delayed_work was initialized.

.. _`batadv_forw_packet_bcast_queue`:

batadv_forw_packet_bcast_queue
==============================

.. c:function:: void batadv_forw_packet_bcast_queue(struct batadv_priv *bat_priv, struct batadv_forw_packet *forw_packet, unsigned long send_time)

    try to queue a broadcast packet

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param forw_packet:
        the forwarding packet to queue
    :type forw_packet: struct batadv_forw_packet \*

    :param send_time:
        timestamp (jiffies) when the packet is to be sent
    :type send_time: unsigned long

.. _`batadv_forw_packet_bcast_queue.description`:

Description
-----------

This function tries to (re)queue a broadcast packet.

Caller needs to ensure that forw_packet->delayed_work was initialized.

.. _`batadv_forw_packet_ogmv1_queue`:

batadv_forw_packet_ogmv1_queue
==============================

.. c:function:: void batadv_forw_packet_ogmv1_queue(struct batadv_priv *bat_priv, struct batadv_forw_packet *forw_packet, unsigned long send_time)

    try to queue an OGMv1 packet

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param forw_packet:
        the forwarding packet to queue
    :type forw_packet: struct batadv_forw_packet \*

    :param send_time:
        timestamp (jiffies) when the packet is to be sent
    :type send_time: unsigned long

.. _`batadv_forw_packet_ogmv1_queue.description`:

Description
-----------

This function tries to (re)queue an OGMv1 packet.

Caller needs to ensure that forw_packet->delayed_work was initialized.

.. _`batadv_add_bcast_packet_to_list`:

batadv_add_bcast_packet_to_list
===============================

.. c:function:: int batadv_add_bcast_packet_to_list(struct batadv_priv *bat_priv, const struct sk_buff *skb, unsigned long delay, bool own_packet)

    queue broadcast packet for multiple sends

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        broadcast packet to add
    :type skb: const struct sk_buff \*

    :param delay:
        number of jiffies to wait before sending
    :type delay: unsigned long

    :param own_packet:
        true if it is a self-generated broadcast packet
    :type own_packet: bool

.. _`batadv_add_bcast_packet_to_list.description`:

Description
-----------

add a broadcast packet to the queue and setup timers. broadcast packets
are sent multiple times to increase probability for being received.

The skb is not consumed, so the caller should make sure that the
skb is freed.

.. _`batadv_add_bcast_packet_to_list.return`:

Return
------

NETDEV_TX_OK on success and NETDEV_TX_BUSY on errors.

.. _`batadv_forw_packet_bcasts_left`:

batadv_forw_packet_bcasts_left
==============================

.. c:function:: bool batadv_forw_packet_bcasts_left(struct batadv_forw_packet *forw_packet, struct batadv_hard_iface *hard_iface)

    check if a retransmission is necessary

    :param forw_packet:
        the forwarding packet to check
    :type forw_packet: struct batadv_forw_packet \*

    :param hard_iface:
        the interface to check on
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_forw_packet_bcasts_left.description`:

Description
-----------

Checks whether a given packet has any (re)transmissions left on the provided
interface.

.. _`batadv_forw_packet_bcasts_left.hard_iface-may-be-null`:

hard_iface may be NULL
----------------------

In that case the number of transmissions this skb had
so far is compared with the maximum amount of retransmissions independent of
any interface instead.

.. _`batadv_forw_packet_bcasts_left.return`:

Return
------

True if (re)transmissions are left, false otherwise.

.. _`batadv_forw_packet_bcasts_inc`:

batadv_forw_packet_bcasts_inc
=============================

.. c:function:: void batadv_forw_packet_bcasts_inc(struct batadv_forw_packet *forw_packet)

    increment retransmission counter of a packet

    :param forw_packet:
        the packet to increase the counter for
    :type forw_packet: struct batadv_forw_packet \*

.. _`batadv_forw_packet_is_rebroadcast`:

batadv_forw_packet_is_rebroadcast
=================================

.. c:function:: bool batadv_forw_packet_is_rebroadcast(struct batadv_forw_packet *forw_packet)

    check packet for previous transmissions

    :param forw_packet:
        the packet to check
    :type forw_packet: struct batadv_forw_packet \*

.. _`batadv_forw_packet_is_rebroadcast.return`:

Return
------

True if this packet was transmitted before, false otherwise.

.. _`batadv_purge_outstanding_packets`:

batadv_purge_outstanding_packets
================================

.. c:function:: void batadv_purge_outstanding_packets(struct batadv_priv *bat_priv, const struct batadv_hard_iface *hard_iface)

    stop/purge scheduled bcast/OGMv1 packets

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param hard_iface:
        the hard interface to cancel and purge bcast/ogm packets on
    :type hard_iface: const struct batadv_hard_iface \*

.. _`batadv_purge_outstanding_packets.description`:

Description
-----------

This method cancels and purges any broadcast and OGMv1 packet on the given
hard_iface. If hard_iface is NULL, broadcast and OGMv1 packets on all hard
interfaces will be canceled and purged.

This function might sleep.

.. This file was automatic generated / don't edit.

