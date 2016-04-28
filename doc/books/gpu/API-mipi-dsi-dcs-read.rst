.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-read:

=================
mipi_dsi_dcs_read
=================

*man mipi_dsi_dcs_read(9)*

*4.6.0-rc5*

send DCS read request command


Synopsis
========

.. c:function:: ssize_t mipi_dsi_dcs_read( struct mipi_dsi_device * dsi, u8 cmd, void * data, size_t len )

Arguments
=========

``dsi``
    DSI peripheral device

``cmd``
    DCS command

``data``
    buffer in which to receive data

``len``
    size of receive buffer


Return
======

The number of bytes read or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
