.. -*- coding: utf-8; mode: rst -*-

========
s5k6aa.c
========



.. _xref_s5k6aa_configure_pixel_clocks:

s5k6aa_configure_pixel_clocks
=============================

.. c:function:: int s5k6aa_configure_pixel_clocks (struct s5k6aa * s5k6aa)

    apply ISP main clock/PLL configuration

    :param struct s5k6aa * s5k6aa:

        _undescribed_



Description
-----------



Configure the internal ISP PLL for the required output frequency.



Locking
-------

called with s5k6aa.lock mutex held.




.. _xref_s5k6aa_configure_video_bus:

s5k6aa_configure_video_bus
==========================

.. c:function:: int s5k6aa_configure_video_bus (struct s5k6aa * s5k6aa, enum v4l2_mbus_type bus_type, int nlanes)

    configure the video output interface

    :param struct s5k6aa * s5k6aa:

        _undescribed_

    :param enum v4l2_mbus_type bus_type:
        video bus type: parallel or MIPI-CSI

    :param int nlanes:
        number of MIPI lanes to be used (MIPI-CSI only)



Note
----

Only parallel bus operation has been tested.




.. _xref_s5k6aa_set_prev_config:

s5k6aa_set_prev_config
======================

.. c:function:: int s5k6aa_set_prev_config (struct s5k6aa * s5k6aa, struct s5k6aa_preset * preset)

    write user preview register set

    :param struct s5k6aa * s5k6aa:

        _undescribed_

    :param struct s5k6aa_preset * preset:

        _undescribed_



Description
-----------



Configure output resolution and color fromat, pixel clock
frequency range, device frame rate type and frame period range.




.. _xref_s5k6aa_initialize_isp:

s5k6aa_initialize_isp
=====================

.. c:function:: int s5k6aa_initialize_isp (struct v4l2_subdev * sd)

    basic ISP MCU initialization

    :param struct v4l2_subdev * sd:

        _undescribed_



Description
-----------



Configure AHB addresses for registers read/write; configure PLLs for
required output pixel clock. The ISP power supply needs to be already
enabled, with an optional H/W reset.



Locking
-------

called with s5k6aa.lock mutex held.


