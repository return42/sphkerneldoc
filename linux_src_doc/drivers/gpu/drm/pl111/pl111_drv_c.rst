.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/pl111/pl111_drv.c

.. _`arm-primecell-pl111-clcd-driver`:

ARM PrimeCell PL111 CLCD Driver
===============================

The PL111 is a simple LCD controller that can support TFT and STN
displays.  This driver exposes a standard KMS interface for them.

This driver uses the same Device Tree binding as the fbdev CLCD
driver.  While the fbdev driver supports panels that may be
connected to the CLCD internally to the CLCD driver, in DRM the
panels get split out to drivers/gpu/drm/panels/.  This means that,
in converting from using fbdev to using DRM, you also need to write
a panel driver (which may be as simple as an entry in
panel-simple.c).

The driver currently doesn't expose the cursor.  The DRM API for
cursors requires support for 64x64 ARGB8888 cursor images, while
the hardware can only support 64x64 monochrome with masking
cursors.  While one could imagine trying to hack something together
to look at the ARGB8888 and program reasonable in monochrome, we
just don't expose the cursor at all instead, and leave cursor
support to the X11 software cursor layer.

TODO:

- Fix race between setting plane base address and getting IRQ for
  vsync firing the pageflip completion.

- Expose the correct set of formats we can support based on the
  "arm,pl11x,tft-r0g0b0-pads" DT property.

- Use the "max-memory-bandwidth" DT property to filter the
  supported formats.

- Read back hardware state at boot to skip reprogramming the
  hardware when doing a no-op modeset.

- Use the CLKSEL bit to support switching between the two external
  clock parents.

.. This file was automatic generated / don't edit.

