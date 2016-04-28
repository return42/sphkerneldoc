.. -*- coding: utf-8; mode: rst -*-

.. _API-of-find-mipi-dsi-device-by-node:

===============================
of_find_mipi_dsi_device_by_node
===============================

*man of_find_mipi_dsi_device_by_node(9)*

*4.6.0-rc5*

find the MIPI DSI device matching a device tree node


Synopsis
========

.. c:function:: struct mipi_dsi_device * of_find_mipi_dsi_device_by_node( struct device_node * np )

Arguments
=========

``np``
    device tree node


Return
======

A pointer to the MIPI DSI device corresponding to ``np`` or NULL if no
such device exists (or has not been registered yet).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
