.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/modedb.c

.. _`fb_try_mode`:

fb_try_mode
===========

.. c:function:: int fb_try_mode(struct fb_var_screeninfo *var, struct fb_info *info, const struct fb_videomode *mode, unsigned int bpp)

    test a video mode

    :param var:
        frame buffer user defined part of display
    :type var: struct fb_var_screeninfo \*

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

    :param mode:
        frame buffer video mode structure
    :type mode: const struct fb_videomode \*

    :param bpp:
        color depth in bits per pixel
    :type bpp: unsigned int

.. _`fb_try_mode.description`:

Description
-----------

     Tries a video mode to test it's validity for device \ ``info``\ .

     Returns 1 on success.

.. _`fb_find_mode`:

fb_find_mode
============

.. c:function:: int fb_find_mode(struct fb_var_screeninfo *var, struct fb_info *info, const char *mode_option, const struct fb_videomode *db, unsigned int dbsize, const struct fb_videomode *default_mode, unsigned int default_bpp)

    finds a valid video mode

    :param var:
        frame buffer user defined part of display
    :type var: struct fb_var_screeninfo \*

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

    :param mode_option:
        string video mode to find
    :type mode_option: const char \*

    :param db:
        video mode database
    :type db: const struct fb_videomode \*

    :param dbsize:
        size of \ ``db``\ 
    :type dbsize: unsigned int

    :param default_mode:
        default video mode to fall back to
    :type default_mode: const struct fb_videomode \*

    :param default_bpp:
        default color depth in bits per pixel
    :type default_bpp: unsigned int

.. _`fb_find_mode.description`:

Description
-----------

Finds a suitable video mode, starting with the specified mode
in \ ``mode_option``\  with fallback to \ ``default_mode``\ .  If
\ ``default_mode``\  fails, all modes in the video mode database will
be tried.

Valid mode specifiers for \ ``mode_option``\ ::

    <xres>x<yres>[M][R][-<bpp>][@<refresh>][i][p][m]

or ::

    <name>[-<bpp>][@<refresh>]

with <xres>, <yres>, <bpp> and <refresh> decimal numbers and
<name> a string.

If 'M' is present after yres (and before refresh/bpp if present),
the function will compute the timings using VESA(tm) Coordinated
Video Timings (CVT).  If 'R' is present after 'M', will compute with
reduced blanking (for flatpanels).  If 'i' or 'p' are present, compute
interlaced or progressive mode.  If 'm' is present, add margins equal
to 1.8% of xres rounded down to 8 pixels, and 1.8% of yres. The char
'i', 'p' and 'm' must be after 'M' and 'R'. Example::

    1024x768MR-8@60m - Reduced blank with margins at 60Hz.

.. _`fb_find_mode.note`:

NOTE
----

The passed struct \ ``var``\  is _not_ cleared!  This allows you
to supply values for e.g. the grayscale and accel_flags fields.

Returns zero for failure, 1 if using specified \ ``mode_option``\ ,
2 if using specified \ ``mode_option``\  with an ignored refresh rate,
3 if default mode is used, 4 if fall back to any valid mode.

.. _`fb_var_to_videomode`:

fb_var_to_videomode
===================

.. c:function:: void fb_var_to_videomode(struct fb_videomode *mode, const struct fb_var_screeninfo *var)

    convert fb_var_screeninfo to fb_videomode

    :param mode:
        pointer to struct fb_videomode
    :type mode: struct fb_videomode \*

    :param var:
        pointer to struct fb_var_screeninfo
    :type var: const struct fb_var_screeninfo \*

.. _`fb_videomode_to_var`:

fb_videomode_to_var
===================

.. c:function:: void fb_videomode_to_var(struct fb_var_screeninfo *var, const struct fb_videomode *mode)

    convert fb_videomode to fb_var_screeninfo

    :param var:
        pointer to struct fb_var_screeninfo
    :type var: struct fb_var_screeninfo \*

    :param mode:
        pointer to struct fb_videomode
    :type mode: const struct fb_videomode \*

.. _`fb_mode_is_equal`:

fb_mode_is_equal
================

.. c:function:: int fb_mode_is_equal(const struct fb_videomode *mode1, const struct fb_videomode *mode2)

    compare 2 videomodes

    :param mode1:
        first videomode
    :type mode1: const struct fb_videomode \*

    :param mode2:
        second videomode
    :type mode2: const struct fb_videomode \*

.. _`fb_mode_is_equal.return`:

Return
------

1 if equal, 0 if not

.. _`fb_find_best_mode`:

fb_find_best_mode
=================

.. c:function:: const struct fb_videomode *fb_find_best_mode(const struct fb_var_screeninfo *var, struct list_head *head)

    find best matching videomode

    :param var:
        pointer to struct fb_var_screeninfo
    :type var: const struct fb_var_screeninfo \*

    :param head:
        pointer to struct list_head of modelist
    :type head: struct list_head \*

.. _`fb_find_best_mode.return`:

Return
------

struct fb_videomode, NULL if none found

.. _`fb_find_best_mode.important`:

IMPORTANT
---------

This function assumes that all modelist entries in
info->modelist are valid.

.. _`fb_find_best_mode.notes`:

NOTES
-----

Finds best matching videomode which has an equal or greater dimension than
var->xres and var->yres.  If more than 1 videomode is found, will return
the videomode with the highest refresh rate

.. _`fb_find_nearest_mode`:

fb_find_nearest_mode
====================

.. c:function:: const struct fb_videomode *fb_find_nearest_mode(const struct fb_videomode *mode, struct list_head *head)

    find closest videomode

    :param mode:
        pointer to struct fb_videomode
    :type mode: const struct fb_videomode \*

    :param head:
        pointer to modelist
    :type head: struct list_head \*

.. _`fb_find_nearest_mode.description`:

Description
-----------

Finds best matching videomode, smaller or greater in dimension.
If more than 1 videomode is found, will return the videomode with
the closest refresh rate.

.. _`fb_match_mode`:

fb_match_mode
=============

.. c:function:: const struct fb_videomode *fb_match_mode(const struct fb_var_screeninfo *var, struct list_head *head)

    find a videomode which exactly matches the timings in var

    :param var:
        pointer to struct fb_var_screeninfo
    :type var: const struct fb_var_screeninfo \*

    :param head:
        pointer to struct list_head of modelist
    :type head: struct list_head \*

.. _`fb_match_mode.return`:

Return
------

struct fb_videomode, NULL if none found

.. _`fb_add_videomode`:

fb_add_videomode
================

.. c:function:: int fb_add_videomode(const struct fb_videomode *mode, struct list_head *head)

    adds videomode entry to modelist

    :param mode:
        videomode to add
    :type mode: const struct fb_videomode \*

    :param head:
        struct list_head of modelist
    :type head: struct list_head \*

.. _`fb_add_videomode.notes`:

NOTES
-----

Will only add unmatched mode entries

.. _`fb_delete_videomode`:

fb_delete_videomode
===================

.. c:function:: void fb_delete_videomode(const struct fb_videomode *mode, struct list_head *head)

    removed videomode entry from modelist

    :param mode:
        videomode to remove
    :type mode: const struct fb_videomode \*

    :param head:
        struct list_head of modelist
    :type head: struct list_head \*

.. _`fb_delete_videomode.notes`:

NOTES
-----

Will remove all matching mode entries

.. _`fb_destroy_modelist`:

fb_destroy_modelist
===================

.. c:function:: void fb_destroy_modelist(struct list_head *head)

    destroy modelist

    :param head:
        struct list_head of modelist
    :type head: struct list_head \*

.. _`fb_videomode_to_modelist`:

fb_videomode_to_modelist
========================

.. c:function:: void fb_videomode_to_modelist(const struct fb_videomode *modedb, int num, struct list_head *head)

    convert mode array to mode list

    :param modedb:
        array of struct fb_videomode
    :type modedb: const struct fb_videomode \*

    :param num:
        number of entries in array
    :type num: int

    :param head:
        struct list_head of modelist
    :type head: struct list_head \*

.. This file was automatic generated / don't edit.

