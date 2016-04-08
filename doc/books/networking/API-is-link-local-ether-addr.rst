
.. _API-is-link-local-ether-addr:

========================
is_link_local_ether_addr
========================

*man is_link_local_ether_addr(9)*

*4.6.0-rc1*

Determine if given Ethernet address is link-local


Synopsis
========

.. c:function:: bool is_link_local_ether_addr( const u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Return true if address is link local reserved addr (01:80:c2:00:00:0X) per IEEE 802.1Q 8.6.3 Frame filtering.


Please note
===========

addr must be aligned to u16.
