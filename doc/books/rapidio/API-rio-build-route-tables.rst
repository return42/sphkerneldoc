.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-build-route-tables:

======================
rio_build_route_tables
======================

*man rio_build_route_tables(9)*

*4.6.0-rc5*

Generate route tables from switch route entries


Synopsis
========

.. c:function:: void rio_build_route_tables( struct rio_net * net )

Arguments
=========

``net``
    RIO network to run route tables scan on


Description
===========

For each switch device, generate a route table by copying existing route
entries from the switch.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
