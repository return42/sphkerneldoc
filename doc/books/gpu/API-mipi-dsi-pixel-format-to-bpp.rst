.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-pixel-format-to-bpp:

============================
mipi_dsi_pixel_format_to_bpp
============================

*man mipi_dsi_pixel_format_to_bpp(9)*

*4.6.0-rc5*

obtain the number of bits per pixel for any given pixel format defined
by the MIPI DSI specification


Synopsis
========

.. c:function:: int mipi_dsi_pixel_format_to_bpp( enum mipi_dsi_pixel_format fmt )

Arguments
=========

``fmt``
    MIPI DSI pixel format


Returns
=======

The number of bits per pixel of the given pixel format.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
