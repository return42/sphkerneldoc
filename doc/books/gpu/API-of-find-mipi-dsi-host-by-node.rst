
.. _API-of-find-mipi-dsi-host-by-node:

=============================
of_find_mipi_dsi_host_by_node
=============================

*man of_find_mipi_dsi_host_by_node(9)*

*4.6.0-rc1*

find the MIPI DSI host matching a device tree node


Synopsis
========

.. c:function:: struct mipi_dsi_host ⋆ of_find_mipi_dsi_host_by_node( struct device_node * node )

Arguments
=========

``node``
    device tree node


Returns
=======

A pointer to the MIPI DSI host corresponding to ``node`` or NULL if no such device exists (or has not been registered yet).
