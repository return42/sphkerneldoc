.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/v3d/v3d_drv.c

.. _`broadcom-v3d-graphics-driver`:

Broadcom V3D Graphics Driver
============================

This driver supports the Broadcom V3D 3.3 and 4.1 OpenGL ES GPUs.
For V3D 2.x support, see the VC4 driver.

Currently only single-core rendering using the binner and renderer
is supported.  The TFU (texture formatting unit) and V3D 4.x's CSD
(compute shader dispatch) are not yet supported.

.. This file was automatic generated / don't edit.

