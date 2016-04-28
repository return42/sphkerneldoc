.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-route-get-entry:

===================
rio_route_get_entry
===================

*man rio_route_get_entry(9)*

*4.6.0-rc5*

Read an entry from a switch routing table


Synopsis
========

.. c:function:: int rio_route_get_entry( struct rio_dev * rdev, u16 table, u16 route_destid, u8 * route_port, int lock )

Arguments
=========

``rdev``
    RIO device

``table``
    Routing table ID

``route_destid``
    Destination ID to be routed

``route_port``
    Pointer to read port number into

``lock``
    apply a hardware lock on switch device flag (1=lock, 0=no_lock)


Description
===========

If available calls the switch specific ``get_entry`` method to fetch a
route entry from a switch routing table. Otherwise uses standard RT read
method as defined by RapidIO specification. A specific routing table can
be selected using the ``table`` argument if a switch has per port
routing tables or the standard (or global) table may be used by passing
``RIO_GLOBAL_TABLE`` in ``table``.

Returns ``0`` on success or ``-EINVAL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
