
.. _API-mipi-dsi-dcs-set-display-off:

============================
mipi_dsi_dcs_set_display_off
============================

*man mipi_dsi_dcs_set_display_off(9)*

*4.6.0-rc1*

stop displaying the image data on the display device


Synopsis
========

.. c:function:: int mipi_dsi_dcs_set_display_off( struct mipi_dsi_device * dsi )

Arguments
=========

``dsi``
    DSI peripheral device


Return
======

0 on success or a negative error code on failure.
