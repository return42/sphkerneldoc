
.. _API-is-multicast-ether-addr:

=======================
is_multicast_ether_addr
=======================

*man is_multicast_ether_addr(9)*

*4.6.0-rc1*

Determine if the Ethernet address is a multicast.


Synopsis
========

.. c:function:: bool is_multicast_ether_addr( const u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Return true if the address is a multicast address. By definition the broadcast address is also a multicast address.
