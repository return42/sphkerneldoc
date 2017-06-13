.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/video_s3c.h

.. _`s3c_fb_pd_win`:

struct s3c_fb_pd_win
====================

.. c:type:: struct s3c_fb_pd_win

    per window setup data

.. _`s3c_fb_pd_win.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_pd_win {
        unsigned short default_bpp;
        unsigned short max_bpp;
        unsigned short xres;
        unsigned short yres;
        unsigned short virtual_x;
        unsigned short virtual_y;
    }

.. _`s3c_fb_pd_win.members`:

Members
-------

default_bpp
    *undescribed*

max_bpp
    *undescribed*

xres
    The window X size.

yres
    The window Y size.

virtual_x
    The virtual X size.

virtual_y
    The virtual Y size.

.. _`s3c_fb_platdata`:

struct s3c_fb_platdata
======================

.. c:type:: struct s3c_fb_platdata

    S3C driver platform specific information

.. _`s3c_fb_platdata.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_platdata {
        void (*setup_gpio)(void);
        struct s3c_fb_pd_win  *win;
        struct fb_videomode *vtiming;
        u32 vidcon0;
        u32 vidcon1;
    }

.. _`s3c_fb_platdata.members`:

Members
-------

setup_gpio
    Setup the external GPIO pins to the right state to transfer
    the data from the display system to the connected display
    device.

win
    The setup data for each hardware window, or NULL for unused.

vtiming
    Video timing when connected to a RGB type panel.

vidcon0
    The base vidcon0 values to control the panel data format.

vidcon1
    The base vidcon1 values to control the panel data output.

.. _`s3c_fb_platdata.description`:

Description
-----------

The platform data supplies the video driver with all the information
it requires to work with the display(s) attached to the machine. It
controls the initial mode, the number of display windows (0 is always
the base framebuffer) that are initialised etc.

.. This file was automatic generated / don't edit.

