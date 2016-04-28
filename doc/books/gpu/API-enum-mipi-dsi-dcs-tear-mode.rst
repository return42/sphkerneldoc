.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-mipi-dsi-dcs-tear-mode:

===========================
enum mipi_dsi_dcs_tear_mode
===========================

*man enum mipi_dsi_dcs_tear_mode(9)*

*4.6.0-rc5*

Tearing Effect Output Line mode


Synopsis
========

.. code-block:: c

    enum mipi_dsi_dcs_tear_mode {
      MIPI_DSI_DCS_TEAR_MODE_VBLANK,
      MIPI_DSI_DCS_TEAR_MODE_VHBLANK
    };


Constants
=========

MIPI_DSI_DCS_TEAR_MODE_VBLANK
    the TE output line consists of V-Blanking information only

MIPI_DSI_DCS_TEAR_MODE_VHBLANK
    the TE output line consists of both V-Blanking and H-Blanking
    information


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
