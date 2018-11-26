.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/sstfb.c

.. _`sstfb_check_var`:

sstfb_check_var
===============

.. c:function:: int sstfb_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    Optional function.  Validates a var passed in.

    :param var:
        frame buffer variable screen structure
    :type var: struct fb_var_screeninfo \*

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`sstfb_check_var.description`:

Description
-----------

Limit to the abilities of a single chip as SLI is not supported
by this driver.

.. _`sstfb_set_par`:

sstfb_set_par
=============

.. c:function:: int sstfb_set_par(struct fb_info *info)

    Optional function.  Alters the hardware state.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`sstfb_setcolreg`:

sstfb_setcolreg
===============

.. c:function:: int sstfb_setcolreg(u_int regno, u_int red, u_int green, u_int blue, u_int transp, struct fb_info *info)

    Optional function. Sets a color register.

    :param regno:
        hardware colormap register
    :type regno: u_int

    :param red:
        frame buffer colormap structure
    :type red: u_int

    :param green:
        The green value which can be up to 16 bits wide
    :type green: u_int

    :param blue:
        The blue value which can be up to 16 bits wide.
    :type blue: u_int

    :param transp:
        If supported the alpha value which can be up to 16 bits wide.
    :type transp: u_int

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

.. This file was automatic generated / don't edit.

