.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-set-display-off:

============================
mipi_dsi_dcs_set_display_off
============================

*man mipi_dsi_dcs_set_display_off(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
