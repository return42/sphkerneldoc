.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/s1d13xxxfb.c

.. _`s1d13xxxfb_set_par`:

s1d13xxxfb_set_par
==================

.. c:function:: int s1d13xxxfb_set_par(struct fb_info *info)

    Alters the hardware state.

    :param struct fb_info \*info:
        frame buffer structure

.. _`s1d13xxxfb_set_par.description`:

Description
-----------

Using the fb_var_screeninfo in fb_info we set the depth of the
framebuffer. This function alters the par AND the
fb_fix_screeninfo stored in fb_info. It doesn't not alter var in
fb_info since we are using that data. This means we depend on the
data in var inside fb_info to be supported by the hardware.
xxxfb_check_var is always called before xxxfb_set_par to ensure this.

.. _`s1d13xxxfb_set_par.xxx-todo`:

XXX TODO
--------

write proper \ :c:func:`s1d13xxxfb_check_var`\ , without which that
function is quite useless.

.. _`s1d13xxxfb_setcolreg`:

s1d13xxxfb_setcolreg
====================

.. c:function:: int s1d13xxxfb_setcolreg(u_int regno, u_int red, u_int green, u_int blue, u_int transp, struct fb_info *info)

    sets a color register.

    :param u_int regno:
        Which register in the CLUT we are programming

    :param u_int red:
        The red value which can be up to 16 bits wide

    :param u_int green:
        The green value which can be up to 16 bits wide

    :param u_int blue:
        The blue value which can be up to 16 bits wide.

    :param u_int transp:
        If supported the alpha value which can be up to 16 bits wide.

    :param struct fb_info \*info:
        frame buffer info structure

.. _`s1d13xxxfb_setcolreg.description`:

Description
-----------

Returns negative errno on error, or zero on success.

.. _`s1d13xxxfb_blank`:

s1d13xxxfb_blank
================

.. c:function:: int s1d13xxxfb_blank(int blank_mode, struct fb_info *info)

    blanks the display.

    :param int blank_mode:
        the blank mode we want.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`s1d13xxxfb_blank.description`:

Description
-----------

Blank the screen if blank_mode != 0, else unblank. Return 0 if
blanking succeeded, != 0 if un-/blanking failed due to e.g. a
video mode which doesn't support it. Implements VESA suspend
and powerdown modes on hardware that supports disabling hsync/vsync:
blank_mode == 2: suspend vsync
blank_mode == 3: suspend hsync
blank_mode == 4: powerdown

Returns negative errno on error, or zero on success.

.. _`s1d13xxxfb_pan_display`:

s1d13xxxfb_pan_display
======================

.. c:function:: int s1d13xxxfb_pan_display(struct fb_var_screeninfo *var, struct fb_info *info)

    Pans the display.

    :param struct fb_var_screeninfo \*var:
        frame buffer variable screen structure

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`s1d13xxxfb_pan_display.description`:

Description
-----------

Pan (or wrap, depending on the \`vmode' field) the display using the
\`yoffset' field of the \`var' structure (\`xoffset'  not yet supported).
If the values don't fit, return -EINVAL.

Returns negative errno on error, or zero on success.

.. _`bltbit_wait_bitclear`:

bltbit_wait_bitclear
====================

.. c:function:: u8 bltbit_wait_bitclear(struct fb_info *info, u8 bit, int timeout)

    waits for change in register value

    :param struct fb_info \*info:
        frambuffer structure

    :param u8 bit:
        value currently in register

    :param int timeout:
        ...

.. _`bltbit_wait_bitclear.description`:

Description
-----------

waits until value changes FROM bit

.. _`s1d13xxxfb_fetch_hw_state`:

s1d13xxxfb_fetch_hw_state
=========================

.. c:function:: void s1d13xxxfb_fetch_hw_state(struct fb_info *info)

    Configure the framebuffer according to hardware setup.

    :param struct fb_info \*info:
        frame buffer structure

.. _`s1d13xxxfb_fetch_hw_state.description`:

Description
-----------

We setup the framebuffer structures according to the current
hardware setup. On some machines, the BIOS will have filled
the chip registers with such info, on others, these values will
have been written in some init procedure. In any case, the
software values needs to match the hardware ones. This is what
this function ensures.

.. _`s1d13xxxfb_fetch_hw_state.note`:

Note
----

some of the hardcoded values here might need some love to
work on various chips, and might need to no longer be hardcoded.

.. This file was automatic generated / don't edit.

