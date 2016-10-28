.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/leo.c

.. _`leo_setcolreg`:

leo_setcolreg
=============

.. c:function:: int leo_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

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

.. _`leo_blank`:

leo_blank
=========

.. c:function:: int leo_blank(int blank, struct fb_info *info)

    Optional function.  Blanks the display.

    :param int blank:
        *undescribed*

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. This file was automatic generated / don't edit.

