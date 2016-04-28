.. -*- coding: utf-8; mode: rst -*-

.. _API-gnet-stats-finish-copy:

======================
gnet_stats_finish_copy
======================

*man gnet_stats_finish_copy(9)*

*4.6.0-rc5*

finish dumping procedure


Synopsis
========

.. c:function:: int gnet_stats_finish_copy( struct gnet_dump * d )

Arguments
=========

``d``
    dumping handle


Description
===========

Corrects the length of the top level TLV to include all TLVs added by
``gnet_stats_copy_XXX`` calls. Adds the backward compatibility TLVs if
``gnet_stats_start_copy_compat`` was used and releases the statistics
lock.

Returns 0 on success or -1 with the statistic lock released if the room
in the socket buffer was not sufficient.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
