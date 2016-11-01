.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/i810/i810_main.c

.. _`i810_screen_off`:

i810_screen_off
===============

.. c:function:: void i810_screen_off(u8 __iomem *mmio, u8 mode)

    turns off/on display

    :param u8 __iomem \*mmio:
        address of register space

    :param u8 mode:
        on or off

.. _`i810_screen_off.description`:

Description
-----------

Blanks/unblanks the display

.. _`i810_dram_off`:

i810_dram_off
=============

.. c:function:: void i810_dram_off(u8 __iomem *mmio, u8 mode)

    turns off/on dram refresh

    :param u8 __iomem \*mmio:
        address of register space

    :param u8 mode:
        on or off

.. _`i810_dram_off.description`:

Description
-----------

Turns off DRAM refresh.  Must be off for only 2 vsyncs
before data becomes corrupt

.. _`i810_protect_regs`:

i810_protect_regs
=================

.. c:function:: void i810_protect_regs(u8 __iomem *mmio, int mode)

    allows rw/ro mode of certain VGA registers

    :param u8 __iomem \*mmio:
        address of register space

    :param int mode:
        protect/unprotect

.. _`i810_protect_regs.description`:

Description
-----------

The IBM VGA standard allows protection of certain VGA registers.
This will  protect or unprotect them.

.. _`i810_load_pll`:

i810_load_pll
=============

.. c:function:: void i810_load_pll(struct i810fb_par *par)

    loads values for the hardware PLL clock

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_load_pll.description`:

Description
-----------

Loads the P, M, and N registers.

.. _`i810_load_vga`:

i810_load_vga
=============

.. c:function:: void i810_load_vga(struct i810fb_par *par)

    load standard VGA registers

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_load_vga.description`:

Description
-----------

Load values to VGA registers

.. _`i810_load_vgax`:

i810_load_vgax
==============

.. c:function:: void i810_load_vgax(struct i810fb_par *par)

    load extended VGA registers

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_load_vgax.description`:

Description
-----------

Load values to extended VGA registers

.. _`i810_load_2d`:

i810_load_2d
============

.. c:function:: void i810_load_2d(struct i810fb_par *par)

    load grahics registers

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_load_2d.description`:

Description
-----------

Load values to graphics registers

.. _`i810_hires`:

i810_hires
==========

.. c:function:: void i810_hires(u8 __iomem *mmio)

    enables high resolution mode

    :param u8 __iomem \*mmio:
        address of register space

.. _`i810_load_pitch`:

i810_load_pitch
===============

.. c:function:: void i810_load_pitch(struct i810fb_par *par)

    loads the characters per line of the display

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_load_pitch.description`:

Description
-----------

Loads the characters per line

.. _`i810_load_color`:

i810_load_color
===============

.. c:function:: void i810_load_color(struct i810fb_par *par)

    loads the color depth of the display

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_load_color.description`:

Description
-----------

Loads the color depth of the display and the graphics engine

.. _`i810_load_regs`:

i810_load_regs
==============

.. c:function:: void i810_load_regs(struct i810fb_par *par)

    loads all registers for the mode

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_load_regs.description`:

Description
-----------

Loads registers

.. _`get_line_length`:

get_line_length
===============

.. c:function:: u32 get_line_length(struct i810fb_par *par, int xres_virtual, int bpp)

    calculates buffer pitch in bytes

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

    :param int xres_virtual:
        virtual resolution of the frame

    :param int bpp:
        bits per pixel

.. _`get_line_length.description`:

Description
-----------

Calculates buffer pitch in bytes.

.. _`i810_calc_dclk`:

i810_calc_dclk
==============

.. c:function:: void i810_calc_dclk(u32 freq, u32 *m, u32 *n, u32 *p)

    calculates the P, M, and N values of a pixelclock value

    :param u32 freq:
        target pixelclock in picoseconds

    :param u32 \*m:
        where to write M register

    :param u32 \*n:
        where to write N register

    :param u32 \*p:
        where to write P register

.. _`i810_calc_dclk.description`:

Description
-----------

Based on the formula Freq_actual = (4\*M\*Freq_ref)/(N^P)
Repeatedly computes the Freq until the actual Freq is equal to
the target Freq or until the loop count is zero.  In the latter
case, the actual frequency nearest the target will be used.

.. _`i810_enable_cursor`:

i810_enable_cursor
==================

.. c:function:: void i810_enable_cursor(u8 __iomem *mmio, int mode)

    show or hide the hardware cursor

    :param u8 __iomem \*mmio:
        address of register space

    :param int mode:
        show (1) or hide (0)

.. _`i810_enable_cursor.description`:

Description
-----------

Shows or hides the hardware cursor

.. _`i810_init_cursor`:

i810_init_cursor
================

.. c:function:: void i810_init_cursor(struct i810fb_par *par)

    initializes the cursor

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_init_cursor.description`:

Description
-----------

Initializes the cursor registers

.. _`i810_round_off`:

i810_round_off
==============

.. c:function:: void i810_round_off(struct fb_var_screeninfo *var)

    Round off values to capability of hardware

    :param struct fb_var_screeninfo \*var:
        pointer to fb_var_screeninfo structure

.. _`i810_round_off.description`:

Description
-----------

@var contains user-defined information for the mode to be set.
This will try modify those values to ones nearest the
capability of the hardware

.. _`set_color_bitfields`:

set_color_bitfields
===================

.. c:function:: void set_color_bitfields(struct fb_var_screeninfo *var)

    sets rgba fields

    :param struct fb_var_screeninfo \*var:
        pointer to fb_var_screeninfo

.. _`set_color_bitfields.description`:

Description
-----------

The length, offset and ordering  for each color field
(red, green, blue)  will be set as specified
by the hardware

.. _`i810_check_params`:

i810_check_params
=================

.. c:function:: int i810_check_params(struct fb_var_screeninfo *var, struct fb_info *info)

    check if contents in var are valid

    :param struct fb_var_screeninfo \*var:
        pointer to fb_var_screeninfo

    :param struct fb_info \*info:
        pointer to fb_info

.. _`i810_check_params.description`:

Description
-----------

This will check if the framebuffer size is sufficient
for the current mode and if the user's monitor has the
required specifications to display the current mode.

.. _`encode_fix`:

encode_fix
==========

.. c:function:: int encode_fix(struct fb_fix_screeninfo *fix, struct fb_info *info)

    fill up fb_fix_screeninfo structure

    :param struct fb_fix_screeninfo \*fix:
        pointer to fb_fix_screeninfo

    :param struct fb_info \*info:
        pointer to fb_info

.. _`encode_fix.description`:

Description
-----------

This will set up parameters that are unmodifiable by the user.

.. _`decode_var`:

decode_var
==========

.. c:function:: void decode_var(const struct fb_var_screeninfo *var, struct i810fb_par *par)

    modify par according to contents of var

    :param const struct fb_var_screeninfo \*var:
        pointer to fb_var_screeninfo

    :param struct i810fb_par \*par:
        pointer to i810fb_par

.. _`decode_var.description`:

Description
-----------

Based on the contents of \ ``var``\ , \ ``par``\  will be dynamically filled up.
\ ``par``\  contains all information necessary to modify the hardware.

.. _`i810fb_getcolreg`:

i810fb_getcolreg
================

.. c:function:: int i810fb_getcolreg(u8 regno, u8 *red, u8 *green, u8 *blue, u8 *transp, struct fb_info *info)

    gets red, green and blue values of the hardware DAC

    :param u8 regno:
        DAC index

    :param u8 \*red:
        red

    :param u8 \*green:
        green

    :param u8 \*blue:
        blue

    :param u8 \*transp:
        transparency (alpha)

    :param struct fb_info \*info:
        pointer to fb_info

.. _`i810fb_getcolreg.description`:

Description
-----------

Gets the red, green and blue values of the hardware DAC as pointed by \ ``regno``\ 
and writes them to \ ``red``\ , \ ``green``\  and \ ``blue``\  respectively

.. _`i810_init_monspecs`:

i810_init_monspecs
==================

.. c:function:: void i810_init_monspecs(struct fb_info *info)

    :param struct fb_info \*info:
        pointer to device specific info structure

.. _`i810_init_monspecs.description`:

Description
-----------

Sets the user monitor's horizontal and vertical
frequency limits

.. _`i810_init_defaults`:

i810_init_defaults
==================

.. c:function:: void i810_init_defaults(struct i810fb_par *par, struct fb_info *info)

    initializes default values to use

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

    :param struct fb_info \*info:
        pointer to current fb_info structure

.. _`i810_init_device`:

i810_init_device
================

.. c:function:: void i810_init_device(struct i810fb_par *par)

    initialize device

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. This file was automatic generated / don't edit.

