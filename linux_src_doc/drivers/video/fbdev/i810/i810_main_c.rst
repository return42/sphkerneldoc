.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/i810/i810_main.c

.. _`i810_screen_off`:

i810_screen_off
===============

.. c:function:: void i810_screen_off(u8 __iomem *mmio, u8 mode)

    turns off/on display

    :param mmio:
        address of register space
    :type mmio: u8 __iomem \*

    :param mode:
        on or off
    :type mode: u8

.. _`i810_screen_off.description`:

Description
-----------

Blanks/unblanks the display

.. _`i810_dram_off`:

i810_dram_off
=============

.. c:function:: void i810_dram_off(u8 __iomem *mmio, u8 mode)

    turns off/on dram refresh

    :param mmio:
        address of register space
    :type mmio: u8 __iomem \*

    :param mode:
        on or off
    :type mode: u8

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

    :param mmio:
        address of register space
    :type mmio: u8 __iomem \*

    :param mode:
        protect/unprotect
    :type mode: int

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

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_load_pll.description`:

Description
-----------

Loads the P, M, and N registers.

.. _`i810_load_vga`:

i810_load_vga
=============

.. c:function:: void i810_load_vga(struct i810fb_par *par)

    load standard VGA registers

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_load_vga.description`:

Description
-----------

Load values to VGA registers

.. _`i810_load_vgax`:

i810_load_vgax
==============

.. c:function:: void i810_load_vgax(struct i810fb_par *par)

    load extended VGA registers

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_load_vgax.description`:

Description
-----------

Load values to extended VGA registers

.. _`i810_load_2d`:

i810_load_2d
============

.. c:function:: void i810_load_2d(struct i810fb_par *par)

    load grahics registers

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_load_2d.description`:

Description
-----------

Load values to graphics registers

.. _`i810_hires`:

i810_hires
==========

.. c:function:: void i810_hires(u8 __iomem *mmio)

    enables high resolution mode

    :param mmio:
        address of register space
    :type mmio: u8 __iomem \*

.. _`i810_load_pitch`:

i810_load_pitch
===============

.. c:function:: void i810_load_pitch(struct i810fb_par *par)

    loads the characters per line of the display

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_load_pitch.description`:

Description
-----------

Loads the characters per line

.. _`i810_load_color`:

i810_load_color
===============

.. c:function:: void i810_load_color(struct i810fb_par *par)

    loads the color depth of the display

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_load_color.description`:

Description
-----------

Loads the color depth of the display and the graphics engine

.. _`i810_load_regs`:

i810_load_regs
==============

.. c:function:: void i810_load_regs(struct i810fb_par *par)

    loads all registers for the mode

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_load_regs.description`:

Description
-----------

Loads registers

.. _`get_line_length`:

get_line_length
===============

.. c:function:: u32 get_line_length(struct i810fb_par *par, int xres_virtual, int bpp)

    calculates buffer pitch in bytes

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

    :param xres_virtual:
        virtual resolution of the frame
    :type xres_virtual: int

    :param bpp:
        bits per pixel
    :type bpp: int

.. _`get_line_length.description`:

Description
-----------

Calculates buffer pitch in bytes.

.. _`i810_calc_dclk`:

i810_calc_dclk
==============

.. c:function:: void i810_calc_dclk(u32 freq, u32 *m, u32 *n, u32 *p)

    calculates the P, M, and N values of a pixelclock value

    :param freq:
        target pixelclock in picoseconds
    :type freq: u32

    :param m:
        where to write M register
    :type m: u32 \*

    :param n:
        where to write N register
    :type n: u32 \*

    :param p:
        where to write P register
    :type p: u32 \*

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

    :param mmio:
        address of register space
    :type mmio: u8 __iomem \*

    :param mode:
        show (1) or hide (0)
    :type mode: int

.. _`i810_enable_cursor.description`:

Description
-----------

Shows or hides the hardware cursor

.. _`i810_init_cursor`:

i810_init_cursor
================

.. c:function:: void i810_init_cursor(struct i810fb_par *par)

    initializes the cursor

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. _`i810_init_cursor.description`:

Description
-----------

Initializes the cursor registers

.. _`i810_round_off`:

i810_round_off
==============

.. c:function:: void i810_round_off(struct fb_var_screeninfo *var)

    Round off values to capability of hardware

    :param var:
        pointer to fb_var_screeninfo structure
    :type var: struct fb_var_screeninfo \*

.. _`i810_round_off.description`:

Description
-----------

\ ``var``\  contains user-defined information for the mode to be set.
This will try modify those values to ones nearest the
capability of the hardware

.. _`set_color_bitfields`:

set_color_bitfields
===================

.. c:function:: void set_color_bitfields(struct fb_var_screeninfo *var)

    sets rgba fields

    :param var:
        pointer to fb_var_screeninfo
    :type var: struct fb_var_screeninfo \*

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

    :param var:
        pointer to fb_var_screeninfo
    :type var: struct fb_var_screeninfo \*

    :param info:
        pointer to fb_info
    :type info: struct fb_info \*

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

    :param fix:
        pointer to fb_fix_screeninfo
    :type fix: struct fb_fix_screeninfo \*

    :param info:
        pointer to fb_info
    :type info: struct fb_info \*

.. _`encode_fix.description`:

Description
-----------

This will set up parameters that are unmodifiable by the user.

.. _`decode_var`:

decode_var
==========

.. c:function:: void decode_var(const struct fb_var_screeninfo *var, struct i810fb_par *par)

    modify par according to contents of var

    :param var:
        pointer to fb_var_screeninfo
    :type var: const struct fb_var_screeninfo \*

    :param par:
        pointer to i810fb_par
    :type par: struct i810fb_par \*

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

    :param regno:
        DAC index
    :type regno: u8

    :param red:
        red
    :type red: u8 \*

    :param green:
        green
    :type green: u8 \*

    :param blue:
        blue
    :type blue: u8 \*

    :param transp:
        transparency (alpha)
    :type transp: u8 \*

    :param info:
        pointer to fb_info
    :type info: struct fb_info \*

.. _`i810fb_getcolreg.description`:

Description
-----------

Gets the red, green and blue values of the hardware DAC as pointed by \ ``regno``\ 
and writes them to \ ``red``\ , \ ``green``\  and \ ``blue``\  respectively

.. _`i810_init_monspecs`:

i810_init_monspecs
==================

.. c:function:: void i810_init_monspecs(struct fb_info *info)

    :param info:
        pointer to device specific info structure
    :type info: struct fb_info \*

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

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

    :param info:
        pointer to current fb_info structure
    :type info: struct fb_info \*

.. _`i810_init_device`:

i810_init_device
================

.. c:function:: void i810_init_device(struct i810fb_par *par)

    initialize device

    :param par:
        pointer to i810fb_par structure
    :type par: struct i810fb_par \*

.. This file was automatic generated / don't edit.

