.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/routing.c

.. _`_batadv_update_route`:

_batadv_update_route
====================

.. c:function:: void _batadv_update_route(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_hard_iface *recv_if, struct batadv_neigh_node *neigh_node)

    set the router for this originator

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig node which is to be configured

    :param struct batadv_hard_iface \*recv_if:
        the receive interface for which this route is set

    :param struct batadv_neigh_node \*neigh_node:
        neighbor which should be the next router

.. _`_batadv_update_route.description`:

Description
-----------

This function does not perform any error checks

.. _`batadv_update_route`:

batadv_update_route
===================

.. c:function:: void batadv_update_route(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_hard_iface *recv_if, struct batadv_neigh_node *neigh_node)

    set the router for this originator

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig node which is to be configured

    :param struct batadv_hard_iface \*recv_if:
        the receive interface for which this route is set

    :param struct batadv_neigh_node \*neigh_node:
        neighbor which should be the next router

.. _`batadv_window_protected`:

batadv_window_protected
=======================

.. c:function:: bool batadv_window_protected(struct batadv_priv *bat_priv, s32 seq_num_diff, s32 seq_old_max_diff, unsigned long *last_reset, bool *protection_started)

    checks whether the host restarted and is in the protection time.

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param s32 seq_num_diff:
        difference between the current/received sequence number and
        the last sequence number

    :param s32 seq_old_max_diff:
        maximum age of sequence number not considered as restart

    :param unsigned long \*last_reset:
        jiffies timestamp of the last reset, will be updated when reset
        is detected

    :param bool \*protection_started:
        is set to true if the protection window was started,
        doesn't change otherwise.

.. _`batadv_window_protected.return`:

Return
------

false if the packet is to be accepted.
true if the packet is to be ignored.

.. _`batadv_recv_my_icmp_packet`:

batadv_recv_my_icmp_packet
==========================

.. c:function:: int batadv_recv_my_icmp_packet(struct batadv_priv *bat_priv, struct sk_buff *skb)

    receive an icmp packet locally

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        icmp packet to process

.. _`batadv_recv_my_icmp_packet.return`:

Return
------

NET_RX_SUCCESS if the packet has been consumed or NET_RX_DROP
otherwise.

.. _`batadv_check_unicast_packet`:

batadv_check_unicast_packet
===========================

.. c:function:: int batadv_check_unicast_packet(struct batadv_priv *bat_priv, struct sk_buff *skb, int hdr_size)

    Check for malformed unicast packets

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        packet to check

    :param int hdr_size:
        size of header to pull

.. _`batadv_check_unicast_packet.description`:

Description
-----------

Check for short header and bad addresses in given packet.

.. _`batadv_check_unicast_packet.return`:

Return
------

negative value when check fails and 0 otherwise. The negative value

.. _`batadv_check_unicast_packet.depends-on-the-reason`:

depends on the reason
---------------------

-ENODATA for bad header, -EBADR for broadcast
destination or source, and -EREMOTE for non-local (other host) destination.

.. _`batadv_last_bonding_get`:

batadv_last_bonding_get
=======================

.. c:function:: struct batadv_orig_ifinfo *batadv_last_bonding_get(struct batadv_orig_node *orig_node)

    Get last_bonding_candidate of orig_node

    :param struct batadv_orig_node \*orig_node:
        originator node whose last bonding candidate should be retrieved

.. _`batadv_last_bonding_get.return`:

Return
------

last bonding candidate of router or NULL if not found

The object is returned with refcounter increased by 1.

.. _`batadv_last_bonding_replace`:

batadv_last_bonding_replace
===========================

.. c:function:: void batadv_last_bonding_replace(struct batadv_orig_node *orig_node, struct batadv_orig_ifinfo *new_candidate)

    Replace last_bonding_candidate of orig_node

    :param struct batadv_orig_node \*orig_node:
        originator node whose bonding candidates should be replaced

    :param struct batadv_orig_ifinfo \*new_candidate:
        new bonding candidate or NULL

.. _`batadv_find_router`:

batadv_find_router
==================

.. c:function:: struct batadv_neigh_node *batadv_find_router(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_hard_iface *recv_if)

    find a suitable router for this originator

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        the destination node

    :param struct batadv_hard_iface \*recv_if:
        pointer to interface this packet was received on

.. _`batadv_find_router.return`:

Return
------

the router which should be used for this orig_node on
this interface, or NULL if not available.

.. _`batadv_reroute_unicast_packet`:

batadv_reroute_unicast_packet
=============================

.. c:function:: bool batadv_reroute_unicast_packet(struct batadv_priv *bat_priv, struct batadv_unicast_packet *unicast_packet, u8 *dst_addr, unsigned short vid)

    update the unicast header for re-routing

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_unicast_packet \*unicast_packet:
        the unicast header to be updated

    :param u8 \*dst_addr:
        the payload destination

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_reroute_unicast_packet.description`:

Description
-----------

Search the translation table for dst_addr and update the unicast header with
the new corresponding information (originator address where the destination
client currently is and its known TTVN)

.. _`batadv_reroute_unicast_packet.return`:

Return
------

true if the packet header has been updated, false otherwise

.. _`batadv_recv_unhandled_unicast_packet`:

batadv_recv_unhandled_unicast_packet
====================================

.. c:function:: int batadv_recv_unhandled_unicast_packet(struct sk_buff *skb, struct batadv_hard_iface *recv_if)

    receive and process packets which are in the unicast number space but not yet known to the implementation

    :param struct sk_buff \*skb:
        unicast tvlv packet to process

    :param struct batadv_hard_iface \*recv_if:
        pointer to interface this packet was received on

.. _`batadv_recv_unhandled_unicast_packet.return`:

Return
------

NET_RX_SUCCESS if the packet has been consumed or NET_RX_DROP
otherwise.

.. _`batadv_recv_unicast_tvlv`:

batadv_recv_unicast_tvlv
========================

.. c:function:: int batadv_recv_unicast_tvlv(struct sk_buff *skb, struct batadv_hard_iface *recv_if)

    receive and process unicast tvlv packets

    :param struct sk_buff \*skb:
        unicast tvlv packet to process

    :param struct batadv_hard_iface \*recv_if:
        pointer to interface this packet was received on

.. _`batadv_recv_unicast_tvlv.return`:

Return
------

NET_RX_SUCCESS if the packet has been consumed or NET_RX_DROP
otherwise.

.. _`batadv_recv_frag_packet`:

batadv_recv_frag_packet
=======================

.. c:function:: int batadv_recv_frag_packet(struct sk_buff *skb, struct batadv_hard_iface *recv_if)

    process received fragment

    :param struct sk_buff \*skb:
        the received fragment

    :param struct batadv_hard_iface \*recv_if:
        interface that the skb is received on

.. _`batadv_recv_frag_packet.this-function-does-one-of-the-three-following-things`:

This function does one of the three following things
----------------------------------------------------

1) Forward fragment, if
the assembled packet will exceed our MTU; 2) Buffer fragment, if we till
lack further fragments; 3) Merge fragments, if we have all needed parts.

.. _`batadv_recv_frag_packet.return`:

Return
------

NET_RX_DROP if the skb is not consumed, NET_RX_SUCCESS otherwise.

.. This file was automatic generated / don't edit.

