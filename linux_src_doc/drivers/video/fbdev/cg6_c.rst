.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/cg6.c

.. _`cg6_fillrect`:

cg6_fillrect
============

.. c:function:: void cg6_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    Draws a rectangle on the screen.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param rect:
        structure defining the rectagle and operation.
    :type rect: const struct fb_fillrect \*

.. _`cg6_copyarea`:

cg6_copyarea
============

.. c:function:: void cg6_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    Copies one area of the screen to another area.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param area:
        Structure providing the data to copy the framebuffer contents
        from one region to another.
    :type area: const struct fb_copyarea \*

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

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param image:
        structure defining the image.
    :type image: const struct fb_image \*

.. _`cg6_setcolreg`:

cg6_setcolreg
=============

.. c:function:: int cg6_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    Sets a color register.

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

.. _`cg6_blank`:

cg6_blank
=========

.. c:function:: int cg6_blank(int blank, struct fb_info *info)

    Blanks the display.

    :param blank:
        *undescribed*
    :type blank: int

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. This file was automatic generated / don't edit.

