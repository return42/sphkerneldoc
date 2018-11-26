.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ethernet/eth.c

.. _`eth_header`:

eth_header
==========

.. c:function:: int eth_header(struct sk_buff *skb, struct net_device *dev, unsigned short type, const void *daddr, const void *saddr, unsigned int len)

    create the Ethernet header

    :param skb:
        buffer to alter
    :type skb: struct sk_buff \*

    :param dev:
        source device
    :type dev: struct net_device \*

    :param type:
        Ethernet type field
    :type type: unsigned short

    :param daddr:
        destination address (NULL leave destination address)
    :type daddr: const void \*

    :param saddr:
        source address (NULL use device source address)
    :type saddr: const void \*

    :param len:
        packet length (<= skb->len)
    :type len: unsigned int

.. _`eth_header.description`:

Description
-----------


Set the protocol type. For a packet of type ETH_P_802_3/2 we put the length
in here instead.

.. _`eth_get_headlen`:

eth_get_headlen
===============

.. c:function:: u32 eth_get_headlen(void *data, unsigned int len)

    determine the length of header for an ethernet frame

    :param data:
        pointer to start of frame
    :type data: void \*

    :param len:
        total length of frame
    :type len: unsigned int

.. _`eth_get_headlen.description`:

Description
-----------

Make a best effort attempt to pull the length for all of the headers for
a given frame in a linear buffer.

.. _`eth_type_trans`:

eth_type_trans
==============

.. c:function:: __be16 eth_type_trans(struct sk_buff *skb, struct net_device *dev)

    determine the packet's protocol ID.

    :param skb:
        received socket data
    :type skb: struct sk_buff \*

    :param dev:
        receiving network device
    :type dev: struct net_device \*

.. _`eth_type_trans.description`:

Description
-----------

The rule here is that we
assume 802.3 if the type field is short enough to be a length.
This is normal practice and works for any 'now in use' protocol.

.. _`eth_header_parse`:

eth_header_parse
================

.. c:function:: int eth_header_parse(const struct sk_buff *skb, unsigned char *haddr)

    extract hardware address from packet

    :param skb:
        packet to extract header from
    :type skb: const struct sk_buff \*

    :param haddr:
        destination buffer
    :type haddr: unsigned char \*

.. _`eth_header_cache`:

eth_header_cache
================

.. c:function:: int eth_header_cache(const struct neighbour *neigh, struct hh_cache *hh, __be16 type)

    fill cache entry from neighbour

    :param neigh:
        source neighbour
    :type neigh: const struct neighbour \*

    :param hh:
        destination cache entry
    :type hh: struct hh_cache \*

    :param type:
        Ethernet type field
    :type type: __be16

.. _`eth_header_cache.description`:

Description
-----------

Create an Ethernet header template from the neighbour.

.. _`eth_header_cache_update`:

eth_header_cache_update
=======================

.. c:function:: void eth_header_cache_update(struct hh_cache *hh, const struct net_device *dev, const unsigned char *haddr)

    update cache entry

    :param hh:
        destination cache entry
    :type hh: struct hh_cache \*

    :param dev:
        network device
    :type dev: const struct net_device \*

    :param haddr:
        new hardware address
    :type haddr: const unsigned char \*

.. _`eth_header_cache_update.description`:

Description
-----------

Called by Address Resolution module to notify changes in address.

.. _`eth_prepare_mac_addr_change`:

eth_prepare_mac_addr_change
===========================

.. c:function:: int eth_prepare_mac_addr_change(struct net_device *dev, void *p)

    prepare for mac change

    :param dev:
        network device
    :type dev: struct net_device \*

    :param p:
        socket address
    :type p: void \*

.. _`eth_commit_mac_addr_change`:

eth_commit_mac_addr_change
==========================

.. c:function:: void eth_commit_mac_addr_change(struct net_device *dev, void *p)

    commit mac change

    :param dev:
        network device
    :type dev: struct net_device \*

    :param p:
        socket address
    :type p: void \*

.. _`eth_mac_addr`:

eth_mac_addr
============

.. c:function:: int eth_mac_addr(struct net_device *dev, void *p)

    set new Ethernet hardware address

    :param dev:
        network device
    :type dev: struct net_device \*

    :param p:
        socket address
    :type p: void \*

.. _`eth_mac_addr.description`:

Description
-----------

Change hardware address of device.

This doesn't change hardware matching, so needs to be overridden
for most real devices.

.. _`eth_change_mtu`:

eth_change_mtu
==============

.. c:function:: int eth_change_mtu(struct net_device *dev, int new_mtu)

    set new MTU size

    :param dev:
        network device
    :type dev: struct net_device \*

    :param new_mtu:
        new Maximum Transfer Unit
    :type new_mtu: int

.. _`eth_change_mtu.description`:

Description
-----------

Allow changing MTU size. Needs to be overridden for devices
supporting jumbo frames.

.. _`ether_setup`:

ether_setup
===========

.. c:function:: void ether_setup(struct net_device *dev)

    setup Ethernet network device

    :param dev:
        network device
    :type dev: struct net_device \*

.. _`ether_setup.description`:

Description
-----------

Fill in the fields of the device structure with Ethernet-generic values.

.. _`alloc_etherdev_mqs`:

alloc_etherdev_mqs
==================

.. c:function:: struct net_device *alloc_etherdev_mqs(int sizeof_priv, unsigned int txqs, unsigned int rxqs)

    Allocates and sets up an Ethernet device

    :param sizeof_priv:
        Size of additional driver-private structure to be allocated
        for this Ethernet device
    :type sizeof_priv: int

    :param txqs:
        The number of TX queues this device has.
    :type txqs: unsigned int

    :param rxqs:
        The number of RX queues this device has.
    :type rxqs: unsigned int

.. _`alloc_etherdev_mqs.description`:

Description
-----------

Fill in the fields of the device structure with Ethernet-generic
values. Basically does everything except registering the device.

Constructs a new net device, complete with a private data area of
size (sizeof_priv).  A 32-byte (not bit) alignment is enforced for
this private data area.

.. This file was automatic generated / don't edit.

