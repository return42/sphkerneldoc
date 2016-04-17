.. -*- coding: utf-8; mode: rst -*-

======================
vc4_validate_shaders.c
======================


.. _`shader-validator-for-vc4.`:

Shader validator for VC4.
=========================

The VC4 has no IOMMU between it and system memory, so a user with
access to execute shaders could escalate privilege by overwriting
system memory (using the VPM write address register in the
general-purpose DMA mode) or reading system memory it shouldn't
(reading it as a texture, or uniform data, or vertex data).

This walks over a shader BO, ensuring that its accesses are
appropriately bounded, and recording how many texture accesses are
made and where so that we can do relocations for them in the
uniform stream.

