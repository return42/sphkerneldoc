.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/cg3.c

.. _`cg3_setcolreg`:

cg3_setcolreg
=============

.. c:function:: int cg3_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

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

.. _`cg3_setcolreg.description`:

Description
-----------

The cg3 palette is loaded with 4 color values at each time

.. _`cg3_setcolreg.so-you-end-up-with`:

so you end up with
------------------

(rgb)(r), (gb)(rg), (b)(rgb), and so on.
We keep a sw copy of the hw cmap to assist us in this esoteric
loading procedure.

.. _`cg3_blank`:

cg3_blank
=========

.. c:function:: int cg3_blank(int blank, struct fb_info *info)

    Optional function.  Blanks the display.

    :param blank:
        *undescribed*
    :type blank: int

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. This file was automatic generated / don't edit.

