.. -*- coding: utf-8; mode: rst -*-

.. _API-is-valid-ether-addr:

===================
is_valid_ether_addr
===================

*man is_valid_ether_addr(9)*

*4.6.0-rc5*

Determine if the given Ethernet address is valid


Synopsis
========

.. c:function:: bool is_valid_ether_addr( const u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Check that the Ethernet address (MAC) is not 00:00:00:00:00:00, is not a
multicast address, and is not FF:FF:FF:FF:FF:FF.

Return true if the address is valid.


Please note
===========

addr must be aligned to u16.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
