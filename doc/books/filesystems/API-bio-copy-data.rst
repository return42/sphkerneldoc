
.. _API-bio-copy-data:

=============
bio_copy_data
=============

*man bio_copy_data(9)*

*4.6.0-rc1*

copy contents of data buffers from one chain of bios to another


Synopsis
========

.. c:function:: void bio_copy_data( struct bio * dst, struct bio * src )

Arguments
=========

``dst``
    destination bio list

``src``
    source bio list


Description
===========

If ``src`` and ``dst`` are single bios, bi_next must be NULL - otherwise, treats ``src`` and ``dst`` as linked lists of bios.

Stops when it reaches the end of either ``src`` or ``dst`` - that is, copies min(src->bi_size, dst->bi_size) bytes (or the equivalent for lists of bios).
