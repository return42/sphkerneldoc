.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/ffb.c

.. _`ffb_fillrect`:

ffb_fillrect
============

.. c:function:: void ffb_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    Draws a rectangle on the screen.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param rect:
        structure defining the rectagle and operation.
    :type rect: const struct fb_fillrect \*

.. _`ffb_copyarea`:

ffb_copyarea
============

.. c:function:: void ffb_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    Copies on area of the screen to another area.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param area:
        structure defining the source and destination.
    :type area: const struct fb_copyarea \*

.. _`ffb_imageblit`:

ffb_imageblit
=============

.. c:function:: void ffb_imageblit(struct fb_info *info, const struct fb_image *image)

    Copies a image from system memory to the screen.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

    :param image:
        structure defining the image.
    :type image: const struct fb_image \*

.. _`ffb_setcolreg`:

ffb_setcolreg
=============

.. c:function:: int ffb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

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

.. _`ffb_blank`:

ffb_blank
=========

.. c:function:: int ffb_blank(int blank, struct fb_info *info)

    Optional function.  Blanks the display.

    :param blank:
        *undescribed*
    :type blank: int

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. This file was automatic generated / don't edit.

