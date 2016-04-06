
.. _API-of-find-mipi-dsi-device-by-node:

===============================
of_find_mipi_dsi_device_by_node
===============================

*man of_find_mipi_dsi_device_by_node(9)*

*4.6.0-rc1*

find the MIPI DSI device matching a device tree node


Synopsis
========

.. c:function:: struct mipi_dsi_device ⋆ of_find_mipi_dsi_device_by_node( struct device_node * np )

Arguments
=========

``np``
    device tree node


Return
======

A pointer to the MIPI DSI device corresponding to ``np`` or NULL if no such device exists (or has not been registered yet).
