
.. _API-mipi-dsi-shutdown-peripheral:

============================
mipi_dsi_shutdown_peripheral
============================

*man mipi_dsi_shutdown_peripheral(9)*

*4.6.0-rc1*

sends a Shutdown Peripheral command


Synopsis
========

.. c:function:: int mipi_dsi_shutdown_peripheral( struct mipi_dsi_device * dsi )

Arguments
=========

``dsi``
    DSI peripheral device


Return
======

0 on success or a negative error code on failure.
