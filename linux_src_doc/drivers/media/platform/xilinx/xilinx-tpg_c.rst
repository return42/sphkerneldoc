.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-tpg.c

.. _`xtpg_device`:

struct xtpg_device
==================

.. c:type:: struct xtpg_device

    Xilinx Test Pattern Generator device structure

.. _`xtpg_device.definition`:

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
        const struct xvip_video_format *vip_format;
        bool bayer;
        struct v4l2_ctrl_handler ctrl_handler;
        struct v4l2_ctrl *hblank;
        struct v4l2_ctrl *vblank;
        struct v4l2_ctrl *pattern;
        bool streaming;
        struct xvtc_device *vtc;
        struct gpio_desc *vtmux_gpio;
    }

.. _`xtpg_device.members`:

Members
-------

xvip
    Xilinx Video IP device

pads
    media pads

npads
    number of pads (1 or 2)

has_input
    whether an input is connected to the sink pad

formats
    active V4L2 media bus format for each pad

default_format
    default V4L2 media bus format

vip_format
    format information corresponding to the active format

bayer
    boolean flag if TPG is set to any bayer format

ctrl_handler
    control handler

hblank
    horizontal blanking control

vblank
    vertical blanking control

pattern
    test pattern control

streaming
    is the video stream active

vtc
    video timing controller

vtmux_gpio
    video timing mux GPIO

.. This file was automatic generated / don't edit.

