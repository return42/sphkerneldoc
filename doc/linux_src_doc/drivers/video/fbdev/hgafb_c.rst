.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/hgafb.c

.. _`hgafb_open`:

hgafb_open
==========

.. c:function:: int hgafb_open(struct fb_info *info, int init)

    open the framebuffer device

    :param struct fb_info \*info:
        pointer to fb_info object containing info for current hga board

    :param int init:
        *undescribed*

.. _`hgafb_release`:

hgafb_release
=============

.. c:function:: int hgafb_release(struct fb_info *info, int init)

    open the framebuffer device

    :param struct fb_info \*info:
        pointer to fb_info object containing info for current hga board

    :param int init:
        *undescribed*

.. _`hgafb_setcolreg`:

hgafb_setcolreg
===============

.. c:function:: int hgafb_setcolreg(u_int regno, u_int red, u_int green, u_int blue, u_int transp, struct fb_info *info)

    set color registers

    :param u_int regno:
        register index to set

    :param u_int red:
        red value, unused

    :param u_int green:
        green value, unused

    :param u_int blue:
        blue value, unused

    :param u_int transp:
        transparency value, unused

    :param struct fb_info \*info:
        unused

.. _`hgafb_setcolreg.description`:

Description
-----------

This callback function is used to set the color registers of a HGA
board. Since we have only two fixed colors only \ ``regno``\  is checked.
A zero is returned on success and 1 for failure.

.. _`hgafb_pan_display`:

hgafb_pan_display
=================

.. c:function:: int hgafb_pan_display(struct fb_var_screeninfo *var, struct fb_info *info)

    pan or wrap the display

    :param struct fb_var_screeninfo \*var:
        contains new xoffset, yoffset and vmode values

    :param struct fb_info \*info:
        pointer to fb_info object containing info for current hga board

.. _`hgafb_pan_display.description`:

Description
-----------

This function looks only at xoffset, yoffset and the \ ``FB_VMODE_YWRAP``\ 
flag in \ ``var``\ . If input parameters are correct it calls \ :c:func:`hga_pan`\  to
program the hardware. \ ``info``\ ->var is updated to the new values.
A zero is returned on success and \ ``-EINVAL``\  for failure.

.. _`hgafb_blank`:

hgafb_blank
===========

.. c:function:: int hgafb_blank(int blank_mode, struct fb_info *info)

    (un)blank the screen

    :param int blank_mode:
        blanking method to use

    :param struct fb_info \*info:
        unused

.. _`hgafb_blank.description`:

Description
-----------

Blank the screen if blank_mode != 0, else unblank.
Implements VESA suspend and powerdown modes on hardware that supports
disabling hsync/vsync:
\ ``blank_mode``\  == 2 means suspend vsync,
\ ``blank_mode``\  == 3 means suspend hsync,
\ ``blank_mode``\  == 4 means powerdown.

.. This file was automatic generated / don't edit.

