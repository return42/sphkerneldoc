
.. _API-is-local-ether-addr:

===================
is_local_ether_addr
===================

*man is_local_ether_addr(9)*

*4.6.0-rc1*

Determine if the Ethernet address is locally-assigned one (IEEE 802).


Synopsis
========

.. c:function:: bool is_local_ether_addr( const u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Return true if the address is a local address.
