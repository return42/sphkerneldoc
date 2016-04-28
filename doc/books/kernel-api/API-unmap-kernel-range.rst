.. -*- coding: utf-8; mode: rst -*-

.. _API-unmap-kernel-range:

==================
unmap_kernel_range
==================

*man unmap_kernel_range(9)*

*4.6.0-rc5*

unmap kernel VM area and flush cache and TLB


Synopsis
========

.. c:function:: void unmap_kernel_range( unsigned long addr, unsigned long size )

Arguments
=========

``addr``
    start of the VM area to unmap

``size``
    size of the VM area to unmap


Description
===========

Similar to ``unmap_kernel_range_noflush`` but flushes vcache before the
unmapping and tlb after.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
