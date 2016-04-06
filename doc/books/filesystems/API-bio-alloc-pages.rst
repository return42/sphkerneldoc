
.. _API-bio-alloc-pages:

===============
bio_alloc_pages
===============

*man bio_alloc_pages(9)*

*4.6.0-rc1*

allocates a single page for each bvec in a bio


Synopsis
========

.. c:function:: int bio_alloc_pages( struct bio * bio, gfp_t gfp_mask )

Arguments
=========

``bio``
    bio to allocate pages for

``gfp_mask``
    flags for allocation


Description
===========

Allocates pages up to ``bio``->bi_vcnt.

Returns 0 on success, -ENOMEM on failure. On failure, any allocated pages are freed.
