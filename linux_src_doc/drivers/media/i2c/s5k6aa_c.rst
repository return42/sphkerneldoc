.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/s5k6aa.c

.. _`s5k6aa_configure_pixel_clocks`:

s5k6aa_configure_pixel_clocks
=============================

.. c:function:: int s5k6aa_configure_pixel_clocks(struct s5k6aa *s5k6aa)

    apply ISP main clock/PLL configuration

    :param struct s5k6aa \*s5k6aa:
        pointer to \ :c:type:`struct s5k6aa <s5k6aa>`\  describing the device

.. _`s5k6aa_configure_pixel_clocks.description`:

Description
-----------

Configure the internal ISP PLL for the required output frequency.

.. _`s5k6aa_configure_pixel_clocks.locking`:

Locking
-------

called with s5k6aa.lock mutex held.

.. _`s5k6aa_configure_video_bus`:

s5k6aa_configure_video_bus
==========================

.. c:function:: int s5k6aa_configure_video_bus(struct s5k6aa *s5k6aa, enum v4l2_mbus_type bus_type, int nlanes)

    configure the video output interface

    :param struct s5k6aa \*s5k6aa:
        pointer to \ :c:type:`struct s5k6aa <s5k6aa>`\  describing the device

    :param enum v4l2_mbus_type bus_type:
        video bus type: parallel or MIPI-CSI

    :param int nlanes:
        number of MIPI lanes to be used (MIPI-CSI only)

.. _`s5k6aa_configure_video_bus.note`:

Note
----

Only parallel bus operation has been tested.

.. _`s5k6aa_set_prev_config`:

s5k6aa_set_prev_config
======================

.. c:function:: int s5k6aa_set_prev_config(struct s5k6aa *s5k6aa, struct s5k6aa_preset *preset)

    write user preview register set

    :param struct s5k6aa \*s5k6aa:
        pointer to \ :c:type:`struct s5k6aa <s5k6aa>`\  describing the device

    :param struct s5k6aa_preset \*preset:
        s5kaa preset to be applied

.. _`s5k6aa_set_prev_config.description`:

Description
-----------

Configure output resolution and color fromat, pixel clock
frequency range, device frame rate type and frame period range.

.. _`s5k6aa_initialize_isp`:

s5k6aa_initialize_isp
=====================

.. c:function:: int s5k6aa_initialize_isp(struct v4l2_subdev *sd)

    basic ISP MCU initialization

    :param struct v4l2_subdev \*sd:
        pointer to V4L2 sub-device descriptor

.. _`s5k6aa_initialize_isp.description`:

Description
-----------

Configure AHB addresses for registers read/write; configure PLLs for
required output pixel clock. The ISP power supply needs to be already
enabled, with an optional H/W reset.

.. _`s5k6aa_initialize_isp.locking`:

Locking
-------

called with s5k6aa.lock mutex held.

.. This file was automatic generated / don't edit.

