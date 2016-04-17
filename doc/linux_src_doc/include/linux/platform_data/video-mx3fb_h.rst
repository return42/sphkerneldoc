.. -*- coding: utf-8; mode: rst -*-

=============
video-mx3fb.h
=============


.. _`mx3fb_platform_data`:

struct mx3fb_platform_data
==========================

.. c:type:: mx3fb_platform_data

    mx3fb platform data


.. _`mx3fb_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct mx3fb_platform_data {
    struct device * dma_dev;
    const struct fb_videomode * mode;
  };


.. _`mx3fb_platform_data.members`:

Members
-------

:``dma_dev``:
    pointer to the dma-device, used for dma-slave connection

:``mode``:
    pointer to a platform-provided per :c:func:`mxc_register_fb` videomode


