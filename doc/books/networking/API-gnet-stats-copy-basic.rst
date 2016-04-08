
.. _API-gnet-stats-copy-basic:

=====================
gnet_stats_copy_basic
=====================

*man gnet_stats_copy_basic(9)*

*4.6.0-rc1*

copy basic statistics into statistic TLV


Synopsis
========

.. c:function:: int gnet_stats_copy_basic( struct gnet_dump * d, struct gnet_stats_basic_cpu __percpu * cpu, struct gnet_stats_basic_packed * b )

Arguments
=========

``d``
    dumping handle

``cpu``
    copy statistic per cpu

``b``
    basic statistics


Description
===========

Appends the basic statistics to the top level TLV created by ``gnet_stats_start_copy``.

Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.
