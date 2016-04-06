
.. _API-vm-unmap-ram:

============
vm_unmap_ram
============

*man vm_unmap_ram(9)*

*4.6.0-rc1*

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
