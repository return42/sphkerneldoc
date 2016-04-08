
.. _API-rio-unmap-inb-region:

====================
rio_unmap_inb_region
====================

*man rio_unmap_inb_region(9)*

*4.6.0-rc1*

- Unmap the inbound memory region


Synopsis
========

.. c:function:: void rio_unmap_inb_region( struct rio_mport * mport, dma_addr_t lstart )

Arguments
=========

``mport``
    Master port

``lstart``
    physical address of memory region to be unmapped
