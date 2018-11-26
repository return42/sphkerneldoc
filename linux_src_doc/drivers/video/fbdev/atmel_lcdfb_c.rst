.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/atmel_lcdfb.c

.. _`atmel_lcdfb_alloc_video_memory`:

atmel_lcdfb_alloc_video_memory
==============================

.. c:function:: int atmel_lcdfb_alloc_video_memory(struct atmel_lcdfb_info *sinfo)

    Allocate framebuffer memory

    :param sinfo:
        the frame buffer to allocate memory for
    :type sinfo: struct atmel_lcdfb_info \*

.. _`atmel_lcdfb_alloc_video_memory.description`:

Description
-----------

This function is called only from the \ :c:func:`atmel_lcdfb_probe`\ 
so no locking by fb_info->mm_lock around smem_len setting is needed.

.. _`atmel_lcdfb_check_var`:

atmel_lcdfb_check_var
=====================

.. c:function:: int atmel_lcdfb_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    Validates a var passed in.

    :param var:
        frame buffer variable screen structure
    :type var: struct fb_var_screeninfo \*

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`atmel_lcdfb_check_var.description`:

Description
-----------

Checks to see if the hardware supports the state requested by
var passed in. This function does not alter the hardware
state!!!  This means the data stored in struct fb_info and
struct atmel_lcdfb_info do not change. This includes the var
inside of struct fb_info.  Do NOT change these. This function
can be called on its own if we intent to only test a mode and
not actually set it. The stuff in modedb.c is a example of
this. If the var passed in is slightly off by what the
hardware can support then we alter the var PASSED in to what
we can do. If the hardware doesn't support mode change a
-EINVAL will be returned by the upper layers. You don't need
to implement this function then. If you hardware doesn't
support changing the resolution then this function is not
needed. In this case the driver would just provide a var that
represents the static state the screen is in.

Returns negative errno on error, or zero on success.

.. _`atmel_lcdfb_set_par`:

atmel_lcdfb_set_par
===================

.. c:function:: int atmel_lcdfb_set_par(struct fb_info *info)

    Alters the hardware state.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`atmel_lcdfb_set_par.description`:

Description
-----------

Using the fb_var_screeninfo in fb_info we set the resolution
of the this particular framebuffer. This function alters the
par AND the fb_fix_screeninfo stored in fb_info. It doesn't
not alter var in fb_info since we are using that data. This
means we depend on the data in var inside fb_info to be
supported by the hardware.  atmel_lcdfb_check_var is always called
before atmel_lcdfb_set_par to ensure this.  Again if you can't
change the resolution you don't need this function.

.. _`atmel_lcdfb_setcolreg`:

atmel_lcdfb_setcolreg
=====================

.. c:function:: int atmel_lcdfb_setcolreg(unsigned int regno, unsigned int red, unsigned int green, unsigned int blue, unsigned int transp, struct fb_info *info)

    Optional function. Sets a color register.

    :param regno:
        Which register in the CLUT we are programming
    :type regno: unsigned int

    :param red:
        The red value which can be up to 16 bits wide
    :type red: unsigned int

    :param green:
        The green value which can be up to 16 bits wide
    :type green: unsigned int

    :param blue:
        The blue value which can be up to 16 bits wide.
    :type blue: unsigned int

    :param transp:
        If supported the alpha value which can be up to 16 bits wide.
    :type transp: unsigned int

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

.. _`atmel_lcdfb_setcolreg.description`:

Description
-----------

Set a single color register. The values supplied have a 16 bit
magnitude which needs to be scaled in this function for the hardware.
Things to take into consideration are how many color registers, if
any, are supported with the current color visual. With truecolor mode
no color palettes are supported. Here a pseudo palette is created
which we store the value in pseudo_palette in struct fb_info. For
pseudocolor mode we have a limited color palette. To deal with this
we can program what color is displayed for a particular pixel value.
DirectColor is similar in that we can program each color field. If
we have a static colormap we don't need to implement this function.

Returns negative errno on error, or zero on success. In an
ideal world, this would have been the case, but as it turns
out, the other drivers return 1 on failure, so that's what
we're going to do.

.. This file was automatic generated / don't edit.

