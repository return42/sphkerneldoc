
.. _API-gnet-stats-finish-copy:

======================
gnet_stats_finish_copy
======================

*man gnet_stats_finish_copy(9)*

*4.6.0-rc1*

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

Corrects the length of the top level TLV to include all TLVs added by ``gnet_stats_copy_XXX`` calls. Adds the backward compatibility TLVs if ``gnet_stats_start_copy_compat`` was
used and releases the statistics lock.

Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.
