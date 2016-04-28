.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-random-addr:

===============
eth_random_addr
===============

*man eth_random_addr(9)*

*4.6.0-rc5*

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

Generate a random Ethernet address (MAC) that is not multicast and has
the local assigned bit set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
