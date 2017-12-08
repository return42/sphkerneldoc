.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/panel/panel-raspberrypi-touchscreen.c

.. _`rpi_dsi_driver_name`:

RPI_DSI_DRIVER_NAME
===================

.. c:function::  RPI_DSI_DRIVER_NAME()

.. _`rpi_dsi_driver_name.description`:

Description
-----------

The 7" touchscreen consists of a DPI LCD panel, a Toshiba
TC358762XBG DSI-DPI bridge, and an I2C-connected Atmel ATTINY88-MUR
controlling power management, the LCD PWM, and initial register
setup of the Tohsiba.

This driver controls the TC358762 and ATTINY88, presenting a DSI
device with a drm_panel.

.. This file was automatic generated / don't edit.

