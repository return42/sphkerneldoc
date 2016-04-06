
.. _API-mipi-dsi-dcs-write:

==================
mipi_dsi_dcs_write
==================

*man mipi_dsi_dcs_write(9)*

*4.6.0-rc1*

send DCS write command


Synopsis
========

.. c:function:: ssize_t mipi_dsi_dcs_write( struct mipi_dsi_device * dsi, u8 cmd, const void * data, size_t len )

Arguments
=========

``dsi``
    DSI peripheral device

``cmd``
    DCS command

``data``
    buffer containing the command payload

``len``
    command payload length


Description
===========

This function will automatically choose the right data type depending on the command payload length.


Return
======

The number of bytes successfully transmitted or a negative error code on failure.
