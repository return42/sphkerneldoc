
.. _API-rps-may-expire-flow:

===================
rps_may_expire_flow
===================

*man rps_may_expire_flow(9)*

*4.6.0-rc1*

check whether an RFS hardware filter may be removed


Synopsis
========

.. c:function:: bool rps_may_expire_flow( struct net_device * dev, u16 rxq_index, u32 flow_id, u16 filter_id )

Arguments
=========

``dev``
    Device on which the filter was set

``rxq_index``
    RX queue index

``flow_id``
    Flow ID passed to ``ndo_rx_flow_steer``

``filter_id``
    Filter ID returned by ``ndo_rx_flow_steer``


Description
===========

Drivers that implement ``ndo_rx_flow_steer`` should periodically call this function for each installed filter and remove the filters for which it returns ``true``.
