.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_render_cl.c

.. _`render-command-list-generation`:

Render command list generation
==============================

In the V3D hardware, render command lists are what load and store
tiles of a framebuffer and optionally call out to binner-generated
command lists to do the 3D drawing for that tile.

In the VC4 driver, render command list generation is performed by the
kernel instead of userspace.  We do this because validating a
user-submitted command list is hard to get right and has high CPU overhead,
while the number of valid configurations for render command lists is
actually fairly low.

.. This file was automatic generated / don't edit.

