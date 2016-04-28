.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-map-sector-rcu:

===================
disk_map_sector_rcu
===================

*man disk_map_sector_rcu(9)*

*4.6.0-rc5*

map sector to partition


Synopsis
========

.. c:function:: struct hd_struct * disk_map_sector_rcu( struct gendisk * disk, sector_t sector )

Arguments
=========

``disk``
    gendisk of interest

``sector``
    sector to map


Description
===========

Find out which partition ``sector`` maps to on ``disk``. This is
primarily used for stats accounting.


CONTEXT
=======

RCU read locked. The returned partition pointer is valid only while
preemption is disabled.


RETURNS
=======

Found partition on success, part0 is returned if no partition matches


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
