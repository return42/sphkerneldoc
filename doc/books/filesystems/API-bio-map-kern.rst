
.. _API-bio-map-kern:

============
bio_map_kern
============

*man bio_map_kern(9)*

*4.6.0-rc1*

map kernel address into bio


Synopsis
========

.. c:function:: struct bio ⋆ bio_map_kern( struct request_queue * q, void * data, unsigned int len, gfp_t gfp_mask )

Arguments
=========

``q``
    the struct request_queue for the bio

``data``
    pointer to buffer to map

``len``
    length in bytes

``gfp_mask``
    allocation flags for bio allocation


Description
===========

Map the kernel address into a bio suitable for io to a block device. Returns an error pointer in case of error.
