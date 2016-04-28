.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-shutdown-peripheral:

============================
mipi_dsi_shutdown_peripheral
============================

*man mipi_dsi_shutdown_peripheral(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
