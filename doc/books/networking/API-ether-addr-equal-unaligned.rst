.. -*- coding: utf-8; mode: rst -*-

.. _API-ether-addr-equal-unaligned:

==========================
ether_addr_equal_unaligned
==========================

*man ether_addr_equal_unaligned(9)*

*4.6.0-rc5*

Compare two not u16 aligned Ethernet addresses


Synopsis
========

.. c:function:: bool ether_addr_equal_unaligned( const u8 * addr1, const u8 * addr2 )

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

Use only when any Ethernet address may not be u16 aligned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
