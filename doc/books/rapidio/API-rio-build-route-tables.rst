
.. _API-rio-build-route-tables:

======================
rio_build_route_tables
======================

*man rio_build_route_tables(9)*

*4.6.0-rc1*

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

For each switch device, generate a route table by copying existing route entries from the switch.
