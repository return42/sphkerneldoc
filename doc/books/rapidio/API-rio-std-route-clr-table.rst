.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-std-route-clr-table:

=======================
rio_std_route_clr_table
=======================

*man rio_std_route_clr_table(9)*

*4.6.0-rc5*

Clear swotch route table using standard registers defined in RIO
specification rev.1.3.


Synopsis
========

.. c:function:: int rio_std_route_clr_table( struct rio_mport * mport, u16 destid, u8 hopcount, u16 table )

Arguments
=========

``mport``
    Master port to issue transaction

``destid``
    Destination ID of the device

``hopcount``
    Number of switch hops to the device

``table``
    routing table ID (global or port-specific)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
