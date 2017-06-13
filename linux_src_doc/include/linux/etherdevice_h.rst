.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/etherdevice.h

.. _`is_link_local_ether_addr`:

is_link_local_ether_addr
========================

.. c:function:: bool is_link_local_ether_addr(const u8 *addr)

    Determine if given Ethernet address is link-local

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_link_local_ether_addr.description`:

Description
-----------

Return true if address is link local reserved addr (01:80:c2:00:00:0X) per
IEEE 802.1Q 8.6.3 Frame filtering.

Please note: addr must be aligned to u16.

.. _`is_zero_ether_addr`:

is_zero_ether_addr
==================

.. c:function:: bool is_zero_ether_addr(const u8 *addr)

    Determine if give Ethernet address is all zeros.

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_zero_ether_addr.description`:

Description
-----------

Return true if the address is all zeroes.

Please note: addr must be aligned to u16.

.. _`is_multicast_ether_addr`:

is_multicast_ether_addr
=======================

.. c:function:: bool is_multicast_ether_addr(const u8 *addr)

    Determine if the Ethernet address is a multicast.

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_multicast_ether_addr.description`:

Description
-----------

Return true if the address is a multicast address.
By definition the broadcast address is also a multicast address.

.. _`is_local_ether_addr`:

is_local_ether_addr
===================

.. c:function:: bool is_local_ether_addr(const u8 *addr)

    Determine if the Ethernet address is locally-assigned one (IEEE 802).

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_local_ether_addr.description`:

Description
-----------

Return true if the address is a local address.

.. _`is_broadcast_ether_addr`:

is_broadcast_ether_addr
=======================

.. c:function:: bool is_broadcast_ether_addr(const u8 *addr)

    Determine if the Ethernet address is broadcast

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_broadcast_ether_addr.description`:

Description
-----------

Return true if the address is the broadcast address.

Please note: addr must be aligned to u16.

.. _`is_unicast_ether_addr`:

is_unicast_ether_addr
=====================

.. c:function:: bool is_unicast_ether_addr(const u8 *addr)

    Determine if the Ethernet address is unicast

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_unicast_ether_addr.description`:

Description
-----------

Return true if the address is a unicast address.

.. _`is_valid_ether_addr`:

is_valid_ether_addr
===================

.. c:function:: bool is_valid_ether_addr(const u8 *addr)

    Determine if the given Ethernet address is valid

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_valid_ether_addr.description`:

Description
-----------

Check that the Ethernet address (MAC) is not 00:00:00:00:00:00, is not
a multicast address, and is not FF:FF:FF:FF:FF:FF.

Return true if the address is valid.

Please note: addr must be aligned to u16.

.. _`eth_proto_is_802_3`:

eth_proto_is_802_3
==================

.. c:function:: bool eth_proto_is_802_3(__be16 proto)

    Determine if a given Ethertype/length is a protocol

    :param __be16 proto:
        Ethertype/length value to be tested

.. _`eth_proto_is_802_3.description`:

Description
-----------

Check that the value from the Ethertype/length field is a valid Ethertype.

Return true if the valid is an 802.3 supported Ethertype.

.. _`eth_random_addr`:

eth_random_addr
===============

.. c:function:: void eth_random_addr(u8 *addr)

    Generate software assigned random Ethernet address

    :param u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`eth_random_addr.description`:

Description
-----------

Generate a random Ethernet address (MAC) that is not multicast
and has the local assigned bit set.

.. _`eth_broadcast_addr`:

eth_broadcast_addr
==================

.. c:function:: void eth_broadcast_addr(u8 *addr)

    Assign broadcast address

    :param u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`eth_broadcast_addr.description`:

Description
-----------

Assign the broadcast address to the given address array.

.. _`eth_zero_addr`:

eth_zero_addr
=============

.. c:function:: void eth_zero_addr(u8 *addr)

    Assign zero address

    :param u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`eth_zero_addr.description`:

Description
-----------

Assign the zero address to the given address array.

.. _`eth_hw_addr_random`:

eth_hw_addr_random
==================

.. c:function:: void eth_hw_addr_random(struct net_device *dev)

    Generate software assigned random Ethernet and set device flag

    :param struct net_device \*dev:
        pointer to net_device structure

.. _`eth_hw_addr_random.description`:

Description
-----------

Generate a random Ethernet address (MAC) to be used by a net device
and set addr_assign_type so the state can be read by sysfs and be
used by userspace.

.. _`ether_addr_copy`:

ether_addr_copy
===============

.. c:function:: void ether_addr_copy(u8 *dst, const u8 *src)

    Copy an Ethernet address

    :param u8 \*dst:
        Pointer to a six-byte array Ethernet address destination

    :param const u8 \*src:
        Pointer to a six-byte array Ethernet address source

.. _`ether_addr_copy.description`:

Description
-----------

Please note: dst & src must both be aligned to u16.

.. _`eth_hw_addr_inherit`:

eth_hw_addr_inherit
===================

.. c:function:: void eth_hw_addr_inherit(struct net_device *dst, struct net_device *src)

    Copy dev_addr from another net_device

    :param struct net_device \*dst:
        pointer to net_device to copy dev_addr to

    :param struct net_device \*src:
        pointer to net_device to copy dev_addr from

.. _`eth_hw_addr_inherit.description`:

Description
-----------

Copy the Ethernet address from one net_device to another along with
the address attributes (addr_assign_type).

.. _`ether_addr_equal`:

ether_addr_equal
================

.. c:function:: bool ether_addr_equal(const u8 *addr1, const u8 *addr2)

    Compare two Ethernet addresses

    :param const u8 \*addr1:
        Pointer to a six-byte array containing the Ethernet address

    :param const u8 \*addr2:
        Pointer other six-byte array containing the Ethernet address

.. _`ether_addr_equal.description`:

Description
-----------

Compare two Ethernet addresses, returns true if equal

Please note: addr1 & addr2 must both be aligned to u16.

.. _`ether_addr_equal_64bits`:

ether_addr_equal_64bits
=======================

.. c:function:: bool ether_addr_equal_64bits(const u8 addr1, const u8 addr2)

    Compare two Ethernet addresses

    :param const u8 addr1:
        Pointer to an array of 8 bytes

    :param const u8 addr2:
        Pointer to an other array of 8 bytes

.. _`ether_addr_equal_64bits.description`:

Description
-----------

Compare two Ethernet addresses, returns true if equal, false otherwise.

The function doesn't need any conditional branches and possibly uses
word memory accesses on CPU allowing cheap unaligned memory reads.
arrays = { byte1, byte2, byte3, byte4, byte5, byte6, pad1, pad2 }

Please note that alignment of addr1 & addr2 are only guaranteed to be 16 bits.

.. _`ether_addr_equal_unaligned`:

ether_addr_equal_unaligned
==========================

.. c:function:: bool ether_addr_equal_unaligned(const u8 *addr1, const u8 *addr2)

    Compare two not u16 aligned Ethernet addresses

    :param const u8 \*addr1:
        Pointer to a six-byte array containing the Ethernet address

    :param const u8 \*addr2:
        Pointer other six-byte array containing the Ethernet address

.. _`ether_addr_equal_unaligned.description`:

Description
-----------

Compare two Ethernet addresses, returns true if equal

Please note: Use only when any Ethernet address may not be u16 aligned.

.. _`ether_addr_equal_masked`:

ether_addr_equal_masked
=======================

.. c:function:: bool ether_addr_equal_masked(const u8 *addr1, const u8 *addr2, const u8 *mask)

    Compare two Ethernet addresses with a mask

    :param const u8 \*addr1:
        Pointer to a six-byte array containing the 1st Ethernet address

    :param const u8 \*addr2:
        Pointer to a six-byte array containing the 2nd Ethernet address

    :param const u8 \*mask:
        Pointer to a six-byte array containing the Ethernet address bitmask

.. _`ether_addr_equal_masked.description`:

Description
-----------

Compare two Ethernet addresses with a mask, returns true if for every bit
set in the bitmask the equivalent bits in the ethernet addresses are equal.
Using a mask with all bits set is a slower ether_addr_equal.

.. _`ether_addr_to_u64`:

ether_addr_to_u64
=================

.. c:function:: u64 ether_addr_to_u64(const u8 *addr)

    Convert an Ethernet address into a u64 value.

    :param const u8 \*addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`ether_addr_to_u64.description`:

Description
-----------

Return a u64 value of the address

.. _`u64_to_ether_addr`:

u64_to_ether_addr
=================

.. c:function:: void u64_to_ether_addr(u64 u, u8 *addr)

    Convert a u64 to an Ethernet address.

    :param u64 u:
        u64 to convert to an Ethernet MAC address

    :param u8 \*addr:
        Pointer to a six-byte array to contain the Ethernet address

.. _`eth_addr_dec`:

eth_addr_dec
============

.. c:function:: void eth_addr_dec(u8 *addr)

    Decrement the given MAC address

    :param u8 \*addr:
        Pointer to a six-byte array containing Ethernet address to decrement

.. _`is_etherdev_addr`:

is_etherdev_addr
================

.. c:function:: bool is_etherdev_addr(const struct net_device *dev, const u8 addr)

    Tell if given Ethernet address belongs to the device.

    :param const struct net_device \*dev:
        Pointer to a device structure

    :param const u8 addr:
        Pointer to a six-byte array containing the Ethernet address

.. _`is_etherdev_addr.description`:

Description
-----------

Compare passed address with all addresses of the device. Return true if the
address if one of the device addresses.

Note that this function calls \ :c:func:`ether_addr_equal_64bits`\  so take care of
the right padding.

.. _`compare_ether_header`:

compare_ether_header
====================

.. c:function:: unsigned long compare_ether_header(const void *a, const void *b)

    Compare two Ethernet headers

    :param const void \*a:
        Pointer to Ethernet header

    :param const void \*b:
        Pointer to Ethernet header

.. _`compare_ether_header.description`:

Description
-----------

Compare two Ethernet headers, returns 0 if equal.
This assumes that the network header (i.e., IP header) is 4-byte
aligned OR the platform can handle unaligned access.  This is the
case for all packets coming into netif_receive_skb or similar
entry points.

.. _`eth_skb_pad`:

eth_skb_pad
===========

.. c:function:: int eth_skb_pad(struct sk_buff *skb)

    Pad buffer to mininum number of octets for Ethernet frame

    :param struct sk_buff \*skb:
        Buffer to pad

.. _`eth_skb_pad.description`:

Description
-----------

An Ethernet frame should have a minimum size of 60 bytes.  This function
takes short frames and pads them with zeros up to the 60 byte limit.

.. This file was automatic generated / don't edit.

