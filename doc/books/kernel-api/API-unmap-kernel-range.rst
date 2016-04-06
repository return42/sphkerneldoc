
.. _API-unmap-kernel-range:

==================
unmap_kernel_range
==================

*man unmap_kernel_range(9)*

*4.6.0-rc1*

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

Similar to ``unmap_kernel_range_noflush`` but flushes vcache before the unmapping and tlb after.
