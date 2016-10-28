.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fbmon.c

.. _`fb_create_modedb`:

fb_create_modedb
================

.. c:function:: struct fb_videomode *fb_create_modedb(unsigned char *edid, int *dbsize, const struct fb_monspecs *specs)

    create video mode database

    :param unsigned char \*edid:
        EDID data

    :param int \*dbsize:
        database size

    :param const struct fb_monspecs \*specs:
        *undescribed*

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

    :param struct fb_videomode \*modedb:
        mode database to destroy

.. _`fb_destroy_modedb.description`:

Description
-----------

Destroy mode database created by fb_create_modedb

.. _`fb_edid_add_monspecs`:

fb_edid_add_monspecs
====================

.. c:function:: void fb_edid_add_monspecs(unsigned char *edid, struct fb_monspecs *specs)

    add monitor video modes from E-EDID data

    :param unsigned char \*edid:
        128 byte array with an E-EDID block

    :param struct fb_monspecs \*specs:
        *undescribed*

.. _`fb_get_vblank`:

fb_get_vblank
=============

.. c:function:: u32 fb_get_vblank(u32 hfreq)

    get vertical blank time

    :param u32 hfreq:
        horizontal freq

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

    :param u32 hfreq:
        horizontal freq

    :param u32 xres:
        horizontal resolution in pixels

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

    :param u32 dclk:
        pixelclock in Hz

    :param u32 xres:
        horizontal resolution in pixels

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

    :param u32 vfreq:
        vertical refresh rate

    :param u32 yres:
        vertical resolution

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

    :param struct device_node \*np:
        device_node with the timing specification

    :param struct fb_videomode \*fb:
        will be set to the return value

    :param int index:
        index into the list of display timings in devicetree

.. _`of_get_fb_videomode.description`:

Description
-----------

This function is expensive and should only be used, if only one mode is to be
read from DT. To get multiple modes start with of_get_display_timings ond
work with that instead.

.. This file was automatic generated / don't edit.

