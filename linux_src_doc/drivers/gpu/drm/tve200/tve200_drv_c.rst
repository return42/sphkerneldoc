.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tve200/tve200_drv.c

.. _`faraday-tv-encoder-tve200-drm-driver`:

Faraday TV Encoder TVE200 DRM Driver
====================================

The Faraday TV Encoder TVE200 is also known as the Gemini TV Interface
Controller (TVC) and is found in the Gemini Chipset from Storlink
Semiconductor (later Storm Semiconductor, later Cortina Systems)
but also in the Grain Media GM8180 chipset. On the Gemini the module
is connected to 8 data lines and a single clock line, comprising an
8-bit BT.656 interface.

This is a very basic YUV display driver. The datasheet specifies that
it supports the ITU BT.656 standard. It requires a 27 MHz clock which is
the hallmark of any TV encoder supporting both PAL and NTSC.

This driver exposes a standard KMS interface for this TV encoder.

.. This file was automatic generated / don't edit.

