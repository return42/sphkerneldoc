
.. _API-blk-integrity-compare:

=====================
blk_integrity_compare
=====================

*man blk_integrity_compare(9)*

*4.6.0-rc1*

Compare integrity profile of two disks


Synopsis
========

.. c:function:: int blk_integrity_compare( struct gendisk * gd1, struct gendisk * gd2 )

Arguments
=========

``gd1``
    Disk to compare

``gd2``
    Disk to compare


Description
===========

Meta-devices like DM and MD need to verify that all sub-devices use the same integrity format before advertising to upper layers that they can send/receive integrity metadata. This
function can be used to check whether two gendisk devices have compatible integrity formats.
