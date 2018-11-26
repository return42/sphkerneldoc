.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fbmon.c

.. _`fb_create_modedb`:

fb_create_modedb
================

.. c:function:: struct fb_videomode *fb_create_modedb(unsigned char *edid, int *dbsize, const struct fb_monspecs *specs)

    create video mode database

    :param edid:
        EDID data
    :type edid: unsigned char \*

    :param dbsize:
        database size
    :type dbsize: int \*

    :param specs:
        *undescribed*
    :type specs: const struct fb_monspecs \*

.. _`fb_create_modedb.return`:

Return
------

struct fb_videomode, \ ``dbsize``\  contains length of database

.. _`fb_create_modedb.description`:

Description
-----------

This function builds a mode database using the contents of the EDID
data

.. _`fb_destroy_modedb`:

fb_destroy_modedb
=================

.. c:function:: void fb_destroy_modedb(struct fb_videomode *modedb)

    destroys mode database

    :param modedb:
        mode database to destroy
    :type modedb: struct fb_videomode \*

.. _`fb_destroy_modedb.description`:

Description
-----------

Destroy mode database created by fb_create_modedb

.. _`fb_edid_add_monspecs`:

fb_edid_add_monspecs
====================

.. c:function:: void fb_edid_add_monspecs(unsigned char *edid, struct fb_monspecs *specs)

    add monitor video modes from E-EDID data

    :param edid:
        128 byte array with an E-EDID block
    :type edid: unsigned char \*

    :param specs:
        *undescribed*
    :type specs: struct fb_monspecs \*

.. _`fb_get_vblank`:

fb_get_vblank
=============

.. c:function:: u32 fb_get_vblank(u32 hfreq)

    get vertical blank time

    :param hfreq:
        horizontal freq
    :type hfreq: u32

.. _`fb_get_vblank.description`:

Description
-----------

vblank = right_margin + vsync_len + left_margin

.. _`fb_get_vblank.given`:

given
-----

right_margin = 1 (V_FRONTPORCH)
vsync_len    = 3
flyback      = 550

flyback \* hfreq
left_margin  = --------------- - vsync_len
1000000

.. _`fb_get_hblank_by_hfreq`:

fb_get_hblank_by_hfreq
======================

.. c:function:: u32 fb_get_hblank_by_hfreq(u32 hfreq, u32 xres)

    get horizontal blank time given hfreq

    :param hfreq:
        horizontal freq
    :type hfreq: u32

    :param xres:
        horizontal resolution in pixels
    :type xres: u32

.. _`fb_get_hblank_by_hfreq.description`:

Description
-----------


xres \* duty_cycle
hblank = ------------------
100 - duty_cycle

duty cycle = percent of htotal assigned to inactive display
duty cycle = C - (M/Hfreq)

.. _`fb_get_hblank_by_hfreq.where`:

where
-----

C = ((offset - scale factor) \* blank_scale)
-------------------------------------- + scale factor
256
M = blank_scale \* gradient

.. _`fb_get_hblank_by_dclk`:

fb_get_hblank_by_dclk
=====================

.. c:function:: u32 fb_get_hblank_by_dclk(u32 dclk, u32 xres)

    get horizontal blank time given pixelclock

    :param dclk:
        pixelclock in Hz
    :type dclk: u32

    :param xres:
        horizontal resolution in pixels
    :type xres: u32

.. _`fb_get_hblank_by_dclk.description`:

Description
-----------


xres \* duty_cycle
hblank = ------------------
100 - duty_cycle

duty cycle = percent of htotal assigned to inactive display
duty cycle = C - (M \* h_period)

.. _`fb_get_hblank_by_dclk.where`:

where
-----

h_period = SQRT(100 - C + (0.4 \* xres \* M)/dclk) + C - 100
-----------------------------------------------
2 \* M
M = 300;
C = 30;

.. _`fb_get_hfreq`:

fb_get_hfreq
============

.. c:function:: u32 fb_get_hfreq(u32 vfreq, u32 yres)

    estimate hsync

    :param vfreq:
        vertical refresh rate
    :type vfreq: u32

    :param yres:
        vertical resolution
    :type yres: u32

.. _`fb_get_hfreq.description`:

Description
-----------


(yres + front_port) \* vfreq \* 1000000
hfreq = -------------------------------------
(1000000 - (vfreq \* FLYBACK)

.. _`of_get_fb_videomode`:

of_get_fb_videomode
===================

.. c:function:: int of_get_fb_videomode(struct device_node *np, struct fb_videomode *fb, int index)

    get a fb_videomode from devicetree

    :param np:
        device_node with the timing specification
    :type np: struct device_node \*

    :param fb:
        will be set to the return value
    :type fb: struct fb_videomode \*

    :param index:
        index into the list of display timings in devicetree
    :type index: int

.. _`of_get_fb_videomode.description`:

Description
-----------

This function is expensive and should only be used, if only one mode is to be
read from DT. To get multiple modes start with of_get_display_timings ond
work with that instead.

.. This file was automatic generated / don't edit.

