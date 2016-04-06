
.. _API-fb-find-mode:

============
fb_find_mode
============

*man fb_find_mode(9)*

*4.6.0-rc1*

finds a valid video mode


Synopsis
========

.. c:function:: int fb_find_mode( struct fb_var_screeninfo * var, struct fb_info * info, const char * mode_option, const struct fb_videomode * db, unsigned int dbsize, const struct fb_videomode * default_mode, unsigned int default_bpp )

Arguments
=========

``var``
    frame buffer user defined part of display

``info``
    frame buffer info structure

``mode_option``
    string video mode to find

``db``
    video mode database

``dbsize``
    size of ``db``

``default_mode``
    default video mode to fall back to

``default_bpp``
    default color depth in bits per pixel


Description
===========

Finds a suitable video mode, starting with the specified mode in ``mode_option`` with fallback to ``default_mode``. If ``default_mode`` fails, all modes in the video mode database
will be tried.

Valid mode specifiers for ``mode_option``:

<xres>x<yres>[M][R][-<bpp>][@<refresh>][i][m] or <name>[-<bpp>][@<refresh>]

with <xres>, <yres>, <bpp> and <refresh> decimal numbers and <name> a string.

If 'M' is present after yres (and before refresh/bpp if present), the function will compute the timings using VESA(tm) Coordinated Video Timings (CVT). If 'R' is present after 'M',
will compute with reduced blanking (for flatpanels). If 'i' is present, compute interlaced mode. If 'm' is present, add margins equal to 1.8% of xres rounded down to 8 pixels, and
1.8% of yres. The char 'i' and 'm' must be after 'M' and 'R'. Example:

1024x768MR-8\ ``60m`` - Reduced blank with margins at 60Hz.


NOTE
====

The passed struct ``var`` is _not_ cleared! This allows you to supply values for e.g. the grayscale and accel_flags fields.

Returns zero for failure, 1 if using specified ``mode_option``, 2 if using specified ``mode_option`` with an ignored refresh rate, 3 if default mode is used, 4 if fall back to any
valid mode.
