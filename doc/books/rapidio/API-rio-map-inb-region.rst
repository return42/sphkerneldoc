
.. _API-rio-map-inb-region:

==================
rio_map_inb_region
==================

*man rio_map_inb_region(9)*

*4.6.0-rc1*

- Map inbound memory region.


Synopsis
========

.. c:function:: int rio_map_inb_region( struct rio_mport * mport, dma_addr_t local, u64 rbase, u32 size, u32 rflags )

Arguments
=========

``mport``
    Master port.

``local``
    physical address of memory region to be mapped

``rbase``
    RIO base address assigned to this window

``size``
    Size of the memory region

``rflags``
    Flags for mapping.


Return
======

0 -- Success.

This function will create the mapping from RIO space to local memory.
