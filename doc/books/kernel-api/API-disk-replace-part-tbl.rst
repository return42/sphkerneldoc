.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-replace-part-tbl:

=====================
disk_replace_part_tbl
=====================

*man disk_replace_part_tbl(9)*

*4.6.0-rc5*

replace disk->part_tbl in RCU-safe way


Synopsis
========

.. c:function:: void disk_replace_part_tbl( struct gendisk * disk, struct disk_part_tbl * new_ptbl )

Arguments
=========

``disk``
    disk to replace part_tbl for

``new_ptbl``
    new part_tbl to install


Description
===========

Replace disk->part_tbl with ``new_ptbl`` in RCU-safe way. The original
ptbl is freed using RCU callback.


LOCKING
=======

Matching bd_mutx locked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
