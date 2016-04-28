.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-get-pixel-format:

=============================
mipi_dsi_dcs_get_pixel_format
=============================

*man mipi_dsi_dcs_get_pixel_format(9)*

*4.6.0-rc5*

gets the pixel format for the RGB image data used by the interface


Synopsis
========

.. c:function:: int mipi_dsi_dcs_get_pixel_format( struct mipi_dsi_device * dsi, u8 * format )

Arguments
=========

``dsi``
    DSI peripheral device

``format``
    return location for the pixel format


Return
======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
