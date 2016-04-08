
.. _API-eth-random-addr:

===============
eth_random_addr
===============

*man eth_random_addr(9)*

*4.6.0-rc1*

Generate software assigned random Ethernet address


Synopsis
========

.. c:function:: void eth_random_addr( u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Generate a random Ethernet address (MAC) that is not multicast and has the local assigned bit set.
