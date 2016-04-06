
.. _API-mipi-dsi-dcs-nop:

================
mipi_dsi_dcs_nop
================

*man mipi_dsi_dcs_nop(9)*

*4.6.0-rc1*

send DCS nop packet


Synopsis
========

.. c:function:: int mipi_dsi_dcs_nop( struct mipi_dsi_device * dsi )

Arguments
=========

``dsi``
    DSI peripheral device


Return
======

0 on success or a negative error code on failure.
