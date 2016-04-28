.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-unmap-inb-region:

====================
rio_unmap_inb_region
====================

*man rio_unmap_inb_region(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
