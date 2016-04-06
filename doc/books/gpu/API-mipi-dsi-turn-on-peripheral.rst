
.. _API-mipi-dsi-turn-on-peripheral:

===========================
mipi_dsi_turn_on_peripheral
===========================

*man mipi_dsi_turn_on_peripheral(9)*

*4.6.0-rc1*

sends a Turn On Peripheral command


Synopsis
========

.. c:function:: int mipi_dsi_turn_on_peripheral( struct mipi_dsi_device * dsi )

Arguments
=========

``dsi``
    DSI peripheral device


Return
======

0 on success or a negative error code on failure.
