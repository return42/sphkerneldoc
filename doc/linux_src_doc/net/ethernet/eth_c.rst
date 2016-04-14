.. -*- coding: utf-8; mode: rst -*-

=====
eth.c
=====

.. _`eth_header`:

eth_header
==========

.. c:function:: int eth_header (struct sk_buff *skb, struct net_device *dev, unsigned short type, const void *daddr, const void *saddr, unsigned int len)

    create the Ethernet header

    :param struct sk_buff \*skb:
        buffer to alter

    :param struct net_device \*dev:
        source device

    :param unsigned short type:
        Ethernet type field

    :param const void \*daddr:
        destination address (NULL leave destination address)

    :param const void \*saddr:
        source address (NULL use device source address)

    :param unsigned int len:
        packet length (<= skb->len)


.. _`eth_header.description`:

Description
-----------


Set the protocol type. For a packet of type ETH_P_802_3/2 we put the length
in here instead.


.. _`eth_get_headlen`:

eth_get_headlen
===============

.. c:function:: u32 eth_get_headlen (void *data, unsigned int len)

    determine the length of header for an ethernet frame

    :param void \*data:
        pointer to start of frame

    :param unsigned int len:
        total length of frame


.. _`eth_get_headlen.description`:

Description
-----------

Make a best effort attempt to pull the length for all of the headers for
a given frame in a linear buffer.


.. _`eth_type_trans`:

eth_type_trans
==============

.. c:function:: __be16 eth_type_trans (struct sk_buff *skb, struct net_device *dev)

    determine the packet's protocol ID.

    :param struct sk_buff \*skb:
        received socket data

    :param struct net_device \*dev:
        receiving network device


.. _`eth_type_trans.description`:

Description
-----------

The rule here is that we
assume 802.3 if the type field is short enough to be a length.
This is normal practice and works for any 'now in use' protocol.


.. _`eth_header_parse`:

eth_header_parse
================

.. c:function:: int eth_header_parse (const struct sk_buff *skb, unsigned char *haddr)

    extract hardware address from packet

    :param const struct sk_buff \*skb:
        packet to extract header from

    :param unsigned char \*haddr:
        destination buffer


.. _`eth_header_cache`:

eth_header_cache
================

.. c:function:: int eth_header_cache (const struct neighbour *neigh, struct hh_cache *hh, __be16 type)

    fill cache entry from neighbour

    :param const struct neighbour \*neigh:
        source neighbour

    :param struct hh_cache \*hh:
        destination cache entry

    :param __be16 type:
        Ethernet type field


.. _`eth_header_cache.description`:

Description
-----------

Create an Ethernet header template from the neighbour.


.. _`eth_header_cache_update`:

eth_header_cache_update
=======================

.. c:function:: void eth_header_cache_update (struct hh_cache *hh, const struct net_device *dev, const unsigned char *haddr)

    update cache entry

    :param struct hh_cache \*hh:
        destination cache entry

    :param const struct net_device \*dev:
        network device

    :param const unsigned char \*haddr:
        new hardware address


.. _`eth_header_cache_update.description`:

Description
-----------

Called by Address Resolution module to notify changes in address.


.. _`eth_prepare_mac_addr_change`:

eth_prepare_mac_addr_change
===========================

.. c:function:: int eth_prepare_mac_addr_change (struct net_device *dev, void *p)

    prepare for mac change

    :param struct net_device \*dev:
        network device

    :param void \*p:
        socket address


.. _`eth_commit_mac_addr_change`:

eth_commit_mac_addr_change
==========================

.. c:function:: void eth_commit_mac_addr_change (struct net_device *dev, void *p)

    commit mac change

    :param struct net_device \*dev:
        network device

    :param void \*p:
        socket address


.. _`eth_mac_addr`:

eth_mac_addr
============

.. c:function:: int eth_mac_addr (struct net_device *dev, void *p)

    set new Ethernet hardware address

    :param struct net_device \*dev:
        network device

    :param void \*p:
        socket address


.. _`eth_mac_addr.description`:

Description
-----------

Change hardware address of device.

This doesn't change hardware matching, so needs to be overridden
for most real devices.


.. _`eth_change_mtu`:

eth_change_mtu
==============

.. c:function:: int eth_change_mtu (struct net_device *dev, int new_mtu)

    set new MTU size

    :param struct net_device \*dev:
        network device

    :param int new_mtu:
        new Maximum Transfer Unit


.. _`eth_change_mtu.description`:

Description
-----------

Allow changing MTU size. Needs to be overridden for devices
supporting jumbo frames.


.. _`ether_setup`:

ether_setup
===========

.. c:function:: void ether_setup (struct net_device *dev)

    setup Ethernet network device

    :param struct net_device \*dev:
        network device


.. _`ether_setup.description`:

Description
-----------

Fill in the fields of the device structure with Ethernet-generic values.


.. _`alloc_etherdev_mqs`:

alloc_etherdev_mqs
==================

.. c:function:: struct net_device *alloc_etherdev_mqs (int sizeof_priv, unsigned int txqs, unsigned int rxqs)

    Allocates and sets up an Ethernet device

    :param int sizeof_priv:
        Size of additional driver-private structure to be allocated
        for this Ethernet device

    :param unsigned int txqs:
        The number of TX queues this device has.

    :param unsigned int rxqs:
        The number of RX queues this device has.


.. _`alloc_etherdev_mqs.description`:

Description
-----------

Fill in the fields of the device structure with Ethernet-generic
values. Basically does everything except registering the device.

Constructs a new net device, complete with a private data area of
size (sizeof_priv).  A 32-byte (not bit) alignment is enforced for
this private data area.

