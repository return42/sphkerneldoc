.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/meson/meson_drv.c

.. _`video-processing-unit`:

Video Processing Unit
=====================

VPU Handles the Global Video Processing, it includes management of the
clocks gates, blocks reset lines and power domains.

What is missing :

- Full reset of entire video processing HW blocks
- Scaling and setup of the VPU clock
- Bus clock gates
- Powering up video processing HW blocks
- Powering Up HDMI controller and PHY

.. This file was automatic generated / don't edit.

