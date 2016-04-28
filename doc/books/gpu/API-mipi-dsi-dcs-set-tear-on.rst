.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-set-tear-on:

========================
mipi_dsi_dcs_set_tear_on
========================

*man mipi_dsi_dcs_set_tear_on(9)*

*4.6.0-rc5*

turn on the display module's Tearing Effect output signal on the TE
signal line.


Synopsis
========

.. c:function:: int mipi_dsi_dcs_set_tear_on( struct mipi_dsi_device * dsi, enum mipi_dsi_dcs_tear_mode mode )

Arguments
=========

``dsi``
    DSI peripheral device

``mode``
    the Tearing Effect Output Line mode


Return
======

0 on success or a negative error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
