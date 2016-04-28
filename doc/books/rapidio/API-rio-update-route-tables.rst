.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-update-route-tables:

=======================
rio_update_route_tables
=======================

*man rio_update_route_tables(9)*

*4.6.0-rc5*

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

For each enumerated device, ensure that each switch in a system has
correct routing entries. Add routes for devices that where unknown
dirung the first enumeration pass through the switch.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
