.. -*- coding: utf-8; mode: rst -*-

===============
vc4_render_cl.c
===============


.. _`render-command-list-generation`:

Render command list generation
==============================

In the VC4 driver, render command list generation is performed by the
kernel instead of userspace.  We do this because validating a
user-submitted command list is hard to get right and has high CPU overhead,
while the number of valid configurations for render command lists is
actually fairly low.

