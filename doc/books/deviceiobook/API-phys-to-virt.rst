.. -*- coding: utf-8; mode: rst -*-

.. _API-phys-to-virt:

============
phys_to_virt
============

*man phys_to_virt(9)*

*4.6.0-rc5*

map physical address to virtual


Synopsis
========

.. c:function:: void * phys_to_virt( phys_addr_t address )

Arguments
=========

``address``
    address to remap


Description
===========

The returned virtual address is a current CPU mapping for the memory
address given. It is only valid to use this function on addresses that
have a kernel mapping

This function does not handle bus mappings for DMA transfers. In almost
all conceivable cases a device driver should not be using this function


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
