.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/macmodes.c

.. _`mac_vmode_to_var`:

mac_vmode_to_var
================

.. c:function:: int mac_vmode_to_var(int vmode, int cmode, struct fb_var_screeninfo *var)

    converts vmode/cmode pair to var structure

    :param int vmode:
        MacOS video mode

    :param int cmode:
        MacOS color mode

    :param struct fb_var_screeninfo \*var:
        frame buffer video mode structure

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

    :param const struct fb_var_screeninfo \*var:
        frame buffer video mode structure

    :param int \*vmode:
        MacOS video mode

    :param int \*cmode:
        MacOS color mode

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

    :param int sense:
        Macintosh monitor sense number

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

    :param struct fb_var_screeninfo \*var:
        frame buffer user defined part of display

    :param struct fb_info \*info:
        frame buffer info structure

    :param const char \*mode_option:
        video mode name (see mac_modedb[])

    :param unsigned int default_bpp:
        default color depth in bits per pixel

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

Function marked as \__init and can only be used during
system boot.

Returns error code from fb_find_mode (see fb_find_mode
function).

.. This file was automatic generated / don't edit.

