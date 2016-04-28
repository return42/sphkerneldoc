.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-unmap-outb-region:

=====================
rio_unmap_outb_region
=====================

*man rio_unmap_outb_region(9)*

*4.6.0-rc5*

- Unmap the inbound memory region


Synopsis
========

.. c:function:: void rio_unmap_outb_region( struct rio_mport * mport, u16 destid, u64 rstart )

Arguments
=========

``mport``
    Master port

``destid``
    destination id mapping points to

``rstart``
    RIO base address window translates to


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
