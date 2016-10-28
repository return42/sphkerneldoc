.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/multicast.c

.. _`batadv_mcast_mla_softif_get`:

batadv_mcast_mla_softif_get
===========================

.. c:function:: int batadv_mcast_mla_softif_get(struct net_device *dev, struct hlist_head *mcast_list)

    get softif multicast listeners

    :param struct net_device \*dev:
        the device to collect multicast addresses from

    :param struct hlist_head \*mcast_list:
        a list to put found addresses into

.. _`batadv_mcast_mla_softif_get.description`:

Description
-----------

Collect multicast addresses of the local multicast listeners
on the given soft interface, dev, in the given mcast_list.

.. _`batadv_mcast_mla_softif_get.return`:

Return
------

-ENOMEM on memory allocation error or the number of
items added to the mcast_list otherwise.

.. _`batadv_mcast_mla_is_duplicate`:

batadv_mcast_mla_is_duplicate
=============================

.. c:function:: bool batadv_mcast_mla_is_duplicate(u8 *mcast_addr, struct hlist_head *mcast_list)

    check whether an address is in a list

    :param u8 \*mcast_addr:
        the multicast address to check

    :param struct hlist_head \*mcast_list:
        the list with multicast addresses to search in

.. _`batadv_mcast_mla_is_duplicate.return`:

Return
------

true if the given address is already in the given list.
Otherwise returns false.

.. _`batadv_mcast_mla_list_free`:

batadv_mcast_mla_list_free
==========================

.. c:function:: void batadv_mcast_mla_list_free(struct batadv_priv *bat_priv, struct hlist_head *mcast_list)

    free a list of multicast addresses

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct hlist_head \*mcast_list:
        the list to free

.. _`batadv_mcast_mla_list_free.description`:

Description
-----------

Removes and frees all items in the given mcast_list.

.. _`batadv_mcast_mla_tt_retract`:

batadv_mcast_mla_tt_retract
===========================

.. c:function:: void batadv_mcast_mla_tt_retract(struct batadv_priv *bat_priv, struct hlist_head *mcast_list)

    clean up multicast listener announcements

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct hlist_head \*mcast_list:
        a list of addresses which should \_not\_ be removed

.. _`batadv_mcast_mla_tt_retract.description`:

Description
-----------

Retracts the announcement of any multicast listener from the
translation table except the ones listed in the given mcast_list.

If mcast_list is NULL then all are retracted.

.. _`batadv_mcast_mla_tt_add`:

batadv_mcast_mla_tt_add
=======================

.. c:function:: void batadv_mcast_mla_tt_add(struct batadv_priv *bat_priv, struct hlist_head *mcast_list)

    add multicast listener announcements

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct hlist_head \*mcast_list:
        a list of addresses which are going to get added

.. _`batadv_mcast_mla_tt_add.description`:

Description
-----------

Adds multicast listener announcements from the given mcast_list to the
translation table if they have not been added yet.

.. _`batadv_mcast_has_bridge`:

batadv_mcast_has_bridge
=======================

.. c:function:: bool batadv_mcast_has_bridge(struct batadv_priv *bat_priv)

    check whether the soft-iface is bridged

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_has_bridge.description`:

Description
-----------

Checks whether there is a bridge on top of our soft interface.

.. _`batadv_mcast_has_bridge.return`:

Return
------

true if there is a bridge, false otherwise.

.. _`batadv_mcast_mla_tvlv_update`:

batadv_mcast_mla_tvlv_update
============================

.. c:function:: bool batadv_mcast_mla_tvlv_update(struct batadv_priv *bat_priv)

    update multicast tvlv

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_mla_tvlv_update.description`:

Description
-----------

Updates the own multicast tvlv with our current multicast related settings,
capabilities and inabilities.

.. _`batadv_mcast_mla_tvlv_update.return`:

Return
------

true if the tvlv container is registered afterwards. Otherwise
returns false.

.. _`batadv_mcast_mla_update`:

batadv_mcast_mla_update
=======================

.. c:function:: void batadv_mcast_mla_update(struct batadv_priv *bat_priv)

    update the own MLAs

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_mla_update.description`:

Description
-----------

Updates the own multicast listener announcements in the translation
table as well as the own, announced multicast tvlv container.

.. _`batadv_mcast_forw_mode_check_ipv4`:

batadv_mcast_forw_mode_check_ipv4
=================================

.. c:function:: int batadv_mcast_forw_mode_check_ipv4(struct batadv_priv *bat_priv, struct sk_buff *skb, bool *is_unsnoopable)

    check for optimized forwarding potential

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the IPv4 packet to check

    :param bool \*is_unsnoopable:
        stores whether the destination is snoopable

.. _`batadv_mcast_forw_mode_check_ipv4.description`:

Description
-----------

Checks whether the given IPv4 packet has the potential to be forwarded with a
mode more optimal than classic flooding.

.. _`batadv_mcast_forw_mode_check_ipv4.return`:

Return
------

If so then 0. Otherwise -EINVAL or -ENOMEM in case of memory
allocation failure.

.. _`batadv_mcast_forw_mode_check_ipv6`:

batadv_mcast_forw_mode_check_ipv6
=================================

.. c:function:: int batadv_mcast_forw_mode_check_ipv6(struct batadv_priv *bat_priv, struct sk_buff *skb, bool *is_unsnoopable)

    check for optimized forwarding potential

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the IPv6 packet to check

    :param bool \*is_unsnoopable:
        stores whether the destination is snoopable

.. _`batadv_mcast_forw_mode_check_ipv6.description`:

Description
-----------

Checks whether the given IPv6 packet has the potential to be forwarded with a
mode more optimal than classic flooding.

.. _`batadv_mcast_forw_mode_check_ipv6.return`:

Return
------

If so then 0. Otherwise -EINVAL is or -ENOMEM if we are out of memory

.. _`batadv_mcast_forw_mode_check`:

batadv_mcast_forw_mode_check
============================

.. c:function:: int batadv_mcast_forw_mode_check(struct batadv_priv *bat_priv, struct sk_buff *skb, bool *is_unsnoopable)

    check for optimized forwarding potential

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the multicast frame to check

    :param bool \*is_unsnoopable:
        stores whether the destination is snoopable

.. _`batadv_mcast_forw_mode_check.description`:

Description
-----------

Checks whether the given multicast ethernet frame has the potential to be
forwarded with a mode more optimal than classic flooding.

.. _`batadv_mcast_forw_mode_check.return`:

Return
------

If so then 0. Otherwise -EINVAL is or -ENOMEM if we are out of memory

.. _`batadv_mcast_forw_want_all_ip_count`:

batadv_mcast_forw_want_all_ip_count
===================================

.. c:function:: int batadv_mcast_forw_want_all_ip_count(struct batadv_priv *bat_priv, struct ethhdr *ethhdr)

    count nodes with unspecific mcast interest

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct ethhdr \*ethhdr:
        ethernet header of a packet

.. _`batadv_mcast_forw_want_all_ip_count.return`:

Return
------

the number of nodes which want all IPv4 multicast traffic if the
given ethhdr is from an IPv4 packet or the number of nodes which want all
IPv6 traffic if it matches an IPv6 packet.

.. _`batadv_mcast_forw_tt_node_get`:

batadv_mcast_forw_tt_node_get
=============================

.. c:function:: struct batadv_orig_node *batadv_mcast_forw_tt_node_get(struct batadv_priv *bat_priv, struct ethhdr *ethhdr)

    get a multicast tt node

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct ethhdr \*ethhdr:
        the ether header containing the multicast destination

.. _`batadv_mcast_forw_tt_node_get.return`:

Return
------

an orig_node matching the multicast address provided by ethhdr
via a translation table lookup. This increases the returned nodes refcount.

.. _`batadv_mcast_forw_ipv4_node_get`:

batadv_mcast_forw_ipv4_node_get
===============================

.. c:function:: struct batadv_orig_node *batadv_mcast_forw_ipv4_node_get(struct batadv_priv *bat_priv)

    get a node with an ipv4 flag

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_forw_ipv4_node_get.return`:

Return
------

an orig_node which has the BATADV_MCAST_WANT_ALL_IPV4 flag set and
increases its refcount.

.. _`batadv_mcast_forw_ipv6_node_get`:

batadv_mcast_forw_ipv6_node_get
===============================

.. c:function:: struct batadv_orig_node *batadv_mcast_forw_ipv6_node_get(struct batadv_priv *bat_priv)

    get a node with an ipv6 flag

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_forw_ipv6_node_get.return`:

Return
------

an orig_node which has the BATADV_MCAST_WANT_ALL_IPV6 flag set
and increases its refcount.

.. _`batadv_mcast_forw_ip_node_get`:

batadv_mcast_forw_ip_node_get
=============================

.. c:function:: struct batadv_orig_node *batadv_mcast_forw_ip_node_get(struct batadv_priv *bat_priv, struct ethhdr *ethhdr)

    get a node with an ipv4/ipv6 flag

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct ethhdr \*ethhdr:
        an ethernet header to determine the protocol family from

.. _`batadv_mcast_forw_ip_node_get.return`:

Return
------

an orig_node which has the BATADV_MCAST_WANT_ALL_IPV4 or
BATADV_MCAST_WANT_ALL_IPV6 flag, depending on the provided ethhdr, set and
increases its refcount.

.. _`batadv_mcast_forw_unsnoop_node_get`:

batadv_mcast_forw_unsnoop_node_get
==================================

.. c:function:: struct batadv_orig_node *batadv_mcast_forw_unsnoop_node_get(struct batadv_priv *bat_priv)

    get a node with an unsnoopable flag

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_forw_unsnoop_node_get.return`:

Return
------

an orig_node which has the BATADV_MCAST_WANT_ALL_UNSNOOPABLES flag
set and increases its refcount.

.. _`batadv_mcast_forw_mode`:

batadv_mcast_forw_mode
======================

.. c:function:: enum batadv_forw_mode batadv_mcast_forw_mode(struct batadv_priv *bat_priv, struct sk_buff *skb, struct batadv_orig_node **orig)

    check on how to forward a multicast packet

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        The multicast packet to check

    :param struct batadv_orig_node \*\*orig:
        an originator to be set to forward the skb to

.. _`batadv_mcast_forw_mode.return`:

Return
------

the forwarding mode as enum batadv_forw_mode and in case of
BATADV_FORW_SINGLE set the orig to the single originator the skb
should be forwarded to.

.. _`batadv_mcast_want_unsnoop_update`:

batadv_mcast_want_unsnoop_update
================================

.. c:function:: void batadv_mcast_want_unsnoop_update(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 mcast_flags)

    update unsnoop counter and list

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig:
        the orig_node which multicast state might have changed of

    :param u8 mcast_flags:
        flags indicating the new multicast state

.. _`batadv_mcast_want_unsnoop_update.description`:

Description
-----------

If the BATADV_MCAST_WANT_ALL_UNSNOOPABLES flag of this originator,
orig, has toggled then this method updates counter and list accordingly.

Caller needs to hold orig->mcast_handler_lock.

.. _`batadv_mcast_want_ipv4_update`:

batadv_mcast_want_ipv4_update
=============================

.. c:function:: void batadv_mcast_want_ipv4_update(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 mcast_flags)

    update want-all-ipv4 counter and list

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig:
        the orig_node which multicast state might have changed of

    :param u8 mcast_flags:
        flags indicating the new multicast state

.. _`batadv_mcast_want_ipv4_update.description`:

Description
-----------

If the BATADV_MCAST_WANT_ALL_IPV4 flag of this originator, orig, has
toggled then this method updates counter and list accordingly.

Caller needs to hold orig->mcast_handler_lock.

.. _`batadv_mcast_want_ipv6_update`:

batadv_mcast_want_ipv6_update
=============================

.. c:function:: void batadv_mcast_want_ipv6_update(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 mcast_flags)

    update want-all-ipv6 counter and list

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig:
        the orig_node which multicast state might have changed of

    :param u8 mcast_flags:
        flags indicating the new multicast state

.. _`batadv_mcast_want_ipv6_update.description`:

Description
-----------

If the BATADV_MCAST_WANT_ALL_IPV6 flag of this originator, orig, has
toggled then this method updates counter and list accordingly.

Caller needs to hold orig->mcast_handler_lock.

.. _`batadv_mcast_tvlv_ogm_handler_v1`:

batadv_mcast_tvlv_ogm_handler_v1
================================

.. c:function:: void batadv_mcast_tvlv_ogm_handler_v1(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len)

    process incoming multicast tvlv container

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig:
        the orig_node of the ogm

    :param u8 flags:
        flags indicating the tvlv state (see batadv_tvlv_handler_flags)

    :param void \*tvlv_value:
        tvlv buffer containing the multicast data

    :param u16 tvlv_value_len:
        tvlv buffer length

.. _`batadv_mcast_init`:

batadv_mcast_init
=================

.. c:function:: void batadv_mcast_init(struct batadv_priv *bat_priv)

    initialize the multicast optimizations structures

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_free`:

batadv_mcast_free
=================

.. c:function:: void batadv_mcast_free(struct batadv_priv *bat_priv)

    free the multicast optimizations structures

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_purge_orig`:

batadv_mcast_purge_orig
=======================

.. c:function:: void batadv_mcast_purge_orig(struct batadv_orig_node *orig)

    reset originator global mcast state modifications

    :param struct batadv_orig_node \*orig:
        the originator which is going to get purged

.. This file was automatic generated / don't edit.

