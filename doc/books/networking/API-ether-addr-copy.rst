
.. _API-ether-addr-copy:

===============
ether_addr_copy
===============

*man ether_addr_copy(9)*

*4.6.0-rc1*

Copy an Ethernet address


Synopsis
========

.. c:function:: void ether_addr_copy( u8 * dst, const u8 * src )

Arguments
=========

``dst``
    Pointer to a six-byte array Ethernet address destination

``src``
    Pointer to a six-byte array Ethernet address source


Please note
===========

dst & src must both be aligned to u16.
