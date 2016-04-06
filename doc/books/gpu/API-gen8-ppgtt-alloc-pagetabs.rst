
.. _API-gen8-ppgtt-alloc-pagetabs:

=========================
gen8_ppgtt_alloc_pagetabs
=========================

*man gen8_ppgtt_alloc_pagetabs(9)*

*4.6.0-rc1*

Allocate page tables for VA range.


Synopsis
========

.. c:function:: int gen8_ppgtt_alloc_pagetabs( struct i915_address_space * vm, struct i915_page_directory * pd, uint64_t start, uint64_t length, unsigned long * new_pts )

Arguments
=========

``vm``
    Master vm structure.

``pd``
    Page directory for this address range.

``start``
    Starting virtual address to begin allocations.

``length``
    Size of the allocations.

``new_pts``
    Bitmap set by function with new allocations. Likely used by the caller to free on error.


Description
===========

Allocate the required number of page tables. Extremely similar to ``gen8_ppgtt_alloc_page_directories``. The main difference is here we are limited by the page directory boundary
(instead of the page directory pointer). That boundary is 1GB virtual. Therefore, unlike ``gen8_ppgtt_alloc_page_directories``, it is possible, and likely that the caller will need
to use multiple calls of this function to achieve the appropriate allocation.


Return
======

0 if success; negative error code otherwise.
