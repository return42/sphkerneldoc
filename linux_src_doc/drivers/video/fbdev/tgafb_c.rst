.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/tgafb.c

.. _`tgafb_check_var`:

tgafb_check_var
===============

.. c:function:: int tgafb_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    Optional function.  Validates a var passed in.

    :param var:
        frame buffer variable screen structure
    :type var: struct fb_var_screeninfo \*

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`tgafb_set_par`:

tgafb_set_par
=============

.. c:function:: int tgafb_set_par(struct fb_info *info)

    Optional function.  Alters the hardware state.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`tgafb_setcolreg`:

tgafb_setcolreg
===============

.. c:function:: int tgafb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    Optional function. Sets a color register.

    :param regno:
        boolean, 0 copy local, 1 \ :c:func:`get_user`\  function
    :type regno: unsigned

    :param red:
        frame buffer colormap structure
    :type red: unsigned

    :param green:
        The green value which can be up to 16 bits wide
    :type green: unsigned

    :param blue:
        The blue value which can be up to 16 bits wide.
    :type blue: unsigned

    :param transp:
        If supported the alpha value which can be up to 16 bits wide.
    :type transp: unsigned

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

.. _`tgafb_blank`:

tgafb_blank
===========

.. c:function:: int tgafb_blank(int blank, struct fb_info *info)

    Optional function.  Blanks the display.

    :param blank:
        *undescribed*
    :type blank: int

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`tgafb_imageblit`:

tgafb_imageblit
===============

.. c:function:: void tgafb_imageblit(struct fb_info *info, const struct fb_image *image)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Copies a image from system memory to the screen.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param image:
        structure defining the image.
    :type image: const struct fb_image \*

.. _`tgafb_fillrect`:

tgafb_fillrect
==============

.. c:function:: void tgafb_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Draws a rectangle on the screen.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param rect:
        structure defining the rectagle and operation.
    :type rect: const struct fb_fillrect \*

.. _`copyarea_line_8bpp`:

copyarea_line_8bpp
==================

.. c:function:: void copyarea_line_8bpp(struct fb_info *info, u32 dy, u32 sy, u32 height, u32 width)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Copies on area of the screen to another area.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param dy:
        *undescribed*
    :type dy: u32

    :param sy:
        *undescribed*
    :type sy: u32

    :param height:
        *undescribed*
    :type height: u32

    :param width:
        *undescribed*
    :type width: u32

.. This file was automatic generated / don't edit.

