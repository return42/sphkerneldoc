.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/multicast.c

.. _`batadv_mcast_start_timer`:

batadv_mcast_start_timer
========================

.. c:function:: void batadv_mcast_start_timer(struct batadv_priv *bat_priv)

    schedule the multicast periodic worker

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_mcast_get_bridge`:

batadv_mcast_get_bridge
=======================

.. c:function:: struct net_device *batadv_mcast_get_bridge(struct net_device *soft_iface)

    get the bridge on top of the softif if it exists

    :param struct net_device \*soft_iface:
        netdev struct of the mesh interface

.. _`batadv_mcast_get_bridge.description`:

Description
-----------

If the given soft interface has a bridge on top then the refcount
of the according net device is increased.

.. _`batadv_mcast_get_bridge.return`:

Return
------

NULL if no such bridge exists. Otherwise the net device of the
bridge.

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

Collects multicast addresses of multicast listeners residing
on this kernel on the given soft interface, dev, in
the given mcast_list. In general, multicast listeners provided by
your multicast receiving applications run directly on this node.

If there is a bridge interface on top of dev, collects from that one
instead. Just like with IP addresses and routes, multicast listeners
will(/should) register to the bridge interface instead of an
enslaved bat0.

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

.. _`batadv_mcast_mla_br_addr_cpy`:

batadv_mcast_mla_br_addr_cpy
============================

.. c:function:: void batadv_mcast_mla_br_addr_cpy(char *dst, const struct br_ip *src)

    copy a bridge multicast address

    :param char \*dst:
        destination to write to - a multicast MAC address

    :param const struct br_ip \*src:
        source to read from - a multicast IP address

.. _`batadv_mcast_mla_br_addr_cpy.description`:

Description
-----------

Converts a given multicast IPv4/IPv6 address from a bridge
to its matching multicast MAC address and copies it into the given
destination buffer.

Caller needs to make sure the destination buffer can hold
at least ETH_ALEN bytes.

.. _`batadv_mcast_mla_bridge_get`:

batadv_mcast_mla_bridge_get
===========================

.. c:function:: int batadv_mcast_mla_bridge_get(struct net_device *dev, struct hlist_head *mcast_list)

    get bridged-in multicast listeners

    :param struct net_device \*dev:
        a bridge slave whose bridge to collect multicast addresses from

    :param struct hlist_head \*mcast_list:
        a list to put found addresses into

.. _`batadv_mcast_mla_bridge_get.description`:

Description
-----------

Collects multicast addresses of multicast listeners residing
on foreign, non-mesh devices which we gave access to our mesh via
a bridge on top of the given soft interface, dev, in the given
mcast_list.

.. _`batadv_mcast_mla_bridge_get.return`:

Return
------

-ENOMEM on memory allocation error or the number of
items added to the mcast_list otherwise.

.. _`batadv_mcast_mla_list_free`:

batadv_mcast_mla_list_free
==========================

.. c:function:: void batadv_mcast_mla_list_free(struct hlist_head *mcast_list)

    free a list of multicast addresses

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

Do not call outside of the mcast worker! (or cancel mcast worker first)

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

Do not call outside of the mcast worker! (or cancel mcast worker first)

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

.. _`batadv_mcast_querier_log`:

batadv_mcast_querier_log
========================

.. c:function:: void batadv_mcast_querier_log(struct batadv_priv *bat_priv, char *str_proto, struct batadv_mcast_querier_state *old_state, struct batadv_mcast_querier_state *new_state)

    debug output regarding the querier status on link

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param char \*str_proto:
        a string for the querier protocol (e.g. "IGMP" or "MLD")

    :param struct batadv_mcast_querier_state \*old_state:
        the previous querier state on our link

    :param struct batadv_mcast_querier_state \*new_state:
        the new querier state on our link

.. _`batadv_mcast_querier_log.description`:

Description
-----------

Outputs debug messages to the logging facility with log level 'mcast'
regarding changes to the querier status on the link which are relevant
to our multicast optimizations.

Usually this is about whether a querier appeared or vanished in
our mesh or whether the querier is in the suboptimal position of being

.. _`batadv_mcast_querier_log.behind-our-local-bridge-segment`:

behind our local bridge segment
-------------------------------

Snooping switches will directly
forward listener reports to the querier, therefore batman-adv and
the bridge will potentially not see these listeners - the querier is
potentially shadowing listeners from us then.

This is only interesting for nodes with a bridge on top of their
soft interface.

.. _`batadv_mcast_bridge_log`:

batadv_mcast_bridge_log
=======================

.. c:function:: void batadv_mcast_bridge_log(struct batadv_priv *bat_priv, bool bridged, struct batadv_mcast_querier_state *querier_ipv4, struct batadv_mcast_querier_state *querier_ipv6)

    debug output for topology changes in bridged setups

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param bool bridged:
        a flag about whether the soft interface is currently bridged or not

    :param struct batadv_mcast_querier_state \*querier_ipv4:
        (maybe) new status of a potential, selected IGMP querier

    :param struct batadv_mcast_querier_state \*querier_ipv6:
        (maybe) new status of a potential, selected MLD querier

.. _`batadv_mcast_bridge_log.description`:

Description
-----------

If no bridges are ever used on this node, then this function does nothing.

Otherwise this function outputs debug information to the 'mcast' log level
which might be relevant to our multicast optimizations.

More precisely, it outputs information when a bridge interface is added or
removed from a soft interface. And when a bridge is present, it further
outputs information about the querier state which is relevant for the
multicast flags this node is going to set.

.. _`batadv_mcast_flags_log`:

batadv_mcast_flags_log
======================

.. c:function:: void batadv_mcast_flags_log(struct batadv_priv *bat_priv, u8 flags)

    output debug information about mcast flag changes

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 flags:
        flags indicating the new multicast state

.. _`batadv_mcast_flags_log.description`:

Description
-----------

Whenever the multicast flags this nodes announces changes (@mcast_flags vs.
bat_priv->mcast.flags), this notifies userspace via the 'mcast' log level.

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

false if we want all IPv4 && IPv6 multicast traffic and true
otherwise.

.. _`__batadv_mcast_mla_update`:

__batadv_mcast_mla_update
=========================

.. c:function:: void __batadv_mcast_mla_update(struct batadv_priv *bat_priv)

    update the own MLAs

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`__batadv_mcast_mla_update.description`:

Description
-----------

Updates the own multicast listener announcements in the translation
table as well as the own, announced multicast tvlv container.

Note that non-conflicting reads and writes to bat_priv->mcast.mla_list
in \ :c:func:`batadv_mcast_mla_tt_retract`\  and \ :c:func:`batadv_mcast_mla_tt_add`\  are
ensured by the non-parallel execution of the worker this function
belongs to.

.. _`batadv_mcast_mla_update`:

batadv_mcast_mla_update
=======================

.. c:function:: void batadv_mcast_mla_update(struct work_struct *work)

    update the own MLAs

    :param struct work_struct \*work:
        kernel work struct

.. _`batadv_mcast_mla_update.description`:

Description
-----------

Updates the own multicast listener announcements in the translation
table as well as the own, announced multicast tvlv container.

In the end, reschedules the work timer.

.. _`batadv_mcast_is_report_ipv4`:

batadv_mcast_is_report_ipv4
===========================

.. c:function:: bool batadv_mcast_is_report_ipv4(struct sk_buff *skb)

    check for IGMP reports

    :param struct sk_buff \*skb:
        the ethernet frame destined for the mesh

.. _`batadv_mcast_is_report_ipv4.description`:

Description
-----------

This call might reallocate skb data.

Checks whether the given frame is a valid IGMP report.

.. _`batadv_mcast_is_report_ipv4.return`:

Return
------

If so then true, otherwise false.

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

.. _`batadv_mcast_is_report_ipv6`:

batadv_mcast_is_report_ipv6
===========================

.. c:function:: bool batadv_mcast_is_report_ipv6(struct sk_buff *skb)

    check for MLD reports

    :param struct sk_buff \*skb:
        the ethernet frame destined for the mesh

.. _`batadv_mcast_is_report_ipv6.description`:

Description
-----------

This call might reallocate skb data.

Checks whether the given frame is a valid MLD report.

.. _`batadv_mcast_is_report_ipv6.return`:

Return
------

If so then true, otherwise false.

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

.. _`batadv_mcast_tvlv_ogm_handler`:

batadv_mcast_tvlv_ogm_handler
=============================

.. c:function:: void batadv_mcast_tvlv_ogm_handler(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len)

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

.. _`batadv_mcast_flags_print_header`:

batadv_mcast_flags_print_header
===============================

.. c:function:: void batadv_mcast_flags_print_header(struct batadv_priv *bat_priv, struct seq_file *seq)

    print own mcast flags to debugfs table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct seq_file \*seq:
        debugfs table seq_file struct

.. _`batadv_mcast_flags_print_header.description`:

Description
-----------

Prints our own multicast flags including a more specific reason why
they are set, that is prints the bridge and querier state too, to
the debugfs table specified via \ ``seq``\ .

.. _`batadv_mcast_flags_seq_print_text`:

batadv_mcast_flags_seq_print_text
=================================

.. c:function:: int batadv_mcast_flags_seq_print_text(struct seq_file *seq, void *offset)

    print the mcast flags of other nodes

    :param struct seq_file \*seq:
        seq file to print on

    :param void \*offset:
        not used

.. _`batadv_mcast_flags_seq_print_text.description`:

Description
-----------

This prints a table of (primary) originators and their according
multicast flags, including (in the header) our own.

.. _`batadv_mcast_flags_seq_print_text.return`:

Return
------

always 0

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

