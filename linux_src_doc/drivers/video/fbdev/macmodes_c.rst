.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/macmodes.c

.. _`mac_vmode_to_var`:

mac_vmode_to_var
================

.. c:function:: int mac_vmode_to_var(int vmode, int cmode, struct fb_var_screeninfo *var)

    converts vmode/cmode pair to var structure

    :param vmode:
        MacOS video mode
    :type vmode: int

    :param cmode:
        MacOS color mode
    :type cmode: int

    :param var:
        frame buffer video mode structure
    :type var: struct fb_var_screeninfo \*

.. _`mac_vmode_to_var.description`:

Description
-----------

     Converts a MacOS vmode/cmode pair to a frame buffer video
     mode structure.

     Returns negative errno on error, or zero for success.

.. _`mac_var_to_vmode`:

mac_var_to_vmode
================

.. c:function:: int mac_var_to_vmode(const struct fb_var_screeninfo *var, int *vmode, int *cmode)

    convert var structure to MacOS vmode/cmode pair

    :param var:
        frame buffer video mode structure
    :type var: const struct fb_var_screeninfo \*

    :param vmode:
        MacOS video mode
    :type vmode: int \*

    :param cmode:
        MacOS color mode
    :type cmode: int \*

.. _`mac_var_to_vmode.description`:

Description
-----------

     Converts a frame buffer video mode structure to a MacOS
     vmode/cmode pair.

     Returns negative errno on error, or zero for success.

.. _`mac_map_monitor_sense`:

mac_map_monitor_sense
=====================

.. c:function:: int mac_map_monitor_sense(int sense)

    Convert monitor sense to vmode

    :param sense:
        Macintosh monitor sense number
    :type sense: int

.. _`mac_map_monitor_sense.description`:

Description
-----------

     Converts a Macintosh monitor sense number to a MacOS
     vmode number.

     Returns MacOS vmode video mode number.

.. _`mac_find_mode`:

mac_find_mode
=============

.. c:function:: int mac_find_mode(struct fb_var_screeninfo *var, struct fb_info *info, const char *mode_option, unsigned int default_bpp)

    find a video mode

    :param var:
        frame buffer user defined part of display
    :type var: struct fb_var_screeninfo \*

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

    :param mode_option:
        video mode name (see mac_modedb[])
    :type mode_option: const char \*

    :param default_bpp:
        default color depth in bits per pixel
    :type default_bpp: unsigned int

.. _`mac_find_mode.description`:

Description
-----------

     Finds a suitable video mode.  Tries to set mode specified
     by \ ``mode_option``\ .  If the name of the wanted mode begins with
     'mac', the Mac video mode database will be used, otherwise it
     will fall back to the standard video mode database.

.. _`mac_find_mode.note`:

Note
----

Function marked as __init and can only be used during
     system boot.

     Returns error code from fb_find_mode (see fb_find_mode
     function).

.. This file was automatic generated / don't edit.

