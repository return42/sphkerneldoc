.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-std-route-get-entry:

=======================
rio_std_route_get_entry
=======================

*man rio_std_route_get_entry(9)*

*4.6.0-rc5*

Read switch route table entry (port number) associated with specified
destID using standard registers defined in RIO specification rev.1.3


Synopsis
========

.. c:function:: int rio_std_route_get_entry( struct rio_mport * mport, u16 destid, u8 hopcount, u16 table, u16 route_destid, u8 * route_port )

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

``route_destid``
    destID entry in the RT

``route_port``
    returned destination port for specified destID


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
