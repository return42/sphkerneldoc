.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-expand-part-tbl:

====================
disk_expand_part_tbl
====================

*man disk_expand_part_tbl(9)*

*4.6.0-rc5*

expand disk->part_tbl


Synopsis
========

.. c:function:: int disk_expand_part_tbl( struct gendisk * disk, int partno )

Arguments
=========

``disk``
    disk to expand part_tbl for

``partno``
    expand such that this partno can fit in


Description
===========

Expand disk->part_tbl such that ``partno`` can fit in. disk->part_tbl
uses RCU to allow unlocked dereferencing for stats and other stuff.


LOCKING
=======

Matching bd_mutex locked, might sleep.


RETURNS
=======

0 on success, -errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
