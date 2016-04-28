.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-integrity-compare:

=====================
blk_integrity_compare
=====================

*man blk_integrity_compare(9)*

*4.6.0-rc5*

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

Meta-devices like DM and MD need to verify that all sub-devices use the
same integrity format before advertising to upper layers that they can
send/receive integrity metadata. This function can be used to check
whether two gendisk devices have compatible integrity formats.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
