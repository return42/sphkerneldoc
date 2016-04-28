.. -*- coding: utf-8; mode: rst -*-

.. _API-vm-unmap-ram:

============
vm_unmap_ram
============

*man vm_unmap_ram(9)*

*4.6.0-rc5*

unmap linear kernel address space set up by vm_map_ram


Synopsis
========

.. c:function:: void vm_unmap_ram( const void * mem, unsigned int count )

Arguments
=========

``mem``
    the pointer returned by vm_map_ram

``count``
    the count passed to that vm_map_ram call (cannot unmap partial)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
