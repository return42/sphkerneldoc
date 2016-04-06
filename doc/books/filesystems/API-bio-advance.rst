
.. _API-bio-advance:

===========
bio_advance
===========

*man bio_advance(9)*

*4.6.0-rc1*

increment/complete a bio by some number of bytes


Synopsis
========

.. c:function:: void bio_advance( struct bio * bio, unsigned bytes )

Arguments
=========

``bio``
    bio to advance

``bytes``
    number of bytes to complete


Description
===========

This updates bi_sector, bi_size and bi_idx; if the number of bytes to complete doesn't align with a bvec boundary, then bv_len and bv_offset will be updated on the last bvec
as well.

``bio`` will then represent the remaining, uncompleted portion of the io.
