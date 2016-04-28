.. -*- coding: utf-8; mode: rst -*-

.. _API-ether-addr-equal:

================
ether_addr_equal
================

*man ether_addr_equal(9)*

*4.6.0-rc5*

Compare two Ethernet addresses


Synopsis
========

.. c:function:: bool ether_addr_equal( const u8 * addr1, const u8 * addr2 )

Arguments
=========

``addr1``
    Pointer to a six-byte array containing the Ethernet address

``addr2``
    Pointer other six-byte array containing the Ethernet address


Description
===========

Compare two Ethernet addresses, returns true if equal


Please note
===========

addr1 & addr2 must both be aligned to u16.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
