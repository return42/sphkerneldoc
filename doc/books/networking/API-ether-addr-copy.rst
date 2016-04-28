.. -*- coding: utf-8; mode: rst -*-

.. _API-ether-addr-copy:

===============
ether_addr_copy
===============

*man ether_addr_copy(9)*

*4.6.0-rc5*

Copy an Ethernet address


Synopsis
========

.. c:function:: void ether_addr_copy( u8 * dst, const u8 * src )

Arguments
=========

``dst``
    Pointer to a six-byte array Ethernet address destination

``src``
    Pointer to a six-byte array Ethernet address source


Please note
===========

dst & src must both be aligned to u16.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
