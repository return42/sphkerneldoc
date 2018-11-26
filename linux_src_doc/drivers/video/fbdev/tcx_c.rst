.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/tcx.c

.. _`tcx_setcolreg`:

tcx_setcolreg
=============

.. c:function:: int tcx_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

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

.. _`tcx_blank`:

tcx_blank
=========

.. c:function:: int tcx_blank(int blank, struct fb_info *info)

    Optional function.  Blanks the display.

    :param blank:
        *undescribed*
    :type blank: int

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. This file was automatic generated / don't edit.

