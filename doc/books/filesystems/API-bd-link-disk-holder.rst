
.. _API-bd-link-disk-holder:

===================
bd_link_disk_holder
===================

*man bd_link_disk_holder(9)*

*4.6.0-rc1*

create symlinks between holding disk and slave bdev


Synopsis
========

.. c:function:: int bd_link_disk_holder( struct block_device * bdev, struct gendisk * disk )

Arguments
=========

``bdev``
    the claimed slave bdev

``disk``
    the holding disk


Description
===========

DON'T USE THIS UNLESS YOU'RE ALREADY USING IT.

This functions creates the following sysfs symlinks.

- from “slaves” directory of the holder ``disk`` to the claimed ``bdev`` - from “holders” directory of the ``bdev`` to the holder ``disk``

For example, if /dev/dm-0 maps to /dev/sda and disk for dm-0 is passed to ``bd_link_disk_holder``, then:

/sys/block/dm-0/slaves/sda --> /sys/block/sda /sys/block/sda/holders/dm-0 --> /sys/block/dm-0

The caller must have claimed ``bdev`` before calling this function and ensure that both ``bdev`` and ``disk`` are valid during the creation and lifetime of these symlinks.


CONTEXT
=======

Might sleep.


RETURNS
=======

0 on success, -errno on failure.
