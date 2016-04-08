
.. _API-rio-unmap-outb-region:

=====================
rio_unmap_outb_region
=====================

*man rio_unmap_outb_region(9)*

*4.6.0-rc1*

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
