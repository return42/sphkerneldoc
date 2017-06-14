.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/meson/meson_dw_hdmi.c

.. _`hdmi-output`:

HDMI Output
===========

HDMI Output is composed of :

- A Synopsys DesignWare HDMI Controller IP
- A TOP control block controlling the Clocks and PHY
- A custom HDMI PHY in order convert video to TMDS signal

.. code::

   ___________________________________
  |            HDMI TOP               |<= HPD
  |___________________________________|
  |                  |                |
  |  Synopsys HDMI   |   HDMI PHY     |=> TMDS
  |    Controller    |________________|
  |___________________________________|<=> DDC


The HDMI TOP block only supports HPD sensing.
The Synopsys HDMI Controller interrupt is routed
through the TOP Block interrupt.
Communication to the TOP Block and the Synopsys
HDMI Controller is done a pair of addr+read/write
registers.
The HDMI PHY is configured by registers in the
HHI register block.

Pixel data arrives in 4:4:4 format from the VENC
block and the VPU HDMI mux selects either the ENCI
encoder for the 576i or 480i formats or the ENCP
encoder for all the other formats including
interlaced HD formats.
The VENC uses a DVI encoder on top of the ENCI
or ENCP encoders to generate DVI timings for the
HDMI controller.

GXBB, GXL and GXM embeds the Synopsys DesignWare
HDMI TX IP version 2.01a with HDCP and I2C & S/PDIF
audio source interfaces.

We handle the following features :

- HPD Rise & Fall interrupt
- HDMI Controller Interrupt
- HDMI PHY Init for 480i to 1080p60
- VENC & HDMI Clock setup for 480i to 1080p60
- VENC Mode setup for 480i to 1080p60

What is missing :

- PHY, Clock and Mode setup for 2k && 4k modes
- SDDC Scrambling mode for HDMI 2.0a
- HDCP Setup
- CEC Management

.. This file was automatic generated / don't edit.

