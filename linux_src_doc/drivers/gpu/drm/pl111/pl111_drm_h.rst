.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/pl111/pl111_drm.h

.. _`pl111_variant_data`:

struct pl111_variant_data
=========================

.. c:type:: struct pl111_variant_data

    encodes IP differences

.. _`pl111_variant_data.definition`:

Definition
----------

.. code-block:: c

    struct pl111_variant_data {
        const char *name;
        bool is_pl110;
        bool is_lcdc;
        bool external_bgr;
        bool broken_clockdivider;
        bool broken_vblank;
        bool st_bitmux_control;
        const u32 *formats;
        unsigned int nformats;
        unsigned int fb_bpp;
    }

.. _`pl111_variant_data.members`:

Members
-------

name
    the name of this variant

is_pl110
    this is the early PL110 variant

is_lcdc
    this is the ST Microelectronics Nomadik LCDC variant

external_bgr
    this is the Versatile Pl110 variant with external
    BGR/RGB routing

broken_clockdivider
    the clock divider is broken and we need to
    use the supplied clock directly

broken_vblank
    the vblank IRQ is broken on this variant

st_bitmux_control
    this variant is using the ST Micro bitmux
    extensions to the control register

formats
    array of supported pixel formats on this variant

nformats
    the length of the array of supported pixel formats

fb_bpp
    desired bits per pixel on the default framebuffer

.. This file was automatic generated / don't edit.

