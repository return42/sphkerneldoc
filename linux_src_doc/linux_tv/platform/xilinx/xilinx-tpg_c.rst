.. -*- coding: utf-8; mode: rst -*-

============
xilinx-tpg.c
============



.. _xref_struct_xtpg_device:

struct xtpg_device
==================

.. c:type:: struct xtpg_device

    Xilinx Test Pattern Generator device structure



Definition
----------

.. code-block:: c

  struct xtpg_device {
    struct xvip_device xvip;
    struct media_pad pads[2];
    unsigned int npads;
    bool has_input;
    struct v4l2_mbus_framefmt formats[2];
    struct v4l2_mbus_framefmt default_format;
    const struct xvip_video_format * vip_format;
    bool bayer;
    struct v4l2_ctrl_handler ctrl_handler;
    struct v4l2_ctrl * hblank;
    struct v4l2_ctrl * vblank;
    struct v4l2_ctrl * pattern;
    bool streaming;
    struct xvtc_device * vtc;
    struct gpio_desc * vtmux_gpio;
  };



Members
-------

:``struct xvip_device xvip``:
    Xilinx Video IP device

:``struct media_pad pads[2]``:
    media pads

:``unsigned int npads``:
    number of pads (1 or 2)

:``bool has_input``:
    whether an input is connected to the sink pad

:``struct v4l2_mbus_framefmt formats[2]``:
    active V4L2 media bus format for each pad

:``struct v4l2_mbus_framefmt default_format``:
    default V4L2 media bus format

:``const struct xvip_video_format * vip_format``:
    format information corresponding to the active format

:``bool bayer``:
    boolean flag if TPG is set to any bayer format

:``struct v4l2_ctrl_handler ctrl_handler``:
    control handler

:``struct v4l2_ctrl * hblank``:
    horizontal blanking control

:``struct v4l2_ctrl * vblank``:
    vertical blanking control

:``struct v4l2_ctrl * pattern``:
    test pattern control

:``bool streaming``:
    is the video stream active

:``struct xvtc_device * vtc``:
    video timing controller

:``struct gpio_desc * vtmux_gpio``:
    video timing mux GPIO



