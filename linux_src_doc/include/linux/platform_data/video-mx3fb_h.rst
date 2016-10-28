.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/video-mx3fb.h

.. _`mx3fb_platform_data`:

struct mx3fb_platform_data
==========================

.. c:type:: struct mx3fb_platform_data

    mx3fb platform data

.. _`mx3fb_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct mx3fb_platform_data {
        struct device *dma_dev;
        const char *name;
        const struct fb_videomode *mode;
        int num_modes;
        enum disp_data_mapping disp_data_fmt;
    }

.. _`mx3fb_platform_data.members`:

Members
-------

dma_dev
    pointer to the dma-device, used for dma-slave connection

name
    *undescribed*

mode
    pointer to a platform-provided per \ :c:func:`mxc_register_fb`\  videomode

num_modes
    *undescribed*

disp_data_fmt
    *undescribed*

.. This file was automatic generated / don't edit.

