.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_vec.c

.. _`vc4-sdtv-module`:

VC4 SDTV module
===============

The VEC encoder generates PAL or NTSC composite video output.

TV mode selection is done by an atomic property on the encoder,
because a drm_mode_modeinfo is insufficient to distinguish between
PAL and PAL-M or NTSC and NTSC-J.

.. This file was automatic generated / don't edit.

