
.. _API-dev-get-stats:

=============
dev_get_stats
=============

*man dev_get_stats(9)*

*4.6.0-rc1*

get network device statistics


Synopsis
========

.. c:function:: struct rtnl_link_stats64 ⋆ dev_get_stats( struct net_device * dev, struct rtnl_link_stats64 * storage )

Arguments
=========

``dev``
    device to get statistics from

``storage``
    place to store stats


Description
===========

Get network statistics from device. Return ``storage``. The device driver may provide its own method by setting dev->netdev_ops->get_stats64 or dev->netdev_ops->get_stats;
otherwise the internal statistics structure is used.
