
.. _API-rio-map-outb-region:

===================
rio_map_outb_region
===================

*man rio_map_outb_region(9)*

*4.6.0-rc1*

- Map outbound memory region.


Synopsis
========

.. c:function:: int rio_map_outb_region( struct rio_mport * mport, u16 destid, u64 rbase, u32 size, u32 rflags, dma_addr_t * local )

Arguments
=========

``mport``
    Master port.

``destid``
    destination id window points to

``rbase``
    RIO base address window translates to

``size``
    Size of the memory region

``rflags``
    Flags for mapping.

``local``
    physical address of memory region mapped


Return
======

0 -- Success.

This function will create the mapping from RIO space to local memory.
