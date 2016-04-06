
.. _API-bio-clone-bioset:

================
bio_clone_bioset
================

*man bio_clone_bioset(9)*

*4.6.0-rc1*

clone a bio


Synopsis
========

.. c:function:: struct bio ⋆ bio_clone_bioset( struct bio * bio_src, gfp_t gfp_mask, struct bio_set * bs )

Arguments
=========

``bio_src``
    bio to clone

``gfp_mask``
    allocation priority

``bs``
    bio_set to allocate from


Description
===========

Clone bio. Caller will own the returned bio, but not the actual data it points to. Reference count of returned bio will be one.
