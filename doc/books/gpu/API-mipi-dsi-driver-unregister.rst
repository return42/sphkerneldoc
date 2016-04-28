.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-driver-unregister:

==========================
mipi_dsi_driver_unregister
==========================

*man mipi_dsi_driver_unregister(9)*

*4.6.0-rc5*

unregister a driver for DSI devices


Synopsis
========

.. c:function:: void mipi_dsi_driver_unregister( struct mipi_dsi_driver * drv )

Arguments
=========

``drv``
    DSI driver structure


Return
======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
