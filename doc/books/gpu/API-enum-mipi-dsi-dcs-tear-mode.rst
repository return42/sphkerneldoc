
.. _API-enum-mipi-dsi-dcs-tear-mode:

===========================
enum mipi_dsi_dcs_tear_mode
===========================

*man enum mipi_dsi_dcs_tear_mode(9)*

*4.6.0-rc1*

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
    the TE output line consists of both V-Blanking and H-Blanking information
