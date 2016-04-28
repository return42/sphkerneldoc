.. -*- coding: utf-8; mode: rst -*-

.. _API-gen8-ppgtt-alloc-page-dirpointers:

=================================
gen8_ppgtt_alloc_page_dirpointers
=================================

*man gen8_ppgtt_alloc_page_dirpointers(9)*

*4.6.0-rc5*

Allocate pdps for VA range.


Synopsis
========

.. c:function:: int gen8_ppgtt_alloc_page_dirpointers( struct i915_address_space * vm, struct i915_pml4 * pml4, uint64_t start, uint64_t length, unsigned long * new_pdps )

Arguments
=========

``vm``
    Master vm structure.

``pml4``
    Page map level 4 for this address range.

``start``
    Starting virtual address to begin allocations.

``length``
    Size of the allocations.

``new_pdps``
    Bitmap set by function with new allocations. Likely used by the
    caller to free on error.


Description
===========

Allocate the required number of page directory pointers. Extremely
similar to ``gen8_ppgtt_alloc_page_directories`` and
``gen8_ppgtt_alloc_pagetabs``. The main difference is here we are
limited by the pml4 boundary (instead of the page directory pointer).


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
