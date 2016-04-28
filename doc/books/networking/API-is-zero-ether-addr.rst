.. -*- coding: utf-8; mode: rst -*-

.. _API-is-zero-ether-addr:

==================
is_zero_ether_addr
==================

*man is_zero_ether_addr(9)*

*4.6.0-rc5*

Determine if give Ethernet address is all zeros.


Synopsis
========

.. c:function:: bool is_zero_ether_addr( const u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Return true if the address is all zeroes.


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
