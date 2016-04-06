
.. _API-bd-unlink-disk-holder:

=====================
bd_unlink_disk_holder
=====================

*man bd_unlink_disk_holder(9)*

*4.6.0-rc1*

destroy symlinks created by ``bd_link_disk_holder``


Synopsis
========

.. c:function:: void bd_unlink_disk_holder( struct block_device * bdev, struct gendisk * disk )

Arguments
=========

``bdev``
    the calimed slave bdev

``disk``
    the holding disk


Description
===========

DON'T USE THIS UNLESS YOU'RE ALREADY USING IT.


CONTEXT
=======

Might sleep.
