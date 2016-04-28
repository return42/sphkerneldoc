.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-soft-reset:

=======================
mipi_dsi_dcs_soft_reset
=======================

*man mipi_dsi_dcs_soft_reset(9)*

*4.6.0-rc5*

perform a software reset of the display module


Synopsis
========

.. c:function:: int mipi_dsi_dcs_soft_reset( struct mipi_dsi_device * dsi )

Arguments
=========

``dsi``
    DSI peripheral device


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
