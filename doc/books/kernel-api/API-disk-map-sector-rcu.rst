
.. _API-disk-map-sector-rcu:

===================
disk_map_sector_rcu
===================

*man disk_map_sector_rcu(9)*

*4.6.0-rc1*

map sector to partition


Synopsis
========

.. c:function:: struct hd_struct ⋆ disk_map_sector_rcu( struct gendisk * disk, sector_t sector )

Arguments
=========

``disk``
    gendisk of interest

``sector``
    sector to map


Description
===========

Find out which partition ``sector`` maps to on ``disk``. This is primarily used for stats accounting.


CONTEXT
=======

RCU read locked. The returned partition pointer is valid only while preemption is disabled.


RETURNS
=======

Found partition on success, part0 is returned if no partition matches
