.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-write-buffer:

=========================
mipi_dsi_dcs_write_buffer
=========================

*man mipi_dsi_dcs_write_buffer(9)*

*4.6.0-rc5*

transmit a DCS command with payload


Synopsis
========

.. c:function:: ssize_t mipi_dsi_dcs_write_buffer( struct mipi_dsi_device * dsi, const void * data, size_t len )

Arguments
=========

``dsi``
    DSI peripheral device

``data``
    buffer containing data to be transmitted

``len``
    size of transmission buffer


Description
===========

This function will automatically choose the right data type depending on
the command payload length.


Return
======

The number of bytes successfully transmitted or a negative error code on
failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
