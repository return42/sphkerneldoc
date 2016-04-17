.. -*- coding: utf-8; mode: rst -*-

=========
vc4_hvs.c
=========


.. _`vc4-hvs-module.`:

VC4 HVS module.
===============

The HVS is the piece of hardware that does translation, scaling,
colorspace conversion, and compositing of pixels stored in
framebuffers into a FIFO of pixels going out to the Pixel Valve
(CRTC).  It operates at the system clock rate (the system audio
clock gate, specifically), which is much higher than the pixel
clock rate.

There is a single global HVS, with multiple output FIFOs that can
be consumed by the PVs.  This file just manages the resources for
the HVS, while the vc4_crtc.c code actually drives HVS setup for
each CRTC.

