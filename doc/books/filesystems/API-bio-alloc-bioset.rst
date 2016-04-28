.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-alloc-bioset:

================
bio_alloc_bioset
================

*man bio_alloc_bioset(9)*

*4.6.0-rc5*

allocate a bio for I/O


Synopsis
========

.. c:function:: struct bio * bio_alloc_bioset( gfp_t gfp_mask, int nr_iovecs, struct bio_set * bs )

Arguments
=========

``gfp_mask``
    the GFP_ mask given to the slab allocator

``nr_iovecs``
    number of iovecs to pre-allocate

``bs``
    the bio_set to allocate from.


Description
===========

If ``bs`` is NULL, uses ``kmalloc`` to allocate the bio; else the
allocation is backed by the ``bs``'s mempool.

When ``bs`` is not NULL, if ``__GFP_DIRECT_RECLAIM`` is set then
bio_alloc will always be able to allocate a bio. This is due to the
mempool guarantees. To make this work, callers must never allocate more
than 1 bio at a time from this pool. Callers that need to allocate more
than 1 bio must always submit the previously allocated bio for IO before
attempting to allocate a new one. Failure to do so can cause deadlocks
under memory pressure.

Note that when running under ``generic_make_request`` (i.e. any block
driver), bios are not submitted until after you return - see the code in
``generic_make_request`` that converts recursion into iteration, to
prevent stack overflows.

This would normally mean allocating multiple bios under
``generic_make_request`` would be susceptible to deadlocks, but we have
deadlock avoidance code that resubmits any blocked bios from a rescuer
thread.

However, we do not guarantee forward progress for allocations from other
mempools. Doing multiple allocations from the same mempool under
``generic_make_request`` should be avoided - instead, use bio_set's
front_pad for per bio allocations.


RETURNS
=======

Pointer to new bio on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
