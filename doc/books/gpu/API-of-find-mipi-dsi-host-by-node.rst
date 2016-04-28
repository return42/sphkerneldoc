.. -*- coding: utf-8; mode: rst -*-

.. _API-of-find-mipi-dsi-host-by-node:

=============================
of_find_mipi_dsi_host_by_node
=============================

*man of_find_mipi_dsi_host_by_node(9)*

*4.6.0-rc5*

find the MIPI DSI host matching a device tree node


Synopsis
========

.. c:function:: struct mipi_dsi_host * of_find_mipi_dsi_host_by_node( struct device_node * node )

Arguments
=========

``node``
    device tree node


Returns
=======

A pointer to the MIPI DSI host corresponding to ``node`` or NULL if no
such device exists (or has not been registered yet).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
