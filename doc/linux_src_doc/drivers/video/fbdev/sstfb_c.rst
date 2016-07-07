.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/sstfb.c

.. _`sstfb_check_var`:

sstfb_check_var
===============

.. c:function:: int sstfb_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    Optional function.  Validates a var passed in.

    :param struct fb_var_screeninfo \*var:
        frame buffer variable screen structure

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

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

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`sstfb_setcolreg`:

sstfb_setcolreg
===============

.. c:function:: int sstfb_setcolreg(u_int regno, u_int red, u_int green, u_int blue, u_int transp, struct fb_info *info)

    Optional function. Sets a color register.

    :param u_int regno:
        hardware colormap register

    :param u_int red:
        frame buffer colormap structure

    :param u_int green:
        The green value which can be up to 16 bits wide

    :param u_int blue:
        The blue value which can be up to 16 bits wide.

    :param u_int transp:
        If supported the alpha value which can be up to 16 bits wide.

    :param struct fb_info \*info:
        frame buffer info structure

.. This file was automatic generated / don't edit.

