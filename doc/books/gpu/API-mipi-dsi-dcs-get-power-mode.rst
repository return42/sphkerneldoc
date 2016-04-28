.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-get-power-mode:

===========================
mipi_dsi_dcs_get_power_mode
===========================

*man mipi_dsi_dcs_get_power_mode(9)*

*4.6.0-rc5*

query the display module's current power mode


Synopsis
========

.. c:function:: int mipi_dsi_dcs_get_power_mode( struct mipi_dsi_device * dsi, u8 * mode )

Arguments
=========

``dsi``
    DSI peripheral device

``mode``
    return location for the current power mode


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
