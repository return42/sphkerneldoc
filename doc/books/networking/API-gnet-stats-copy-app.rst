.. -*- coding: utf-8; mode: rst -*-

.. _API-gnet-stats-copy-app:

===================
gnet_stats_copy_app
===================

*man gnet_stats_copy_app(9)*

*4.6.0-rc5*

copy application specific statistics into statistics TLV


Synopsis
========

.. c:function:: int gnet_stats_copy_app( struct gnet_dump * d, void * st, int len )

Arguments
=========

``d``
    dumping handle

``st``
    application specific statistics data

``len``
    length of data


Description
===========

Appends the application specific statistics to the top level TLV created
by ``gnet_stats_start_copy`` and remembers the data for XSTATS if the
dumping handle is in backward compatibility mode.

Returns 0 on success or -1 with the statistic lock released if the room
in the socket buffer was not sufficient.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
