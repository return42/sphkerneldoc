.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/riva/fbdev.c

.. _`rivafb_load_cursor_image`:

rivafb_load_cursor_image
========================

.. c:function:: void rivafb_load_cursor_image(struct riva_par *par, u8 *data8, u16 bg, u16 fg, u32 w, u32 h)

    load cursor image to hardware

    :param struct riva_par \*par:
        pointer to private data

    :param u8 \*data8:
        *undescribed*

    :param u16 bg:
        background color (ARGB1555) - alpha bit determines opacity

    :param u16 fg:
        foreground color (ARGB1555)

    :param u32 w:
        width of cursor image in pixels

    :param u32 h:
        height of cursor image in scanlines

.. _`rivafb_load_cursor_image.description`:

Description
-----------

Loads cursor image based on a monochrome source and mask bitmap.  The
image bits determines the color of the pixel, 0 for background, 1 for
foreground.  Only the affected region (as determined by \ ``w``\  and \ ``h``\ 
parameters) will be updated.

.. _`rivafb_load_cursor_image.called-from`:

CALLED FROM
-----------

\ :c:func:`rivafb_cursor`\ 

.. _`riva_wclut`:

riva_wclut
==========

.. c:function:: void riva_wclut(RIVA_HW_INST *chip, unsigned char regnum, unsigned char red, unsigned char green, unsigned char blue)

    set CLUT entry

    :param RIVA_HW_INST \*chip:
        pointer to RIVA_HW_INST object

    :param unsigned char regnum:
        register number

    :param unsigned char red:
        red component

    :param unsigned char green:
        green component

    :param unsigned char blue:
        blue component

.. _`riva_wclut.description`:

Description
-----------

Sets color register \ ``regnum``\ .

.. _`riva_wclut.called-from`:

CALLED FROM
-----------

\ :c:func:`rivafb_setcolreg`\ 

.. _`riva_rclut`:

riva_rclut
==========

.. c:function:: void riva_rclut(RIVA_HW_INST *chip, unsigned char regnum, unsigned char *red, unsigned char *green, unsigned char *blue)

    read fromCLUT register

    :param RIVA_HW_INST \*chip:
        pointer to RIVA_HW_INST object

    :param unsigned char regnum:
        register number

    :param unsigned char \*red:
        red component

    :param unsigned char \*green:
        green component

    :param unsigned char \*blue:
        blue component

.. _`riva_rclut.description`:

Description
-----------

Reads red, green, and blue from color register \ ``regnum``\ .

.. _`riva_rclut.called-from`:

CALLED FROM
-----------

\ :c:func:`rivafb_setcolreg`\ 

.. _`riva_save_state`:

riva_save_state
===============

.. c:function:: void riva_save_state(struct riva_par *par, struct riva_regs *regs)

    saves current chip state

    :param struct riva_par \*par:
        pointer to riva_par object containing info for current riva board

    :param struct riva_regs \*regs:
        pointer to riva_regs object

.. _`riva_save_state.description`:

Description
-----------

Saves current chip state to \ ``regs``\ .

.. _`riva_save_state.called-from`:

CALLED FROM
-----------

\ :c:func:`rivafb_probe`\ 

.. _`riva_load_state`:

riva_load_state
===============

.. c:function:: void riva_load_state(struct riva_par *par, struct riva_regs *regs)

    loads current chip state

    :param struct riva_par \*par:
        pointer to riva_par object containing info for current riva board

    :param struct riva_regs \*regs:
        pointer to riva_regs object

.. _`riva_load_state.description`:

Description
-----------

Loads chip state from \ ``regs``\ .

.. _`riva_load_state.called-from`:

CALLED FROM
-----------

\ :c:func:`riva_load_video_mode`\ 
\ :c:func:`rivafb_probe`\ 
\ :c:func:`rivafb_remove`\ 

.. _`riva_load_video_mode`:

riva_load_video_mode
====================

.. c:function:: int riva_load_video_mode(struct fb_info *info)

    calculate timings

    :param struct fb_info \*info:
        pointer to fb_info object containing info for current riva board

.. _`riva_load_video_mode.description`:

Description
-----------

Calculate some timings and then send em off to \ :c:func:`riva_load_state`\ .

.. _`riva_load_video_mode.called-from`:

CALLED FROM
-----------

\ :c:func:`rivafb_set_par`\ 

.. _`rivafb_do_maximize`:

rivafb_do_maximize
==================

.. c:function:: int rivafb_do_maximize(struct fb_info *info, struct fb_var_screeninfo *var, int nom, int den)

    :param struct fb_info \*info:
        pointer to fb_info object containing info for current riva board

    :param struct fb_var_screeninfo \*var:
        *undescribed*

    :param int nom:
        *undescribed*

    :param int den:
        *undescribed*

.. _`rivafb_do_maximize.description`:

Description
-----------

.

.. _`rivafb_do_maximize.return`:

Return
------

-EINVAL on failure, 0 on success

.. _`rivafb_do_maximize.called-from`:

CALLED FROM
-----------

\ :c:func:`rivafb_check_var`\ 

.. _`riva_get_cmap_len`:

riva_get_cmap_len
=================

.. c:function:: int riva_get_cmap_len(const struct fb_var_screeninfo *var)

    query current color map length

    :param const struct fb_var_screeninfo \*var:
        standard kernel fb changeable data

.. _`riva_get_cmap_len.description`:

Description
-----------

Get current color map length.

.. _`riva_get_cmap_len.return`:

Return
------

Length of color map

.. _`riva_get_cmap_len.called-from`:

CALLED FROM
-----------

\ :c:func:`rivafb_setcolreg`\ 

.. _`rivafb_pan_display`:

rivafb_pan_display
==================

.. c:function:: int rivafb_pan_display(struct fb_var_screeninfo *var, struct fb_info *info)

    :param struct fb_var_screeninfo \*var:
        standard kernel fb changeable data

    :param struct fb_info \*info:
        pointer to fb_info object containing info for current riva board

.. _`rivafb_pan_display.description`:

Description
-----------

Pan (or wrap, depending on the \`vmode' field) the display using the
\`xoffset' and \`yoffset' fields of the \`var' structure.
If the values don't fit, return -EINVAL.

This call looks only at xoffset, yoffset and the FB_VMODE_YWRAP flag

.. _`rivafb_setcolreg`:

rivafb_setcolreg
================

.. c:function:: int rivafb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    :param unsigned regno:
        register index

    :param unsigned red:
        red component

    :param unsigned green:
        green component

    :param unsigned blue:
        blue component

    :param unsigned transp:
        transparency

    :param struct fb_info \*info:
        pointer to fb_info object containing info for current riva board

.. _`rivafb_setcolreg.description`:

Description
-----------

Set a single color register. The values supplied have a 16 bit
magnitude.

.. _`rivafb_setcolreg.return`:

Return
------

Return != 0 for invalid regno.

.. _`rivafb_setcolreg.called-from`:

CALLED FROM
-----------

fbcmap.c:fb_set_cmap()

.. _`rivafb_fillrect`:

rivafb_fillrect
===============

.. c:function:: void rivafb_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    hardware accelerated color fill function

    :param struct fb_info \*info:
        pointer to fb_info structure

    :param const struct fb_fillrect \*rect:
        pointer to fb_fillrect structure

.. _`rivafb_fillrect.description`:

Description
-----------

This function fills up a region of framebuffer memory with a solid
color with a choice of two different ROP's, copy or invert.

.. _`rivafb_fillrect.called-from`:

CALLED FROM
-----------

framebuffer hook

.. _`rivafb_copyarea`:

rivafb_copyarea
===============

.. c:function:: void rivafb_copyarea(struct fb_info *info, const struct fb_copyarea *region)

    hardware accelerated blit function

    :param struct fb_info \*info:
        pointer to fb_info structure

    :param const struct fb_copyarea \*region:
        pointer to fb_copyarea structure

.. _`rivafb_copyarea.description`:

Description
-----------

This copies an area of pixels from one location to another

.. _`rivafb_copyarea.called-from`:

CALLED FROM
-----------

framebuffer hook

.. _`rivafb_imageblit`:

rivafb_imageblit
================

.. c:function:: void rivafb_imageblit(struct fb_info *info, const struct fb_image *image)

    hardware accelerated color expand function

    :param struct fb_info \*info:
        pointer to fb_info structure

    :param const struct fb_image \*image:
        pointer to fb_image structure

.. _`rivafb_imageblit.description`:

Description
-----------

If the source is a monochrome bitmap, the function fills up a a region
of framebuffer memory with pixels whose color is determined by the bit
setting of the bitmap, 1 - foreground, 0 - background.

If the source is not a monochrome bitmap, color expansion is not done.
In this case, it is channeled to a software function.

.. _`rivafb_imageblit.called-from`:

CALLED FROM
-----------

framebuffer hook

.. _`rivafb_cursor`:

rivafb_cursor
=============

.. c:function:: int rivafb_cursor(struct fb_info *info, struct fb_cursor *cursor)

    hardware cursor function

    :param struct fb_info \*info:
        pointer to info structure

    :param struct fb_cursor \*cursor:
        pointer to fbcursor structure

.. _`rivafb_cursor.description`:

Description
-----------

A cursor function that supports displaying a cursor image via hardware.
Within the kernel, copy and invert rops are supported.  If exported
to user space, only the copy rop will be supported.

CALLED FROM
framebuffer hook

.. This file was automatic generated / don't edit.

