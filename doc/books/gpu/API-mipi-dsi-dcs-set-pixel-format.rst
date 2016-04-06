
.. _API-mipi-dsi-dcs-set-pixel-format:

=============================
mipi_dsi_dcs_set_pixel_format
=============================

*man mipi_dsi_dcs_set_pixel_format(9)*

*4.6.0-rc1*

sets the pixel format for the RGB image data used by the interface


Synopsis
========

.. c:function:: int mipi_dsi_dcs_set_pixel_format( struct mipi_dsi_device * dsi, u8 format )

Arguments
=========

``dsi``
    DSI peripheral device

``format``
    pixel format


Return
======

0 on success or a negative error code on failure.
