
.. _API-mipi-dsi-dcs-set-tear-on:

========================
mipi_dsi_dcs_set_tear_on
========================

*man mipi_dsi_dcs_set_tear_on(9)*

*4.6.0-rc1*

turn on the display module's Tearing Effect output signal on the TE signal line.


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
