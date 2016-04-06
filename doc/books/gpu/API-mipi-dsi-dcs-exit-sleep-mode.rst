
.. _API-mipi-dsi-dcs-exit-sleep-mode:

============================
mipi_dsi_dcs_exit_sleep_mode
============================

*man mipi_dsi_dcs_exit_sleep_mode(9)*

*4.6.0-rc1*

enable all blocks inside the display module


Synopsis
========

.. c:function:: int mipi_dsi_dcs_exit_sleep_mode( struct mipi_dsi_device * dsi )

Arguments
=========

``dsi``
    DSI peripheral device


Return
======

0 on success or a negative error code on failure.
