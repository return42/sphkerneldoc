.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/cg6.c

.. _`cg6_fillrect`:

cg6_fillrect
============

.. c:function:: void cg6_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    Draws a rectangle on the screen.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_fillrect \*rect:
        structure defining the rectagle and operation.

.. _`cg6_copyarea`:

cg6_copyarea
============

.. c:function:: void cg6_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    Copies one area of the screen to another area.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_copyarea \*area:
        Structure providing the data to copy the framebuffer contents
        from one region to another.

.. _`cg6_copyarea.description`:

Description
-----------

This drawing operation copies a rectangular area from one area of the
screen to another area.

.. _`cg6_imageblit`:

cg6_imageblit
=============

.. c:function:: void cg6_imageblit(struct fb_info *info, const struct fb_image *image)

    Copies a image from system memory to the screen.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param const struct fb_image \*image:
        structure defining the image.

.. _`cg6_setcolreg`:

cg6_setcolreg
=============

.. c:function:: int cg6_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

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

.. _`cg6_blank`:

cg6_blank
=========

.. c:function:: int cg6_blank(int blank, struct fb_info *info)

    Blanks the display.

    :param int blank:
        *undescribed*

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. This file was automatic generated / don't edit.

