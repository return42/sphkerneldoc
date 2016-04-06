
.. _API-unmap-kernel-range-noflush:

==========================
unmap_kernel_range_noflush
==========================

*man unmap_kernel_range_noflush(9)*

*4.6.0-rc1*

unmap kernel VM area


Synopsis
========

.. c:function:: void unmap_kernel_range_noflush( unsigned long addr, unsigned long size )

Arguments
=========

``addr``
    start of the VM area to unmap

``size``
    size of the VM area to unmap


Description
===========

Unmap PFN_UP( ``size``) pages at ``addr``. The VM area ``addr`` and ``size`` specify should have been allocated using ``get_vm_area`` and its friends.


NOTE
====

This function does NOT do any cache flushing. The caller is responsible for calling ``flush_cache_vunmap`` on to-be-mapped areas before calling this function and
``flush_tlb_kernel_range`` after.
