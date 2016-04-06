
.. _API-bio-split:

=========
bio_split
=========

*man bio_split(9)*

*4.6.0-rc1*

split a bio


Synopsis
========

.. c:function:: struct bio ⋆ bio_split( struct bio * bio, int sectors, gfp_t gfp, struct bio_set * bs )

Arguments
=========

``bio``
    bio to split

``sectors``
    number of sectors to split from the front of ``bio``

``gfp``
    gfp mask

``bs``
    bio set to allocate from


Description
===========

Allocates and returns a new bio which represents ``sectors`` from the start of ``bio``, and updates ``bio`` to represent the remaining sectors.

Unless this is a discard request the newly allocated bio will point to ``bio``'s bi_io_vec; it is the caller's responsibility to ensure that ``bio`` is not freed before the
split.
