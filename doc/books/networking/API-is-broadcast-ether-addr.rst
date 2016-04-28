.. -*- coding: utf-8; mode: rst -*-

.. _API-is-broadcast-ether-addr:

=======================
is_broadcast_ether_addr
=======================

*man is_broadcast_ether_addr(9)*

*4.6.0-rc5*

Determine if the Ethernet address is broadcast


Synopsis
========

.. c:function:: bool is_broadcast_ether_addr( const u8 * addr )

Arguments
=========

``addr``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Return true if the address is the broadcast address.


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
