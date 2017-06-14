.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/meson/meson_vpp.c

.. _`video-post-processing`:

Video Post Processing
=====================

VPP Handles all the Post Processing after the Scanout from the VIU
We handle the following post processings :

- Postblend, Blends the OSD1 only
     We exclude OSD2, VS1, VS1 and Preblend output
- Vertical OSD Scaler for OSD1 only, we disable vertical scaler and
     use it only for interlace scanout
- Intermediate FIFO with default Amlogic values

What is missing :

- Preblend for video overlay pre-scaling
- OSD2 support for cursor framebuffer
- Video pre-scaling before postblend
- Full Vertical/Horizontal OSD scaling to support TV overscan
- HDR conversion

.. This file was automatic generated / don't edit.

