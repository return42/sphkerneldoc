
.. _API-eth-broadcast-addr:

==================
eth_broadcast_addr
==================

*man eth_broadcast_addr(9)*

*4.6.0-rc1*

Assign broadcast address


Synopsis
========

.. c:function:: void eth_broadcast_addr( u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Assign the broadcast address to the given address array.
