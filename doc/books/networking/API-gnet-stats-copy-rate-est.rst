
.. _API-gnet-stats-copy-rate-est:

========================
gnet_stats_copy_rate_est
========================

*man gnet_stats_copy_rate_est(9)*

*4.6.0-rc1*

copy rate estimator statistics into statistics TLV


Synopsis
========

.. c:function:: int gnet_stats_copy_rate_est( struct gnet_dump * d, const struct gnet_stats_basic_packed * b, struct gnet_stats_rate_est64 * r )

Arguments
=========

``d``
    dumping handle

``b``
    basic statistics

``r``
    rate estimator statistics


Description
===========

Appends the rate estimator statistics to the top level TLV created by ``gnet_stats_start_copy``.

Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.
