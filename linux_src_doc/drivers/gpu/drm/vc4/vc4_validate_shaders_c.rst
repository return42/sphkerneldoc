.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_validate_shaders.c

.. _`shader-validator-for-vc4.`:

Shader validator for VC4.
=========================

Since the VC4 has no IOMMU between it and system memory, a user
with access to execute shaders could escalate privilege by
overwriting system memory (using the VPM write address register in
the general-purpose DMA mode) or reading system memory it shouldn't
(reading it as a texture, uniform data, or direct-addressed TMU
lookup).

The shader validator walks over a shader's BO, ensuring that its
accesses are appropriately bounded, and recording where texture
accesses are made so that we can do relocations for them in the
uniform stream.

Shader BO are immutable for their lifetimes (enforced by not
allowing mmaps, GEM prime export, or rendering to from a CL), so
this validation is only performed at BO creation time.

.. This file was automatic generated / don't edit.

