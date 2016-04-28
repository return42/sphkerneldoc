.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-device-register-full:

=============================
mipi_dsi_device_register_full
=============================

*man mipi_dsi_device_register_full(9)*

*4.6.0-rc5*

create a MIPI DSI device


Synopsis
========

.. c:function:: struct mipi_dsi_device * mipi_dsi_device_register_full( struct mipi_dsi_host * host, const struct mipi_dsi_device_info * info )

Arguments
=========

``host``
    DSI host to which this device is connected

``info``
    pointer to template containing DSI device information


Description
===========

Create a MIPI DSI device by using the device information provided by
mipi_dsi_device_info template


Returns
=======

A pointer to the newly created MIPI DSI device, or, a pointer encoded
with an error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
