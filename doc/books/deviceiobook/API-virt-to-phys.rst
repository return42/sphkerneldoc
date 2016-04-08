
.. _API-virt-to-phys:

============
virt_to_phys
============

*man virt_to_phys(9)*

*4.6.0-rc1*

map virtual addresses to physical


Synopsis
========

.. c:function:: phys_addr_t virt_to_phys( volatile void * address )

Arguments
=========

``address``
    address to remap


Description
===========

The returned physical address is the physical (CPU) mapping for the memory address given. It is only valid to use this function on addresses directly mapped or allocated via
kmalloc.

This function does not give bus mappings for DMA transfers. In almost all conceivable cases a device driver should not be using this function
