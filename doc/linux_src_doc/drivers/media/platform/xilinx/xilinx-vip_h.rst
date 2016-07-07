.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-vip.h

.. _`xvip_device`:

struct xvip_device
==================

.. c:type:: struct xvip_device

    Xilinx Video IP device structure

.. _`xvip_device.definition`:

Definition
----------

.. code-block:: c

    struct xvip_device {
        struct v4l2_subdev subdev;
        struct device *dev;
        void __iomem *iomem;
        struct clk *clk;
        u32 saved_ctrl;
    }

.. _`xvip_device.members`:

Members
-------

subdev
    V4L2 subdevice

dev
    (OF) device

iomem
    device I/O register space remapped to kernel virtual memory

clk
    video core clock

saved_ctrl
    saved control register for resume / suspend

.. _`xvip_video_format`:

struct xvip_video_format
========================

.. c:type:: struct xvip_video_format

    Xilinx Video IP video format description

.. _`xvip_video_format.definition`:

Definition
----------

.. code-block:: c

    struct xvip_video_format {
        unsigned int vf_code;
        unsigned int width;
        const char *pattern;
        unsigned int code;
        unsigned int bpp;
        u32 fourcc;
        const char *description;
    }

.. _`xvip_video_format.members`:

Members
-------

vf_code
    AXI4 video format code

width
    AXI4 format width in bits per component

pattern
    CFA pattern for Mono/Sensor formats

code
    media bus format code

bpp
    bytes per pixel (when stored in memory)

fourcc
    V4L2 pixel format FCC identifier

description
    format description, suitable for userspace

.. This file was automatic generated / don't edit.

