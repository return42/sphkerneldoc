.. -*- coding: utf-8; mode: rst -*-

==============
br_multicast.c
==============


.. _`br_multicast_list_adjacent`:

br_multicast_list_adjacent
==========================

.. c:function:: int br_multicast_list_adjacent (struct net_device *dev, struct list_head *br_ip_list)

    Returns snooped multicast addresses

    :param struct net_device \*dev:
        The bridge port adjacent to which to retrieve addresses

    :param struct list_head \*br_ip_list:
        The list to store found, snooped multicast IP addresses in



.. _`br_multicast_list_adjacent.description`:

Description
-----------

Creates a list of IP addresses (struct br_ip_list) sensed by the multicast
snooping feature on all bridge ports of dev's bridge device, excluding
the addresses from dev itself.

Returns the number of items added to br_ip_list.



.. _`br_multicast_list_adjacent.notes`:

Notes
-----

- br_ip_list needs to be initialized by caller
- br_ip_list might contain duplicates in the end

  (needs to be taken care of by caller)

- br_ip_list needs to be freed by caller



.. _`br_multicast_has_querier_anywhere`:

br_multicast_has_querier_anywhere
=================================

.. c:function:: bool br_multicast_has_querier_anywhere (struct net_device *dev, int proto)

    Checks for a querier on a bridge

    :param struct net_device \*dev:
        The bridge port providing the bridge on which to check for a querier

    :param int proto:
        The protocol family to check for: IGMP -> ETH_P_IP, MLD -> ETH_P_IPV6



.. _`br_multicast_has_querier_anywhere.description`:

Description
-----------

Checks whether the given interface has a bridge on top and if so returns
true if a valid querier exists anywhere on the bridged link layer.
Otherwise returns false.



.. _`br_multicast_has_querier_adjacent`:

br_multicast_has_querier_adjacent
=================================

.. c:function:: bool br_multicast_has_querier_adjacent (struct net_device *dev, int proto)

    Checks for a querier behind a bridge port

    :param struct net_device \*dev:
        The bridge port adjacent to which to check for a querier

    :param int proto:
        The protocol family to check for: IGMP -> ETH_P_IP, MLD -> ETH_P_IPV6



.. _`br_multicast_has_querier_adjacent.description`:

Description
-----------

Checks whether the given interface has a bridge on top and if so returns
true if a selected querier is behind one of the other ports of this
bridge. Otherwise returns false.

