.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/ffb.c

.. _`ffb_fillrect`:

ffb_fillrect
============

.. c:function:: void ffb_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    Draws a rectangle on the screen.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_fillrect \*rect:
        structure defining the rectagle and operation.

.. _`ffb_copyarea`:

ffb_copyarea
============

.. c:function:: void ffb_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    Copies on area of the screen to another area.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_copyarea \*area:
        structure defining the source and destination.

.. _`ffb_imageblit`:

ffb_imageblit
=============

.. c:function:: void ffb_imageblit(struct fb_info *info, const struct fb_image *image)

    Copies a image from system memory to the screen.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_image \*image:
        structure defining the image.

.. _`ffb_setcolreg`:

ffb_setcolreg
=============

.. c:function:: int ffb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    Sets a color register.

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

.. _`ffb_blank`:

ffb_blank
=========

.. c:function:: int ffb_blank(int blank, struct fb_info *info)

    Optional function.  Blanks the display.

    :param int blank:
        *undescribed*

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. This file was automatic generated / don't edit.

