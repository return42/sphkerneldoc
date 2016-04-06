
.. _API-bio-copy-kern:

=============
bio_copy_kern
=============

*man bio_copy_kern(9)*

*4.6.0-rc1*

copy kernel address into bio


Synopsis
========

.. c:function:: struct bio ⋆ bio_copy_kern( struct request_queue * q, void * data, unsigned int len, gfp_t gfp_mask, int reading )

Arguments
=========

``q``
    the struct request_queue for the bio

``data``
    pointer to buffer to copy

``len``
    length in bytes

``gfp_mask``
    allocation flags for bio and page allocation

``reading``
    data direction is READ


Description
===========

copy the kernel address into a bio suitable for io to a block device. Returns an error pointer in case of error.
