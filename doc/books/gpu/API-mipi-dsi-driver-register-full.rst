
.. _API-mipi-dsi-driver-register-full:

=============================
mipi_dsi_driver_register_full
=============================

*man mipi_dsi_driver_register_full(9)*

*4.6.0-rc1*

register a driver for DSI devices


Synopsis
========

.. c:function:: int mipi_dsi_driver_register_full( struct mipi_dsi_driver * drv, struct module * owner )

Arguments
=========

``drv``
    DSI driver structure

``owner``
    owner module


Return
======

0 on success or a negative error code on failure.
