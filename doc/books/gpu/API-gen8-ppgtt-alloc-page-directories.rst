.. -*- coding: utf-8; mode: rst -*-

.. _API-gen8-ppgtt-alloc-page-directories:

=================================
gen8_ppgtt_alloc_page_directories
=================================

*man gen8_ppgtt_alloc_page_directories(9)*

*4.6.0-rc5*

Allocate page directories for VA range.


Synopsis
========

.. c:function:: int gen8_ppgtt_alloc_page_directories( struct i915_address_space * vm, struct i915_page_directory_pointer * pdp, uint64_t start, uint64_t length, unsigned long * new_pds )

Arguments
=========

``vm``
    Master vm structure.

``pdp``
    Page directory pointer for this address range.

``start``
    Starting virtual address to begin allocations.

``length``
    Size of the allocations.

``new_pds``
    Bitmap set by function with new allocations. Likely used by the
    caller to free on error.


Description
===========

Allocate the required number of page directories starting at the pde
index of ``start``, and ending at the pde index ``start`` + ``length``.
This function will skip over already allocated page directories within
the range, and only allocate new ones, setting the appropriate pointer
within the pdp as well as the correct position in the bitmap
``new_pds``.

The function will only allocate the pages within the range for a give
page directory pointer. In other words, if ``start`` + ``length``
straddles a virtually addressed PDP boundary (512GB for 4k pages), there
will be more allocations required by the caller, This is not currently
possible, and the BUG in the code will prevent it.


Return
======

0 if success; negative error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
