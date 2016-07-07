.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/i810/i810_accel.c

.. _`wait_for_space`:

wait_for_space
==============

.. c:function:: int wait_for_space(struct fb_info *info, u32 space)

    check ring buffer free space

    :param struct fb_info \*info:
        *undescribed*

    :param u32 space:
        amount of ringbuffer space needed in bytes

.. _`wait_for_space.description`:

Description
-----------

The function waits until a free space from the ringbuffer
is available

.. _`wait_for_engine_idle`:

wait_for_engine_idle
====================

.. c:function:: int wait_for_engine_idle(struct fb_info *info)

    waits for all hardware engines to finish

    :param struct fb_info \*info:
        *undescribed*

.. _`wait_for_engine_idle.description`:

Description
-----------

This waits for lring(0), iring(1), and batch(3), etc to finish and
waits until ringbuffer is empty.

.. _`end_iring`:

end_iring
=========

.. c:function:: void end_iring(struct i810fb_par *par)

    advances the buffer

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`end_iring.description`:

Description
-----------

This advances the tail of the ringbuffer, effectively
beginning the execution of the graphics instruction sequence.

.. _`source_copy_blit`:

source_copy_blit
================

.. c:function:: void source_copy_blit(int dwidth, int dheight, int dpitch, int xdir, int src, int dest, int rop, int blit_bpp, struct fb_info *info)

    BLIT transfer operation

    :param int dwidth:
        width of rectangular graphics data

    :param int dheight:
        height of rectangular graphics data

    :param int dpitch:
        bytes per line of destination buffer

    :param int xdir:
        direction of copy (left to right or right to left)

    :param int src:
        address of first pixel to read from

    :param int dest:
        address of first pixel to write to

    :param int rop:
        raster operation

    :param int blit_bpp:
        pixel format which can be different from the
        framebuffer's pixelformat

    :param struct fb_info \*info:
        *undescribed*

.. _`source_copy_blit.description`:

Description
-----------

This is a BLIT operation typically used when doing
a 'Copy and Paste'

.. _`color_blit`:

color_blit
==========

.. c:function:: void color_blit(int width, int height, int pitch, int dest, int rop, int what, int blit_bpp, struct fb_info *info)

    solid color BLIT operation

    :param int width:
        width of destination

    :param int height:
        height of destination

    :param int pitch:
        pixels per line of the buffer

    :param int dest:
        address of first pixel to write to

    :param int rop:
        raster operation

    :param int what:
        color to transfer

    :param int blit_bpp:
        pixel format which can be different from the
        framebuffer's pixelformat

    :param struct fb_info \*info:
        *undescribed*

.. _`color_blit.description`:

Description
-----------

A BLIT operation which can be used for  color fill/rectangular fill

.. _`mono_src_copy_imm_blit`:

mono_src_copy_imm_blit
======================

.. c:function:: void mono_src_copy_imm_blit(int dwidth, int dheight, int dpitch, int dsize, int blit_bpp, int rop, int dest, const u32 *src, int bg, int fg, struct fb_info *info)

    color expand from system memory to framebuffer

    :param int dwidth:
        width of destination

    :param int dheight:
        height of destination

    :param int dpitch:
        pixels per line of the buffer

    :param int dsize:
        size of bitmap in double words

    :param int blit_bpp:
        pixelformat to use which can be different from the
        framebuffer's pixelformat

    :param int rop:
        raster operation

    :param int dest:
        address of first byte of pixel;

    :param const u32 \*src:
        address of image data

    :param int bg:
        backgound color

    :param int fg:
        forground color

    :param struct fb_info \*info:
        *undescribed*

.. _`mono_src_copy_imm_blit.description`:

Description
-----------

A color expand operation where the  source data is placed in the
ringbuffer itself. Useful for drawing text.

.. _`mono_src_copy_imm_blit.requirement`:

REQUIREMENT
-----------

The end of a scanline must be padded to the next word.

.. _`i810fb_iring_enable`:

i810fb_iring_enable
===================

.. c:function:: void i810fb_iring_enable(struct i810fb_par *par, u32 mode)

    enables/disables the ringbuffer

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

    :param u32 mode:
        enable or disable

.. _`i810fb_iring_enable.description`:

Description
-----------

Enables or disables the ringbuffer, effectively enabling or
disabling the instruction/acceleration engine.

.. _`i810fb_init_ringbuffer`:

i810fb_init_ringbuffer
======================

.. c:function:: void i810fb_init_ringbuffer(struct fb_info *info)

    initialize the ringbuffer

    :param struct fb_info \*info:
        *undescribed*

.. _`i810fb_init_ringbuffer.description`:

Description
-----------

Initializes the ringbuffer by telling the device the
size and location of the ringbuffer.  It also sets
the head and tail pointers = 0

.. This file was automatic generated / don't edit.

