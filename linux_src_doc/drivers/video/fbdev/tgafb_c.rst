.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/tgafb.c

.. _`tgafb_check_var`:

tgafb_check_var
===============

.. c:function:: int tgafb_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    Optional function.  Validates a var passed in.

    :param struct fb_var_screeninfo \*var:
        frame buffer variable screen structure

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`tgafb_set_par`:

tgafb_set_par
=============

.. c:function:: int tgafb_set_par(struct fb_info *info)

    Optional function.  Alters the hardware state.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`tgafb_setcolreg`:

tgafb_setcolreg
===============

.. c:function:: int tgafb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    Optional function. Sets a color register.

    :param unsigned regno:
        boolean, 0 copy local, 1 \ :c:func:`get_user`\  function

    :param unsigned red:
        frame buffer colormap structure

    :param unsigned green:
        The green value which can be up to 16 bits wide

    :param unsigned blue:
        The blue value which can be up to 16 bits wide.

    :param unsigned transp:
        If supported the alpha value which can be up to 16 bits wide.

    :param struct fb_info \*info:
        frame buffer info structure

.. _`tgafb_blank`:

tgafb_blank
===========

.. c:function:: int tgafb_blank(int blank, struct fb_info *info)

    Optional function.  Blanks the display.

    :param int blank:
        *undescribed*

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`tgafb_imageblit`:

tgafb_imageblit
===============

.. c:function:: void tgafb_imageblit(struct fb_info *info, const struct fb_image *image)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Copies a image from system memory to the screen.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_image \*image:
        structure defining the image.

.. _`tgafb_fillrect`:

tgafb_fillrect
==============

.. c:function:: void tgafb_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Draws a rectangle on the screen.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_fillrect \*rect:
        structure defining the rectagle and operation.

.. _`copyarea_line_8bpp`:

copyarea_line_8bpp
==================

.. c:function:: void copyarea_line_8bpp(struct fb_info *info, u32 dy, u32 sy, u32 height, u32 width)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Copies on area of the screen to another area.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param u32 dy:
        *undescribed*

    :param u32 sy:
        *undescribed*

    :param u32 height:
        *undescribed*

    :param u32 width:
        *undescribed*

.. This file was automatic generated / don't edit.

