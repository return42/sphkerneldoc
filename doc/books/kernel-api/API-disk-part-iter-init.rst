
.. _API-disk-part-iter-init:

===================
disk_part_iter_init
===================

*man disk_part_iter_init(9)*

*4.6.0-rc1*

initialize partition iterator


Synopsis
========

.. c:function:: void disk_part_iter_init( struct disk_part_iter * piter, struct gendisk * disk, unsigned int flags )

Arguments
=========

``piter``
    iterator to initialize

``disk``
    disk to iterate over

``flags``
    DISK_PITER_⋆ flags


Description
===========

Initialize ``piter`` so that it iterates over partitions of ``disk``.


CONTEXT
=======

Don't care.
