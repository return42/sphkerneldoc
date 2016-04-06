
.. _API-mipi-dsi-generic-write:

======================
mipi_dsi_generic_write
======================

*man mipi_dsi_generic_write(9)*

*4.6.0-rc1*

transmit data using a generic write packet


Synopsis
========

.. c:function:: ssize_t mipi_dsi_generic_write( struct mipi_dsi_device * dsi, const void * payload, size_t size )

Arguments
=========

``dsi``
    DSI peripheral device

``payload``
    buffer containing the payload

``size``
    size of payload buffer


Description
===========

This function will automatically choose the right data type depending on the payload length.


Return
======

The number of bytes transmitted on success or a negative error code on failure.
