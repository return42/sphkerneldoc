.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-dcs-set-tear-off:

=========================
mipi_dsi_dcs_set_tear_off
=========================

*man mipi_dsi_dcs_set_tear_off(9)*

*4.6.0-rc5*

turn off the display module's Tearing Effect output signal on the TE
signal line


Synopsis
========

.. c:function:: int mipi_dsi_dcs_set_tear_off( struct mipi_dsi_device * dsi )

Arguments
=========

``dsi``
    DSI peripheral device


Return
======

0 on success or a negative error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
