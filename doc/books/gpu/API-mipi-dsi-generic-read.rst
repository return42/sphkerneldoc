.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-generic-read:

=====================
mipi_dsi_generic_read
=====================

*man mipi_dsi_generic_read(9)*

*4.6.0-rc5*

receive data using a generic read packet


Synopsis
========

.. c:function:: ssize_t mipi_dsi_generic_read( struct mipi_dsi_device * dsi, const void * params, size_t num_params, void * data, size_t size )

Arguments
=========

``dsi``
    DSI peripheral device

``params``
    buffer containing the request parameters

``num_params``
    number of request parameters

``data``
    buffer in which to return the received data

``size``
    size of receive buffer


Description
===========

This function will automatically choose the right data type depending on
the number of parameters passed in.


Return
======

The number of bytes successfully read or a negative error code on
failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
