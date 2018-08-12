.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/v3d/v3d_mmu.c

.. _`broadcom-v3d-mmu`:

Broadcom V3D MMU
================

The V3D 3.x hardware (compared to VC4) now includes an MMU.  It has
a single level of page tables for the V3D's 4GB address space to
map to AXI bus addresses, thus it could need up to 4MB of
physically contiguous memory to store the PTEs.

Because the 4MB of contiguous memory for page tables is precious,
and switching between them is expensive, we load all BOs into the
same 4GB address space.

To protect clients from each other, we should use the GMP to
quickly mask out (at 128kb granularity) what pages are available to
each client.  This is not yet implemented.

.. This file was automatic generated / don't edit.

