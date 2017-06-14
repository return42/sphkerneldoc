.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_drv.c

.. _`broadcom-vc4-graphics-driver`:

Broadcom VC4 Graphics Driver
============================

The Broadcom VideoCore 4 (present in the Raspberry Pi) contains a
OpenGL ES 2.0-compatible 3D engine called V3D, and a highly
configurable display output pipeline that supports HDMI, DSI, DPI,
and Composite TV output.

The 3D engine also has an interface for submitting arbitrary
compute shader-style jobs using the same shader processor as is
used for vertex and fragment shaders in GLES 2.0.  However, given
that the hardware isn't able to expose any standard interfaces like
OpenGL compute shaders or OpenCL, it isn't supported by this
driver.

.. This file was automatic generated / don't edit.

