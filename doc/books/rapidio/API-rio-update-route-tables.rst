
.. _API-rio-update-route-tables:

=======================
rio_update_route_tables
=======================

*man rio_update_route_tables(9)*

*4.6.0-rc1*

Updates route tables in switches


Synopsis
========

.. c:function:: void rio_update_route_tables( struct rio_net * net )

Arguments
=========

``net``
    RIO network to run update on


Description
===========

For each enumerated device, ensure that each switch in a system has correct routing entries. Add routes for devices that where unknown dirung the first enumeration pass through the
switch.
