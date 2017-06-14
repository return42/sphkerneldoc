.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/meson/meson_viu.c

.. _`video-input-unit`:

Video Input Unit
================

VIU Handles the Pixel scanout and the basic Colorspace conversions
We handle the following features :

- OSD1 RGB565/RGB888/xRGB8888 scanout
- RGB conversion to x/cb/cr
- Progressive or Interlace buffer scanout
- OSD1 Commit on Vsync
- HDR OSD matrix for GXL/GXM

What is missing :

- BGR888/xBGR8888/BGRx8888/BGRx8888 modes
- YUV4:2:2 Y0CbY1Cr scanout
- Conversion to YUV 4:4:4 from 4:2:2 input
- Colorkey Alpha matching
- Big endian scanout
- X/Y reverse scanout
- Global alpha setup
- OSD2 support, would need interlace switching on vsync
- OSD1 full scaling to support TV overscan

.. This file was automatic generated / don't edit.

